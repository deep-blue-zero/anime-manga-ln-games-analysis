---
series: GKM
generation: V2
artifact_type: audiovisual_documentation
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
source_boundary: "AVE-FULL-20260910: 27 source recordings computationally processed; 565 sampled still points reviewed; no fresh direct listening or continuous-motion review. Earlier evidence generations retain their stated provenance."
last_updated: '2026-09-10'
---

> **Public repository representation.** Machine-specific paths use `WORKSPACE/`, `LOCAL_USER/` or `LOCAL_DRIVE_*` placeholders; configure these roots before reproduction. Direct Drive URLs are represented by source-object IDs. Original execution hashes and exported-byte claims identify the archived originals; public code/data snippets containing these substitutions are explicitly derivatives. The import manifest records their final repository hashes and decoded payload hashes.


> **Repository adoption — 2026-09-10.** This is the owner-requested branch revision of the exported rebuild. Pre-import candidate labels and repository-state statements in preserved records describe their original execution. Current analytical use remains bounded by the stated evidence modalities. The [import record](../../../10_RELEASE_MANIFEST_AND_ARCHIVE/GKM_AVE_FULL_REBUILD_IMPORT_20260910.md) identifies export hashes and repository transformations.

# Frozen toolkit runtime source and license

Reconstruct each file at the indicated relative path under toolkit/. Exact SHA-256 values bind UTF-8 source bytes; save with LF line endings and the final newline shown in the original source. This is AV Evidence Toolkit 1.0.0 plus the explicitly identified trial WAV layout patch, not an unmodified copy of the published 1.0.0 release. The required runtime modules, package metadata, README and licenses are embedded below. The tested source tree, including tests and additional documentation, remains in the working evidence directory. The previously published AV_Evidence_Toolkit_1.0.0.zip has SHA-256 646110fe05f1fed908dbc1388a72c51e7015b440b161dac87b353c5348f4eb6b and does not include this trial patch; no new standalone toolkit ZIP is implied by this character-packet delivery.

## avevidence/__init__.py

SHA-256: `a8e8920a4d7ae51a392f7d17d082b7e99015d04317bcd46d84d9208ea371d65a`.

```python
"""Auditable audiovisual evidence preparation. Computation is not perception."""
__version__ = "1.0.0"
```

## avevidence/__main__.py

SHA-256: `935a1c1166b0c1ea35a82256345000bf2c73ded718d77773bc27a71ecce28f7d`.

```python
from .cli import main

raise SystemExit(main())
```

## avevidence/audio.py

SHA-256: `7af497132250d3414620525efdf9700d703fab7d2a2388ab6995772887ee7efb`.

```python
"""Audio preparation with stable identities, explicit clocks and bounded claims.

Stored PCM is compact: missing timestamp intervals are not invented as silence.
Every derivative carries a sample-range to parent-clock map. No function here
establishes perceptual listening, speaker identity, or audiovisual equivalence.
"""
from __future__ import annotations

from contextlib import contextmanager
from fractions import Fraction
import importlib.metadata
import inspect
import json
import math
from pathlib import Path
import re
import shutil
import struct

from .common import (AVError, file_record, finite, finish_run, interval,
                     output_transaction, probe_source, read_csv, read_json, run,
                     safe_member, select_stream, sha256, write_csv, write_json)

CLOCK = "original_pts_minus_source_origin"
_FRAME = re.compile(r"\bn:(\d+)\s+pts:(-?\d+)\s+pts_time:[^\s]+.*?\brate:(\d+)\s+nb_samples:(\d+)")


@contextmanager
def _scratch(stage):
    folder = Path(stage) / ".audio-working"
    folder.mkdir()
    try:
        yield folder
    finally:
        # Only files created in this fixed, fresh staging subdirectory are removed.
        for p in folder.iterdir():
            if not p.is_file() or p.is_symlink():
                raise AVError("Unexpected object in audio scratch directory")
            p.unlink()
        folder.rmdir()


def _layout(stream):
    layout = stream.get("channel_layout")
    if layout and layout != "unknown":
        return layout
    return "mono" if int(stream.get("channels", 0)) == 1 else None


def _decode(source, stream, folder, stem):
    """Decode unchanged rate/channel order to f64, keeping decoder-frame PTS."""
    rate = int(stream.get("sample_rate", 0))
    channels = int(stream.get("channels", 0))
    if rate <= 0 or channels <= 0:
        raise AVError("Audio rate and channel count must be known")
    raw = Path(folder) / (stem + ".f64le")
    filters = f"aformat=sample_fmts=dbl,asettb=expr=1/{rate},ashowinfo"
    command = ["ffmpeg", "-hide_banner", "-nostdin", "-v", "info", "-copyts",
               "-i", source["path"], "-map", f"0:{stream['index']}", "-vn", "-sn", "-dn",
               "-af", filters, "-c:a", "pcm_f64le", "-f", "f64le", "-"]
    result = run(command, binary=True, stdout_file=raw)
    stderr = result.stderr.decode("utf8", "replace") if isinstance(result.stderr, bytes) else result.stderr
    size = raw.stat().st_size
    if size == 0 or size % (8 * channels):
        raise AVError("No complete positive-length decoded audio; empty audio cannot be verified")
    frames = []
    for match in _FRAME.finditer(stderr):
        number, pts, frame_rate, count = map(int, match.groups())
        if number != len(frames) or frame_rate != rate or count <= 0:
            raise AVError("Inconsistent decoded audio frame timing")
        frames.append({"pts_samples": pts, "sample_count": count})
    if not frames or sum(x["sample_count"] for x in frames) != size // (8 * channels):
        raise AVError("Cannot bind every decoded sample to a timestamped frame")
    try:
        tick = abs(float(Fraction(stream.get("time_base", f"1/{rate}"))))
    except (ValueError, ZeroDivisionError):
        raise AVError("Audio stream time base is unavailable")
    tolerance = max(tick, 1 / rate) + 1e-9
    segments, offset, max_adjustment = [], 0, 0.0
    for frame in frames:
        observed = frame["pts_samples"] / rate - source["origin_seconds"]
        count = frame["sample_count"]
        if segments:
            prior = segments[-1]
            delta = observed - prior["source_end_seconds"]
            if abs(delta) <= tolerance:
                max_adjustment = max(max_adjustment, abs(delta))
                prior["sample_end"] += count
                prior["source_end_seconds"] = prior["source_start_seconds"] + (prior["sample_end"] - prior["sample_start"]) / rate
                offset += count
                continue
            if delta < 0:
                raise AVError("Overlapping audio timestamps exceed source granularity; explicit clock repair is required")
        segments.append({"sample_start": offset, "sample_end": offset + count,
                         "source_start_seconds": observed, "source_end_seconds": observed + count / rate})
        offset += count
    return {"raw_path": raw, "pcm_sha256": sha256(raw), "pcm_bytes": size,
            "sample_frames": offset, "sample_rate_hz": rate, "channels": channels,
            "channel_layout": _layout(stream), "stream_index": stream["index"],
            "encoding": "f64le interleaved native rate and channel order; no normalization or downmix",
            "segments": segments, "decoder_frames": frames,
            "clock": CLOCK, "origin_seconds": source["origin_seconds"],
            "timestamp_quantization_tolerance_seconds": tolerance,
            "max_timestamp_adjustment_seconds": max_adjustment,
            "timestamp_policy": "Contiguous samples within one source time-base tick are joined; larger gaps remain explicit; larger overlaps refuse"}


def _identity(decoded):
    return {k: decoded[k] for k in ("pcm_sha256", "pcm_bytes", "sample_frames", "sample_rate_hz",
            "channels", "channel_layout", "encoding", "clock", "origin_seconds",
            "timestamp_quantization_tolerance_seconds", "max_timestamp_adjustment_seconds", "timestamp_policy")}


def _sample_equal(a, b):
    return all(a[k] == b[k] for k in ("pcm_sha256", "pcm_bytes", "sample_frames", "sample_rate_hz", "channels"))


def _raw_input(decoded, path=None):
    args = ["-f", "f64le", "-ar", str(decoded["sample_rate_hz"]), "-ac", str(decoded["channels"])]
    if decoded["channel_layout"]:
        args += ["-channel_layout", decoded["channel_layout"]]
    else:
        args += ["-guess_layout_max", "0"]
    return args + ["-i", str(path or decoded["raw_path"])]


def _selection(decoded, start, end):
    """Half-open interval selection; count missing time separately from rounding."""
    rate = decoded["sample_rate_hz"]
    parts, coverage = [], 0.0
    for segment in decoded["segments"]:
        lo = max(start, segment["source_start_seconds"])
        hi = min(end, segment["source_end_seconds"])
        if hi <= lo:
            continue
        coverage += hi - lo
        first = segment["sample_start"] + max(0, math.ceil((lo - segment["source_start_seconds"]) * rate - 1e-6))
        last = segment["sample_start"] + math.ceil((hi - segment["source_start_seconds"]) * rate - 1e-6)
        last = min(last, segment["sample_end"])
        if last > first:
            actual = segment["source_start_seconds"] + (first - segment["sample_start"]) / rate
            parts.append({"input_sample_start": first, "input_sample_end": last,
                          "source_start_seconds": actual, "source_end_seconds": actual + (last-first)/rate})
    missing = max(0.0, end-start-coverage)
    status = "MISSING" if not parts else "COMPLETE" if missing <= 1/rate + 1e-8 else "PARTIAL"
    return {"status": status, "requested_start_seconds": start, "requested_end_seconds": end,
            "covered_seconds": coverage, "missing_seconds": missing, "parts": parts,
            "boundary_rounding": "Sample onsets in the half-open interval; both endpoint indices use ceil"}


def _slice(decoded, selection, target):
    if not selection["parts"]:
        raise AVError("Requested interval contains no decoded audio")
    stride, offset, segments = decoded["channels"] * 8, 0, []
    with decoded["raw_path"].open("rb") as src, Path(target).open("xb") as dst:
        for part in selection["parts"]:
            count = part["input_sample_end"] - part["input_sample_start"]
            src.seek(part["input_sample_start"] * stride)
            remaining = count * stride
            while remaining:
                block = src.read(min(remaining, 1024 * 1024))
                if not block:
                    raise AVError("Decoded sample file ended unexpectedly")
                dst.write(block)
                remaining -= len(block)
            segments.append({"sample_start": offset, "sample_end": offset+count,
                             "source_start_seconds": part["source_start_seconds"], "source_end_seconds": part["source_end_seconds"]})
            offset += count
    result = dict(decoded, raw_path=Path(target), segments=segments, sample_frames=offset,
                  pcm_bytes=offset*stride, pcm_sha256=sha256(target))
    return result


def _preserve_wav_channel_mask(decoded, output):
    """Upgrade generated mono/stereo IEEE-float headers without changing payload.

    FFmpeg can omit the channel mask for <=2-channel float WAV even with an
    explicit layout. Only layouts known from the parent are supplied here;
    channel counts alone never establish a stereo layout. Re-decoding and
    exact ordered sample/layout verification remain mandatory at the caller.
    """
    masks = {"mono": (1, 0x4), "stereo": (2, 0x3)}
    specification = masks.get(decoded["channel_layout"])
    if specification is None:
        return
    channels, mask = specification
    if decoded["channels"] != channels:
        raise AVError("Known WAV layout does not match the decoded channel count")
    output = Path(output)
    temporary = output.with_name(output.name + ".layout-working")
    with output.open("rb") as original:
        header = bytearray(original.read(12))
        if len(header) != 12 or header[:4] not in (b"RIFF", b"RF64") or header[8:] != b"WAVE":
            raise AVError("Generated float WAV has no supported RIFF/RF64 header")
        prefix = bytearray()
        ds64_offset = None
        while True:
            chunk = original.read(8)
            if len(chunk) != 8:
                raise AVError("Generated float WAV has no complete fmt chunk")
            length = struct.unpack_from("<I", chunk, 4)[0]
            if chunk[:4] == b"fmt ":
                value = original.read(length)
                if len(value) != length:
                    raise AVError("Generated float WAV fmt chunk is truncated")
                if length >= 40 and struct.unpack_from("<H", value)[0] == 0xFFFE:
                    return  # Existing mask is checked by the caller's re-decode.
                break
            # This operates only on a freshly generated header, never arbitrary
            # input media. Refuse surprising large pre-format metadata.
            if chunk[:4] == b"data" or length > 1024 * 1024:
                raise AVError("Unexpected generated WAV header before fmt chunk")
            value = original.read(length + (length & 1))
            if len(value) != length + (length & 1):
                raise AVError("Generated float WAV metadata is truncated")
            if chunk[:4] == b"ds64":
                if ds64_offset is not None or length < 28:
                    raise AVError("Generated RF64 has an invalid ds64 chunk")
                ds64_offset = len(prefix) + 8
            prefix.extend(chunk + value)
        rate = decoded["sample_rate_hz"]
        expected = (3, channels, rate, rate * channels * 8, channels * 8, 64, 0)
        if length != 18 or struct.unpack("<HHIIHHH", value) != expected:
            raise AVError("Generated float WAV header is not the expected native f64 format")
        extension = struct.pack("<HHIIHHHHI", 0xFFFE, channels, rate, rate * channels * 8,
                                channels * 8, 64, 22, 64, mask)
        extension += bytes.fromhex("0300000000001000800000aa00389b71")
        delta = len(extension) - length
        if header[:4] == b"RF64":
            if ds64_offset is None:
                raise AVError("Generated RF64 has no size mapping")
            old_size = struct.unpack_from("<Q", prefix, ds64_offset)[0]
            struct.pack_into("<Q", prefix, ds64_offset, old_size + delta)
        else:
            old_size = struct.unpack_from("<I", header, 4)[0]
            if old_size + delta > 0xFFFFFFFF:
                raise AVError("WAV layout header exceeds RIFF capacity; explicit RF64 is required")
            struct.pack_into("<I", header, 4, old_size + delta)
        created = False
        try:
            with temporary.open("xb") as changed:
                created = True
                changed.write(header)
                changed.write(prefix)
                changed.write(b"fmt " + struct.pack("<I", len(extension)) + extension)
                shutil.copyfileobj(original, changed, length=1024 * 1024)
        except BaseException:
            if created and temporary.exists():
                temporary.unlink()
            raise
    temporary.replace(output)


def _encode_wav(decoded, output):
    run(["ffmpeg", "-hide_banner", "-nostdin", "-v", "error", "-n"] + _raw_input(decoded) +
        ["-map", "0:a:0", "-c:a", "pcm_f64le", "-rf64", "auto", output])
    _preserve_wav_channel_mask(decoded, output)


def _review_segments(parent, artifact):
    result = []
    rate = parent["sample_rate_hz"]
    for original in parent["segments"]:
        for derived in artifact["segments"]:
            first = max(original["sample_start"], derived["sample_start"])
            last = min(original["sample_end"], derived["sample_end"])
            if last <= first:
                continue
            result.append({"parent_start_seconds": original["source_start_seconds"]+(first-original["sample_start"])/rate,
                           "parent_end_seconds": original["source_start_seconds"]+(last-original["sample_start"])/rate,
                           "derivative_start_seconds": derived["source_start_seconds"]+(first-derived["sample_start"])/rate,
                           "derivative_end_seconds": derived["source_start_seconds"]+(last-derived["sample_start"])/rate})
    return result


def _derivative_result(stage, source, stream, decoded, artifact, artifact_decoded, *, kind, selection=None):
    if not _sample_equal(decoded, artifact_decoded):
        raise AVError("Derivative changed decoded f64 samples/rate/channels; sample-preserving conversion refused")
    if decoded["channel_layout"] is not None and artifact_decoded["channel_layout"] != decoded["channel_layout"]:
        raise AVError("Derivative changed the known channel layout")
    relative = Path(artifact).relative_to(stage).as_posix()
    digest = sha256(artifact)
    segments = [dict(s, sample_rate_hz=decoded["sample_rate_hz"], parent_source_sha256=source["sha256"],
                     parent_stream_index=stream["index"]) for s in decoded["segments"]]
    mapping = {"modality": "audio", "artifact_kind": kind, "artifact_path": relative, "artifact_sha256": digest,
               "derivative_stream_index": artifact_decoded["stream_index"],
               "parent_source_sha256": source["sha256"], "parent_stream_index": stream["index"],
               "clock": CLOCK, "origin_seconds": source["origin_seconds"], "segments": _review_segments(decoded, artifact_decoded)}
    if len(mapping["segments"]) == 1:
        mapping.update(mapping["segments"][0])
    result = {"schema": "ave.audio.v1", "parent_source_sha256": source["sha256"], "parent_stream_index": stream["index"],
              "clock": CLOCK, "origin_seconds": source["origin_seconds"],
              "artifact_path": relative, "artifact_sha256": digest, "derivative_stream_index": artifact_decoded["stream_index"],
              "identity": _identity(decoded), "segments": segments, "review_mapping": mapping,
              "sample_preservation_verified": True, "artifact_channel_layout": artifact_decoded["channel_layout"],
              "channel_layout_preservation": "MATCH" if decoded["channel_layout"] is not None else "SOURCE_LAYOUT_UNKNOWN",
              "wav_layout_policy": "Known mono/stereo native f64 WAV exports use WAVEFORMATEXTENSIBLE masks; source-unknown layouts are not inferred from channel count; exact decoded sample/layout checks still apply",
              "selection": selection,
              "storage_policy": "PCM sample indices are compact; source gaps/delays remain explicit in the mapping, never assumed to be silence",
              "perceptual_review": "NOT_PERFORMED", "av_synchronization_verified": False}
    write_json(Path(stage)/"audio.json", result)
    return {"result_file": "audio.json", "review_mapping": mapping}


def extract_audio(input, output, *, stream_index=None, format="wav"):
    if format not in {"wav", "preserve", "flac"}:
        raise AVError("Audio format must be wav, preserve or flac")
    with output_transaction(output, [input]) as stage:
        source = probe_source(input)
        stream = select_stream(source, "audio", stream_index)
        with _scratch(stage) as scratch:
            decoded = _decode(source, stream, scratch, "source")
            if format == "preserve":
                codec = stream.get("codec_name", "")
                ext = ".wav" if codec.startswith("pcm_") else {"aac": ".m4a", "alac": ".m4a", "mp3": ".mp3", "flac": ".flac", "opus": ".ogg", "vorbis": ".ogg"}.get(codec, ".mka")
                artifact = stage / ("audio" + ext)
                run(["ffmpeg", "-hide_banner", "-nostdin", "-v", "error", "-n", "-i", source["path"],
                     "-map", f"0:{stream['index']}", "-vn", "-sn", "-dn", "-c:a", "copy", artifact])
            elif format == "flac":
                artifact = stage / "audio.flac"
                run(["ffmpeg", "-hide_banner", "-nostdin", "-v", "error", "-n"] + _raw_input(decoded) + ["-map", "0:a:0", "-c:a", "flac", artifact])
            else:
                artifact = stage / "audio.wav"
                _encode_wav(decoded, artifact)
            derived_source = probe_source(artifact)
            derived = _decode(derived_source, select_stream(derived_source, "audio"), scratch, "derivative")
            meta = _derivative_result(stage, source, stream, decoded, artifact, derived, kind="audio_pcm")
        result = finish_run(stage, "extract_audio", [source], {"stream_index": stream["index"], "format": format}, meta)
    return result


def clip_audio(input, output, *, stream_index=None, start, end, pad=0.0):
    a, b = interval(start, end)
    pad = finite(pad, "padding", 0)
    with output_transaction(output, [input]) as stage:
        source = probe_source(input)
        stream = select_stream(source, "audio", stream_index)
        with _scratch(stage) as scratch:
            decoded = _decode(source, stream, scratch, "source")
            requested = _selection(decoded, a, b)
            if requested["status"] == "MISSING":
                raise AVError("Requested clip interval contains no decoded audio")
            upper = b + pad
            if source["duration_seconds"] is not None:
                upper = min(upper, source["duration_seconds"])
            selected = _selection(decoded, max(0, a-pad), upper)
            clipped = _slice(decoded, selected, scratch/"clip.f64le")
            artifact = stage / "audio.wav"
            _encode_wav(clipped, artifact)
            derived_source = probe_source(artifact)
            derived = _decode(derived_source, select_stream(derived_source, "audio"), scratch, "derivative")
            selected["requested_unpadded"] = requested
            meta = _derivative_result(stage, source, stream, clipped, artifact, derived, kind="audio_clip", selection=selected)
        result = finish_run(stage, "clip_audio", [source], {"stream_index": stream["index"], "start": a, "end": b, "pad": pad}, meta)
    return result


def _number(value):
    try:
        result = float(value)
        return result if math.isfinite(result) else None
    except (TypeError, ValueError):
        return None


def _loudness(decoded):
    base = ["ffmpeg", "-hide_banner", "-nostdin", "-nostats"] + _raw_input(decoded) + ["-map", "0:a:0"]
    loud = run(base + ["-af", "loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json", "-f", "null", "-"])
    vol = run(base + ["-af", "volumedetect", "-f", "null", "-"])
    match = re.search(r'\{\s*"input_i".*?\}', loud.stderr, flags=re.S)
    if not match:
        raise AVError("FFmpeg did not supply loudnorm input measurements")
    raw = json.loads(match.group(0))
    values = {}
    for key in ("mean_volume", "max_volume"):
        found = re.findall(key + r":\s*([-+\d.inf]+)\s*dB", vol.stderr)
        if not found:
            raise AVError("FFmpeg did not supply volumedetect measurements")
        values[key] = _number(found[-1])
    return {"loudnorm_input": {"integrated_lufs": _number(raw["input_i"]), "loudness_range_lu": _number(raw["input_lra"]),
            "true_peak_dbtp": _number(raw["input_tp"]), "integrated_gating_threshold_lufs": _number(raw["input_thresh"])},
            "raw_loudnorm_report": raw,
            "volumedetect": {"mean_volume_dbfs": values["mean_volume"], "sample_peak_dbfs": values["max_volume"],
                             "processing": "FFmpeg volumedetect converts to signed 16-bit samples"},
            "normalization_written_to_source": False,
            "null_policy": "Nonfinite filter results are unavailable; exact raw filter strings are retained"}


def measure_audio(input, output, *, stream_index=None, start=None, end=None):
    with output_transaction(output, [input]) as stage:
        source = probe_source(input)
        stream = select_stream(source, "audio", stream_index)
        with _scratch(stage) as scratch:
            decoded = _decode(source, stream, scratch, "source")
            if start is None and end is None:
                a, b = decoded["segments"][0]["source_start_seconds"], decoded["segments"][-1]["source_end_seconds"]
            else:
                a, b = interval(start, end, decoded["segments"][-1]["source_end_seconds"])
            selection = _selection(decoded, a, b)
            measurements = None
            if selection["status"] == "COMPLETE":
                selected = _slice(decoded, selection, scratch/"selected.f64le")
                measurements = _loudness(selected)
            report = {"schema": "ave.audio_metrics.v1", "parent_source_sha256": source["sha256"],
                      "parent_stream_index": stream["index"], "clock": CLOCK, "origin_seconds": source["origin_seconds"],
                      "container_duration_seconds": source.get("format_duration_seconds", source["duration_seconds"]),
                      "canonical_source_duration_seconds": source["duration_seconds"],
                      "decoded_audio_seconds": decoded["sample_frames"]/decoded["sample_rate_hz"],
                      "identity": _identity(decoded), "selection": selection, "measurements": measurements,
                      "scope": "Selected final-mix channels; gaps are unavailable, not invented silence; not speaker-isolated",
                      "perceptual_review": "NOT_PERFORMED"}
            write_json(stage/"metrics.json", report)
        result = finish_run(stage, "measure_audio", [source], {"stream_index": stream["index"], "start": start, "end": end},
                            {"result_file": "metrics.json", "coverage_status": selection["status"]})
    return result


def compare_audio(a, b, output, *, a_stream=None, b_stream=None):
    with output_transaction(output, [a, b]) as stage:
        sources = [probe_source(a), probe_source(b)]
        streams = [select_stream(sources[0], "audio", a_stream), select_stream(sources[1], "audio", b_stream)]
        with _scratch(stage) as scratch:
            left = _decode(sources[0], streams[0], scratch, "a")
            right = _decode(sources[1], streams[1], scratch, "b")
            samples_equal = _sample_equal(left, right)
            layout = "UNKNOWN" if left["channel_layout"] is None or right["channel_layout"] is None else "MATCH" if left["channel_layout"] == right["channel_layout"] else "DIFFERENT"
            tolerance = max(left["timestamp_quantization_tolerance_seconds"], right["timestamp_quantization_tolerance_seconds"])
            timing_equal = len(left["segments"]) == len(right["segments"]) and all(
                x["sample_start"] == y["sample_start"] and x["sample_end"] == y["sample_end"] and
                abs(x["source_start_seconds"]-y["source_start_seconds"]) <= tolerance and
                abs(x["source_end_seconds"]-y["source_end_seconds"]) <= tolerance
                for x, y in zip(left["segments"], right["segments"]))
            status = "DIFFERENT" if not samples_equal or not timing_equal or layout == "DIFFERENT" else "INDETERMINATE" if layout == "UNKNOWN" else "MATCH"
            report = {"schema": "ave.audio_comparison.v1", "comparison_status": status,
                      "a": dict(_identity(left), segments=left["segments"], source_sha256=sources[0]["sha256"], stream_index=streams[0]["index"]),
                      "b": dict(_identity(right), segments=right["segments"], source_sha256=sources[1]["sha256"], stream_index=streams[1]["index"]),
                      "native_decoded_samples_equal": samples_equal, "channel_layout_comparison": layout,
                      "canonical_timing_equal_within_source_granularity": timing_equal, "timing_tolerance_seconds": tolerance,
                      "source_origins_equal": sources[0]["origin_seconds"] == sources[1]["origin_seconds"],
                      "encoded_packet_identity": "NOT_ESTABLISHED", "audiovisual_equivalence": "NOT_ESTABLISHED",
                      "perceptual_review": "NOT_PERFORMED",
                      "comparison_scope": "Native f64 decoded ordered samples, known channel layout and canonical audio timing; not matching video or narrative"}
            write_json(stage/"comparison.json", report)
        result = finish_run(stage, "compare_audio", sources, {"a_stream": streams[0]["index"], "b_stream": streams[1]["index"]},
                            {"result_file": "comparison.json", "comparison_status": status})
    return result


def _verified_artifact(folder, manifest, relative):
    path = safe_member(folder, relative)
    entries = [x for x in manifest.get("artifacts", []) if x.get("path") == relative]
    if len(entries) != 1 or not path.is_file() or path.stat().st_size != entries[0]["size_bytes"] or sha256(path) != entries[0]["sha256"]:
        raise AVError("Audio run artifact is missing or changed")
    return path


def _cue_input(value, stream_index, scratch):
    path = Path(value).resolve()
    folder = path if path.is_dir() else path.parent
    if (folder/"run.json").is_file() and (folder/"audio.json").is_file():
        manifest = read_json(folder/"run.json")
        if manifest.get("operation") not in {"extract_audio", "clip_audio"}:
            raise AVError("Expected an extraction or audio-clip run")
        receipt_path = _verified_artifact(folder, manifest, manifest["metadata"]["result_file"])
        receipt = read_json(receipt_path)
        artifact = _verified_artifact(folder, manifest, receipt["artifact_path"])
        if not path.is_dir() and path != artifact:
            raise AVError("The supplied path is not this audio run's artifact")
        if sha256(artifact) != receipt["artifact_sha256"]:
            raise AVError("Audio receipt and artifact disagree")
        if stream_index is not None and int(stream_index) != receipt["parent_stream_index"]:
            raise AVError("Requested parent audio stream differs from the extraction")
        source = probe_source(artifact)
        decoded = _decode(source, select_stream(source, "audio", receipt["derivative_stream_index"]), scratch, "cue_input")
        if not all(decoded[k] == receipt["identity"][k] for k in ("pcm_sha256", "pcm_bytes", "sample_frames", "sample_rate_hz", "channels")):
            raise AVError("Audio derivative no longer reproduces its parent sample identity")
        decoded["segments"] = receipt["segments"]
        decoded["origin_seconds"] = receipt["origin_seconds"]
        parent = {"parent_source_sha256": receipt["parent_source_sha256"], "parent_stream_index": receipt["parent_stream_index"],
                  "clock": CLOCK, "origin_seconds": receipt["origin_seconds"]}
        dependencies = [source, file_record(folder/"run.json", "audio_run_manifest"), file_record(receipt_path, "audio_mapping")]
    else:
        source = probe_source(path)
        stream = select_stream(source, "audio", stream_index)
        decoded = _decode(source, stream, scratch, "cue_input")
        parent = {"parent_source_sha256": source["sha256"], "parent_stream_index": stream["index"], "clock": CLOCK, "origin_seconds": source["origin_seconds"]}
        dependencies = [source]
    return decoded, parent, dependencies


def _db(amplitude):
    return 20*math.log10(amplitude) if amplitude > 0 else None


def _features(samples, rate, profile, pitch_options):
    import numpy as np
    total_energy, peak, crossings, previous = 0.0, 0.0, 0, None
    for offset in range(0, len(samples), 1024*1024):
        chunk = samples[offset:offset+1024*1024]
        if not np.isfinite(chunk).all():
            raise AVError("Nonfinite audio samples cannot be measured")
        total_energy += float(np.sum(chunk*chunk, dtype=np.float64))
        peak = max(peak, float(np.max(np.abs(chunk))))
        signs = np.signbit(chunk)
        crossings += int(np.count_nonzero(signs[1:] != signs[:-1]))
        if previous is not None:
            crossings += int(previous != signs[0])
        previous = signs[-1]
    if not math.isfinite(total_energy):
        raise AVError("Audio energy exceeds the numeric measurement range")
    frame = max(32, round(rate * (1024/16000 if profile == "speech" else 2048/22050)))
    hop = max(1, round(rate * (160/16000 if profile == "speech" else 512/22050)))
    result = {"rms_dbfs": _db(math.sqrt(total_energy/len(samples))),
              "sample_peak_dbfs": _db(peak), "sample_frames": len(samples),
              "zero_crossing_rate": crossings/(len(samples)-1) if len(samples) > 1 else None,
              "rms_zero_amplitude": total_energy == 0, "frame_length": frame, "hop_length": hop,
              "center": False, "window": "hann", "channel_policy": "independent channel; no averaging/downmix"}
    if len(samples) >= frame:
        frames = np.lib.stride_tricks.sliding_window_view(samples, frame)[::hop]
        freq = np.fft.rfftfreq(frame, 1/rate)
        window = np.hanning(frame)
        centroids, rolloffs, low_energy = [], [], 0
        for offset in range(0, len(frames), 256):
            batch = frames[offset:offset+256]
            energy = np.sqrt(np.mean(batch*batch, axis=1, dtype=np.float64))
            low_energy += int(np.count_nonzero(energy < 10**(pitch_options["energy_threshold_dbfs"]/20)))
            spectral = np.abs(np.fft.rfft(batch * window, axis=1))
            totals = spectral.sum(axis=1)
            valid = totals > 1e-12
            if valid.any():
                centroids.extend((np.sum(spectral[valid]*freq, axis=1)/totals[valid]).tolist())
                rolloffs.extend(freq[np.argmax(np.cumsum(spectral[valid], axis=1) >= .85*totals[valid,None], axis=1)].tolist())
        result.update({"analysis_frames": len(frames), "nonempty_spectral_frames": len(centroids),
                       "low_energy_frame_fraction": low_energy/len(frames),
                       "low_energy_is_not_silence_or_vad": True,
                       "spectral_centroid_hz_median": float(np.median(centroids)) if centroids else None,
                       "spectral_rolloff85_hz_median": float(np.median(rolloffs)) if rolloffs else None})
    else:
        result.update({"analysis_frames": 0, "nonempty_spectral_frames": 0, "low_energy_frame_fraction": None,
                       "spectral_centroid_hz_median": None, "spectral_rolloff85_hz_median": None,
                       "frame_status": "INSUFFICIENT_SAMPLES"})
    if pitch_options["pitch"]:
        result["pitch"] = _pitch(samples, rate, pitch_options)
    else:
        result["pitch"] = {"status": "NOT_REQUESTED"}
    return result


def _pitch(samples, rate, options):
    import numpy as np
    try:
        import librosa
    except ImportError as exc:
        raise AVError("Pitch requires the optional librosa dependencies") from exc
    base = {"algorithm": "librosa.pyin", "librosa_version": importlib.metadata.version("librosa"),
            "sample_rate_hz": 16000, "frame_length": 1024, "hop_length": 160, "center": False,
            "fmin_hz": options["fmin"], "fmax_hz": options["fmax"],
            "minimum_voiced_probability": options["min_voiced_probability"],
            "energy_threshold_dbfs": options["energy_threshold_dbfs"],
            "isolation": "OPERATOR_DECLARED_NOT_VERIFIED",
            "resampler": "librosa.resample soxr_hq, fix=True, scale=False when rate differs",
            "scope": "Estimated F0; not speaker identity, emotion, voice quality or perceptual listening"}
    if len(samples)/rate > 60:
        return dict(base, status="SKIPPED_INTERVAL_OVER_60_SECONDS", qualified_f0_median_hz=None)
    y = librosa.resample(samples, orig_sr=rate, target_sr=16000, res_type="soxr_hq", fix=True, scale=False) if rate != 16000 else samples
    if len(y) < 1024:
        return dict(base, status="INSUFFICIENT_SAMPLES", qualified_f0_median_hz=None)
    try:
        parameters = {name: p.default for name, p in inspect.signature(librosa.pyin).parameters.items()
                      if name != "y" and p.default is not inspect.Parameter.empty}
        parameters.update(sr=16000, fmin=options["fmin"], fmax=options["fmax"], frame_length=1024,
                          hop_length=160, center=False, fill_na=np.nan)
        base["resolved_pyin_parameters"] = {k: "NaN (unvoiced)" if isinstance(v, float) and math.isnan(v) else v for k, v in parameters.items()}
        f0, voiced, probability = librosa.pyin(y, **parameters)
        framed = np.lib.stride_tricks.sliding_window_view(y, 1024)[::160]
        energy = np.sqrt(np.mean(framed*framed, axis=1, dtype=np.float64))
        if len(energy) != len(f0):
            raise AVError("Pitch and energy frames do not align")
        valid = voiced & np.isfinite(f0) & np.isfinite(probability) & (probability >= options["min_voiced_probability"]) & (energy > 10**(options["energy_threshold_dbfs"]/20))
        track = [{"relative_center_seconds": (i*160+512)/16000,
                  "estimated_f0_hz": float(value) if math.isfinite(float(value)) else None,
                  "voiced_probability": _number(prob), "qualified": bool(keep)}
                 for i, (value, prob, keep) in enumerate(zip(f0, probability, valid))]
        return dict(base, status="QUALIFIED_ESTIMATES" if valid.any() else "NO_QUALIFIED_FRAMES",
                    qualified_frames=int(valid.sum()), total_frames=len(f0),
                    qualified_f0_median_hz=float(np.median(f0[valid])) if valid.any() else None,
                    qualified_f0_p10_hz=float(np.percentile(f0[valid], 10)) if valid.any() else None,
                    qualified_f0_p90_hz=float(np.percentile(f0[valid], 90)) if valid.any() else None,
                    frame_track=track)
    except Exception as exc:
        return dict(base, status="FAILED", error=f"{type(exc).__name__}: {exc}", qualified_f0_median_hz=None)


def cue_features(audio_run_or_audio_path, dialogue_csv, output, *, stream_index=None,
                 pitch=False, confirm_isolated_speech=False, profile="speech", fmin=65.0, fmax=1000.0,
                 min_voiced_probability=0.9, energy_threshold_dbfs=-45.0):
    if profile not in {"speech", "music"}:
        raise AVError("Profile must be speech or music")
    if pitch and (not confirm_isolated_speech or profile != "speech"):
        raise AVError("Pitch requires speech profile and explicit isolated-speech confirmation")
    fmin, fmax = finite(fmin, "fmin", 0), finite(fmax, "fmax", 0)
    probability = finite(min_voiced_probability, "voiced probability", 0)
    threshold = finite(energy_threshold_dbfs, "energy threshold")
    if not 0 < fmin < fmax < 8000 or probability > 1:
        raise AVError("Require 0 < fmin < fmax < 8000 and probability between zero and one")
    try:
        import numpy as np
    except ImportError as exc:
        raise AVError("Cue features require NumPy") from exc
    with output_transaction(output, [audio_run_or_audio_path, dialogue_csv]) as stage:
        dialogue_record = file_record(dialogue_csv, "dialogue_csv")
        cues = read_csv(dialogue_csv)
        with _scratch(stage) as scratch:
            decoded, parent, dependencies = _cue_input(audio_run_or_audio_path, stream_index, scratch)
            dependencies.append(dialogue_record)
            options = {"pitch": pitch, "fmin": fmin, "fmax": fmax, "min_voiced_probability": probability, "energy_threshold_dbfs": threshold}
            method = {"profile": profile, "numpy_version": importlib.metadata.version("numpy"), "sample_rate_hz": decoded["sample_rate_hz"],
                      "channels": decoded["channels"], "channel_layout": decoded["channel_layout"], "channel_policy": "Separate channels; no downmix",
                      "rms": "Whole complete cue, float64 mean square, no amplitude floor; zero amplitude dBFS is null",
                      "framing": "Complete uncentered frames; speech 64 ms/10 ms, music 2048/22050 s and 512/22050 s; rounded to native samples",
                      "spectral": "NumPy rFFT, symmetric Hann, magnitude centroid and 85% rolloff, median over nonempty frames",
                      "zero_crossing_rate": "Fraction of adjacent sample sign-bit changes, measured per channel; not voicing/activity",
                      "low_energy": "Fraction of full RMS frames under the declared threshold; not silence/pause duration or VAD",
                      "pitch_options": options}
            memory = np.memmap(decoded["raw_path"], dtype="<f8", mode="r", shape=(decoded["sample_frames"], decoded["channels"]))
            results, csv_rows, all_bound = [], [], True
            try:
                for number, cue in enumerate(cues, 1):
                    if cue.get("start_seconds") in (None, "") or cue.get("end_seconds") in (None, ""):
                        raise AVError("Every cue requires explicit start_seconds and end_seconds")
                    a, b = interval(cue["start_seconds"], cue["end_seconds"])
                    bound = bool(cue.get("parent_source_sha256"))
                    if bound and (cue["parent_source_sha256"] != parent["parent_source_sha256"] or cue.get("clock") != CLOCK or
                                  abs(finite(cue.get("origin_seconds"), "cue origin")-parent["origin_seconds"]) > 1e-9):
                        raise AVError("Cue source hash/clock/origin does not match the audio parent")
                    all_bound = all_bound and bound
                    selection = _selection(decoded, a, b)
                    row = {"cue_index": cue.get("cue_index", str(number)), "source_start_seconds": a, "source_end_seconds": b,
                           "status": selection["status"], "coverage": selection, "per_channel": None,
                           "name": cue.get("name", ""), "text": cue.get("text_plain", cue.get("text", "")),
                           "dialogue_clock_status": "VERIFIED_SOURCE_BINDING" if bound else "UNBOUND_OPERATOR_TIMES"}
                    if selection["status"] == "COMPLETE":
                        pieces = [np.asarray(memory[p["input_sample_start"]:p["input_sample_end"]]) for p in selection["parts"]]
                        samples = pieces[0] if len(pieces) == 1 else np.concatenate(pieces, axis=0)
                        row["per_channel"] = []
                        for channel in range(decoded["channels"]):
                            value = _features(samples[:, channel], decoded["sample_rate_hz"], profile, options)
                            value["channel_index"] = channel
                            if "frame_track" in value["pitch"]:
                                offset = selection["parts"][0]["source_start_seconds"]
                                for frame in value["pitch"]["frame_track"]:
                                    frame["source_center_seconds"] = offset + frame["relative_center_seconds"]
                            row["per_channel"].append(value)
                    for channel in range(decoded["channels"]):
                        value = row["per_channel"][channel] if row["per_channel"] else {}
                        csv_rows.append(dict(parent, dialogue_csv_sha256=dialogue_record["sha256"], cue_index=row["cue_index"],
                                             start_seconds=a, end_seconds=b, status=row["status"], dialogue_clock_status=row["dialogue_clock_status"],
                                             channel_index=channel, rms_dbfs=value.get("rms_dbfs"), sample_peak_dbfs=value.get("sample_peak_dbfs"),
                                             zero_crossing_rate=value.get("zero_crossing_rate"),
                                             spectral_centroid_hz_median=value.get("spectral_centroid_hz_median"),
                                             pitch_status=value.get("pitch", {}).get("status"), qualified_f0_median_hz=value.get("pitch", {}).get("qualified_f0_median_hz")))
                    results.append(row)
            finally:
                # Release mmap before the scratch file is deleted on Windows.
                memory._mmap.close()
            report = dict(parent, schema="ave.cue_features.v1", dialogue_csv_sha256=dialogue_record["sha256"],
                          dialogue_clock_status="VERIFIED_SOURCE_BINDING" if all_bound and cues else "UNBOUND_OPERATOR_TIMES",
                          method=method, rows=results, perceptual_review="NOT_PERFORMED",
                          limitations=["Subtitle names do not isolate or identify an audible speaker", "Missing/partial windows have null measurements", "Acoustics do not establish emotion or narrative intent"])
            write_json(stage/"features.json", report)
            fields = ["parent_source_sha256", "parent_stream_index", "clock", "origin_seconds", "dialogue_csv_sha256", "cue_index",
                      "start_seconds", "end_seconds", "status", "dialogue_clock_status", "channel_index", "rms_dbfs", "sample_peak_dbfs",
                      "zero_crossing_rate", "spectral_centroid_hz_median", "pitch_status", "qualified_f0_median_hz"]
            write_csv(stage/"features.csv", csv_rows, fields)
        result = finish_run(stage, "cue_features", dependencies, dict(options, profile=profile, confirm_isolated_speech=confirm_isolated_speech),
                            {"result_file": "features.json", "csv_file": "features.csv", "parent_source_sha256": parent["parent_source_sha256"]})
    return result
```

## avevidence/bundle.py

SHA-256: `f14e89ba88451fd254af1368ee50f2f62a9a132bd243af26c761a7200d66539a`.

Repository representation: the following **base64-encoded python payload** preserves the source block while separating embedded example links from repository navigation. Decode this block with `base64.b64decode` before following the original extraction/reproduction instructions. Decoded UTF-8 payload SHA-256: `f14e89ba88451fd254af1368ee50f2f62a9a132bd243af26c761a7200d66539a`; bytes: 5085.

```base64
IiIiQ29tcG9zZSBpbmRlcGVuZGVudGx5IHZlcmlmaWFibGUgZXZpZGVuY2UgcnVucyBpbnRvIGFuIGVwaXNvZGUgYnVuZGxlLiIi
Igpmcm9tIF9fZnV0dXJlX18gaW1wb3J0IGFubm90YXRpb25zCgpmcm9tIHBhdGhsaWIgaW1wb3J0IFBhdGgKCmZyb20gLmNvbW1v
biBpbXBvcnQgKEFWRXJyb3IsIGZpbGVfcmVjb3JkLCBmaW5pc2hfcnVuLCBvdXRwdXRfdHJhbnNhY3Rpb24sIHByb2JlX3NvdXJj
ZSwKICAgICAgICAgICAgICAgICAgICAgc2VsZWN0X3N0cmVhbSwgd3JpdGVfanNvbikKCgpkZWYgYnVpbGRfYnVuZGxlKGlucHV0
LCBvdXRwdXQsICosIHN1YnRpdGxlcz1Ob25lLCBzdWJ0aXRsZV9zdHJlYW09Tm9uZSwgYXVkaW9fc3RyZWFtPU5vbmUsCiAgICAg
ICAgICAgICAgICAgdmlkZW9fc3RyZWFtPU5vbmUsIGludGVydmFsPTIuMCwgd2lkdGg9MTI4MCwgc2hvdHM9RmFsc2UsIGZlYXR1
cmVzPUZhbHNlKToKICAgIGZyb20gLmF1ZGlvIGltcG9ydCBleHRyYWN0X2F1ZGlvLCBtZWFzdXJlX2F1ZGlvLCBjdWVfZmVhdHVy
ZXMKICAgIGZyb20gLmludmVudG9yeSBpbXBvcnQgaW52ZW50b3J5CiAgICBmcm9tIC5zdWJ0aXRsZXMgaW1wb3J0IHBhcnNlX3N1
YnRpdGxlcwogICAgZnJvbSAudGltZWxpbmUgaW1wb3J0IGFsaWduX3RpbWVsaW5lCiAgICBmcm9tIC52aXN1YWwgaW1wb3J0IGV4
dHJhY3RfZnJhbWVzLCBjb250YWN0X3NoZWV0cwoKICAgIHNvdXJjZSA9IHByb2JlX3NvdXJjZShpbnB1dCkKICAgIHZpZGVvID0g
c2VsZWN0X3N0cmVhbShzb3VyY2UsICJ2aWRlbyIsIHZpZGVvX3N0cmVhbSwgcmVxdWlyZWQ9RmFsc2UpCiAgICBhdWRpbyA9IHNl
bGVjdF9zdHJlYW0oc291cmNlLCAiYXVkaW8iLCBhdWRpb19zdHJlYW0sIHJlcXVpcmVkPUZhbHNlKQogICAgaWYgbm90IHZpZGVv
IGFuZCBub3QgYXVkaW86CiAgICAgICAgcmFpc2UgQVZFcnJvcigiQnVuZGxlIHNvdXJjZSBoYXMgbm8gc2VsZWN0ZWQgYXVkaW8v
dmlkZW8iKQogICAgaWYgc3VidGl0bGVzIGFuZCBzdWJ0aXRsZV9zdHJlYW0gaXMgbm90IE5vbmU6CiAgICAgICAgcmFpc2UgQVZF
cnJvcigiQ2hvb3NlIGV4dGVybmFsIHN1YnRpdGxlcyBvciBhbiBlbWJlZGRlZCBzdWJ0aXRsZSBzdHJlYW0sIG5vdCBib3RoIikK
ICAgIGRlcGVuZGVuY2llcyA9IFtzb3VyY2VdCiAgICBpZiBzdWJ0aXRsZXM6CiAgICAgICAgZGVwZW5kZW5jaWVzLmFwcGVuZChm
aWxlX3JlY29yZChzdWJ0aXRsZXMsICJzdWJ0aXRsZSIpKQogICAgaWYgZmVhdHVyZXMgYW5kIChub3QgYXVkaW8gb3Igbm90IChz
dWJ0aXRsZXMgb3Igc3VidGl0bGVfc3RyZWFtIGlzIG5vdCBOb25lKSk6CiAgICAgICAgcmFpc2UgQVZFcnJvcigiQ3VlIGZlYXR1
cmVzIHJlcXVpcmUgc2VsZWN0ZWQgYXVkaW8gYW5kIGV4cGxpY2l0bHkgYm91bmQgc3VidGl0bGVzIikKICAgIHdpdGggb3V0cHV0
X3RyYW5zYWN0aW9uKG91dHB1dCwgW3NbInBhdGgiXSBmb3IgcyBpbiBkZXBlbmRlbmNpZXNdKSBhcyBvdXQ6CiAgICAgICAgc2Vs
ZWN0ZWQgPSB7fQogICAgICAgIGlmIHZpZGVvOiBzZWxlY3RlZFsidmlkZW8iXSA9IHZpZGVvWyJpbmRleCJdCiAgICAgICAgaWYg
YXVkaW86IHNlbGVjdGVkWyJhdWRpbyJdID0gYXVkaW9bImluZGV4Il0KICAgICAgICByZXF1aXJlZCA9IChbImF1ZGlvIl0gaWYg
YXVkaW8gZWxzZSBbXSkgKyAoWyJtb3Rpb24iXSBpZiB2aWRlbyBlbHNlIFtdKQogICAgICAgIGNvbmZpZyA9IHsic291cmNlcyI6
IFt7ImxvZ2ljYWxfc291cmNlX2lkIjogInNvdXJjZV8iICsgc291cmNlWyJzaGEyNTYiXVs6MTZdLAogICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgIm1hdGVyaWFsaXphdGlvbl9pZCI6ICJzaGEyNTZfIiArIHNvdXJjZVsic2hhMjU2Il0sICJwYXRoIjog
c291cmNlWyJwYXRoIl0sCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAic2VsZWN0ZWRfc3RyZWFtcyI6IHNlbGVjdGVk
LCAicmVxdWlyZWRfbW9kYWxpdGllcyI6IHJlcXVpcmVkLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgInByZWZlcnJl
ZCI6IFRydWV9XX0KICAgICAgICB3cml0ZV9qc29uKG91dCAvICJzb3VyY2VzLmpzb24iLCBjb25maWcpCiAgICAgICAgaW52ZW50
b3J5KG91dCAvICJzb3VyY2VzLmpzb24iLCBvdXQgLyAiaW52ZW50b3J5IikKICAgICAgICBjaGlsZHJlbiA9IFsiaW52ZW50b3J5
Il0KICAgICAgICBpZiBhdWRpbzoKICAgICAgICAgICAgZXh0cmFjdF9hdWRpbyhpbnB1dCwgb3V0IC8gImF1ZGlvIiwgc3RyZWFt
X2luZGV4PWF1ZGlvWyJpbmRleCJdKQogICAgICAgICAgICBtZWFzdXJlX2F1ZGlvKGlucHV0LCBvdXQgLyAibWV0cmljcyIsIHN0
cmVhbV9pbmRleD1hdWRpb1siaW5kZXgiXSkKICAgICAgICAgICAgY2hpbGRyZW4gKz0gWyJhdWRpbyIsICJtZXRyaWNzIl0KICAg
ICAgICBpZiB2aWRlbzoKICAgICAgICAgICAgZXh0cmFjdF9mcmFtZXMoaW5wdXQsIG91dCAvICJmcmFtZXMiLCBtb2RlPSJpbnRl
cnZhbCIsIGludGVydmFsPWludGVydmFsLCB3aWR0aD13aWR0aCwgc3RyZWFtX2luZGV4PXZpZGVvWyJpbmRleCJdKQogICAgICAg
ICAgICBjb250YWN0X3NoZWV0cyhvdXQgLyAiZnJhbWVzIiwgb3V0IC8gImNvbnRhY3RzIikKICAgICAgICAgICAgY2hpbGRyZW4g
Kz0gWyJmcmFtZXMiLCAiY29udGFjdHMiXQogICAgICAgICAgICBpZiBzaG90czoKICAgICAgICAgICAgICAgIGV4dHJhY3RfZnJh
bWVzKGlucHV0LCBvdXQgLyAic2hvdHMiLCBtb2RlPSJzaG90cyIsIHdpZHRoPXdpZHRoLCBzdHJlYW1faW5kZXg9dmlkZW9bImlu
ZGV4Il0pCiAgICAgICAgICAgICAgICBjaGlsZHJlbi5hcHBlbmQoInNob3RzIikKICAgICAgICBjYXB0aW9uID0gTm9uZQogICAg
ICAgIGlmIHN1YnRpdGxlczoKICAgICAgICAgICAgY2FwdGlvbiA9IHBhcnNlX3N1YnRpdGxlcyhzdWJ0aXRsZXMsIG91dCAvICJz
dWJ0aXRsZXMiLCBzb3VyY2VfbWVkaWE9aW5wdXQpCiAgICAgICAgZWxpZiBzdWJ0aXRsZV9zdHJlYW0gaXMgbm90IE5vbmU6CiAg
ICAgICAgICAgIGNhcHRpb24gPSBwYXJzZV9zdWJ0aXRsZXMoaW5wdXQsIG91dCAvICJzdWJ0aXRsZXMiLCBzdHJlYW1faW5kZXg9
c3VidGl0bGVfc3RyZWFtLCBtZWRpYT1UcnVlKQogICAgICAgIGlmIGNhcHRpb246CiAgICAgICAgICAgIGNoaWxkcmVuLmFwcGVu
ZCgic3VidGl0bGVzIikKICAgICAgICAgICAgaWYgZmVhdHVyZXM6CiAgICAgICAgICAgICAgICBjc3ZfZmlsZSA9IGNhcHRpb24u
Z2V0KCJtZXRhZGF0YSIsIHt9KS5nZXQoImNzdl9maWxlIiwgImRpYWxvZ3VlLmNzdiIpCiAgICAgICAgICAgICAgICBjdWVfZmVh
dHVyZXMob3V0IC8gImF1ZGlvIiwgb3V0IC8gInN1YnRpdGxlcyIgLyBjc3ZfZmlsZSwgb3V0IC8gImZlYXR1cmVzIikKICAgICAg
ICAgICAgICAgIGNoaWxkcmVuLmFwcGVuZCgiZmVhdHVyZXMiKQogICAgICAgICAgICBpZiB2aWRlbzoKICAgICAgICAgICAgICAg
IGFsaWduX3RpbWVsaW5lKG91dCAvICJzdWJ0aXRsZXMiLCBvdXQgLyAiZnJhbWVzIiwgb3V0IC8gInRpbWVsaW5lIiwKICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgIGF1ZGlvX3J1bj1vdXQgLyAiZmVhdHVyZXMiIGlmIGZlYXR1cmVzIGVsc2UgTm9uZSkK
ICAgICAgICAgICAgICAgIGNoaWxkcmVuLmFwcGVuZCgidGltZWxpbmUiKQogICAgICAgIGRhdGEgPSB7InNjaGVtYSI6ICJhdmUu
YnVuZGxlLnYxIiwgInNvdXJjZV9zaGEyNTYiOiBzb3VyY2VbInNoYTI1NiJdLCAic2VsZWN0ZWRfc3RyZWFtcyI6IHNlbGVjdGVk
LAogICAgICAgICAgICAgICAgImNoaWxkcmVuIjogY2hpbGRyZW4sICJpbnZlbnRvcnlfcnVuIjogImludmVudG9yeSIsICJyZXZp
ZXdfc3RhdHVzIjogIk5PVF9SRVZJRVdFRCIsCiAgICAgICAgICAgICAgICAic2NvcGUiOiAiUHJlcGFyZWQgZXZpZGVuY2UgYW5k
IG5hdmlnYXRpb24uIE5vIGFjdHVhbCBpbWFnZSwgbW90aW9uIG9yIGxpc3RlbmluZyByZXZpZXcgaXMgYXNzZXJ0ZWQuIn0KICAg
ICAgICB3cml0ZV9qc29uKG91dCAvICJidW5kbGUuanNvbiIsIGRhdGEpCiAgICAgICAgdGV4dCA9ICIjIEFWIGV2aWRlbmNlIGJ1
bmRsZVxuXG5TdGF0dXM6ICoqR0VORVJBVEVEIOKAlCBOT1QgUkVWSUVXRUQqKi5cblxuIgogICAgICAgIHRleHQgKz0gIkV2ZXJ5
IGNoaWxkIHJ1biBpbmNsdWRlcyBzb3VyY2UgaWRlbnRpdHksIGNvbW1hbmRzLCBtZXRob2QgcGFyYW1ldGVycyBhbmQgYXJ0aWZh
Y3QgaGFzaGVzLlxuXG4iCiAgICAgICAgdGV4dCArPSAifCBDb21wb25lbnQgfCBNYW5pZmVzdCB8XG58LS0tfC0tLXxcbiIKICAg
ICAgICBmb3IgY2hpbGQgaW4gY2hpbGRyZW46CiAgICAgICAgICAgIHRleHQgKz0gZiJ8IHtjaGlsZH0gfCBbe2NoaWxkfS9ydW4u
anNvbl0oe2NoaWxkfS9ydW4uanNvbikgfFxuIgogICAgICAgIHRleHQgKz0gIlxuVXNlIGFjdHVhbCBvcmlnaW5hbC1QVFMgZnJh
bWUgbG9jYXRvcnMsIGFuZCBkaXN0aW5ndWlzaCByZXF1ZXN0ZWQgdGltZSBmcm9tIGRlY29kZWQgdGltZS4gIgogICAgICAgIHRl
eHQgKz0gIkF1ZGlvIG1lYXN1cmVtZW50cyBkZXNjcmliZSBhIHNpZ25hbDsgdGhleSBkbyBub3QgZXN0YWJsaXNoIGRpcmVjdCBs
aXN0ZW5pbmcgb3Igc3BlYWtlciBpbnRlbnRpb24uICIKICAgICAgICB0ZXh0ICs9ICJDb21wbGV0ZSByZWFsIHJldmlldyBhbmQg
cHJlc2VudGF0aW9uIHJlY29yZHMgc2VwYXJhdGVseSwgdGhlbiB2YWxpZGF0ZSB0aGVtIGFnYWluc3QgdGhlIGludmVudG9yeS5c
biIKICAgICAgICAob3V0IC8gIklOREVYLm1kIikud3JpdGVfdGV4dCh0ZXh0LCBlbmNvZGluZz0idXRmLTgiKQogICAgICAgIHJl
c3VsdCA9IGZpbmlzaF9ydW4ob3V0LCAiYnVuZGxlIiwgZGVwZW5kZW5jaWVzLCB7ImludGVydmFsIjogaW50ZXJ2YWwsICJ3aWR0
aCI6IHdpZHRoLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgInNob3RzIjogc2hvdHMsICJmZWF0dXJlcyI6IGZlYXR1cmVz
fSwgeyJyZXN1bHRfZmlsZSI6ICJidW5kbGUuanNvbiIsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAiY2hpbGRfcnVucyI6
IGNoaWxkcmVuLCAiaW52ZW50b3J5X3J1biI6ICJpbnZlbnRvcnkifSkKICAgIHJldHVybiByZXN1bHQK
```

## avevidence/cli.py

SHA-256: `6b18397ad979210e8a10780371a960a3f13f528774cc706cb7029e429b521fb0`.

```python
"""Portable command-line interface; all media outputs use new run directories."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

from . import __version__
from .common import AVError, environment, finish_run, output_transaction, probe_source, write_json


def parser():
    p = argparse.ArgumentParser(prog="ave", description="Prepare verifiable audiovisual evidence. Computation is not listening.")
    p.add_argument("--version", action="version", version=__version__)
    commands = p.add_subparsers(dest="command", required=True)
    commands.add_parser("doctor", help="Report software dependencies; does not verify perception")
    d = commands.add_parser("probe", help="Record source identity, streams and source clock")
    d.add_argument("input"); d.add_argument("output")
    d = commands.add_parser("inventory", help="Admit logical sources and materializations from JSON")
    d.add_argument("config"); d.add_argument("output")
    d = commands.add_parser("extract-audio", help="Extract native decoded audio with source-time mapping")
    d.add_argument("input"); d.add_argument("output")
    d.add_argument("--audio-stream", type=int)
    d.add_argument("--format", choices=["wav", "flac", "preserve"], default="wav")
    d = commands.add_parser("audio-metrics", help="Bounded or whole-stream loudness measurements")
    d.add_argument("input"); d.add_argument("output")
    d.add_argument("--audio-stream", type=int); d.add_argument("--start"); d.add_argument("--end")
    d = commands.add_parser("cue-features", help="Features for source-bound subtitle windows")
    d.add_argument("audio"); d.add_argument("dialogue_csv"); d.add_argument("output")
    d.add_argument("--audio-stream", type=int)
    d.add_argument("--pitch", action="store_true")
    d.add_argument("--confirm-isolated-speech", action="store_true")
    d.add_argument("--profile", choices=["speech", "music"], default="speech")
    d = commands.add_parser("compare-audio", help="Compare native decoded audio, layout and clocks separately")
    d.add_argument("a"); d.add_argument("b"); d.add_argument("output")
    d.add_argument("--a-stream", type=int); d.add_argument("--b-stream", type=int)
    d = commands.add_parser("frames", help="Extract frames with original source PTS")
    d.add_argument("input"); d.add_argument("output")
    d.add_argument("--mode", choices=["interval", "dense", "source", "exact", "shots"], default="interval")
    d.add_argument("--start"); d.add_argument("--end")
    d.add_argument("--interval", type=float, default=2.0); d.add_argument("--fps", type=float, default=10)
    d.add_argument("--timestamps", nargs="+"); d.add_argument("--threshold", type=float, default=.35)
    d.add_argument("--width", type=int, default=1280); d.add_argument("--video-stream", type=int)
    d = commands.add_parser("contacts", help="Create contact sheets from verified current-run artifacts")
    d.add_argument("frame_run"); d.add_argument("output")
    d.add_argument("--columns", type=int, default=4); d.add_argument("--rows", type=int, default=4)
    d.add_argument("--thumb-width", type=int, default=360)
    d = commands.add_parser("subtitles", help="Parse strict UTF text or extract a selected subtitle stream")
    d.add_argument("input"); d.add_argument("output")
    d.add_argument("--media", action="store_true"); d.add_argument("--subtitle-stream", type=int)
    d.add_argument("--source-media"); d.add_argument("--offset", type=float, default=0)
    d = commands.add_parser("timeline", help="Join source-bound captions, frames and optional audio features")
    d.add_argument("subtitle_run"); d.add_argument("frame_run"); d.add_argument("output")
    d.add_argument("--audio-run"); d.add_argument("--max-distance", type=float, default=2)
    for name in ("clip-audio", "clip-av"):
        d = commands.add_parser(name, help="Create a bounded review derivative with checked source mapping")
        d.add_argument("input"); d.add_argument("output")
        d.add_argument("--start", required=True); d.add_argument("--end", required=True)
        d.add_argument("--pad", type=float, default=0)
        d.add_argument("--audio-stream", type=int)
        if name == "clip-av": d.add_argument("--video-stream", type=int)
    d = commands.add_parser("bundle", help="Prepare a source, audio, frames, captions and navigation bundle")
    d.add_argument("input"); d.add_argument("output")
    d.add_argument("--subtitles"); d.add_argument("--subtitle-stream", type=int)
    d.add_argument("--audio-stream", type=int); d.add_argument("--video-stream", type=int)
    d.add_argument("--interval", type=float, default=2); d.add_argument("--width", type=int, default=1280)
    d.add_argument("--shots", action="store_true"); d.add_argument("--cue-features", action="store_true")
    d = commands.add_parser("verify", help="Verify artifact hashes and run structure")
    d.add_argument("run_dir"); d.add_argument("--verify-sources", action="store_true")
    d = commands.add_parser("review-templates", help="Write invalid-until-completed capability and review examples")
    d.add_argument("output")
    d = commands.add_parser("review-check", help="Validate review declarations; does not prove actual perception")
    d.add_argument("records"); d.add_argument("inventory_or_run"); d.add_argument("capabilities"); d.add_argument("output")
    d = commands.add_parser("pack", help="Create a deterministic allowlisted evidence ZIP")
    d.add_argument("run_dir"); d.add_argument("archive")
    d = commands.add_parser("verify-archive", help="Check archive membership, CRC and hashes without extracting")
    d.add_argument("archive")
    return p


def dispatch(a):
    c = a.command
    if c == "doctor":
        return environment()
    if c == "probe":
        source = probe_source(a.input)
        with output_transaction(a.output, [a.input]) as out:
            write_json(out / "source.json", source)
            value = finish_run(out, "probe", [source], metadata={"result_file": "source.json"})
        return value
    if c in {"inventory", "verify"}:
        from .inventory import inventory, verify_run
        return inventory(a.config, a.output) if c == "inventory" else verify_run(a.run_dir, verify_sources=a.verify_sources)
    if c in {"extract-audio", "audio-metrics", "cue-features", "compare-audio", "clip-audio"}:
        from . import audio
        if c == "extract-audio": return audio.extract_audio(a.input, a.output, stream_index=a.audio_stream, format=a.format)
        if c == "audio-metrics": return audio.measure_audio(a.input, a.output, stream_index=a.audio_stream, start=a.start, end=a.end)
        if c == "cue-features": return audio.cue_features(a.audio, a.dialogue_csv, a.output, stream_index=a.audio_stream,
                    pitch=a.pitch, confirm_isolated_speech=a.confirm_isolated_speech, profile=a.profile)
        if c == "compare-audio": return audio.compare_audio(a.a, a.b, a.output, a_stream=a.a_stream, b_stream=a.b_stream)
        if c == "clip-audio": return audio.clip_audio(a.input, a.output, stream_index=a.audio_stream, start=a.start, end=a.end, pad=a.pad)
    if c in {"frames", "contacts"}:
        from .visual import extract_frames, contact_sheets
        if c == "contacts": return contact_sheets(a.frame_run, a.output, columns=a.columns, rows=a.rows, thumb_width=a.thumb_width)
        return extract_frames(a.input, a.output, mode=a.mode, start=a.start, end=a.end, interval=a.interval,
                              fps=a.fps, timestamps=a.timestamps, threshold=a.threshold, width=a.width, stream_index=a.video_stream)
    if c == "subtitles":
        from .subtitles import parse_subtitles
        return parse_subtitles(a.input, a.output, stream_index=a.subtitle_stream, media=a.media,
                               source_media=a.source_media, offset=a.offset)
    if c == "timeline":
        from .timeline import align_timeline
        return align_timeline(a.subtitle_run, a.frame_run, a.output, audio_run=a.audio_run, max_distance=a.max_distance)
    if c == "clip-av":
        from .clips import clip_av
        return clip_av(a.input, a.output, start=a.start, end=a.end, pad=a.pad, video_stream=a.video_stream, audio_stream=a.audio_stream)
    if c == "bundle":
        from .bundle import build_bundle
        return build_bundle(a.input, a.output, subtitles=a.subtitles, subtitle_stream=a.subtitle_stream,
                            audio_stream=a.audio_stream, video_stream=a.video_stream, interval=a.interval,
                            width=a.width, shots=a.shots, features=a.cue_features)
    if c in {"review-templates", "review-check"}:
        from .reviews import validate_reviews, write_review_templates
        return write_review_templates(a.output) if c == "review-templates" else validate_reviews(a.records, a.inventory_or_run, a.capabilities, a.output)
    if c in {"pack", "verify-archive"}:
        from .packaging import pack_run, verify_archive
        return pack_run(a.run_dir, a.archive) if c == "pack" else verify_archive(a.archive)
    raise AVError("Unknown command")


def main(argv=None):
    a = parser().parse_args(argv)
    try:
        value = dispatch(a)
        if isinstance(value, dict) and value.get("schema") == "ave.run.v1":
            display = {"operation": value["operation"], "output": str(Path(a.output).resolve()),
                       "status": value["status"], "metadata": value.get("metadata", {}),
                       "artifact_count": len(value["artifacts"])}
        else:
            display = value
        print(json.dumps(display, ensure_ascii=False, indent=2, allow_nan=False))
        if a.command == "compare-audio":
            status = value.get("metadata", {}).get("comparison_status")
            return {"MATCH": 0, "DIFFERENT": 1, "INDETERMINATE": 3}.get(status, 3)
        if a.command == "review-check":
            meta = value.get("metadata", {})
            if not meta.get("structural_valid", False): return 2
            return 0 if meta.get("full_required_coverage", False) else 3
        if a.command == "doctor":
            return 0 if all(x.get("path") for x in value["programs"].values()) else 2
        return 0
    except (AVError, OSError, ValueError, KeyError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    except KeyboardInterrupt:
        print("Interrupted. No incomplete run was published.", file=sys.stderr)
        return 130


if __name__ == "__main__":
    raise SystemExit(main())
```

## avevidence/clips.py

SHA-256: `bbbfcde239f088d21b570d9646f74d91d223a30957909e7dd7770b9217eda550`.

```python
"""Bounded AV review clips with explicit source/derivative clock mappings."""
from __future__ import annotations

import json
from pathlib import Path

from .common import (AVError, finite, finish_run, interval, output_transaction,
                     probe_source, run, select_stream, sha256, write_json)


def _rate(value):
    try:
        a, b = str(value).split("/")
        return float(a) / float(b)
    except (ValueError, ZeroDivisionError):
        return None


def _windows(source, stream):
    data = json.loads(run(["ffprobe", "-v", "error", "-select_streams", str(stream["index"]),
                           "-show_frames", "-show_entries",
                           "frame=best_effort_timestamp_time,pts_time,duration_time,pkt_duration_time,nb_samples",
                           "-of", "json", source["path"]]).stdout)
    windows = []
    tolerance = max(0.000002, (_rate(stream.get("time_base")) or 0) * 1.01)
    max_adjustment = 0.0
    for frame in data.get("frames", []):
        raw = frame.get("best_effort_timestamp_time", frame.get("pts_time"))
        if raw is None:
            raise AVError("Decoded clip frame has no presentation timestamp")
        start = finite(raw, "decoded PTS")
        if stream["codec_type"] == "audio":
            samples = int(frame.get("nb_samples", 0))
            duration = samples / int(stream["sample_rate"])
        else:
            duration = frame.get("duration_time", frame.get("pkt_duration_time"))
            # Average frame rate cannot establish a VFR frame's actual extent.
            duration = finite(duration, "frame duration", 0) if duration is not None else 0
        if duration <= 0:
            raise AVError("Decoded clip frame has no positive extent")
        end = start + duration
        if windows and abs(windows[-1][1] - start) <= tolerance:
            max_adjustment = max(max_adjustment, abs(windows[-1][1] - start))
            windows[-1][1] += duration
        else:
            if windows and start < windows[-1][1] - tolerance:
                raise AVError("Overlapping clip timestamps need explicit normalization")
            windows.append([start, end])
    if not windows:
        raise AVError("Requested interval has no decoded frames for a selected modality")
    return windows, tolerance, max_adjustment


def clip_av(input, output, *, start, end, pad=0.0, video_stream=None, audio_stream=None):
    source = probe_source(input)
    video = select_stream(source, "video", video_stream)
    audio = select_stream(source, "audio", audio_stream, required=False)
    from .visual import _geometry
    _geometry(video, 0)
    rotation = video.get("tags", {}).get("rotate", 0)
    if finite(rotation, "rotation") % 360:
        raise AVError("Rotated sources require explicit normalization before review clipping")
    if any(finite(x.get("rotation", 0), "rotation") % 360 for x in video.get("side_data_list", [])):
        raise AVError("Rotated sources require explicit normalization before review clipping")
    a, b = interval(start, end, source["duration_seconds"])
    padding = finite(pad, "padding", 0)
    if b - a + 2 * padding > 120:
        raise AVError("Review clips are limited to 120 seconds including requested padding")
    begin = max(0.0, a - padding)
    finish = min(source["duration_seconds"], b + padding) if source["duration_seconds"] is not None else b + padding
    absolute_begin = begin + source["origin_seconds"]
    absolute_end = finish + source["origin_seconds"]
    with output_transaction(output, inputs=[source["path"]]) as out:
        destination = out / "clip.mkv"
        filters = [f"[0:{video['index']}]trim=start={absolute_begin:.9f}:end={absolute_end:.9f},settb=expr=1/1000000,"
                   f"setpts=PTS-({absolute_begin:.9f})/TB[v]"]
        if audio:
            filters.append(f"[0:{audio['index']}]atrim=start={absolute_begin:.9f}:end={absolute_end:.9f},"
                           f"asetpts=PTS-({absolute_begin:.9f})/TB[a]")
        cmd = ["ffmpeg", "-v", "error", "-nostdin", "-n", "-copyts", "-noautorotate", "-i", source["path"],
               "-filter_complex", ";".join(filters), "-map", "[v]", "-c:v", "ffv1", "-level", "3",
               "-fps_mode", "passthrough", "-enc_time_base:v", "1:1000000"]
        if audio:
            cmd += ["-map", "[a]", "-c:a", "pcm_f64le"]
        cmd += [str(destination)]
        run(cmd, timeout=300)
        derivative = probe_source(destination)
        mappings = []
        for kind, parent in (("video", video), ("audio", audio)):
            if parent is None:
                continue
            selected = select_stream(derivative, kind)
            windows, tolerance, adjustment = _windows(derivative, selected)
            segments = [{"parent_start_seconds": x + begin,
                         "parent_end_seconds": y + begin,
                         "derivative_start_seconds": x - derivative["origin_seconds"],
                         "derivative_end_seconds": y - derivative["origin_seconds"]} for x, y in windows]
            mappings.append({"parent_source_sha256": source["sha256"], "parent_stream_index": parent["index"],
                             "derivative_stream_index": selected["index"],
                             "modality": "motion" if kind == "video" else "audio",
                             "artifact_path": "clip.mkv", "artifact_sha256": sha256(destination),
                             "segments": segments, "timestamp_tolerance_seconds": tolerance,
                             "maximum_timestamp_adjustment_seconds": adjustment})
        data = {"schema": "ave.clip.v1", "artifact_path": "clip.mkv", "artifact_sha256": sha256(destination),
                "requested_interval_seconds": [a, b], "padded_interval_seconds": [begin, finish],
                "derivative_origin_seconds": derivative["origin_seconds"],
                "review_mappings": mappings, "review_status": "NOT_REVIEWED",
                "codecs": {"video": "ffv1", "audio": "pcm_f64le" if audio else None},
                "scope": "Review derivative. Selected source video frames and decoded audio are re-encoded; not an encoded-packet copy.",
                "boundary_policy": "Video frame extents can cross a requested endpoint. Actual decoded extents are recorded, not replaced by requested times."}
        write_json(out / "clip.json", data)
        result = finish_run(out, "clip-av", [source], {"start": a, "end": b, "pad": padding},
                            {"result_file": "clip.json", "review_mappings": mappings})
    return result
```

## avevidence/common.py

SHA-256: `82245b3e182a023ba880c1d90a2fe72cfc91834a19450ec2f4a0863215dab923`.

```python
"""Shared safety, source identity, clock, execution and manifest primitives."""
from __future__ import annotations

import contextlib
import contextvars
import csv
import hashlib
import importlib.metadata
import json
import math
import os
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import uuid
from datetime import datetime, timezone

from . import __version__


class AVError(RuntimeError):
    pass


_journal = contextvars.ContextVar("command_journal", default=None)


def sha256(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def utc_now():
    return datetime.now(timezone.utc).isoformat()


def finite(value, name="value", minimum=None):
    try:
        x = float(value)
    except (ValueError, TypeError) as exc:
        raise AVError(f"{name} must be a finite number") from exc
    if not math.isfinite(x) or (minimum is not None and x < minimum):
        raise AVError(f"Invalid {name}: {value!r}")
    return x


def parse_time(value):
    if value is None:
        return None
    if isinstance(value, str) and ":" in value:
        parts = value.split(":")
        if len(parts) not in (2, 3):
            raise AVError(f"Invalid timecode: {value!r}")
        nums = [finite(x, "time component", 0) for x in parts]
        if any(x >= 60 for x in nums[1:]):
            raise AVError(f"Invalid timecode: {value!r}")
        return sum(x * 60 ** i for i, x in enumerate(reversed(nums)))
    return finite(value, "time", 0)


def interval(start, end, duration=None):
    a = parse_time(start) if start is not None else 0.0
    b = parse_time(end) if end is not None else duration
    if b is None:
        raise AVError("An end time is required when duration is unavailable")
    b = finite(b, "end", 0)
    if b <= a:
        raise AVError("Require start < end")
    if duration is not None and b > duration + 0.001:
        raise AVError("Requested interval exceeds the source timeline")
    return a, b


def run(argv, *, check=True, timeout=180, binary=False, stdout_file=None):
    args = [str(x) for x in argv]
    if not args or not shutil.which(args[0]):
        raise AVError(f"Executable not found: {args[0] if args else '(empty command)'}")
    kwargs = {"stdin": subprocess.DEVNULL, "stderr": subprocess.PIPE, "timeout": timeout}
    if not binary:
        kwargs.update(text=True, encoding="utf-8", errors="replace")
    stream = None
    try:
        if stdout_file is not None:
            stream = Path(stdout_file).open("xb")
        p = subprocess.run(args, stdout=stream or subprocess.PIPE, **kwargs)
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise AVError(f"Command could not complete: {args[0]}: {exc}") from exc
    finally:
        if stream is not None:
            stream.close()
    log = _journal.get()
    if log is not None:
        stderr = p.stderr.decode("utf-8", "replace") if isinstance(p.stderr, bytes) else p.stderr
        stdout = p.stdout if isinstance(p.stdout, str) else None
        log.append({"argv": args, "returncode": p.returncode, "stderr": stderr,
                    "stdout": stdout, "stdout_file": str(stdout_file) if stdout_file else None})
    if check and p.returncode:
        error = p.stderr.decode("utf-8", "replace") if isinstance(p.stderr, bytes) else p.stderr
        raise AVError(f"Command failed ({p.returncode}): {args[0]}\n{error[-4000:]}")
    return p


def write_json(path, obj):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("x", encoding="utf-8", newline="\n") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2, allow_nan=False)
        f.write("\n")


def read_json(path):
    with Path(path).open(encoding="utf-8-sig") as f:
        return json.load(f, parse_constant=lambda s: (_ for _ in ()).throw(AVError(f"Nonfinite JSON: {s}")))


def write_csv(path, rows, fields):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("x", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def read_csv(path):
    with Path(path).open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def file_record(path, kind="file"):
    p = Path(path).resolve()
    if not p.is_file():
        raise AVError(f"Input file does not exist: {p}")
    digest = sha256(p)
    return {"schema": "ave.file.v1", "kind": kind, "path": str(p), "sha256": digest,
            "size_bytes": p.stat().st_size, "duration_seconds": None, "origin_seconds": 0.0,
            "streams": [], "probe": {}}


def probe_source(path):
    from fractions import Fraction
    import tempfile

    p = Path(path).resolve()
    if not p.is_file():
        raise AVError(f"Source file does not exist: {p}")
    before = p.stat()
    digest = sha256(p)
    probe_command = ["ffprobe", "-v", "error", "-show_format", "-show_streams",
                     "-show_chapters", "-of", "json", str(p)]
    raw = json.loads(run(probe_command).stdout)
    after = p.stat()
    if (before.st_size, before.st_mtime_ns) != (after.st_size, after.st_mtime_ns) or sha256(p) != digest:
        raise AVError("Source changed during probe")
    fmt = raw.get("format", {})
    reported_duration = finite(fmt["duration"], "format duration", 0) if fmt.get("duration") not in (None, "N/A") else None
    reported_start = finite(fmt["start_time"], "format start") if fmt.get("start_time") not in (None, "N/A") else None
    names = set(fmt.get("format_name", "").split(","))
    # MOV/MP4 stream duration_ts describes the declared presentation interval,
    # including container edits. Intrinsic lossless-audio sample counts also
    # have a defined zero-origin interpretation. Other container durations are
    # not guessed to mean either a span or an absolute endpoint.
    presentation_container = bool(names & {"mov", "mp4", "m4a", "3gp", "3g2", "mj2"})
    intrinsic_sample_clock = bool(names & {"wav", "flac", "aiff", "au"})
    temporal = [s for s in raw.get("streams", []) if s.get("codec_type") in {"audio", "video", "subtitle"}
                and not (s.get("codec_type") == "video" and s.get("disposition", {}).get("attached_pic"))]
    bounds, pending, uncertainty = [], {}, []
    for stream in temporal:
        index = stream["index"]
        try:
            tb = Fraction(stream["time_base"])
            if tb <= 0:
                raise ValueError("nonpositive time base")
        except (KeyError, ValueError, ZeroDivisionError):
            bounds.append({"stream_index": index, "codec_type": stream["codec_type"], "basis": "UNAVAILABLE",
                           "start_seconds": None, "end_seconds": None, "issues": ["missing valid stream time base"]})
            continue
        start_ticks = stream.get("start_pts")
        duration_ticks = stream.get("duration_ts")
        use_declared = presentation_container or (intrinsic_sample_clock and stream["codec_type"] == "audio")
        if use_declared and duration_ticks not in (None, "N/A") and (start_ticks not in (None, "N/A") or intrinsic_sample_clock):
            start_value = int(start_ticks) if start_ticks not in (None, "N/A") else 0
            duration_value = int(duration_ticks)
            if duration_value >= 0:
                bounds.append({"stream_index": index, "codec_type": stream["codec_type"],
                               "basis": "container_stream_presentation_interval" if presentation_container else "intrinsic_audio_sample_count",
                               "start_pts": start_value, "duration_ticks": duration_value, "time_base": str(tb),
                               "start_seconds": float(start_value * tb), "end_seconds": float((start_value + duration_value) * tb),
                               "issues": []})
                continue
        pending[index] = {"stream_index": index, "codec_type": stream["codec_type"], "basis": "explicit_packet_pts_plus_duration",
                          "time_base": str(tb), "start_seconds": None, "end_seconds": None,
                          "packet_count": 0, "issues": []}
    packet_scan = None
    if pending:
        packet_command = ["ffprobe", "-v", "error", "-show_packets", "-show_entries",
                          "packet=stream_index,pts,duration:packet_side_data=", "-of", "compact=p=0:nk=0", str(p)]
        # Bound memory and command-journal size: aggregate the packet timeline
        # from a temporary file rather than capturing the whole packet table.
        with tempfile.TemporaryDirectory(prefix="ave-clock-") as temporary:
            temporary_path = Path(temporary).resolve()
            if temporary_path.parent != Path(tempfile.gettempdir()).resolve():
                raise AVError("Unexpected packet-probe temporary directory")
            packet_file = temporary_path / "packets.txt"
            run(packet_command, stdout_file=packet_file)
            with packet_file.open(encoding="utf-8", errors="strict") as packet_rows:
                for line in packet_rows:
                    fields = dict(part.split("=", 1) for part in line.strip().split("|") if "=" in part)
                    if "stream_index" not in fields:
                        continue
                    index = int(fields["stream_index"])
                    if index not in pending:
                        continue
                    item = pending[index]
                    item["packet_count"] += 1
                    if fields.get("pts") in (None, "N/A") or fields.get("duration") in (None, "N/A"):
                        if "packet lacks PTS or duration" not in item["issues"]:
                            item["issues"].append("packet lacks PTS or duration")
                        continue
                    pts, ticks = int(fields["pts"]), int(fields["duration"])
                    if ticks <= 0:
                        if "packet lacks positive duration" not in item["issues"]:
                            item["issues"].append("packet lacks positive duration")
                        continue
                    tb = Fraction(item["time_base"])
                    begin, stop = float(pts * tb), float((pts + ticks) * tb)
                    item["start_seconds"] = begin if item["start_seconds"] is None else min(item["start_seconds"], begin)
                    item["end_seconds"] = stop if item["end_seconds"] is None else max(item["end_seconds"], stop)
            packet_scan = {"command": packet_command, "table_sha256": sha256(packet_file),
                           "table_size_bytes": packet_file.stat().st_size,
                           "method": "streamed original packet PTS plus positive packet duration, aggregated per temporal stream"}
        for item in pending.values():
            if item["packet_count"] == 0:
                item["basis"] = "empty_packet_stream"
            if item["issues"]:
                item["observed_partial_end_seconds"] = item["end_seconds"]
                item["end_seconds"] = None
            bounds.append(item)
        uncertainty.append("Packet presentation bounds do not establish decoder trim, codec padding, continuous coverage or AV synchronization.")
    if reported_start is not None:
        origin, origin_basis = reported_start, "format.start_time"
    else:
        known_starts = [b["start_seconds"] for b in bounds if b["start_seconds"] is not None]
        if known_starts:
            origin, origin_basis = min(known_starts), "minimum_known_stream_presentation_start"
        else:
            origin, origin_basis = 0.0, "explicit_fallback_zero_no_known_presentation_start"
            uncertainty.append("No presentation start was available; zero origin is an explicit convention.")
    active = [b for b in bounds if b["basis"] != "empty_packet_stream"]
    if active and all(b["end_seconds"] is not None for b in active):
        duration = max(0.0, max(b["end_seconds"] for b in active) - origin)
        duration_basis = "maximum_stream_presentation_end_minus_source_origin"
    elif bounds and not active:
        duration, duration_basis = 0.0, "no_temporal_packets"
    else:
        duration, duration_basis = None, "UNAVAILABLE_INCOMPLETE_STREAM_BOUNDS"
        uncertainty.append("Canonical duration is unavailable because at least one temporal stream lacks a complete endpoint; supply a bounded interval.")
    if any(b["basis"] == "container_stream_presentation_interval" for b in bounds):
        uncertainty.append("Declared container stream intervals are used as presentation bounds; decoded sample padding may differ.")
    for bound in bounds:
        bound["canonical_start_seconds"] = None if bound["start_seconds"] is None else bound["start_seconds"] - origin
        bound["canonical_end_seconds"] = None if bound["end_seconds"] is None else bound["end_seconds"] - origin
    final_stat = p.stat()
    if (before.st_size, before.st_mtime_ns) != (final_stat.st_size, final_stat.st_mtime_ns) or sha256(p) != digest:
        raise AVError("Source changed during timeline probing")
    return {"schema": "ave.source.v1", "path": str(p), "sha256": digest,
            "size_bytes": after.st_size, "duration_seconds": duration,
            "format_duration_seconds": reported_duration, "format_start_time_seconds": reported_start,
            "duration_basis": duration_basis, "duration_uncertainty": uncertainty,
            "stream_timeline_bounds": sorted(bounds, key=lambda b: b["stream_index"]),
            "packet_bounds_scan": packet_scan, "origin_basis": origin_basis,
            "origin_seconds": origin, "streams": raw.get("streams", []), "probe": raw,
            "probe_command": probe_command}


def select_stream(source, kind, index=None, required=True):
    streams = [s for s in source.get("streams", []) if s.get("codec_type") == kind
               and not (kind == "video" and s.get("disposition", {}).get("attached_pic"))]
    if index is not None:
        if type(index) is not int or index < 0:
            raise AVError("Stream index must be a nonnegative integer")
        streams = [s for s in streams if s.get("index") == index]
    if not streams:
        if required or index is not None:
            raise AVError(f"No matching {kind} stream (indices are absolute ffprobe indices)")
        return None
    if len(streams) != 1:
        raise AVError(f"Multiple {kind} streams; choose an explicit absolute stream index")
    return streams[0]


def verify_source(source):
    if not Path(source["path"]).is_file() or sha256(source["path"]) != source["sha256"]:
        raise AVError("Source changed after admission")


def safe_member(root, relative):
    base = Path(root).resolve()
    rel = Path(relative)
    if rel.is_absolute() or ".." in rel.parts or ":" in str(relative) or "\\" in str(relative):
        raise AVError(f"Unsafe artifact path: {relative!r}")
    p = (base / rel).resolve()
    if not p.is_relative_to(base):
        raise AVError("Artifact path escapes its bundle")
    return p


@contextlib.contextmanager
def output_transaction(output, inputs=()):
    target = Path(output).resolve()
    for item in inputs:
        src = Path(item).resolve()
        if target == src or src.is_relative_to(target) or (src.is_dir() and target.is_relative_to(src)):
            raise AVError("Output must not replace, contain or be created inside an input")
    if target.exists():
        raise AVError(f"Output already exists; use a new run directory: {target}")
    target.parent.mkdir(parents=True, exist_ok=True)
    stage = target.parent / ("." + target.name + ".staging-" + uuid.uuid4().hex)
    stage.mkdir()
    token = _journal.set([])
    try:
        yield stage
        if target.exists():
            raise AVError("Output appeared during processing; refusing replacement")
        stage.rename(target)
    except BaseException as exc:
        if stage.exists():
            try:
                write_json(stage / "FAILED.json", {"status": "FAILED_NOT_PUBLISHED", "error": str(exc),
                                                    "created_at": utc_now()})
            except (OSError, ValueError):
                pass
        raise
    finally:
        _journal.reset(token)


def environment():
    packages = {}
    for name in ("Pillow", "numpy", "soundfile", "librosa"):
        try:
            packages[name] = importlib.metadata.version(name)
        except importlib.metadata.PackageNotFoundError:
            packages[name] = None
    programs = {}
    for name in ("ffmpeg", "ffprobe"):
        executable = shutil.which(name)
        programs[name] = {"path": executable, "version": None}
        if executable:
            programs[name]["version"] = run([name, "-version"], timeout=20).stdout.splitlines()[0]
    code_hashes = {p.name: sha256(p) for p in sorted(Path(__file__).parent.glob("*.py"))}
    return {"tool_version": __version__, "python": sys.version, "platform": platform.platform(),
            "programs": programs, "packages": packages,
            "implementation_sha256": code_hashes,
            "perceptual_capabilities": {"audio": "NOT_VERIFIED", "motion": "NOT_VERIFIED", "images": "NOT_VERIFIED"}}


def finish_run(stage, operation, sources, parameters=None, metadata=None):
    out = Path(stage)
    for source in sources:
        verify_source(source)
    env = environment()
    write_json(out / "commands.json", _journal.get() or [])
    artifacts = []
    for p in sorted(out.rglob("*")):
        if p.is_symlink():
            raise AVError("Symlink artifacts are not allowed")
        if p.is_file():
            artifacts.append({"path": p.relative_to(out).as_posix(), "sha256": sha256(p), "size_bytes": p.stat().st_size})
    manifest = {"schema": "ave.run.v1", "operation": operation, "created_at": utc_now(),
                "status": "GENERATED_NOT_REVIEWED", "sources": sources,
                "parameters": parameters or {}, "metadata": metadata or {},
                "environment": env, "artifacts": artifacts}
    write_json(out / "run.json", manifest)
    return manifest
```

## avevidence/inventory.py

SHA-256: `d5f9d404597b73a9a43046930e6b8d5b3bbb09688a96c41fb05a5b9085d1bd02`.

```python
"""Explicit source admission and portable run verification.

Hashes bind bytes, not source authenticity or perceptual review. Bundle checking
does not require another person's original absolute media paths to exist.
"""
from __future__ import annotations

from collections import defaultdict
from datetime import datetime
from pathlib import Path, PurePosixPath
import re

from .common import (AVError, finish_run, output_transaction, probe_source,
                     read_json, safe_member, select_stream, sha256, utc_now,
                     write_json)

MODALITIES = {"audio", "motion", "visual_stills"}
_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9_.:-]{0,127}\Z")
_HASH = re.compile(r"[0-9a-f]{64}\Z")
_PLACEHOLDER = re.compile(r"\b(?:TODO|TBD|PLACEHOLDER|REPLACE(?:_[A-Z0-9]+)*|YOUR_[A-Z0-9_]+)\b|<[^>]+>", re.I)


def text_value(value, name):
    if not isinstance(value, str) or not value.strip() or value != value.strip():
        raise AVError(f"{name} must be a nonempty trimmed string")
    if _PLACEHOLDER.search(value):
        raise AVError(f"{name} contains an unfinished placeholder")
    return value


def identifier(value, name="identifier"):
    text_value(value, name)
    if not _ID.fullmatch(value):
        raise AVError(f"Invalid {name}")
    return value


def digest_value(value, name="SHA-256"):
    if not isinstance(value, str) or not _HASH.fullmatch(value) or len(set(value)) == 1:
        raise AVError(f"{name} must be a completed lowercase SHA-256 digest")
    return value


def integer(value, name, minimum=0):
    if type(value) is not int or value < minimum:
        raise AVError(f"{name} must be an integer >= {minimum}")
    return value


def number(value, name, minimum=0):
    import math
    if type(value) not in (int, float) or not math.isfinite(value) or value < minimum:
        raise AVError(f"{name} must be a finite JSON number >= {minimum}")
    return float(value)


def date_value(value, name="date"):
    text_value(value, name)
    if not re.fullmatch(r"\d{4}-\d\d-\d\dT\d\LOCAL_DRIVE_D\d\LOCAL_DRIVE_D\d\d(?:\.\d+)?(?:Z|[+-]\d\LOCAL_DRIVE_D\d\d)", value):
        raise AVError(f"{name} must be an ISO date-time with an explicit timezone")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise AVError(f"Invalid {name}") from exc
    if parsed.utcoffset() is None:
        raise AVError(f"{name} requires a timezone")
    return parsed


def intervals(value, duration=None, name="intervals_seconds"):
    if not isinstance(value, list) or not value:
        raise AVError(f"{name} must be a nonempty list of [start, end] pairs")
    result = []
    for pair in value:
        if not isinstance(pair, list) or len(pair) != 2:
            raise AVError(f"Malformed {name} pair")
        a, b = [number(x, name) for x in pair]
        if a >= b or (duration is not None and b > duration + 1e-6):
            raise AVError(f"Invalid or out-of-bounds {name}")
        result.append([a, b])
    return result


def points(value, duration=None, name="points_seconds"):
    if not isinstance(value, list) or not value:
        raise AVError(f"{name} must be a nonempty list")
    result = [number(x, name) for x in value]
    if len(set(result)) != len(result):
        raise AVError(f"Duplicate {name}")
    if duration is not None and any(x >= duration for x in result):
        raise AVError(f"Out-of-bounds {name}")
    return sorted(result)


def _config(path):
    data = read_json(path)
    if not isinstance(data, dict) or not isinstance(data.get("sources"), list) or not data["sources"]:
        raise AVError("Inventory config requires a nonempty sources list")
    allowed = {"schema", "sources", "required_logical_source_ids"}
    if set(data) - allowed:
        raise AVError(f"Unknown inventory config fields: {sorted(set(data) - allowed)}")
    if data.get("schema", "ave.inventory.config.v1") != "ave.inventory.config.v1":
        raise AVError("Unsupported inventory config schema")
    return data


def inventory(config, output):
    """Admit every configured file; fail transactionally on omissions/ambiguity."""
    config = Path(config).resolve()
    data = _config(config)
    rows, logical = [], defaultdict(list)
    seen = set()
    allowed = {"logical_source_id", "materialization_id", "path", "selected_streams",
               "required_modalities", "required_intervals_seconds", "required_points_seconds",
               "preferred", "evidence_weight_group", "expected_sha256", "title", "notes"}
    for row in data["sources"]:
        if not isinstance(row, dict) or set(row) - allowed:
            raise AVError("Invalid/unknown materialization config fields")
        lid = identifier(row.get("logical_source_id"), "logical_source_id")
        mid = identifier(row.get("materialization_id"), "materialization_id")
        if mid in seen:
            raise AVError(f"Duplicate materialization_id: {mid}")
        seen.add(mid)
        path = Path(text_value(row.get("path"), "source path"))
        path = (config.parent / path).resolve() if not path.is_absolute() else path.resolve()
        if not path.is_file():
            raise AVError(f"Configured source is missing: {mid}: {path}")
        modalities = row.get("required_modalities")
        if not isinstance(modalities, list) or not modalities or not all(isinstance(x, str) for x in modalities) or len(set(modalities)) != len(modalities) or set(modalities) - MODALITIES:
            raise AVError("Each source requires distinct explicit required_modalities")
        selected = row.get("selected_streams")
        if not isinstance(selected, dict) or set(selected) - {"audio", "video"}:
            raise AVError("selected_streams must declare absolute audio/video indices")
        for kind, index in selected.items():
            integer(index, f"selected {kind} index")
        needed = {"audio" if x == "audio" else "video" for x in modalities}
        if not needed <= set(selected):
            raise AVError("A required modality has no explicitly selected stream")
        if "preferred" in row and type(row["preferred"]) is not bool:
            raise AVError("preferred must be a JSON boolean")
        if "expected_sha256" in row:
            digest_value(row["expected_sha256"], "expected_sha256")
        for key in ("title", "notes", "evidence_weight_group"):
            if key in row:
                text_value(row[key], key)
        if "evidence_weight_group" in row:
            identifier(row["evidence_weight_group"], "evidence_weight_group")
        item = dict(row, path=str(path), required_modalities=sorted(modalities))
        logical[lid].append(item)
        rows.append(item)
    required = data.get("required_logical_source_ids", sorted(logical))
    if not isinstance(required, list):
        raise AVError("required_logical_source_ids must be a distinct list")
    for x in required:
        identifier(x, "required_logical_source_id")
    if len(set(required)) != len(required):
        raise AVError("required_logical_source_ids must be a distinct list")
    if set(required) != set(logical):
        raise AVError("Configured logical source set does not match required_logical_source_ids")
    for lid, group in logical.items():
        if len({tuple(x["required_modalities"]) for x in group}) != 1:
            raise AVError(f"Conflicting required modalities for {lid}")
        for x in group:
            x["preferred"] = x.get("preferred", len(group) == 1)
        if sum(x["preferred"] for x in group) != 1:
            raise AVError(f"Exactly one preferred materialization is required for {lid}")

    with output_transaction(output, [config] + [r["path"] for r in rows]) as stage:
        sources = []
        for row in rows:
            source = probe_source(row["path"])
            if row.get("expected_sha256", source["sha256"]) != source["sha256"]:
                raise AVError(f"Expected source hash mismatch: {row['materialization_id']}")
            duration = number(source.get("duration_seconds"), "source duration")
            if duration <= 0:
                raise AVError("A positive source duration is required for inventory coverage")
            for kind, index in row["selected_streams"].items():
                select_stream(source, kind, index)
            source.update({k: v for k, v in row.items() if k not in ("path", "expected_sha256")})
            req_intervals = row.get("required_intervals_seconds", {})
            if not isinstance(req_intervals, dict) or set(req_intervals) - (set(row["required_modalities"]) - {"visual_stills"}):
                raise AVError("required_intervals_seconds may only name required audio/motion modalities")
            source["required_intervals_seconds"] = {
                m: intervals(req_intervals.get(m, [[0, duration]]), duration, f"required {m} intervals")
                for m in row["required_modalities"] if m != "visual_stills"}
            if "visual_stills" in row["required_modalities"]:
                source["required_points_seconds"] = points(row.get("required_points_seconds"), duration, "required_points_seconds")
            elif "required_points_seconds" in row:
                raise AVError("required_points_seconds requires the visual_stills modality")
            sources.append(source)

        # Connected components join same logical source, declared relationship,
        # and identical bytes. Copies cannot increase independent evidence weight.
        parent = {x["materialization_id"]: x["materialization_id"] for x in sources}
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]; x = parent[x]
            return x
        def join(a, b):
            parent[find(b)] = find(a)
        for key in ("logical_source_id", "sha256", "evidence_weight_group"):
            buckets = defaultdict(list)
            for x in sources:
                if key in x:
                    buckets[x[key]].append(x["materialization_id"])
            for group in buckets.values():
                for mid in group[1:]:
                    join(group[0], mid)
        components = defaultdict(list)
        for x in sources:
            components[find(x["materialization_id"])].append(x)
        weights = []
        for i, group in enumerate(sorted(components.values(), key=lambda g: min(x["materialization_id"] for x in g)), 1):
            gid = f"evidence-{i:04}"
            for x in group:
                x["computed_evidence_weight_group"] = gid
            weights.append({"group_id": gid, "materialization_ids": sorted(x["materialization_id"] for x in group),
                            "logical_source_ids": sorted({x["logical_source_id"] for x in group}),
                            "maximum_independent_evidence_units": 1})
        byte_groups = defaultdict(list)
        for x in sources:
            byte_groups[x["sha256"]].append(x["materialization_id"])
        admitted = {"schema": "ave.inventory.v1", "created_at": utc_now(),
                    "status": "ADMITTED_CONFIG_COMPLETE_NOT_REVIEWED",
                    "completeness_scope": "Exactly the declared config; no external corpus completeness claim",
                    "required_logical_source_ids": sorted(required), "sources": sources,
                    "logical_sources": [{"logical_source_id": lid,
                        "materialization_ids": sorted(x["materialization_id"] for x in sources if x["logical_source_id"] == lid),
                        "preferred_materialization_id": next(x["materialization_id"] for x in sources if x["logical_source_id"] == lid and x["preferred"]),
                        "required_modalities": logical[lid][0]["required_modalities"]} for lid in sorted(logical)],
                    "byte_duplicate_groups": [{"sha256": h, "materialization_ids": ids} for h, ids in sorted(byte_groups.items()) if len(ids) > 1],
                    "evidence_weight_groups": weights,
                    "trust_boundary": "Identity and relationships are declared; hashes establish byte equality, not authenticity or perception."}
        write_json(stage / "inventory.json", admitted)
        return finish_run(stage, "inventory", sources,
                          {"config_sha256": sha256(config)}, {"result_file": "inventory.json"})


def _artifact_path(root, relative):
    text_value(relative, "artifact path")
    if PurePosixPath(relative).as_posix() != relative or relative in (".", "run.json"):
        raise AVError("Artifact paths must be canonical relative file paths and exclude the owning run.json")
    return safe_member(root, relative)


def _validate_source_record(source):
    if not isinstance(source, dict):
        raise AVError("Malformed run source")
    digest_value(source.get("sha256"), "source sha256")
    integer(source.get("size_bytes"), "source size_bytes")
    text_value(source.get("path"), "source path")
    if "streams" in source:
        if not isinstance(source["streams"], list):
            raise AVError("Source streams must be a list")
        seen_indices = set()
        for stream in source["streams"]:
            if not isinstance(stream, dict):
                raise AVError("Malformed source stream")
            index = integer(stream.get("index"), "source stream index")
            if index in seen_indices:
                raise AVError("Duplicate source stream index")
            seen_indices.add(index)
            text_value(stream.get("codec_type"), "stream codec_type")
    for key in ("logical_source_id", "materialization_id"):
        if key in source:
            identifier(source[key], key)
    if "selected_streams" in source:
        if not isinstance(source["selected_streams"], dict):
            raise AVError("selected_streams must be an object")
        for kind, index in source["selected_streams"].items():
            if kind not in ("audio", "video"):
                raise AVError("Invalid selected stream kind")
            integer(index, "selected stream index")
            select_stream(source, kind, index)


def _resolve_source_for_verification(source, root):
    """Use exact internal bytes when a published/moved run lost its stage path."""
    recorded = Path(source["path"])
    recorded = recorded if recorded.is_absolute() else root / recorded
    if recorded.is_file():
        if recorded.stat().st_size == source["size_bytes"] and sha256(recorded) == source["sha256"]:
            return recorded
        raise AVError("Original source verification failed: recorded file changed")
    for ancestor in (root, *root.parents):
        candidate_manifest = ancestor / "run.json"
        if not candidate_manifest.is_file():
            continue
        data = read_json(candidate_manifest)
        if not isinstance(data, dict) or data.get("schema") != "ave.run.v1":
            continue
        for member in data.get("artifacts", []):
            if not isinstance(member, dict) or member.get("sha256") != source["sha256"] or member.get("size_bytes") != source["size_bytes"]:
                continue
            candidate = safe_member(ancestor, member.get("path"))
            if candidate.is_file() and not candidate.is_symlink() and candidate.stat().st_size == source["size_bytes"] and sha256(candidate) == source["sha256"]:
                return candidate
    raise AVError("Original source verification failed: no original or exact hash-bound internal copy")


def verify_run(path, verify_sources=False):
    """Verify artifact identity/membership recursively; no perception assertion."""
    if type(verify_sources) is not bool:
        raise AVError("verify_sources must be a boolean")
    supplied = Path(path)
    manifest_path = supplied / "run.json" if supplied.is_dir() else supplied
    if manifest_path.name != "run.json" or not manifest_path.is_file() or manifest_path.is_symlink():
        raise AVError("Expected a regular run.json or run directory")
    root = manifest_path.parent.resolve()
    data = read_json(manifest_path)
    if not isinstance(data, dict) or data.get("schema") != "ave.run.v1":
        raise AVError("Unsupported run manifest")
    date_value(data.get("created_at"), "run created_at")
    if data.get("status") != "GENERATED_NOT_REVIEWED":
        raise AVError("Run status must retain GENERATED_NOT_REVIEWED")
    text_value(data.get("operation"), "operation")
    sources = data.get("sources")
    if not isinstance(sources, list):
        raise AVError("Run sources must be a list")
    for source in sources:
        _validate_source_record(source)
        if verify_sources:
            _resolve_source_for_verification(source, root)
    artifacts = data.get("artifacts")
    if not isinstance(artifacts, list):
        raise AVError("Run artifacts must be a list")
    declared = set()
    for artifact in artifacts:
        if not isinstance(artifact, dict):
            raise AVError("Malformed artifact record")
        relative = artifact.get("path")
        p = _artifact_path(root, relative)
        if relative in declared:
            raise AVError("Duplicate artifact member")
        declared.add(relative)
        digest_value(artifact.get("sha256"), "artifact sha256")
        integer(artifact.get("size_bytes"), "artifact size_bytes")
        if not p.is_file() or p.is_symlink() or p.stat().st_size != artifact["size_bytes"] or sha256(p) != artifact["sha256"]:
            raise AVError(f"Artifact verification failed: {relative}")
    actual = set()
    for p in root.rglob("*"):
        if p.is_symlink():
            raise AVError("Symlink bundle members are not allowed")
        if p.is_file() and p != manifest_path.resolve():
            actual.add(p.relative_to(root).as_posix())
    if actual != declared:
        raise AVError(f"Artifact membership mismatch; missing={sorted(declared-actual)}, unlisted={sorted(actual-declared)}")
    metadata = data.get("metadata", {})
    if not isinstance(metadata, dict):
        raise AVError("Run metadata must be an object")
    result_file = metadata.get("result_file")
    if result_file is not None and result_file not in declared:
        raise AVError("metadata.result_file does not reference a listed artifact")
    mappings = []
    if "review_mapping" in metadata:
        if not isinstance(metadata["review_mapping"], dict):
            raise AVError("review_mapping must be an object")
        mappings.append(metadata["review_mapping"])
    if "review_mappings" in metadata:
        if not isinstance(metadata["review_mappings"], list):
            raise AVError("review_mappings must be a list")
        mappings.extend(metadata["review_mappings"])
    for mapping in mappings:
        if not isinstance(mapping, dict):
            raise AVError("Malformed review mapping")
        parent_hash = digest_value(mapping.get("parent_source_sha256"), "mapping parent source hash")
        stream_index = integer(mapping.get("parent_stream_index"), "mapping parent stream index")
        matching = [x for x in sources if x["sha256"] == parent_hash]
        direct = matching and any(any(s.get("index") == stream_index for s in x.get("streams", [])) for x in matching)
        if not direct:
            link = mapping.get("parent_frame_run")
            # A contact sheet depends on a frame-run manifest, not on original
            # media bytes. The declared hash must bind that indirection; review
            # validation separately resolves/checks the parent's point graph.
            indirect = (mapping.get("kind") == "contact_sheet_points" and isinstance(link, dict)
                        and link == metadata.get("parent_frame_run")
                        and any(x["sha256"] == link.get("run_manifest_sha256") for x in sources))
            if not indirect:
                raise AVError("Review mapping refers to an absent parent source/stream")
            digest_value(link.get("run_manifest_sha256"), "parent frame manifest hash")
            text_value(link.get("run_manifest_path"), "parent frame manifest path")
        members = [mapping] if "artifact_path" in mapping else mapping.get("frames", mapping.get("sheets", []))
        if not isinstance(members, list):
            raise AVError("Malformed mapping members")
        for member in members:
            if not isinstance(member, dict) or member.get("artifact_path") not in declared:
                raise AVError("Review mapping artifact is not a manifest member")
            expected = next(a for a in artifacts if a["path"] == member["artifact_path"])
            if member.get("artifact_sha256") != expected["sha256"]:
                raise AVError("Review mapping artifact hash mismatch")
    children = []
    for relative in sorted(declared):
        if PurePosixPath(relative).name == "run.json":
            children.append(verify_run(root / relative, verify_sources=verify_sources))
    return {"schema": "ave.verification.v1", "structural_validity": "VALID",
            "manifest_sha256": sha256(manifest_path), "artifact_count": len(artifacts),
            "source_count": len(sources), "original_sources_verified": verify_sources,
            "nested_runs": children, "perception_truth": "NOT_ESTABLISHED_BY_VALIDATION",
            "trust_boundary": "Portable hashes validate recorded bytes and membership. Authenticity, declared capabilities, presentation and actual perception remain external trust boundaries."}
```

## avevidence/packaging.py

SHA-256: `fbf100c66e2b802117d47c8b48f8b28adeb6a155411bc9dfddcb4b1bfe7bedd5`.

```python
"""Deterministic, allowlisted evidence archives. No source uploads or promotion."""
from __future__ import annotations

import hashlib
from pathlib import Path, PurePosixPath
import re
import uuid
import zipfile
import zlib

from .common import AVError, sha256


def _member_name(name):
    if not isinstance(name, str) or not name:
        raise AVError("Archive member must be a nonempty relative name")
    p = PurePosixPath(name)
    if (p.is_absolute() or ".." in p.parts or "\\" in name or ":" in name
            or str(p) in ("", ".") or p.as_posix() != name
            or any(ord(c) < 32 for c in name)):
        raise AVError(f"Unsafe archive member: {name!r}")
    return name


def deterministic_zip(files, destination, prefix="", *, expected_hashes=None):
    """Pack (relative name, bytes or Path) pairs, streaming file-backed members.

    expected_hashes, when supplied, binds each unprefixed member to a digest
    already verified in its source run. A failed archive remains in staging.
    """
    target = Path(destination).resolve()
    if target.exists():
        raise AVError(f"Archive already exists: {target}")
    if prefix:
        _member_name(prefix.removesuffix("/"))
        if not prefix.endswith("/"):
            raise AVError("Archive prefix must end with /")
    target.parent.mkdir(parents=True, exist_ok=True)
    entries = []
    seen = set()
    for name, data in files:
        final = _member_name(prefix + _member_name(name))
        if final.casefold() in seen:
            raise AVError("Duplicate archive member")
        seen.add(final.casefold())
        if not isinstance(data, (bytes, Path)):
            raise AVError("Archive payload must be bytes or a pathlib.Path")
        if isinstance(data, Path) and (data.is_symlink() or not data.is_file()):
            raise AVError("Archive source must be a regular non-symlink file")
        entries.append((final, data, name))
    checksum_name = prefix + "SHA256SUMS.txt"
    if checksum_name.casefold() in seen:
        raise AVError("Checksum member is reserved")
    if expected_hashes is not None and set(expected_hashes) != {e[2] for e in entries}:
        raise AVError("Expected archive hashes must cover every member exactly")
    staging = target.parent / ("." + target.name + ".staging-" + uuid.uuid4().hex)
    sums = []
    with zipfile.ZipFile(staging, "x", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name, data, original in sorted(entries):
            info = zipfile.ZipInfo(name, (1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            info.file_size = len(data) if isinstance(data, bytes) else data.stat().st_size
            digest = hashlib.sha256()
            with archive.open(info, "w", force_zip64=True) as member:
                if isinstance(data, bytes):
                    member.write(data)
                    digest.update(data)
                else:
                    with data.open("rb") as source:
                        for chunk in iter(lambda: source.read(1024 * 1024), b""):
                            member.write(chunk)
                            digest.update(chunk)
            actual = digest.hexdigest()
            if expected_hashes is not None and expected_hashes[original] != actual:
                raise AVError(f"Artifact changed while archiving: {original}")
            sums.append(f"{actual}  {name}\n")
        info = zipfile.ZipInfo(checksum_name, (1980, 1, 1, 0, 0, 0))
        info.external_attr = 0o100644 << 16
        archive.writestr(info, "".join(sums).encode("utf-8"),
                         compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    if target.exists():
        raise AVError("Archive destination appeared while building; staged archive retained")
    staging.rename(target)
    return {"archive": str(target), "sha256": sha256(target), "members": len(entries) + 1}


def pack_run(run_dir, destination):
    from .inventory import verify_run
    from .common import read_json, safe_member
    root = Path(run_dir).resolve()
    target = Path(destination).resolve()
    if target == root or root in target.parents:
        raise AVError("An archive must be outside its immutable source run")
    verify_run(root)
    manifest = read_json(root / "run.json")
    files = [("run.json", root / "run.json")]
    files += [(e["path"], safe_member(root, e["path"])) for e in manifest["artifacts"]]
    hashes = {e["path"]: e["sha256"] for e in manifest["artifacts"]}
    hashes["run.json"] = sha256(root / "run.json")
    return deterministic_zip(files, target, prefix="evidence/", expected_hashes=hashes)


def verify_archive(path):
    try:
        return _verify_archive(path)
    except (zipfile.BadZipFile, zlib.error, UnicodeError, ValueError, RuntimeError, KeyError, EOFError) as exc:
        if isinstance(exc, AVError):
            raise
        raise AVError(f"Malformed or unsupported evidence archive: {exc}") from exc


def _verify_archive(path):
    with zipfile.ZipFile(path) as z:
        names = z.namelist()
        if len({n.casefold() for n in names}) != len(names):
            raise AVError("Duplicate archive members")
        for info in z.infolist():
            _member_name(info.filename)
            if ((info.external_attr >> 16) & 0o170000) == 0o120000:
                raise AVError("Symlinks are not allowed")
        checksums = [n for n in names if n.endswith("/SHA256SUMS.txt") or n == "SHA256SUMS.txt"]
        if len(checksums) != 1:
            raise AVError("Exactly one checksum inventory is required")
        expected = {}
        for line in z.read(checksums[0]).decode("utf-8").splitlines():
            digest, name = line.split("  ", 1)
            if not re.fullmatch(r"[0-9a-f]{64}", digest) or name in expected:
                raise AVError("Malformed digest or duplicate checksum record")
            expected[name] = digest
        if set(expected) != set(names) - {checksums[0]}:
            raise AVError("Archive membership differs from checksum inventory")
        for name, digest in expected.items():
            h = hashlib.sha256()
            with z.open(name) as member:
                for chunk in iter(lambda: member.read(1024 * 1024), b""):
                    h.update(chunk)
            if h.hexdigest() != digest:
                raise AVError(f"Checksum mismatch: {name}")
    return {"archive": str(Path(path).resolve()), "sha256": sha256(path), "members": len(names),
            "integrity_valid": True, "scope": "Archive byte integrity only; not source authenticity or perceptual review."}
```

## avevidence/reviews.py

SHA-256: `d6bb89d786d12d9c3ad4f512c168c4ce84e4a16749370d241a84e88c7bcbe286`.

```python
"""Structural review validation with an explicit external perception boundary.

Receipts and reviewer declarations are inputs to an audit. Neither this module
nor a generated artifact can certify that a person or model perceived media.
"""
from __future__ import annotations

from collections import defaultdict
from datetime import datetime, timezone, timedelta
from pathlib import Path
import json

from .common import (AVError, file_record, finish_run, output_transaction,
                     read_json, safe_member, sha256, write_json)
from .inventory import (MODALITIES, date_value, digest_value, identifier, integer,
                        intervals, number, points, text_value, verify_run)

MECHANISMS = {"audio": "audio_playback", "motion": "video_playback", "visual_stills": "image_view"}
TRUST = ("Validation checks identity, declarations, receipts and interval arithmetic only. "
         "Capability and presentation receipts are externally trusted declarations; "
         "their presence and hashes do not prove authenticity, actual perception, "
         "attention, comprehension or the truth of an observation.")


class _Dependencies(set):
    """Retain the hashes observed at first read, rather than blessing later edits."""
    def __init__(self, paths=()):
        super().__init__(); self.hashes = {}
        for path in paths:
            self.add(path)

    def add(self, path):
        path = Path(path).resolve()
        if not path.is_file():
            raise AVError(f"Missing validation dependency: {path}")
        digest = sha256(path)
        if path in self.hashes and self.hashes[path] != digest:
            raise AVError("A dependency changed during validation")
        self.hashes[path] = digest
        super().add(path)

    def records(self):
        result = []
        for path in sorted(self, key=str):
            record = file_record(path)
            if record["sha256"] != self.hashes[path]:
                raise AVError("A dependency changed during validation")
            result.append(record)
        return result


def _object(value, required, allowed, name):
    if not isinstance(value, dict) or not set(required) <= set(value):
        raise AVError(f"{name} is missing required fields")
    if set(value) - set(allowed):
        raise AVError(f"Unknown {name} fields: {sorted(set(value)-set(allowed))}")
    return value


def _reviewer(value):
    _object(value, {"id", "type", "name"}, {"id", "type", "name"}, "reviewer")
    identifier(value["id"], "reviewer id")
    if value["type"] not in ("human", "model"):
        raise AVError("Reviewer type must be human or model")
    text_value(value["name"], "reviewer name")
    return value


def _modality(value):
    if not isinstance(value, str) or value not in MODALITIES:
        raise AVError("Modality must separately name audio, motion or visual_stills")
    return value


def _date(value, name):
    d = date_value(value, name)
    if d > datetime.now(timezone.utc) + timedelta(minutes=5):
        raise AVError(f"{name} is in the future")
    return d


def _input_file(base, value, name):
    text_value(value, name)
    p = Path(value)
    p = p.resolve() if p.is_absolute() else (base / p).resolve()
    if not p.is_file():
        raise AVError(f"Missing {name}: {p}")
    return p


def _manifest_reference(base, value, expected, dependencies):
    """Resolve moved sibling runs by recorded hash inside an ancestor bundle."""
    digest_value(expected, "referenced manifest hash")
    text_value(value, "referenced manifest path")
    path = Path(value)
    path = path.resolve() if path.is_absolute() else (base / path).resolve()
    if path.is_file():
        if sha256(path) != expected:
            raise AVError("Referenced run manifest hash mismatch")
        return path
    search_roots = {base.resolve()} | {p.parent for p in dependencies if p.name == "run.json"}
    candidates = set()
    for initial in search_roots:
        for root in (initial, *initial.parents):
            bundle = root / "run.json"
            if not bundle.is_file():
                continue
            manifest = read_json(bundle)
            if not isinstance(manifest, dict):
                continue
            if sha256(bundle) == expected:
                candidates.add(bundle)
            for member in manifest.get("artifacts", []):
                if isinstance(member, dict) and member.get("sha256") == expected and str(member.get("path", "")).endswith("/run.json"):
                    candidate = safe_member(root, member["path"])
                    if candidate.is_file() and sha256(candidate) == expected:
                        candidates.add(candidate)
    if not candidates:
        raise AVError("Referenced run manifest is unavailable; include its hash-matched run in the bundle")
    # Identical manifest bytes copied twice are interchangeable for identity;
    # choose a complete verified copy, never a same-name substitute.
    for candidate in sorted(candidates, key=str):
        try:
            verify_run(candidate)
        except AVError:
            continue
        return candidate
    raise AVError("No complete hash-matched referenced run is available")


def _receipt(value, base, dependencies):
    _object(value, {"kind", "path", "sha256"}, {"kind", "path", "sha256"}, "receipt")
    if value["kind"] not in ("tool_receipt", "human_attestation"):
        raise AVError("Receipt kind must be tool_receipt or human_attestation")
    digest_value(value["sha256"], "receipt sha256")
    path = _input_file(base, value["path"], "receipt file")
    if sha256(path) != value["sha256"]:
        raise AVError("Receipt hash mismatch")
    if not path.stat().st_size:
        raise AVError("A receipt must not be empty")
    dependencies.add(path)
    return value


def union_intervals(items):
    result = []
    for a, b in sorted(items):
        if result and a <= result[-1][1] + 1e-7:
            result[-1][1] = max(result[-1][1], b)
        else:
            result.append([a, b])
    return result


def _missing(required, covered):
    result = []
    for a, b in union_intervals(required):
        cursor = a
        for c, d in union_intervals(covered):
            if d <= cursor or c >= b:
                continue
            if c > cursor + 1e-7:
                result.append([cursor, min(c, b)])
            cursor = max(cursor, min(d, b))
        if cursor < b - 1e-7:
            result.append([cursor, b])
    return result


def _points_subset(wanted, available):
    return all(any(abs(x-y) <= 1e-6 for y in available) for x in wanted)


def _coverage_fields(record, modality, duration):
    if modality == "visual_stills":
        if "intervals_seconds" in record:
            raise AVError("Still images cannot declare temporal coverage intervals")
        return points(record.get("points_seconds"), duration)
    if "points_seconds" in record:
        raise AVError("Audio/motion coverage requires explicit intervals, not point samples")
    return intervals(record.get("intervals_seconds"), duration)


def _load_inventory(path, dependencies):
    supplied = Path(path).resolve()
    manifest_path = supplied / "run.json" if supplied.is_dir() else supplied if supplied.name == "run.json" else supplied.parent / "run.json"
    verify_run(manifest_path)
    dependencies.add(manifest_path)
    manifest = read_json(manifest_path)
    if manifest.get("operation") != "inventory":
        raise AVError("Reviews require an inventory run (select its child directory in a bundle)")
    result = manifest.get("metadata", {}).get("result_file")
    inventory_path = safe_member(manifest_path.parent, result)
    if supplied.is_file() and supplied.name != "run.json" and supplied != inventory_path:
        raise AVError("Specified inventory is not the run's verified result artifact")
    data = read_json(inventory_path)
    dependencies.add(inventory_path)
    if data.get("schema") != "ave.inventory.v1" or not data.get("sources") or not data.get("logical_sources"):
        raise AVError("Malformed admitted inventory")
    if data["sources"] != manifest["sources"]:
        raise AVError("Inventory source records differ from the run admission")
    sources = {}
    for source in data["sources"]:
        mid = identifier(source.get("materialization_id"), "materialization_id")
        if mid in sources:
            raise AVError("Duplicate inventory materialization_id")
        if source not in manifest["sources"]:
            raise AVError("Inventory source record differs from run admission")
        sources[mid] = source
    logical_ids = set()
    for logical in data["logical_sources"]:
        if not isinstance(logical, dict):
            raise AVError("Malformed logical source declaration")
        lid = identifier(logical.get("logical_source_id"), "logical_source_id")
        if lid in logical_ids:
            raise AVError("Duplicate logical source id")
        logical_ids.add(lid)
        preferred = sources.get(logical.get("preferred_materialization_id"))
        if not preferred or preferred["logical_source_id"] != lid or not preferred.get("preferred"):
            raise AVError("Invalid preferred materialization reference")
        required = logical.get("required_modalities")
        if not isinstance(required, list) or not required or not all(isinstance(x, str) for x in required) or set(required) - MODALITIES or required != preferred["required_modalities"]:
            raise AVError("Invalid logical source modality requirements")
        group = [x for x in sources.values() if x["logical_source_id"] == lid]
        if sorted(logical.get("materialization_ids", [])) != sorted(x["materialization_id"] for x in group) or sum(x.get("preferred") is True for x in group) != 1:
            raise AVError("Logical materialization membership or preference is inconsistent")
    if logical_ids != set(data.get("required_logical_source_ids", [])) or logical_ids != {x["logical_source_id"] for x in sources.values()}:
        raise AVError("Inventory completeness declarations disagree")
    return data, sources


def _source_for(record, sources):
    mid = identifier(record.get("materialization_id"), "materialization_id")
    lid = identifier(record.get("logical_source_id"), "logical_source_id")
    source = sources.get(mid)
    if not source or source["logical_source_id"] != lid:
        raise AVError("Review source/materialization pair is not admitted")
    if digest_value(record.get("source_sha256"), "review source hash") != source["sha256"]:
        raise AVError("Review source hash does not match the selected materialization")
    modality = _modality(record.get("modality"))
    kind = "audio" if modality == "audio" else "video"
    index = integer(record.get("stream_index"), "review stream_index")
    if source.get("selected_streams", {}).get(kind) != index:
        raise AVError("Review stream does not exactly match the admitted selected stream")
    return source


def _evidence_identity(evidence):
    return {k: v for k, v in evidence.items() if k not in ("derivative_intervals_seconds", "frame_ids")}


def _mappings(manifest):
    metadata = manifest.get("metadata", {})
    result = []
    if "review_mapping" in metadata:
        result.append(metadata["review_mapping"])
    if "review_mappings" in metadata:
        if not isinstance(metadata["review_mappings"], list):
            raise AVError("review_mappings must be a list")
        result.extend(metadata["review_mappings"])
    if not all(isinstance(x, dict) for x in result):
        raise AVError("Malformed derivative review mapping")
    return result


def _verified_derivative(evidence, base, dependencies):
    expected = digest_value(evidence.get("run_manifest_sha256"), "derivative run manifest hash")
    path = _manifest_reference(base, evidence.get("run_manifest_path"), expected, dependencies)
    verify_run(path)
    dependencies.add(path)
    manifest = read_json(path)
    relative = text_value(evidence.get("artifact_path"), "derivative artifact path")
    digest = digest_value(evidence.get("artifact_sha256"), "derivative artifact hash")
    if not any(a["path"] == relative and a["sha256"] == digest for a in manifest["artifacts"]):
        raise AVError("Derivative artifact/hash is absent from the verified manifest")
    dependencies.add(safe_member(path.parent, relative))
    return path, manifest


def _still_points(mapping, evidence, run_path, manifest, dependencies):
    kind = mapping.get("kind")
    result_file = manifest.get("metadata", {}).get("result_file")
    if not result_file:
        raise AVError("Still mapping requires a verified result file")
    result = read_json(safe_member(run_path.parent, result_file))
    dependencies.add(safe_member(run_path.parent, result_file))
    requested_ids = evidence.get("frame_ids")
    if not isinstance(requested_ids, list) or not requested_ids or len(set(requested_ids)) != len(requested_ids):
        raise AVError("Visual derivative evidence requires distinct frame_ids")
    for x in requested_ids:
        identifier(x, "frame_id")
    if kind == "still_points":
        if manifest.get("operation") != "extract_frames":
            raise AVError("Still review mapping requires an extract_frames run")
        frames = result.get("rows", []) if isinstance(result, dict) else []
        if not isinstance(frames, list) or not all(isinstance(x, dict) for x in frames):
            raise AVError("Malformed frame rows")
        if len({x.get("frame_id") for x in frames}) != len(frames):
            raise AVError("Duplicate frame IDs in the verified result")
        mapped_frames = mapping.get("frames", [])
        if not isinstance(mapped_frames, list) or not all(isinstance(x, dict) for x in mapped_frames) or len({x.get("frame_id") for x in mapped_frames}) != len(mapped_frames):
            raise AVError("Malformed or duplicate frame mapping IDs")
        points_by_id = {}
        for entry in mapped_frames:
            row = next((x for x in frames if x.get("frame_id") == entry.get("frame_id")), None)
            if not row or any(row.get(k) != v for k, v in {
                "path": entry.get("artifact_path"), "sha256": entry.get("artifact_sha256"),
                "source_sha256": mapping.get("parent_source_sha256"),
                "stream_index": mapping.get("parent_stream_index"),
                "source_seconds": entry.get("source_seconds")}.items()):
                raise AVError("Frame point mapping disagrees with verified frame rows")
            if entry.get("artifact_path") == evidence["artifact_path"] and entry.get("artifact_sha256") == evidence["artifact_sha256"]:
                points_by_id[entry["frame_id"]] = number(entry["source_seconds"], "frame source_seconds")
        if not set(requested_ids) <= set(points_by_id):
            raise AVError("Frame IDs are not represented by the selected image artifact")
        return [points_by_id[x] for x in requested_ids]
    if kind == "contact_sheet_points":
        if manifest.get("operation") != "contact_sheets":
            raise AVError("Contact-sheet point mapping requires a contact_sheets run")
        sheet = next((x for x in mapping.get("sheets", []) if x.get("artifact_path") == evidence["artifact_path"] and x.get("artifact_sha256") == evidence["artifact_sha256"]), None)
        rows = result.get("sheets", []) if isinstance(result, dict) else []
        row = next((x for x in rows if x.get("path") == evidence["artifact_path"]), None)
        if not sheet or not row or row.get("sha256") != evidence["artifact_sha256"] or row.get("frame_ids") != sheet.get("frame_ids"):
            raise AVError("Contact-sheet mapping disagrees with its verified result")
        if not set(requested_ids) <= set(sheet["frame_ids"]):
            raise AVError("Review names a frame absent from its contact sheet")
        parent = mapping.get("parent_frame_run")
        if parent != manifest.get("metadata", {}).get("parent_frame_run") or not isinstance(parent, dict):
            raise AVError("Contact-sheet parent run references disagree")
        parent_path = _manifest_reference(run_path.parent, parent.get("run_manifest_path"), parent.get("run_manifest_sha256"), dependencies)
        verify_run(parent_path)
        dependencies.add(parent_path)
        parent_manifest = read_json(parent_path)
        maps = [x for x in _mappings(parent_manifest) if x.get("kind") == "still_points" and x.get("parent_source_sha256") == mapping["parent_source_sha256"] and x.get("parent_stream_index") == mapping["parent_stream_index"]]
        if len(maps) != 1:
            raise AVError("Contact sheet has no unique matching parent point mapping")
        points_by_id = {}
        for frame in maps[0].get("frames", []):
            if frame.get("frame_id") in requested_ids:
                frame_evidence = {"artifact_path": frame["artifact_path"], "artifact_sha256": frame["artifact_sha256"], "frame_ids": [frame["frame_id"]]}
                points_by_id[frame["frame_id"]] = _still_points(maps[0], frame_evidence, parent_path, parent_manifest, dependencies)[0]
                dependencies.add(safe_member(parent_path.parent, frame["artifact_path"]))
        if set(points_by_id) != set(requested_ids):
            raise AVError("Contact sheet references missing parent frames")
        return [points_by_id[x] for x in requested_ids]
    raise AVError("The selected derivative is not a still-image presentation")


def _evidence_coverage(record, base, dependencies, source):
    evidence = record.get("evidence")
    if not isinstance(evidence, dict):
        raise AVError("Missing evidence object")
    modality = record["modality"]
    claimed = _coverage_fields(record, modality, source["duration_seconds"])
    if evidence.get("kind") == "source":
        if set(evidence) != {"kind"}:
            raise AVError("Direct-source evidence accepts only kind; source/stream/time are explicit record fields")
        return claimed
    if evidence.get("kind") != "derivative":
        raise AVError("Metrics, ASR and generated summaries cannot stand in for audiovisual presentation")
    allowed = {"kind", "run_manifest_path", "run_manifest_sha256", "artifact_path", "artifact_sha256", "derivative_intervals_seconds", "derivative_stream_index", "frame_ids"}
    _object(evidence, {"kind", "run_manifest_path", "run_manifest_sha256", "artifact_path", "artifact_sha256"}, allowed, "derivative evidence")
    run_path, manifest = _verified_derivative(evidence, base, dependencies)
    mappings = [x for x in _mappings(manifest) if x.get("parent_source_sha256") == source["sha256"] and x.get("parent_stream_index") == record["stream_index"]]
    if modality == "visual_stills":
        if "derivative_intervals_seconds" in evidence or "derivative_stream_index" in evidence:
            raise AVError("Still-image evidence has points, not playback intervals/streams")
        mappings = [x for x in mappings if x.get("kind") in ("still_points", "contact_sheet_points")]
        if len(mappings) != 1:
            raise AVError("No unique matching still-image point mapping")
        mapped = _still_points(mappings[0], evidence, run_path, manifest, dependencies)
        if not _points_subset(claimed, mapped) or not _points_subset(mapped, claimed):
            raise AVError("Claimed source points differ from the presented derivative frames")
        return claimed
    if "frame_ids" in evidence:
        raise AVError("Still-frame IDs cannot count as listening or motion playback")
    permitted_operations = {"audio": {"extract_audio", "clip_audio", "clip-av"}, "motion": {"clip-av"}}
    if manifest.get("operation") not in permitted_operations[modality]:
        raise AVError("Only media-producing audio or AV clip runs can declare playback coverage; metrics/ASR cannot")
    index = integer(evidence.get("derivative_stream_index"), "derivative_stream_index")
    mappings = [x for x in mappings if x.get("modality") == modality and x.get("derivative_stream_index") == index and x.get("artifact_path") == evidence["artifact_path"] and x.get("artifact_sha256") == evidence["artifact_sha256"]]
    if len(mappings) != 1:
        raise AVError("No unique derivative mapping for exact parent/derivative streams and modality")
    mapping = mappings[0]
    if mapping.get("kind") in ("still_points", "contact_sheet_points") or not mapping.get("segments"):
        raise AVError("Point or feature artifacts cannot provide playback interval coverage")
    requested = intervals(evidence.get("derivative_intervals_seconds"), name="derivative intervals")
    segments, available = [], []
    for segment in mapping["segments"]:
        if not isinstance(segment, dict):
            raise AVError("Malformed derivative time mapping")
        pa, pb = intervals([[segment.get("parent_start_seconds"), segment.get("parent_end_seconds")]], source["duration_seconds"], "mapped parent interval")[0]
        da, db = intervals([[segment.get("derivative_start_seconds"), segment.get("derivative_end_seconds")]], name="mapped derivative interval")[0]
        if abs((pb-pa)-(db-da)) > 1e-6:
            raise AVError("Retimed playback needs a different explicit mapping schema; rate-one durations disagree")
        segments.append((pa, pb, da, db)); available.append([da, db])
    ordered = sorted(segments, key=lambda x: x[2])
    if any(a[3] > b[2] + 1e-7 for a, b in zip(ordered, ordered[1:])):
        raise AVError("Overlapping derivative mappings are ambiguous")
    if _missing(requested, available):
        raise AVError("Presented derivative interval crosses unmapped padding or absent media")
    mapped = []
    for a, b in requested:
        for pa, pb, da, db in segments:
            lo, hi = max(a, da), min(b, db)
            if lo < hi:
                mapped.append([pa+lo-da, pa+hi-da])
    if _missing(claimed, mapped) or _missing(mapped, claimed):
        raise AVError("Claimed source coverage differs from derivative-to-parent interval mapping")
    return union_intervals(claimed)


def _records(path):
    try:
        if path.suffix.lower() == ".jsonl":
            records = []
            for n, line in enumerate(path.read_text(encoding="utf-8-sig").splitlines(), 1):
                if line.strip():
                    records.append(json.loads(line, parse_constant=lambda s: (_ for _ in ()).throw(AVError(f"Nonfinite JSON at line {n}"))))
        else:
            records = read_json(path)
    except (json.JSONDecodeError, UnicodeError) as exc:
        raise AVError(f"Invalid review record JSON: {exc}") from exc
    if not isinstance(records, list):
        raise AVError("Review input must be a JSON array or JSONL records")
    return records


def validate_reviews(records, inventory_or_run, capabilities, output):
    """Validate declarations and report union coverage; raise AVError if invalid."""
    record_path, cap_path = Path(records).resolve(), Path(capabilities).resolve()
    dependencies = _Dependencies([record_path, cap_path])
    inventory_data, sources = _load_inventory(inventory_or_run, dependencies)
    declarations = read_json(cap_path)
    _object(declarations, {"schema", "capabilities", "presentations"}, {"schema", "capabilities", "presentations"}, "capabilities document")
    if declarations["schema"] != "ave.capabilities.v1" or not isinstance(declarations["capabilities"], list) or not isinstance(declarations["presentations"], list):
        raise AVError("Malformed capabilities document")
    caps, presented = {}, {}
    cap_fields = {"capability_id", "reviewer", "modality", "mechanism", "verified_at", "receipt"}
    for cap in declarations["capabilities"]:
        _object(cap, cap_fields, cap_fields, "capability")
        cid = identifier(cap["capability_id"], "capability_id")
        if cid in caps:
            raise AVError("Duplicate capability_id")
        _reviewer(cap["reviewer"]); modality = _modality(cap["modality"])
        if cap["mechanism"] != MECHANISMS[modality]:
            raise AVError("Capability mechanism does not present the declared modality")
        _date(cap["verified_at"], "capability verified_at")
        _receipt(cap["receipt"], cap_path.parent, dependencies)
        if cap["reviewer"]["type"] == "model" and cap["receipt"]["kind"] != "tool_receipt":
            raise AVError("Model capabilities require a tool presentation receipt, not a human substitute")
        caps[cid] = cap
    presentation_fields = {"presentation_id", "capability_id", "reviewer_id", "reviewer_type", "modality", "mechanism", "presented_at", "logical_source_id", "materialization_id", "source_sha256", "stream_index", "evidence", "receipt"}
    for item in declarations["presentations"]:
        _object(item, presentation_fields, presentation_fields | {"intervals_seconds", "points_seconds"}, "presentation")
        pid = identifier(item["presentation_id"], "presentation_id")
        if pid in presented:
            raise AVError("Duplicate presentation_id")
        cap = caps.get(identifier(item["capability_id"], "capability_id"))
        if not cap or item["reviewer_id"] != cap["reviewer"]["id"] or item["reviewer_type"] != cap["reviewer"]["type"] or item["modality"] != cap["modality"] or item["mechanism"] != cap["mechanism"]:
            raise AVError("Presentation is not bound to the declared reviewer/capability/modality/mechanism")
        if _date(item["presented_at"], "presentation presented_at") < date_value(cap["verified_at"]):
            raise AVError("Presentation predates capability verification")
        _receipt(item["receipt"], cap_path.parent, dependencies)
        if item["reviewer_type"] == "model" and item["receipt"]["kind"] != "tool_receipt":
            raise AVError("A model review requires its own tool presentation receipt")
        source = _source_for(item, sources)
        coverage = _evidence_coverage(item, cap_path.parent, dependencies, source)
        presented[pid] = (item, coverage)
    records_data = _records(record_path)
    review_fields = {"schema", "review_id", "reviewer", "reviewed_at", "logical_source_id", "materialization_id", "source_sha256", "stream_index", "modality", "capability_id", "presentation_id", "evidence", "observation"}
    seen, coverage = set(), defaultdict(list)
    for record in records_data:
        _object(record, review_fields, review_fields | {"intervals_seconds", "points_seconds"}, "review record")
        if record["schema"] != "ave.review.v1":
            raise AVError("Unsupported review schema")
        rid = identifier(record["review_id"], "review_id")
        if rid in seen:
            raise AVError("Duplicate review_id")
        seen.add(rid)
        reviewer = _reviewer(record["reviewer"])
        text_value(record["observation"], "observation")
        reviewed_at = _date(record["reviewed_at"], "review reviewed_at")
        source = _source_for(record, sources)
        cap = caps.get(identifier(record["capability_id"], "capability_id"))
        presentation = presented.get(identifier(record["presentation_id"], "presentation_id"))
        if not cap or cap["reviewer"] != reviewer or cap["modality"] != record["modality"] or not presentation:
            raise AVError("Review lacks matching capability and presentation references")
        item, presentation_coverage = presentation
        for key in ("capability_id", "logical_source_id", "materialization_id", "source_sha256", "stream_index", "modality"):
            if item[key] != record[key]:
                raise AVError(f"Review/presentation mismatch: {key}")
        if _evidence_identity(item["evidence"]) != _evidence_identity(record["evidence"]):
            raise AVError("Review and presentation identify different evidence artifacts")
        if reviewed_at < date_value(item["presented_at"]):
            raise AVError("Review predates presentation")
        declared = _evidence_coverage(record, record_path.parent, dependencies, source)
        if record["modality"] == "visual_stills":
            if not _points_subset(declared, presentation_coverage):
                raise AVError("Review points were not included in the presentation declaration")
        elif _missing(declared, presentation_coverage):
            raise AVError("Review intervals exceed the declared presentation")
        coverage[(record["materialization_id"], record["modality"])].extend(declared)
    results, all_full = [], True
    for logical in inventory_data["logical_sources"]:
        preferred = sources[logical["preferred_materialization_id"]]
        modal_results = []
        for modality in logical["required_modalities"]:
            declared = coverage[(preferred["materialization_id"], modality)]
            if modality == "visual_stills":
                required = points(preferred.get("required_points_seconds"), preferred["duration_seconds"])
                reviewed = sorted(set(declared))
                missing = [x for x in required if not _points_subset([x], reviewed)]
                item = {"modality": modality, "required_points_seconds": required, "declared_points_seconds": reviewed, "missing_points_seconds": missing,
                        "coverage_meaning": "Only the explicitly required still points; no continuous motion or audio coverage"}
            else:
                required = intervals(preferred.get("required_intervals_seconds", {}).get(modality), preferred["duration_seconds"])
                reviewed = union_intervals(declared); missing = _missing(required, reviewed)
                item = {"modality": modality, "required_intervals_seconds": union_intervals(required), "declared_union_intervals_seconds": reviewed, "missing_intervals_seconds": missing,
                        "declared_seconds_within_requirements": sum(b-a for a, b in union_intervals(required)) - sum(b-a for a, b in missing)}
            item["full_declared_coverage"] = not missing
            all_full = all_full and not missing
            modal_results.append(item)
        results.append({"logical_source_id": logical["logical_source_id"], "preferred_materialization_id": preferred["materialization_id"],
                        "modalities": modal_results, "full_required_declared_coverage": all(x["full_declared_coverage"] for x in modal_results)})
    report = {"schema": "ave.review.validation.v1", "structural_valid": True,
              "full_required_coverage": bool(all_full), "status": "FULL_DECLARED_COVERAGE" if all_full else "PARTIAL_DECLARED_COVERAGE",
              "perception_truth": "NOT_ESTABLISHED_BY_VALIDATION", "trust_boundary": TRUST,
              "review_count": len(records_data), "capability_count": len(caps), "presentation_count": len(presented),
              "coverage": results, "other_materialization_policy": "Alternate materialization reviews are retained but do not fill preferred-materialization gaps without an explicit parent mapping.",
              "reviews": records_data, "capability_declarations": declarations,
              "inventory_sha256": sha256(next(x for x in dependencies if x.name == "inventory.json"))}
    with output_transaction(output, dependencies) as stage:
        import copy
        portable = copy.deepcopy(declarations)
        archived = []
        for i, item in enumerate(portable["capabilities"] + portable["presentations"]):
            receipt = item["receipt"]
            p = _input_file(cap_path.parent, receipt["path"], "receipt")
            relative = f"receipts/{i:04}{p.suffix or '.bin'}"
            target = stage / relative; target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(p.read_bytes())
            if sha256(target) != receipt["sha256"]:
                raise AVError("Receipt changed while archiving")
            archived.append({"original_path": receipt["path"], "artifact_path": relative, "sha256": receipt["sha256"], "kind": receipt["kind"]})
            receipt["path"] = relative
        report["receipt_artifacts"] = archived
        report["portable_declarations"] = {"reviews": "reviews.json", "capabilities": "capabilities.json",
                                             "note": "Receipt paths are rewritten to archived copies; assertions are unchanged."}
        write_json(stage / "reviews.json", records_data)
        write_json(stage / "capabilities.json", portable)
        write_json(stage / "review_validation.json", report)
        return finish_run(stage, "validate_reviews", dependencies.records(),
                          {"records_sha256": sha256(record_path), "capabilities_sha256": sha256(cap_path)},
                          {"result_file": "review_validation.json", "structural_valid": True,
                           "full_required_coverage": bool(all_full), "perception_truth": "NOT_ESTABLISHED_BY_VALIDATION"})


def write_review_templates(output):
    """Generate conspicuously incomplete declarations, never review evidence."""
    reviewer = {"id": "REPLACE_REVIEWER_ID", "type": "human", "name": "REPLACE_REVIEWER_NAME"}
    receipt = {"kind": "human_attestation", "path": "REPLACE_RECEIPT_PATH", "sha256": "REPLACE_SHA256"}
    evidence = {"kind": "source"}
    cap = {"capability_id": "REPLACE_CAPABILITY_ID", "reviewer": reviewer, "modality": "audio", "mechanism": "audio_playback", "verified_at": "REPLACE_TIMEZONE_DATE", "receipt": receipt}
    presentation = {"presentation_id": "REPLACE_PRESENTATION_ID", "capability_id": cap["capability_id"], "reviewer_id": reviewer["id"], "reviewer_type": reviewer["type"], "modality": "audio", "mechanism": "audio_playback", "presented_at": "REPLACE_TIMEZONE_DATE", "logical_source_id": "REPLACE_LOGICAL_SOURCE_ID", "materialization_id": "REPLACE_MATERIALIZATION_ID", "source_sha256": "REPLACE_SHA256", "stream_index": 0, "intervals_seconds": [[0, 1]], "evidence": evidence, "receipt": receipt}
    record = {"schema": "ave.review.v1", "review_id": "REPLACE_REVIEW_ID", "reviewer": reviewer, "reviewed_at": "REPLACE_TIMEZONE_DATE", "logical_source_id": presentation["logical_source_id"], "materialization_id": presentation["materialization_id"], "source_sha256": presentation["source_sha256"], "stream_index": 0, "modality": "audio", "capability_id": cap["capability_id"], "presentation_id": presentation["presentation_id"], "intervals_seconds": [[0, 1]], "evidence": evidence, "observation": "REPLACE_WITH_YOUR_ACTUAL_OBSERVATION"}
    with output_transaction(output) as stage:
        write_json(stage / "capabilities.json", {"schema": "ave.capabilities.v1", "capabilities": [cap], "presentations": [presentation]})
        write_json(stage / "reviews.json", [record])
        return finish_run(stage, "review_templates", [], metadata={"result_file": "reviews.json", "template_status": "PLACEHOLDERS_MUST_BE_COMPLETED_AFTER_ACTUAL_REVIEW", "perception_truth": "NOT_ESTABLISHED_BY_VALIDATION"})
```

## avevidence/subtitles.py

SHA-256: `34cc46074764e49127db0d4b2fb589b593ef8700949bd18617c54e2ce053c26d`.

```python
"""Strict text parsing and explicit subtitle-to-media source-clock binding."""
from __future__ import annotations

from fractions import Fraction
import html
import json
from pathlib import Path
import re

from .common import (AVError, file_record, finite, finish_run, output_transaction,
                     parse_time, probe_source, run, select_stream, write_csv, write_json)

CLOCK = "original_pts_minus_source_origin"
_ASS_TAG = re.compile(r"\{[^}]*\}")


def _decode(data):
    try:
        if data.startswith((b"\xff\xfe", b"\xfe\xff")):
            text = data.decode("utf-16")
        else:
            text = data.decode("utf-8-sig")
    except UnicodeError as exc:
        raise AVError("Subtitle decoding failed; use UTF-8 or BOM-marked UTF-16") from exc
    if "\x00" in text:
        raise AVError("NULs in subtitles: unsupported encoding or invalid text")
    return text.replace("\r\n", "\n").replace("\r", "\n")


def _plain_ass(value):
    return _ASS_TAG.sub("", value).replace(r"\N", "\n").replace(r"\n", "\n").replace(r"\h", " ").strip()


def _times(start, end):
    a = parse_time(str(start).replace(",", "."))
    b = parse_time(str(end).replace(",", "."))
    if a is None or b is None or b <= a:
        raise AVError("Every subtitle cue requires finite 0 <= start < end")
    return a, b


def _ass(text):
    events, fields, rows = False, None, []
    for number, line in enumerate(text.splitlines(), 1):
        stripped = line.strip()
        if stripped.startswith("[") and stripped.endswith("]"):
            events = stripped.casefold() == "[events]"
            continue
        if not events:
            continue
        if stripped.casefold().startswith("format:"):
            fields = [x.strip().casefold() for x in stripped.split(":", 1)[1].split(",")]
            if len(set(fields)) != len(fields) or not {"start", "end", "text"}.issubset(fields) or fields[-1] != "text":
                raise AVError("ASS Events Format requires unique Start, End and final Text fields")
            continue
        if not stripped.casefold().startswith("dialogue:"):
            continue
        if not fields:
            raise AVError(f"ASS dialogue before Format at line {number}")
        values = stripped.split(":", 1)[1].lstrip().split(",", len(fields)-1)
        if len(values) != len(fields):
            raise AVError(f"Malformed ASS dialogue at line {number}")
        event = dict(zip(fields, values))
        a, b = _times(event["start"], event["end"])
        rows.append({"start_seconds": a, "end_seconds": b, "name": event.get("name", event.get("actor", "")),
                     "style": event.get("style", ""), "layer": event.get("layer", ""),
                     "text_raw": event["text"], "text_plain": _plain_ass(event["text"]), "source_line": number})
    return rows


def _srt(text):
    rows = []
    for block in re.split(r"\n[ \t]*\n", text.strip()):
        lines = block.splitlines()
        if not lines:
            continue
        if lines[0].strip().isdigit():
            lines.pop(0)
        if len(lines) < 2:
            raise AVError("Malformed or empty SRT cue")
        match = re.fullmatch(r"\s*(\d+:\d{2}:\d{2}[,.]\d+)\s*-->\s*(\d+:\d{2}:\d{2}[,.]\d+)(?:\s+.*)?", lines[0])
        if not match:
            raise AVError("Malformed SRT timing line")
        a, b = _times(*match.groups())
        raw = "\n".join(lines[1:])
        rows.append({"start_seconds": a, "end_seconds": b, "name": "", "style": "", "layer": "",
                     "text_raw": raw, "text_plain": html.unescape(re.sub(r"<[^>]+>", "", raw)).strip()})
    return rows


def _packet_bytes(text):
    chunks = []
    for line in text.splitlines():
        if not line.strip():
            continue
        match = re.match(r"^[0-9a-fA-F]+:\s(.*)$", line)
        if not match:
            raise AVError("Unexpected ffprobe packet hex format")
        chunks.append(match.group(1).split("  ", 1)[0].replace(" ", ""))
    try:
        return bytes.fromhex("".join(chunks))
    except ValueError as exc:
        raise AVError("Could not decode subtitle packet bytes") from exc


def _embedded(source, stream, stage):
    codec = stream.get("codec_name")
    if codec not in {"ass", "ssa", "subrip", "text"}:
        raise AVError(f"Embedded subtitle codec {codec!r} is not supported without a verified text/timing conversion; image OCR is not automatic")
    result = run(["ffprobe", "-v", "error", "-select_streams", str(stream["index"]),
                  "-show_packets", "-show_data", "-show_entries", "packet=pts,duration,data", "-of", "json", source["path"]])
    raw = json.loads(result.stdout)
    write_json(stage / "subtitle_packets.json", raw)
    try:
        tb = Fraction(stream["time_base"])
    except (KeyError, ValueError, ZeroDivisionError) as exc:
        raise AVError("Subtitle time base unavailable") from exc
    rows = []
    for packet in raw.get("packets", []):
        if "pts" not in packet or int(packet.get("duration", 0)) <= 0:
            raise AVError("Subtitle packet needs original PTS and positive duration")
        pts, duration = int(packet["pts"]), int(packet["duration"])
        text = _decode(_packet_bytes(packet.get("data", "")))
        if codec in {"ass", "ssa"}:
            # Matroska ASS packets: ReadOrder,Layer,Style,Name,MarginL,R,V,Effect,Text.
            # Other serialization is refused rather than guessed.
            if "matroska" not in source["probe"].get("format", {}).get("format_name", ""):
                raise AVError("ASS packet parsing currently requires Matroska serialization")
            parts = text.split(",", 8)
            if len(parts) != 9 or not parts[0].isdigit():
                raise AVError("Unexpected ASS packet serialization")
            body, name, style, layer = parts[8], parts[3], parts[2], parts[1]
            plain = _plain_ass(body)
        else:
            body, name, style, layer = text, "", "", ""
            plain = html.unescape(re.sub(r"<[^>]+>", "", body)).strip()
        rows.append({"start_seconds": float(pts * tb) - source["origin_seconds"],
                     "end_seconds": float((pts + duration) * tb) - source["origin_seconds"],
                     "name": name, "style": style, "layer": layer, "text_raw": body, "text_plain": plain,
                     "source_pts": pts, "source_time_base": str(tb), "source_duration_ticks": duration})
    return rows


def parse_subtitles(input, output, *, stream_index=None, media=False, source_media=None, offset=0.0):
    """Parse unbound text, or explicitly bind text times with canonical_time=text_time+offset."""
    offset = finite(offset, "subtitle offset")
    if media and (source_media is not None or offset != 0):
        raise AVError("Embedded captions already use original source PTS; external binding options are incompatible")
    if not media and stream_index is not None:
        raise AVError("stream_index applies only to embedded media subtitles")
    inputs = [input] + ([source_media] if source_media else [])
    with output_transaction(output, inputs=inputs) as stage:
        if media:
            source = probe_source(input)
            stream = select_stream(source, "subtitle", stream_index)
            sources = [source]
            rows = _embedded(source, stream, stage)
            subtitle_index = stream["index"]
            binding = "embedded_original_packet_pts"
        else:
            text_record = file_record(input, kind="subtitle_text")
            text = _decode(Path(input).read_bytes())
            suffix = Path(input).suffix.lower()
            if suffix in {".ass", ".ssa"}:
                rows = _ass(text)
            elif suffix == ".srt":
                rows = _srt(text)
            else:
                raise AVError("External subtitles must be ASS/SSA/SRT")
            source = probe_source(source_media) if source_media else None
            sources = [text_record] + ([source] if source else [])
            subtitle_index = None
            binding = "operator_declared_external_offset" if source else "UNBOUND"
            for row in rows:
                row["subtitle_start_seconds"] = row["start_seconds"]
                row["subtitle_end_seconds"] = row["end_seconds"]
                row["start_seconds"] += offset
                row["end_seconds"] += offset
        if not rows or len(rows) > 100000:
            raise AVError("Subtitle parse produced no cues or exceeds the bounded cue limit")
        clock = CLOCK if source else "unbound_subtitle_clock"
        source_hash = source["sha256"] if source else None
        origin = source["origin_seconds"] if source else None
        for i, row in enumerate(rows, 1):
            a, b = row["start_seconds"], row["end_seconds"]
            if a < -1e-9 or b <= a or not row["text_raw"].strip():
                raise AVError("Subtitle cue is empty or outside the nonnegative source clock")
            if source and source["duration_seconds"] is not None and b > source["duration_seconds"] + 0.001:
                raise AVError("Subtitle cue exceeds admitted source duration")
            row.update(cue_index=i, duration_seconds=b-a, parent_source_sha256=source_hash, clock=clock,
                       origin_seconds=origin, status="GENERATED_NOT_REVIEWED")
        data = {"schema": "ave.subtitles.v1", "parent_source_sha256": source_hash,
                "parent_stream_index": subtitle_index, "clock": clock, "origin_seconds": origin,
                "offset_seconds": offset, "binding_method": binding, "rows": rows,
                "limitations": ["External timing binding is an operator declaration, not automatic synchronization verification.",
                                "Subtitle wording, speaker labels and cue windows do not establish the audible performance."]}
        write_json(stage / "subtitles.json", data)
        write_csv(stage / "dialogue.csv", rows, ["cue_index", "start_seconds", "end_seconds", "duration_seconds",
                                                 "name", "style", "text_raw", "text_plain", "parent_source_sha256",
                                                 "clock", "origin_seconds", "status"])
        return finish_run(stage, "parse_subtitles", sources,
                          {"media": media, "stream_index": subtitle_index, "offset_seconds": offset,
                           "source_media": str(Path(source_media).resolve()) if source_media else None},
                          {"result_file": "subtitles.json", "csv_file": "dialogue.csv", "cue_count": len(rows),
                           "parent_source_sha256": source_hash, "clock": clock})
```

## avevidence/timeline.py

SHA-256: `4237371db68885fc905d0ab5e947d1c67140e5964e64839f3d7429626d7e8f5d`.

```python
"""Verified-source navigation joins; proximity never proves an audiovisual claim."""
from __future__ import annotations

import bisect
import math

from .common import AVError, finite, finish_run, output_transaction, select_stream, write_csv, write_json
from .visual import CLOCK, load_verified_run


def _same_number(a, b):
    return math.isclose(finite(a), finite(b), rel_tol=0, abs_tol=1e-6)


def align_timeline(subtitle_run, frame_run, output, *, audio_run=None, max_distance=2.0):
    max_distance = finite(max_distance, "maximum frame distance", 0)
    with output_transaction(output, inputs=[subtitle_run, frame_run] + ([audio_run] if audio_run else [])) as stage:
        subroot, submanifest, subtitles, subfiles, subrecord = load_verified_run(subtitle_run, {"parse_subtitles"})
        frameroot, framemanifest, frames, framefiles, framerecord = load_verified_run(frame_run, {"extract_frames"})
        source_hash = subtitles.get("parent_source_sha256")
        if not source_hash or source_hash != frames.get("parent_source_sha256"):
            raise AVError("Subtitle/frame source IDs are unbound or differ; bind external captions to the exact media first")
        if subtitles.get("clock") != CLOCK or frames.get("clock") != CLOCK:
            raise AVError("Subtitle/frame clocks are not the supported original-PTS source clock")
        if not _same_number(subtitles.get("origin_seconds"), frames.get("origin_seconds")):
            raise AVError("Subtitle/frame source origins differ")
        source = next((s for s in framemanifest["sources"] if s["sha256"] == source_hash), None)
        if source is None:
            raise AVError("Frame run lacks the declared media source record")
        select_stream(source, "video", frames.get("parent_stream_index"))
        points = sorted(frames.get("rows", []), key=lambda row: finite(row.get("source_seconds")))
        if not points:
            raise AVError("Cannot align against an empty frame run")
        for point in points:
            if point.get("source_sha256") != source_hash or point.get("stream_index") != frames["parent_stream_index"]:
                raise AVError("Frame row/source binding differs")
            if point.get("path") not in framefiles or framefiles[point["path"]]["sha256"] != point.get("sha256"):
                raise AVError("Frame row does not name a verified artifact")
        cues = subtitles.get("rows", [])
        cue_ids = [str(c["cue_index"]) for c in cues]
        if not cues or len(set(cue_ids)) != len(cue_ids):
            raise AVError("Subtitle cues are empty or have duplicate IDs")
        csv_name = submanifest["metadata"].get("csv_file")
        if csv_name not in subfiles:
            raise AVError("Subtitle dialogue CSV is not a verified artifact")
        features = {}
        records = [subrecord, framerecord]
        audio_stream = None
        if audio_run:
            audroot, audmanifest, audio, audfiles, audrecord = load_verified_run(audio_run, {"cue_features"})
            records.append(audrecord)
            if (audio.get("parent_source_sha256") != source_hash or audio.get("clock") != CLOCK
                    or not _same_number(audio.get("origin_seconds"), frames["origin_seconds"])):
                raise AVError("Audio feature source/clock differs from subtitle/frame binding")
            if audio.get("dialogue_clock_status") != "VERIFIED_SOURCE_BINDING":
                raise AVError("Unbound operator cue times cannot enter a verified timeline join")
            if audio.get("dialogue_csv_sha256") != subfiles[csv_name]["sha256"]:
                raise AVError("Audio features were computed from a different subtitle CSV")
            audio_stream = audio.get("parent_stream_index")
            select_stream(source, "audio", audio_stream)
            by_id = {str(c["cue_index"]): c for c in cues}
            for row in audio.get("rows", []):
                key = str(row.get("cue_index"))
                if key in features or key not in by_id:
                    raise AVError("Duplicate or unknown cue in feature join")
                cue = by_id[key]
                start = row.get("source_start_seconds", row.get("start_seconds"))
                end = row.get("source_end_seconds", row.get("end_seconds"))
                if not _same_number(start, cue["start_seconds"]) or not _same_number(end, cue["end_seconds"]):
                    raise AVError("Feature cue interval differs from the caption interval")
                features[key] = row
        times = [finite(p["source_seconds"]) for p in points]
        rows = []
        for cue in cues:
            a = finite(cue["start_seconds"], "cue start", 0)
            b = finite(cue["end_seconds"], "cue end", 0)
            if b <= a:
                raise AVError("Invalid subtitle cue interval")
            mid = (a + b) / 2
            pos = bisect.bisect_left(times, mid)
            candidates = [i for i in (pos-1, pos) if 0 <= i < len(points)]
            index = min(candidates, key=lambda i: (abs(times[i]-mid), times[i], i))
            nearest = points[index]
            delta = times[index] - mid
            if mid < times[0] or mid > times[-1]:
                proximity = "OUTSIDE_FRAME_POINT_RANGE"
            elif abs(delta) > max_distance:
                proximity = "DISTANT"
            else:
                proximity = "NEARBY"
            feature = features.get(str(cue["cue_index"]))
            rows.append({"cue_index": cue["cue_index"], "start_seconds": a, "end_seconds": b,
                         "name": cue.get("name", ""), "text_raw": cue.get("text_raw", ""), "text_plain": cue.get("text_plain", ""),
                         "frame_id": nearest["frame_id"], "frame_path": nearest["path"], "frame_sha256": nearest["sha256"],
                         "frame_source_seconds": times[index], "frame_delta_from_midpoint_seconds": delta,
                         "frame_distance_seconds": abs(delta), "proximity_status": proximity,
                         "frame_inside_cue": a <= times[index] < b,
                         "audio_feature_status": "NOT_PROVIDED" if feature is None else feature.get("status", "UNKNOWN"),
                         "audio_features": feature, "status": "GENERATED_NOT_REVIEWED"})
        data = {"schema": "ave.timeline.v1", "parent_source_sha256": source_hash,
                "clock": CLOCK, "origin_seconds": frames["origin_seconds"], "video_stream_index": frames["parent_stream_index"],
                "audio_stream_index": audio_stream, "subtitle_binding_method": subtitles.get("binding_method"),
                "subtitle_csv_sha256": subfiles[csv_name]["sha256"], "max_distance_seconds": max_distance,
                "input_runs": [{"path": r["path"], "sha256": r["sha256"]} for r in records],
                "rows": rows, "limitations": ["Source IDs and declared clocks are checked; external subtitle synchronization remains operator-declared.",
                                               "Nearest frames are navigation only. Proximity, still points and numerical features are not perceptual review."]}
        write_json(stage / "timeline.json", data)
        write_csv(stage / "timeline.csv", rows, ["cue_index", "start_seconds", "end_seconds", "name", "text_plain",
                                                 "frame_id", "frame_path", "frame_sha256", "frame_source_seconds",
                                                 "frame_delta_from_midpoint_seconds", "frame_distance_seconds", "proximity_status",
                                                 "frame_inside_cue", "audio_feature_status", "status"])
        return finish_run(stage, "align_timeline", records, {"max_distance_seconds": max_distance},
                          {"result_file": "timeline.json", "csv_file": "timeline.csv", "cue_count": len(rows),
                           "parent_source_sha256": source_hash, "clock": CLOCK})
```

## avevidence/visual.py

SHA-256: `9c6fb339130d67b8202af1c03e39e16ad42c3c52bff1de056bf0a1ce915de51e`.

```python
"""Source-clock still preparation. Generated images are never review receipts."""
from __future__ import annotations

import bisect
import math
from fractions import Fraction
from pathlib import Path
import re

from .common import (AVError, file_record, finite, finish_run, interval as checked_interval,
                     output_transaction, parse_time, probe_source, read_json, run,
                     safe_member, select_stream, sha256, write_csv, write_json)

CLOCK = "original_pts_minus_source_origin"
MAX_FRAMES = 10000
MAX_SOURCE_SECONDS = 60.0
_PTS = re.compile(r"\bn:\s*\d+\s+pts:\s*(-?\d+)\b")
_TIME_BASE = re.compile(r"config in time_base:\s*(\d+/\d+)")


def load_verified_run(directory, operation=None):
    """Validate manifest-owned files; directory contents are never inferred evidence."""
    root = Path(directory).resolve()
    record = file_record(root / "run.json", kind="evidence_run_manifest")
    manifest = read_json(root / "run.json")
    if manifest.get("schema") != "ave.run.v1":
        raise AVError("Unsupported evidence run schema")
    if operation is not None and manifest.get("operation") not in set(operation):
        raise AVError("Unexpected evidence run operation")
    artifacts = {}
    for item in manifest.get("artifacts", []):
        name = item.get("path")
        if name in artifacts:
            raise AVError("Duplicate manifest artifact")
        path = safe_member(root, name)
        if path.is_symlink() or not path.is_file() or sha256(path) != item.get("sha256"):
            raise AVError(f"Missing or changed evidence artifact: {name}")
        artifacts[name] = item
    result_name = manifest.get("metadata", {}).get("result_file")
    if result_name not in artifacts:
        raise AVError("Run result is not a verified manifest artifact")
    result = read_json(safe_member(root, result_name))
    if sha256(root / "run.json") != record["sha256"]:
        raise AVError("Evidence manifest changed while loading")
    return root, manifest, result, artifacts, record


def _geometry(stream, width):
    if not isinstance(width, int) or not 0 <= width <= 8192:
        raise AVError("width must be an integer from 0 to 8192 (0 keeps source geometry)")
    for side in stream.get("side_data_list", []):
        if "display matrix" in side.get("side_data_type", "").lower() or side.get("rotation", 0):
            raise AVError("Display-matrix/rotation transforms are unsupported; prepare a verified SDR square-pixel source")
    if finite(stream.get("tags", {}).get("rotate", 0), "rotation") != 0:
        raise AVError("Rotated sources require an explicitly verified geometry conversion")
    sar = stream.get("sample_aspect_ratio", "1:1")
    if sar not in (None, "N/A", "0:1", "1:1"):
        raise AVError("Non-square sample aspect ratio is not supported without an explicit geometry conversion")
    transfer = stream.get("color_transfer", "unknown")
    primaries = stream.get("color_primaries", "unknown")
    space = stream.get("color_space", "unknown")
    pixel = stream.get("pix_fmt", "unknown")
    depth = int(stream.get("bits_per_raw_sample") or 0)
    if (transfer in {"smpte2084", "arib-std-b67"} or "2020" in primaries or "2020" in space
            or depth > 8 or re.search(r"(?:p|gray)(?:9|10|12|14|16)(?:le|be)?$", pixel)):
        raise AVError("HDR/wide-gamut/high-depth source requires an explicit color-managed conversion; automatic conversion refused")
    return {"source_width": stream.get("width"), "source_height": stream.get("height"),
            "sample_aspect_ratio": sar, "pixel_format": pixel,
            "color_range": stream.get("color_range", "unknown"), "color_space": space,
            "color_primaries": primaries, "color_transfer": transfer,
            "output_pixel_format": "rgb24", "output_container": "PNG",
            "conversion": "FFmpeg SDR decode and optional scale; no HDR tone mapping; untagged color remains unspecified",
            "requested_width": width, "autorotate": False}


def _frame_index(source, stream):
    result = run(["ffprobe", "-v", "error", "-select_streams", str(stream["index"]),
                  "-show_frames", "-show_entries", "frame=pts,duration,pkt_duration,width,height",
                  "-of", "json", source["path"]])
    import json
    raw = json.loads(result.stdout)
    try:
        tb = Fraction(stream["time_base"])
    except (KeyError, ValueError, ZeroDivisionError) as exc:
        raise AVError("Source video time base is unavailable") from exc
    if tb <= 0:
        raise AVError("Invalid source video time base")
    entries = []
    for i, row in enumerate(raw.get("frames", [])):
        if "pts" not in row:
            raise AVError("A decoded frame has no original presentation PTS; inferred timestamps are refused")
        pts = int(row["pts"])
        if entries and pts <= entries[-1]["pts"]:
            raise AVError("Non-increasing/duplicate source PTS requires a specialized clock audit")
        if row.get("width") != stream.get("width") or row.get("height") != stream.get("height"):
            raise AVError("Midstream geometry changes are unsupported")
        original = float(pts * tb)
        duration = int(row.get("duration", row.get("pkt_duration", 0)) or 0) * tb
        entries.append({"index": i, "pts": pts, "original": original,
                        "time": original - source["origin_seconds"], "duration": float(duration)})
    if not entries:
        raise AVError("Source has no decoded video frames")
    return entries, tb


def _membership(indices):
    # A balanced expression avoids evaluating thousands of equalities per frame.
    if len(indices) == 1:
        return f"eq(n,{indices[0]})"
    mid = len(indices) // 2
    return f"if(lt(n,{indices[mid]}),{_membership(indices[:mid])},{_membership(indices[mid:])})"


def extract_frames(input, output, *, mode="interval", start=None, end=None, interval=2.0,
                   fps=10.0, timestamps=None, threshold=0.35, width=1280, stream_index=None):
    if mode not in {"interval", "dense", "source", "exact", "shots"}:
        raise AVError("Unknown frame extraction mode")
    with output_transaction(output, inputs=[input]) as stage:
        source = probe_source(input)
        stream = select_stream(source, "video", stream_index)
        geometry = _geometry(stream, width)
        entries, tb = _frame_index(source, stream)
        times = [row["time"] for row in entries]
        tail = entries[-1]["duration"]
        endpoint_method = "last_original_pts_plus_decoded_frame_duration"
        if tail <= 0:
            tail = times[-1] - times[-2] if len(times) > 1 else 0
            endpoint_method = "last_original_pts_plus_previous_frame_delta_estimate"
        endpoint = times[-1] + tail
        if endpoint <= 0:
            raise AVError("Source has no positive video timeline")
        requests = []
        selections = []
        if mode == "exact":
            if start is not None or end is not None:
                raise AVError("Exact mode uses timestamps, not start/end")
            if not timestamps or len(timestamps) > MAX_FRAMES:
                raise AVError(f"Exact mode requires 1–{MAX_FRAMES} requested timestamps")
            requests = [parse_time(x) for x in timestamps]
            if any(x is None for x in requests):
                raise AVError("Empty requested timestamp")
            for target in requests:
                pos = bisect.bisect_left(times, target - 1e-10)
                if pos == len(times):
                    raise AVError(f"No source frame at or after requested time {target}")
                selections.append(pos)
            a, b = None, None
        else:
            if mode in {"source", "dense"} and (start is None or end is None):
                raise AVError("Dense/source extraction requires an explicit bounded start/end")
            a, b = checked_interval(start, end, endpoint)
            if mode == "source" and b - a > MAX_SOURCE_SECONDS:
                raise AVError(f"Source-frame extraction is limited to {MAX_SOURCE_SECONDS:g} seconds per run")
            if mode in {"interval", "dense"}:
                step = finite(interval, "interval", 0) if mode == "interval" else 1 / finite(fps, "fps", 1e-9)
                if step <= 0:
                    raise AVError("interval must be positive")
                count = int(math.ceil((b - a) / step - 1e-10))
                if count > MAX_FRAMES:
                    raise AVError(f"Requested frame count exceeds {MAX_FRAMES}")
                requests = [a + i * step for i in range(count)]
                for target in requests:
                    pos = bisect.bisect_left(times, target - 1e-10)
                    if pos == len(times) or times[pos] >= b - 1e-10:
                        raise AVError(f"No source frame at/after {target} inside the half-open requested interval")
                    selections.append(pos)
            elif mode == "source":
                selections = [i for i, t in enumerate(times) if a - 1e-10 <= t < b - 1e-10]
                requests = [None] * len(selections)
            else:
                threshold = finite(threshold, "threshold")
                if not 0 < threshold < 1:
                    raise AVError("Scene threshold must lie strictly between 0 and 1")
        if mode != "shots" and (not selections or len(selections) > MAX_FRAMES):
            raise AVError("No frames selected or source-frame count exceeds the per-run limit")
        if mode == "shots":
            select = f"gte(t,{a+source['origin_seconds']:.12f})*lt(t,{b+source['origin_seconds']:.12f})*gt(scene,{threshold:.9f})"
        else:
            select = _membership(sorted(set(selections)))
        filters = [f"select='{select}'"]
        if mode == "shots":
            filters.append("metadata=print:key=lavfi.scene_score")
        filters.append("showinfo")
        if width:
            filters.append(f"scale={width}:-1")
        filters.append("format=rgb24")
        script = stage / "selection.filter"
        script.write_text(",".join(filters), encoding="utf-8")
        images = stage / "frames"
        images.mkdir()
        decoded = run(["ffmpeg", "-hide_banner", "-nostdin", "-n", "-xerror", "-err_detect", "explode",
                       "-copyts", "-noautorotate", "-i", source["path"], "-map", f"0:{stream['index']}",
                       "-an", "-sn", "-dn", "-filter_script:v", script, "-fps_mode", "passthrough",
                       "-frames:v", str(MAX_FRAMES + 1 if mode == "shots" else len(set(selections))),
                       "-c:v", "png", "-pix_fmt", "rgb24", images / "frame_%06d.png"])
        actual_pts = [int(m.group(1)) for line in decoded.stderr.splitlines()
                      if "Parsed_showinfo" in line and (m := _PTS.search(line))]
        bases = {Fraction(x) for x in _TIME_BASE.findall(decoded.stderr)}
        if bases != {tb}:
            raise AVError("Decoded filter time base does not match admitted original video time base")
        artifacts = sorted(images.glob("frame_*.png"))
        if len(artifacts) != len(actual_pts):
            raise AVError("Decoded timestamp/image count mismatch")
        pts_to_entry = {entry["pts"]: entry["index"] for entry in entries}
        if any(pts not in pts_to_entry for pts in actual_pts):
            raise AVError("Extracted PTS could not be matched to the original frame index")
        if mode == "shots":
            if len(actual_pts) > MAX_FRAMES:
                raise AVError("Shot artifact count exceeds the per-run limit")
            selections = [pts_to_entry[pts] for pts in actual_pts]
            requests = [None] * len(selections)
            scores = [float(x) for x in re.findall(r"lavfi\.scene_score=([0-9.]+)", decoded.stderr)]
            if len(scores) != len(actual_pts):
                raise AVError("Shot-score/frame correspondence failed")
        else:
            expected = [entries[i]["pts"] for i in sorted(set(selections))]
            if actual_pts != expected:
                raise AVError("Decoded frames differ from selected original PTS")
            scores = None
        by_index = {pts_to_entry[pts]: path for pts, path in zip(actual_pts, artifacts)}
        rows, first_ids = [], {}
        for i, (index, requested) in enumerate(zip(selections, requests), 1):
            entry = entries[index]
            path = by_index[index]
            if not path.is_file() or not path.stat().st_size:
                raise AVError("A selected frame artifact is missing or empty")
            frame_id = f"F{i:06d}"
            duplicate = first_ids.get(index)
            first_ids.setdefault(index, frame_id)
            rows.append({"frame_id": frame_id, "path": path.relative_to(stage).as_posix(), "sha256": sha256(path),
                         "source_sha256": source["sha256"], "stream_index": stream["index"],
                         "source_frame_index": index, "source_pts": entry["pts"], "source_time_base": str(tb),
                         "original_pts_seconds": entry["original"], "source_seconds": entry["time"],
                         "requested_seconds": requested,
                         "timing_delta_seconds": None if requested is None else entry["time"] - requested,
                         "duplicate_of": duplicate, "scene_score": None if scores is None else scores[i-1],
                         "status": "GENERATED_NOT_REVIEWED"})
        result = {"schema": "ave.frames.v1", "mode": mode, "parent_source_sha256": source["sha256"],
                  "parent_stream_index": stream["index"], "clock": CLOCK, "origin_seconds": source["origin_seconds"],
                  "selection_policy": "first source frame at or after each request; source/shot modes retain original PTS",
                  "source_video_endpoint_seconds": endpoint, "video_endpoint_method": endpoint_method,
                  "geometry": geometry, "rows": rows,
                  "unique_frame_count": len(artifacts), "request_row_count": len(rows),
                  "zero_shots": mode == "shots" and not rows}
        write_json(stage / "frames.json", result)
        write_csv(stage / "frames.csv", rows, ["frame_id", "path", "sha256", "source_seconds", "requested_seconds",
                                               "timing_delta_seconds", "source_frame_index", "source_pts", "source_time_base",
                                               "duplicate_of", "scene_score", "status"])
        mapping = {"kind": "still_points", "parent_source_sha256": source["sha256"],
                   "parent_stream_index": stream["index"], "frames": [
                       {"frame_id": r["frame_id"], "artifact_path": r["path"], "artifact_sha256": r["sha256"],
                        "source_seconds": r["source_seconds"]} for r in rows]}
        return finish_run(stage, "extract_frames", [source],
                          {"mode": mode, "start": a, "end": b, "interval": interval, "fps": fps,
                           "timestamps": timestamps, "threshold": threshold, "width": width, "stream_index": stream["index"]},
                          {"result_file": "frames.json", "csv_file": "frames.csv", "review_mapping": mapping,
                           "frame_count": len(rows), "unique_frame_count": len(artifacts)})


def contact_sheets(frame_run, output, *, columns=4, rows=4, thumb_width=360):
    try:
        from PIL import Image, ImageDraw, ImageOps
    except ImportError as exc:
        raise AVError("Pillow is required for contact sheets") from exc
    if any(not isinstance(x, int) or x <= 0 for x in (columns, rows, thumb_width)):
        raise AVError("Contact-sheet dimensions must be positive integers")
    if columns * rows > 100 or columns * thumb_width > 8192:
        raise AVError("Contact sheet exceeds the bounded layout limit")
    with output_transaction(output, inputs=[frame_run]) as stage:
        root, parent, data, owned, parent_record = load_verified_run(frame_run, {"extract_frames"})
        points = data.get("rows", [])
        if not points:
            raise AVError("Frame run contains no frame points")
        for point in points:
            if point.get("path") not in owned or owned[point["path"]]["sha256"] != point.get("sha256"):
                raise AVError("Frame row is not bound to a verified artifact")
        with Image.open(safe_member(root, points[0]["path"])) as im:
            thumb_height = max(1, round(thumb_width * im.height / im.width))
        if rows * (thumb_height + 40) > 8192:
            raise AVError("Contact sheet exceeds the bounded layout limit")
        sheets = []
        per_sheet = columns * rows
        for n, offset in enumerate(range(0, len(points), per_sheet), 1):
            subset = points[offset:offset+per_sheet]
            canvas = Image.new("RGB", (columns * thumb_width, rows * (thumb_height + 40)), "black")
            draw = ImageDraw.Draw(canvas)
            for j, point in enumerate(subset):
                path = safe_member(root, point["path"])
                if sha256(path) != point["sha256"]:
                    raise AVError("Frame changed before rendering")
                with Image.open(path) as im:
                    im = ImageOps.contain(im.convert("RGB"), (thumb_width, thumb_height))
                    x, y = (j % columns) * thumb_width, (j // columns) * (thumb_height + 40)
                    canvas.paste(im, (x, y))
                if sha256(path) != point["sha256"]:
                    raise AVError("Frame changed while rendering")
                draw.text((x+3, y+thumb_height+3), f"{point['frame_id']}  {point['source_seconds']:.6f}s", fill="white")
            filename = f"sheet_{n:04d}.png"
            canvas.save(stage / filename)
            sheets.append({"path": filename, "sha256": sha256(stage / filename),
                           "frame_ids": [p["frame_id"] for p in subset]})
        parent_link = {"run_manifest_path": str(root / "run.json"), "run_manifest_sha256": parent_record["sha256"]}
        data_out = {"schema": "ave.contacts.v1", "parent_frame_run": parent_link,
                    "parent_source_sha256": data["parent_source_sha256"], "parent_stream_index": data["parent_stream_index"],
                    "sheets": sheets, "status": "GENERATED_NOT_REVIEWED", "note": "Navigation images only; no temporal coverage inferred"}
        write_json(stage / "contacts.json", data_out)
        mapping = {"kind": "contact_sheet_points", "parent_source_sha256": data["parent_source_sha256"],
                   "parent_stream_index": data["parent_stream_index"], "parent_frame_run": parent_link,
                   "sheets": [{"artifact_path": s["path"], "artifact_sha256": s["sha256"], "frame_ids": s["frame_ids"]} for s in sheets]}
        return finish_run(stage, "contact_sheets", [parent_record],
                          {"columns": columns, "rows": rows, "thumb_width": thumb_width},
                          {"result_file": "contacts.json", "parent_frame_run": parent_link, "review_mapping": mapping})
```

## pyproject.toml

SHA-256: `10328b50e8c919d385c2c276a24f223932c83f2fcd47f105dc821f6f8ba746f5`.

```toml
[build-system]
requires = ["setuptools>=68"]
build-backend = "setuptools.build_meta"

[project]
name = "av-evidence-toolkit"
version = "1.0.0"
description = "Portable audiovisual evidence preparation with source clocks, provenance and declared-review accounting"
readme = "README.md"
requires-python = ">=3.10"
license = {text = "MIT"}
authors = [{name = "AV Evidence Toolkit contributors"}]
dependencies = ["Pillow>=10"]

[project.optional-dependencies]
audio = ["numpy>=1.26", "soundfile>=0.12", "librosa>=0.10"]
all = ["numpy>=1.26", "soundfile>=0.12", "librosa>=0.10"]

[project.scripts]
ave = "avevidence.cli:main"

[tool.setuptools.packages.find]
include = ["avevidence*"]

[tool.setuptools]
license-files = ["LICENSE", "LICENSES/*.txt"]
```

## README.md

SHA-256: `92f93b5737838ea97dd93334be7841d43e7a82b70c677db4fbde2c537ff8d888`.

Repository representation: the following **base64-encoded markdown payload** preserves the source block while separating embedded example links from repository navigation. Decode this block with `base64.b64decode` before following the original extraction/reproduction instructions. Decoded UTF-8 payload SHA-256: `92f93b5737838ea97dd93334be7841d43e7a82b70c677db4fbde2c537ff8d888`; bytes: 6083.

```base64
IyBBViBFdmlkZW5jZSBUb29sa2l0IDEuMC4wCgpBIHBvcnRhYmxlIFB5dGhvbiBjb21tYW5kLWxpbmUgdG9vbGtpdCBmb3IgcHJl
cGFyaW5nLCBtZWFzdXJpbmcsIGxvY2F0aW5nIGFuZCBhdWRpdGluZyBhdWRpb3Zpc3VhbCBldmlkZW5jZS4gSXQgY29tYmluZXMg
c3VidGl0bGUtb3JpZW50ZWQgZXBpc29kZSBuYXZpZ2F0aW9uIHdpdGggc291cmNlIGlkZW50aXR5LCBvcmlnaW5hbCBwcmVzZW50
YXRpb24gdGltZXN0YW1wcywgbmF0aXZlIGRlY29kZWQtYXVkaW8gY29tcGFyaXNvbiBhbmQgc3RyaWN0IGFjY291bnRpbmcgb2Yg
ZGVjbGFyZWQgcGVyY2VwdHVhbCByZXZpZXcuCgoqKkNvbXB1dGVkIG1lYXN1cmVtZW50cyBhcmUgbm90IGRpcmVjdCBsaXN0ZW5p
bmcuIEdlbmVyYXRlZCBmcmFtZXMgYXJlIG5vdCBpbnNwZWN0ZWQgZnJhbWVzLioqIFRoaXMgdG9vbGtpdCByZWNvcmRzIHRoYXQg
Ym91bmRhcnkgcmF0aGVyIHRoYW4gY2xhaW1pbmcgdG8gc3VwcGx5IGEgbW9kZWwncyBtaXNzaW5nIG1lZGlhLWlucHV0IGNhcGFi
aWxpdHkuCgojIyBTdGFydAoKUmVxdWlyZW1lbnRzOiBQeXRob24gMy4xMCssIEZGbXBlZy9mZnByb2JlIDcuMSsgb24gUEFUSCwg
YW5kIFBpbGxvdy4gTnVtUHksIFNvdW5kRmlsZSBhbmQgbGlicm9zYSBhcmUgb3B0aW9uYWwgZm9yIGN1ZS1sZXZlbCBzcGVjdHJh
bC9waXRjaCBmZWF0dXJlcy4gTm8gbWVkaWEsIG1vZGVsIHdlaWdodHMsIEZGbXBlZyBiaW5hcmllcyBvciBjbG91ZCBjcmVkZW50
aWFscyBhcmUgYnVuZGxlZC4KCkZyb20gdGhlIGV4dHJhY3RlZCB0b29sa2l0IGZvbGRlcjoKCmBgYHNoCnB5dGhvbiAtbSBwaXAg
aW5zdGFsbCAiLlthdWRpb10iCmF2ZSBkb2N0b3IKYGBgCgpXaXRob3V0IGluc3RhbGxpbmcgdGhpcyBwYWNrYWdlLCB1c2UgYHB5
dGhvbiBhdnRvb2wucHlgIG9yIGBweXRob24gLW0gYXZldmlkZW5jZWAgaW4gcGxhY2Ugb2YgYGF2ZWAsIHdpdGggdGhlIGRlcGVu
ZGVuY2llcyBhbHJlYWR5IGluc3RhbGxlZC4gVXNlIGBweXRob24zYCB3aGVyZSB0aGF0IGlzIHRoZSBQeXRob24gY29tbWFuZC4g
QWxsIGV4YW1wbGVzIHdvcmsgd2l0aCBxdW90ZWQgV2luZG93cyBvciBMaW51eCBwYXRocy4KCmBgYHNoCmF2ZSBwcm9iZSAiZXBp
c29kZS5ta3YiICJydW5zL3Byb2JlLTAxIgphdmUgYnVuZGxlICJlcGlzb2RlLm1rdiIgInJ1bnMvZXBpc29kZS0wMSIgLS1zdWJ0
aXRsZXMgImVwaXNvZGUuamEuYXNzIiAtLWludGVydmFsIDIgLS1zaG90cyAtLWN1ZS1mZWF0dXJlcwphdmUgdmVyaWZ5ICJydW5z
L2VwaXNvZGUtMDEiCmBgYAoKV2hlbiBhIG1lZGlhIHR5cGUgaGFzIG11bHRpcGxlIHN0cmVhbXMsIGNob29zZSB0aGUgaW50ZW5k
ZWQgKiphYnNvbHV0ZSBmZnByb2JlIHN0cmVhbSBpbmRleCoqLCBmb3IgZXhhbXBsZSBgLS1hdWRpby1zdHJlYW0gMSAtLXZpZGVv
LXN0cmVhbSAwYC4gQW1iaWd1aXR5IGlzIHJlZnVzZWQuIEVtYmVkZGVkIHN1YnRpdGxlcyBhcmUgc2VsZWN0ZWQgZXhwbGljaXRs
eSB3aXRoIGAtLXN1YnRpdGxlLXN0cmVhbSBOYDsgZXh0ZXJuYWwgc3VidGl0bGVzIGFyZSBib3VuZCB0byB0aGUgc3VwcGxpZWQg
c291cmNlIGluIGEgYnVuZGxlLgoKRXZlcnkgb3V0cHV0IGlzIGEgKipuZXcgZGlyZWN0b3J5KiouIEV4aXN0aW5nIG91dHB1dHMg
YW5kIGlucHV0L291dHB1dCBjb2xsaXNpb25zIGFyZSByZWZ1c2VkLiBXb3JrIGlzIHN0YWdlZDsgZmFpbHVyZXMgcmV0YWluIGEg
Y2xlYXJseSBuYW1lZCBoaWRkZW4gc3RhZ2luZyBkaXJlY3Rvcnkgd2l0aCBgRkFJTEVELmpzb25gLCB3aGlsZSB0aGUgcmVxdWVz
dGVkIGZpbmFsIGRpcmVjdG9yeSByZW1haW5zIHVucHVibGlzaGVkLiBEbyBub3QgdHJlYXQgYSBmYWlsZWQgc3RhZ2luZyBkaXJl
Y3RvcnkgYXMgZXZpZGVuY2UuCgojIyBGb2N1cyBhIHF1ZXN0aW9uCgpgYGBzaAphdmUgZnJhbWVzICJlcGlzb2RlLm1rdiIgInJ1
bnMvZ2VzdHVyZS0wMSIgLS1tb2RlIHNvdXJjZSAtLXN0YXJ0IDAwOjEyOjAzLjI1MCAtLWVuZCAwMDoxMjowNQphdmUgY29udGFj
dHMgInJ1bnMvZ2VzdHVyZS0wMSIgInJ1bnMvZ2VzdHVyZS1jb250YWN0cy0wMSIKYXZlIGF1ZGlvLW1ldHJpY3MgImVwaXNvZGUu
bWt2IiAicnVucy9saW5lLW1ldHJpY3MtMDEiIC0tc3RhcnQgMDA6MTI6MDMgLS1lbmQgMDA6MTI6MDgKYXZlIGNsaXAtYXYgImVw
aXNvZGUubWt2IiAicnVucy9yZXZpZXctY2xpcC0wMSIgLS1zdGFydCAwMDoxMjowMyAtLWVuZCAwMDoxMjowOCAtLXBhZCAxCmBg
YAoKT3JpZ2luYWwgc291cmNlLWZyYW1lIFBUUyBhbmQgcmVxdWVzdGVkIHRpbWVzIGFyZSBzZXBhcmF0ZS4gRXhhY3QgbW9kZSBz
ZWxlY3RzIHRoZSBmaXJzdCBzb3VyY2UgZnJhbWUgYXQgb3IgYWZ0ZXIgYSByZXF1ZXN0OyBpdCBkb2VzIG5vdCBpbnZlbnQgYSBm
cmFtZSBhdCB0aGF0IHJlcXVlc3RlZCBpbnN0YW50LiBTb3VyY2UtZnJhbWUgbW9kZSByZXF1aXJlcyBhIGJvdW5kZWQgaW50ZXJ2
YWwgYW5kIGNhcHMgb3V0cHV0IGNvdW50LiBVbm1hbmFnZWQgSERSLCBnZW9tZXRyeSB0cmFuc2Zvcm1hdGlvbnMgYW5kIHVuc3Vw
cG9ydGVkIHRpbWluZyBhcmUgcmVmdXNlZCByYXRoZXIgdGhhbiBzaWxlbnRseSBpbnRlcnByZXRlZC4KClRoZSBjYW5vbmljYWwg
c291cmNlIGNsb2NrIGlzICoqb3JpZ2luYWwgcHJlc2VudGF0aW9uIHRpbWVzdGFtcCBtaW51cyB0aGUgcmVjb3JkZWQgc291cmNl
IG9yaWdpbioqLiBEZWxheWVkIGF1ZGlvIGFuZCBnYXBzIHJlbWFpbiBleHBsaWNpdCBtYXBwaW5nczsgdGhleSBhcmUgbm90IHNp
bGVudGx5IHJlcGxhY2VkIHdpdGggemVyby1vZmZzZXQgc2FtcGxlIHBvc2l0aW9ucyBvciBzeW50aGV0aWMgc2lsZW5jZS4gU2Vl
IFt0aW1pbmcgYW5kIGV2aWRlbmNlIHJ1bGVzXShkb2NzL01FVEhPRFMubWQpLgoKIyMgQXVkaW8gZmlkZWxpdHkgYW5kIGNvbXBh
cmlzb24KCmBgYHNoCmF2ZSBleHRyYWN0LWF1ZGlvICJlcGlzb2RlLm1rdiIgInJ1bnMvYXVkaW8tMDEiCmF2ZSBjb21wYXJlLWF1
ZGlvICJvcmlnaW5hbC5ta3YiICJjYW5kaWRhdGUubWt2IiAicnVucy9jb21wYXJpc29uLTAxIiAtLWEtc3RyZWFtIDEgLS1iLXN0
cmVhbSAxCmBgYAoKVGhlIHdvcmtpbmcgZm9ybWF0IGlzIG5hdGl2ZS1yYXRlLCBuYXRpdmUtY2hhbm5lbCBmbG9hdDY0IFdBVi4g
SXQgYXZvaWRzIHRoZSBmbG9hdDMyIHByZWNpc2lvbiBjb2xsaXNpb24gYW5kIGF1dG9tYXRpYyBGTEFDIHF1YW50aXphdGlvbiBm
b3VuZCBpbiB0aGUgcHJlZGVjZXNzb3IgYXVkaXRzLiBGTEFDIGV4cG9ydCBtdXN0IHBhc3MgYSBkZWNvZGVkLXNhbXBsZSBwcmVz
ZXJ2YXRpb24gY2hlY2suIFN0cmVhbS1jb3B5IGV4cG9ydCBpcyBhdmFpbGFibGUgc2VwYXJhdGVseTsgY29weWluZyBhIGNvZGVj
IHN0cmVhbSBkb2VzIG5vdCBpdHNlbGYgcHJvdmUgdGltaW5nIG9yIHBhY2tldCBpZGVudGl0eS4KCkNvbXBhcmlzb24gcmVwb3J0
cyBkZWNvZGVkIHNhbXBsZXMsIHJhdGUsIGNoYW5uZWwgbGF5b3V0IGFuZCBzb3VyY2UtY2xvY2sgdGltaW5nIHNlcGFyYXRlbHku
IEl0IGRvZXMgbm90IGVzdGFibGlzaCBlcXVhbCB2aWRlbywgZW5jb2RlZCBwYWNrZXRzLCBzcGVha2VyIGlkZW50aXR5IG9yIHBl
cmNlcHR1YWwgZXF1aXZhbGVuY2UuIE1BVENIL0RJRkZFUkVOVC9JTkRFVEVSTUlOQVRFIGFyZSBleHBsaWNpdCByZXN1bHRzLiBS
TVMsIExVRlMsIGxvdy1lbmVyZ3kgZnJhY3Rpb25zIGFuZCBGMCBoYXZlIHNlcGFyYXRlIG1lYW5pbmdzOyBubyBsb3ctc2FtcGxl
LWFtcGxpdHVkZSBwZXJjZW50YWdlIGlzIGxhYmVsZWQgYXMgbWVhc3VyZWQgcGF1c2UgZHVyYXRpb24uCgojIyBSZXZpZXcgYWNj
b3VudGluZwoKYGBgc2gKYXZlIHJldmlldy10ZW1wbGF0ZXMgInJldmlldy1yZWNvcmRzIgphdmUgcmV2aWV3LWNoZWNrICJyZXZp
ZXctcmVjb3Jkcy9yZXZpZXdzLmpzb24iICJydW5zL2VwaXNvZGUtMDEvaW52ZW50b3J5IiAicmV2aWV3LXJlY29yZHMvY2FwYWJp
bGl0aWVzLmpzb24iICJydW5zL3Jldmlldy1jaGVjay0wMSIKYGBgCgpUZW1wbGF0ZXMgYXJlIGludGVudGlvbmFsbHkgaW52YWxp
ZCB1bnRpbCBjb21wbGV0ZWQgd2l0aCByZWFsIHNvdXJjZSBpZGVudGl0aWVzLCByZXZpZXdlciBkZXRhaWxzIGFuZCBoYXNoZWQg
Y2FwYWJpbGl0eS9wcmVzZW50YXRpb24gcmVjZWlwdHMuIFRoZSBjaGVja2VyIHZhbGlkYXRlcyBkYXRlcywgc3RyZWFtcywgbW9k
YWxpdGllcywgaW50ZXJ2YWxzLCBhcnRpZmFjdCBoYXNoZXMgYW5kIHNvdXJjZS9kZXJpdmF0aXZlIG1hcHBpbmdzLiBJdCByZWpl
Y3RzIG1ldHJpY3Mgb3IgdHJhbnNjcmlwdHMgYXMgbGlzdGVuaW5nIGFuZCBzdGlsbC1pbWFnZSBjb3ZlcmFnZSBhcyBtb3Rpb24g
cmV2aWV3LiBPdmVybGFwcGluZyBpbnRlcnZhbHMgYXJlIGNvdW50ZWQgb25jZTsgZHVwbGljYXRlcyBkbyBub3QgbXVsdGlwbHkg
ZXZpZGVuY2Ugd2VpZ2h0LgoKUGFzc2luZyB2YWxpZGF0ZXMgKip0aGUgY29uc2lzdGVuY3kgb2YgcmVjb3JkZWQgZGVjbGFyYXRp
b25zKiosIG5vdCB0aGUgdHJ1dGggb2YgcGVyY2VwdGlvbiBvciB0aGUgcXVhbGl0eSBvZiBpbnRlcnByZXRhdGlvbi4gUmVhbCBs
aXN0ZW5pbmcgcmVxdWlyZXMgYXVkaW8gdG8gcmVhY2ggYSBjYXBhYmxlIGh1bWFuIG9yIG1vZGVsIHRocm91Z2ggYSB2ZXJpZmll
ZCBtZWNoYW5pc20uIFNlZSBbcmV2aWV3LXJlY29yZCBzY2hlbWFzIGFuZCBleGFtcGxlc10oZG9jcy9SRVZJRVdfUkVDT1JEUy5t
ZCkuCgojIyBTaGFyZSBhbmQgdmVyaWZ5CgpgYGBzaAphdmUgcGFjayAicnVucy9lcGlzb2RlLTAxIiAiZXBpc29kZS1ldmlkZW5j
ZS56aXAiCmF2ZSB2ZXJpZnktYXJjaGl2ZSAiZXBpc29kZS1ldmlkZW5jZS56aXAiCmBgYAoKT25seSBtYW5pZmVzdC1saXN0ZWQg
cnVuIGFydGlmYWN0cyBhcmUgcGFja2VkLiBTb3VyY2UgZmlsZXMgYXJlIHJlZmVyZW5jZWQgYnkgaWRlbnRpdHkgcmF0aGVyIHRo
YW4gYXV0b21hdGljYWxseSBjb3BpZWQgaW50byB0aGUgYXJjaGl2ZS4gRXZpZGVuY2UgYXJjaGl2ZXMgY2FuIGNvbnRhaW4gZ2Vu
ZXJhdGVkIG1lZGlhOyB0aGlzIHNvdXJjZS1jb2RlIHJlbGVhc2UgY29udGFpbnMgbm9uZS4gQ2hlY2tzdW1zIGVzdGFibGlzaCBi
eXRlIGludGVncml0eSwgbm90IGF1dGhlbnRpY2l0eSBvZiBhbiBvcmlnaW5hbCBzb3VyY2Ugb3IgdHJ1dGggb2YgYSByZXZpZXcu
CgojIyBEb2N1bWVudGF0aW9uIGFuZCB2YWxpZGF0aW9uCgotIFtDb21tYW5kIHJlZmVyZW5jZV0oZG9jcy9DT01NQU5EUy5tZCkK
LSBbTWV0aG9kcywgbGltaXRzIGFuZCBzY2hlbWEgY29udmVudGlvbnNdKGRvY3MvTUVUSE9EUy5tZCkKLSBbUmV2aWV3IHJlY29y
ZHNdKGRvY3MvUkVWSUVXX1JFQ09SRFMubWQpCi0gW0NoYW5nZXMgZnJvbSB0aGUgdHdvIHJlZmVyZW5jZSB0b29sa2l0c10oZG9j
cy9PUklHSU5TX0FORF9DSEFOR0VTLm1kKQotIFtBZ2VudCBoYW5kb2ZmIGluc3RydWN0aW9uc10oQUdFTlRfU1RBUlRfSEVSRS5t
ZCkKLSBbVmFsaWRhdGlvbiByZXN1bHRzXShyZXBvcnRzL1ZBTElEQVRJT04ubWQpCgpSdW4gdGhlIHJlZ3Jlc3Npb24gc3VpdGUg
d2l0aCBgcHl0aG9uIHNjcmlwdHMvc2VsZl90ZXN0LnB5YC4gV2luZG93cyBpcyBsb2NhbGx5IHRlc3RlZDsgTGludXggdXNlcyB0
aGUgc2FtZSBQeXRob24vRkZtcGVnIGltcGxlbWVudGF0aW9uIGJ1dCBjb3VsZCBub3QgYmUgZXhlY3V0ZWQgb24gdGhlIGJ1aWxk
IGhvc3QuIFRoZSByZWxlYXNlIHJlY29yZHMgdGhhdCBkaXN0aW5jdGlvbi4gTm8gY29tcGF0aWJpbGl0eSBjbGFpbSBzdWJzdGl0
dXRlcyBmb3IgcnVubmluZyB0aGUgdGVzdHMgb24gYSBuZXcgaG9zdC4KClRoZSB0b29sa2l0IGlzIE1JVCBsaWNlbnNlZC4gVGhl
IHJldGFpbmVkIFtHQkMgdG9vbGtpdCBsaWNlbnNlXShMSUNFTlNFUy9HQkNfVE9PTEtJVF9NSVQudHh0KSBjb3ZlcnMgYWRhcHRl
ZCBtYXRlcmlhbC4gVGhpcyBpcyBhIG5ldyBpbXBsZW1lbnRhdGlvbiBpbmZvcm1lZCBieSB0aGUgc3VwcGxpZWQgdG9vbGtpdHMg
YW5kIGF1ZGl0czsgaXQgZG9lcyBub3QgY2xhaW0gdG8gcmVjb25zdHJ1Y3QgYW4gZWFybGllciBjaGF0J3MgaGlkZGVuIGVudmly
b25tZW50Lgo=
```

## LICENSE

SHA-256: `cd646286b2546b9584ccd9650695045f689538d9c91ac7793bfd309c6322f023`.

```text
MIT License

Copyright (c) 2026 AV Evidence Toolkit contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## LICENSES/GBC_TOOLKIT_MIT.txt

SHA-256: `bb91d286306641691d1cdfb8dc0231662770195c5817e076831a264fc88d7c34`.

```text
MIT License

Copyright (c) 2026 OpenAI ChatGPT and the Manga / Anime analysis project contributor

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
