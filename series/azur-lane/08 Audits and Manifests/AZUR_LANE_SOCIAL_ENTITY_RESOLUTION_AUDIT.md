# Azur Lane Social Entity Resolution Audit

Generated: `2026-08-22T22:42:23.245462Z`

## Conclusion

Raw zero is subsystem-polymorphic. It is Commander only in type-1 Fleet/Dorm3D player rows and is the Port News system account in type-2 Juustagram posts.

Raw client IDs are preserved. Normalization occurs only in derived `author_entity`, `participant_entities`, channel-context, and relationship-evidence fields.

## Confirmed normalization rules

| Subsystem | Raw ID(s) | Type | Meaning / entity | Confidence | Source-semantic basis |
|---|---|---:|---|---:|---|
| fleet_chat | 0 | 1 | `COMMANDER` | 100% | Player-option rows and surrounding lines explicitly address/invite the Commander. |
| dorm3d_chat | 0 | 1 | `COMMANDER` | 100% | First-person player option rows in private-room chat use the raw zero sentinel. |
| juustagram | 0 | 2 | `SYSTEM:JUUSTAGRAM_PORT_NEWS` | 100% | Official Port News posts have blank actor profiles and type 2 system-post semantics. |
| fleet_chat_group | 101, 107 | - | `channel_context` | 100% | These group.ship_group values name multi-party channel categories, not speaking ships. |

## Source-wide special participant IDs

This table covers every noncanonical/null participant encountered in the audited social table families. Named noncanonical profiles are typed as NPCs; unsupported unknown IDs remain explicitly unresolved rather than being forced into the ship ontology.

| Locale | Subsystem | Raw table | Raw ID | Type | Normalized type / ID | Status | Method | Confidence | Records |
|---|---|---|---:|---:|---|---|---|---:|---:|
| CN | dorm3d_chat | dorm3d_ins_chat_language | 0 | 1 | player_role / `COMMANDER` | resolved | chat_type_1_player_option_semantics | 100% | 144 |
| CN | dorm3d_chat | dorm3d_ins_chat_language | 0 | 4 | system / `SYSTEM:DORM3D_CHAT:CONTROL` | resolved | auxiliary_chat_control_record | 95% | 2 |
| CN | fleet_chat | activity_ins_chat_language | 0 | 1 | player_role / `COMMANDER` | resolved | chat_type_1_player_option_semantics | 100% | 1922 |
| CN | fleet_chat | activity_ins_chat_language | 0 | 4 | system / `SYSTEM:FLEET_CHAT:CONTROL` | resolved | auxiliary_chat_control_record | 95% | 92 |
| CN | fleet_chat | activity_ins_chat_language | 0 | 5 | system / `SYSTEM:FLEET_CHAT:CONTROL` | resolved | auxiliary_chat_control_record | 95% | 8 |
| CN | fleet_chat | activity_ins_chat_language | 1 | 5 | system / `SYSTEM:FLEET_CHAT:CONTROL` | resolved | auxiliary_chat_control_record | 95% | 41 |
| CN | fleet_chat_group | activity_ins_chat_group | 101 | None | system / `CHANNEL:FLEET_CHAT:101` | resolved | noncanonical_chat_group_channel_key | 100% | 2 |
| CN | fleet_chat_group | activity_ins_chat_group | 102 | None | system / `CHANNEL:FLEET_CHAT:102` | resolved | noncanonical_chat_group_channel_key | 100% | 1 |
| CN | fleet_chat_group | activity_ins_chat_group | 103 | None | system / `CHANNEL:FLEET_CHAT:103` | resolved | noncanonical_chat_group_channel_key | 100% | 3 |
| CN | fleet_chat_group | activity_ins_chat_group | 104 | None | system / `CHANNEL:FLEET_CHAT:104` | resolved | noncanonical_chat_group_channel_key | 100% | 1 |
| CN | fleet_chat_group | activity_ins_chat_group | 105 | None | system / `CHANNEL:FLEET_CHAT:105` | resolved | noncanonical_chat_group_channel_key | 100% | 1 |
| CN | fleet_chat_group | activity_ins_chat_group | 106 | None | system / `CHANNEL:FLEET_CHAT:106` | resolved | noncanonical_chat_group_channel_key | 100% | 1 |
| CN | fleet_chat_group | activity_ins_chat_group | 107 | None | system / `CHANNEL:FLEET_CHAT:107` | resolved | noncanonical_chat_group_channel_key | 100% | 2 |
| CN | fleet_chat_group | activity_ins_chat_group | 108 | None | system / `CHANNEL:FLEET_CHAT:108` | resolved | noncanonical_chat_group_channel_key | 100% | 1 |
| CN | fleet_chat_group | activity_ins_chat_group | 109 | None | system / `CHANNEL:FLEET_CHAT:109` | resolved | noncanonical_chat_group_channel_key | 100% | 1 |
| CN | fleet_chat_group | activity_ins_chat_group | 110 | None | system / `CHANNEL:FLEET_CHAT:110` | resolved | noncanonical_chat_group_channel_key | 100% | 1 |
| CN | fleet_chat_group | activity_ins_chat_group | 200 | None | system / `CHANNEL:FLEET_CHAT:200` | resolved | noncanonical_chat_group_channel_key | 100% | 1 |
| CN | fleet_chat_group | activity_ins_chat_group | 201 | None | system / `CHANNEL:FLEET_CHAT:201` | resolved | noncanonical_chat_group_channel_key | 100% | 1 |
| CN | juustagram | activity_ins_npc_template | 10121 | None | unresolved / `UNRESOLVED_SOCIAL:JUUSTAGRAM:10121` | unresolved | no_supported_identity_rule | 0% | 5 |
| CN | juustagram | activity_ins_npc_template | 10122 | None | unresolved / `UNRESOLVED_SOCIAL:JUUSTAGRAM:10122` | unresolved | no_supported_identity_rule | 0% | 6 |
| CN | juustagram | activity_ins_npc_template | 10990 | None | unresolved / `UNRESOLVED_SOCIAL:JUUSTAGRAM:10990` | unresolved | no_supported_identity_rule | 0% | 5 |
| CN | juustagram | activity_ins_npc_template | 10991 | None | unresolved / `UNRESOLVED_SOCIAL:JUUSTAGRAM:10991` | unresolved | no_supported_identity_rule | 0% | 4 |
| CN | juustagram | activity_ins_npc_template | 10992 | None | unresolved / `UNRESOLVED_SOCIAL:JUUSTAGRAM:10992` | unresolved | no_supported_identity_rule | 0% | 4 |
| CN | juustagram | activity_ins_npc_template | 10993 | None | unresolved / `UNRESOLVED_SOCIAL:JUUSTAGRAM:10993` | unresolved | no_supported_identity_rule | 0% | 4 |
| CN | juustagram | activity_ins_npc_template | 10994 | None | unresolved / `UNRESOLVED_SOCIAL:JUUSTAGRAM:10994` | unresolved | no_supported_identity_rule | 0% | 4 |
| CN | juustagram | activity_ins_npc_template | 10995 | None | unresolved / `UNRESOLVED_SOCIAL:JUUSTAGRAM:10995` | unresolved | no_supported_identity_rule | 0% | 5 |
| CN | juustagram | activity_ins_npc_template | 301541 | None | unresolved / `UNRESOLVED_SOCIAL:JUUSTAGRAM:301541` | unresolved | no_supported_identity_rule | 0% | 1 |
| CN | juustagram | activity_ins_npc_template | 30187 | None | unresolved / `UNRESOLVED_SOCIAL:JUUSTAGRAM:30187` | unresolved | no_supported_identity_rule | 0% | 6 |
| CN | juustagram | activity_ins_npc_template | 900939 | None | unresolved / `UNRESOLVED_SOCIAL:JUUSTAGRAM:900939` | unresolved | no_supported_identity_rule | 0% | 1 |
| CN | juustagram | activity_ins_template | 0 | 2 | system / `SYSTEM:JUUSTAGRAM_PORT_NEWS` | resolved | juustagram_type_2_official_account | 100% | 4 |
| CN | juustagram | activity_ins_template | 10121 | 1 | npc / `SOCIAL_NPC:10121` | resolved | named_noncanonical_social_profile | 75% | 1 |
| CN | juustagram | activity_ins_template | 10122 | 1 | npc / `SOCIAL_NPC:10122` | resolved | named_noncanonical_social_profile | 75% | 1 |
| CN | juustagram | activity_ins_template | 10990 | 1 | npc / `SOCIAL_NPC:10990` | resolved | named_noncanonical_social_profile | 75% | 1 |
| CN | juustagram | activity_ins_template | 10991 | 1 | npc / `SOCIAL_NPC:10991` | resolved | named_noncanonical_social_profile | 75% | 1 |
| CN | juustagram | activity_ins_template | 10992 | 1 | npc / `SOCIAL_NPC:10992` | resolved | named_noncanonical_social_profile | 75% | 1 |
| CN | juustagram | activity_ins_template | 10993 | 1 | npc / `SOCIAL_NPC:10993` | resolved | named_noncanonical_social_profile | 75% | 1 |
| CN | juustagram | activity_ins_template | 10994 | 1 | npc / `SOCIAL_NPC:10994` | resolved | named_noncanonical_social_profile | 75% | 1 |
| CN | juustagram | activity_ins_template | 10995 | 1 | npc / `SOCIAL_NPC:10995` | resolved | named_noncanonical_social_profile | 75% | 1 |
| CN | juustagram | activity_ins_template | 30187 | 1 | npc / `SOCIAL_NPC:30187` | resolved | named_noncanonical_social_profile | 75% | 1 |
| EN | dorm3d_chat | dorm3d_ins_chat_language | 0 | 1 | player_role / `COMMANDER` | resolved | chat_type_1_player_option_semantics | 100% | 144 |
| EN | dorm3d_chat | dorm3d_ins_chat_language | 0 | 4 | system / `SYSTEM:DORM3D_CHAT:CONTROL` | resolved | auxiliary_chat_control_record | 95% | 2 |
| EN | fleet_chat | activity_ins_chat_language | 0 | 1 | player_role / `COMMANDER` | resolved | chat_type_1_player_option_semantics | 100% | 1922 |
| EN | fleet_chat | activity_ins_chat_language | 0 | 4 | system / `SYSTEM:FLEET_CHAT:CONTROL` | resolved | auxiliary_chat_control_record | 95% | 92 |
| EN | fleet_chat | activity_ins_chat_language | 0 | 5 | system / `SYSTEM:FLEET_CHAT:CONTROL` | resolved | auxiliary_chat_control_record | 95% | 8 |
| EN | fleet_chat | activity_ins_chat_language | 1 | 5 | system / `SYSTEM:FLEET_CHAT:CONTROL` | resolved | auxiliary_chat_control_record | 95% | 41 |
| EN | fleet_chat_group | activity_ins_chat_group | 101 | None | system / `CHANNEL:FLEET_CHAT:101` | resolved | noncanonical_chat_group_channel_key | 100% | 2 |
| EN | fleet_chat_group | activity_ins_chat_group | 102 | None | system / `CHANNEL:FLEET_CHAT:102` | resolved | noncanonical_chat_group_channel_key | 100% | 1 |
| EN | fleet_chat_group | activity_ins_chat_group | 103 | None | system / `CHANNEL:FLEET_CHAT:103` | resolved | noncanonical_chat_group_channel_key | 100% | 3 |
| EN | fleet_chat_group | activity_ins_chat_group | 104 | None | system / `CHANNEL:FLEET_CHAT:104` | resolved | noncanonical_chat_group_channel_key | 100% | 1 |
| EN | fleet_chat_group | activity_ins_chat_group | 105 | None | system / `CHANNEL:FLEET_CHAT:105` | resolved | noncanonical_chat_group_channel_key | 100% | 1 |
| EN | fleet_chat_group | activity_ins_chat_group | 106 | None | system / `CHANNEL:FLEET_CHAT:106` | resolved | noncanonical_chat_group_channel_key | 100% | 1 |
| EN | fleet_chat_group | activity_ins_chat_group | 107 | None | system / `CHANNEL:FLEET_CHAT:107` | resolved | noncanonical_chat_group_channel_key | 100% | 2 |
| EN | fleet_chat_group | activity_ins_chat_group | 108 | None | system / `CHANNEL:FLEET_CHAT:108` | resolved | noncanonical_chat_group_channel_key | 100% | 1 |
| EN | fleet_chat_group | activity_ins_chat_group | 109 | None | system / `CHANNEL:FLEET_CHAT:109` | resolved | noncanonical_chat_group_channel_key | 100% | 1 |
| EN | fleet_chat_group | activity_ins_chat_group | 110 | None | system / `CHANNEL:FLEET_CHAT:110` | resolved | noncanonical_chat_group_channel_key | 100% | 1 |
| EN | fleet_chat_group | activity_ins_chat_group | 200 | None | system / `CHANNEL:FLEET_CHAT:200` | resolved | noncanonical_chat_group_channel_key | 100% | 1 |
| EN | fleet_chat_group | activity_ins_chat_group | 201 | None | system / `CHANNEL:FLEET_CHAT:201` | resolved | noncanonical_chat_group_channel_key | 100% | 1 |
| EN | juustagram | activity_ins_npc_template | 10121 | None | unresolved / `UNRESOLVED_SOCIAL:JUUSTAGRAM:10121` | unresolved | no_supported_identity_rule | 0% | 5 |
| EN | juustagram | activity_ins_npc_template | 10122 | None | unresolved / `UNRESOLVED_SOCIAL:JUUSTAGRAM:10122` | unresolved | no_supported_identity_rule | 0% | 6 |
| EN | juustagram | activity_ins_npc_template | 10990 | None | unresolved / `UNRESOLVED_SOCIAL:JUUSTAGRAM:10990` | unresolved | no_supported_identity_rule | 0% | 5 |
| EN | juustagram | activity_ins_npc_template | 10991 | None | unresolved / `UNRESOLVED_SOCIAL:JUUSTAGRAM:10991` | unresolved | no_supported_identity_rule | 0% | 4 |
| EN | juustagram | activity_ins_npc_template | 10992 | None | unresolved / `UNRESOLVED_SOCIAL:JUUSTAGRAM:10992` | unresolved | no_supported_identity_rule | 0% | 4 |
| EN | juustagram | activity_ins_npc_template | 10993 | None | unresolved / `UNRESOLVED_SOCIAL:JUUSTAGRAM:10993` | unresolved | no_supported_identity_rule | 0% | 4 |
| EN | juustagram | activity_ins_npc_template | 10994 | None | unresolved / `UNRESOLVED_SOCIAL:JUUSTAGRAM:10994` | unresolved | no_supported_identity_rule | 0% | 4 |
| EN | juustagram | activity_ins_npc_template | 10995 | None | unresolved / `UNRESOLVED_SOCIAL:JUUSTAGRAM:10995` | unresolved | no_supported_identity_rule | 0% | 5 |
| EN | juustagram | activity_ins_npc_template | 301541 | None | unresolved / `UNRESOLVED_SOCIAL:JUUSTAGRAM:301541` | unresolved | no_supported_identity_rule | 0% | 1 |
| EN | juustagram | activity_ins_npc_template | 30187 | None | unresolved / `UNRESOLVED_SOCIAL:JUUSTAGRAM:30187` | unresolved | no_supported_identity_rule | 0% | 6 |
| EN | juustagram | activity_ins_npc_template | 900939 | None | unresolved / `UNRESOLVED_SOCIAL:JUUSTAGRAM:900939` | unresolved | no_supported_identity_rule | 0% | 1 |
| EN | juustagram | activity_ins_template | 0 | 2 | system / `SYSTEM:JUUSTAGRAM_PORT_NEWS` | resolved | juustagram_type_2_official_account | 100% | 4 |
| EN | juustagram | activity_ins_template | 10121 | 1 | npc / `SOCIAL_NPC:10121` | resolved | named_noncanonical_social_profile | 75% | 1 |
| EN | juustagram | activity_ins_template | 10122 | 1 | npc / `SOCIAL_NPC:10122` | resolved | named_noncanonical_social_profile | 75% | 1 |
| EN | juustagram | activity_ins_template | 10990 | 1 | npc / `SOCIAL_NPC:10990` | resolved | named_noncanonical_social_profile | 75% | 1 |
| EN | juustagram | activity_ins_template | 10991 | 1 | npc / `SOCIAL_NPC:10991` | resolved | named_noncanonical_social_profile | 75% | 1 |
| EN | juustagram | activity_ins_template | 10992 | 1 | npc / `SOCIAL_NPC:10992` | resolved | named_noncanonical_social_profile | 75% | 1 |
| EN | juustagram | activity_ins_template | 10993 | 1 | npc / `SOCIAL_NPC:10993` | resolved | named_noncanonical_social_profile | 75% | 1 |
| EN | juustagram | activity_ins_template | 10994 | 1 | npc / `SOCIAL_NPC:10994` | resolved | named_noncanonical_social_profile | 75% | 1 |
| EN | juustagram | activity_ins_template | 10995 | 1 | npc / `SOCIAL_NPC:10995` | resolved | named_noncanonical_social_profile | 75% | 1 |
| EN | juustagram | activity_ins_template | 30187 | 1 | npc / `SOCIAL_NPC:30187` | resolved | named_noncanonical_social_profile | 75% | 1 |
| JP | dorm3d_chat | dorm3d_ins_chat_language | 0 | 1 | player_role / `COMMANDER` | resolved | chat_type_1_player_option_semantics | 100% | 144 |
| JP | dorm3d_chat | dorm3d_ins_chat_language | 0 | 4 | system / `SYSTEM:DORM3D_CHAT:CONTROL` | resolved | auxiliary_chat_control_record | 95% | 2 |
| JP | fleet_chat | activity_ins_chat_language | 0 | 1 | player_role / `COMMANDER` | resolved | chat_type_1_player_option_semantics | 100% | 1922 |
| JP | fleet_chat | activity_ins_chat_language | 0 | 4 | system / `SYSTEM:FLEET_CHAT:CONTROL` | resolved | auxiliary_chat_control_record | 95% | 92 |
| JP | fleet_chat | activity_ins_chat_language | 0 | 5 | system / `SYSTEM:FLEET_CHAT:CONTROL` | resolved | auxiliary_chat_control_record | 95% | 8 |
| JP | fleet_chat | activity_ins_chat_language | 1 | 5 | system / `SYSTEM:FLEET_CHAT:CONTROL` | resolved | auxiliary_chat_control_record | 95% | 41 |
| JP | fleet_chat_group | activity_ins_chat_group | 101 | None | system / `CHANNEL:FLEET_CHAT:101` | resolved | noncanonical_chat_group_channel_key | 100% | 2 |
| JP | fleet_chat_group | activity_ins_chat_group | 102 | None | system / `CHANNEL:FLEET_CHAT:102` | resolved | noncanonical_chat_group_channel_key | 100% | 1 |
| JP | fleet_chat_group | activity_ins_chat_group | 103 | None | system / `CHANNEL:FLEET_CHAT:103` | resolved | noncanonical_chat_group_channel_key | 100% | 3 |
| JP | fleet_chat_group | activity_ins_chat_group | 104 | None | system / `CHANNEL:FLEET_CHAT:104` | resolved | noncanonical_chat_group_channel_key | 100% | 1 |
| JP | fleet_chat_group | activity_ins_chat_group | 105 | None | system / `CHANNEL:FLEET_CHAT:105` | resolved | noncanonical_chat_group_channel_key | 100% | 1 |
| JP | fleet_chat_group | activity_ins_chat_group | 106 | None | system / `CHANNEL:FLEET_CHAT:106` | resolved | noncanonical_chat_group_channel_key | 100% | 1 |
| JP | fleet_chat_group | activity_ins_chat_group | 107 | None | system / `CHANNEL:FLEET_CHAT:107` | resolved | noncanonical_chat_group_channel_key | 100% | 2 |
| JP | fleet_chat_group | activity_ins_chat_group | 108 | None | system / `CHANNEL:FLEET_CHAT:108` | resolved | noncanonical_chat_group_channel_key | 100% | 1 |
| JP | fleet_chat_group | activity_ins_chat_group | 109 | None | system / `CHANNEL:FLEET_CHAT:109` | resolved | noncanonical_chat_group_channel_key | 100% | 1 |
| JP | fleet_chat_group | activity_ins_chat_group | 110 | None | system / `CHANNEL:FLEET_CHAT:110` | resolved | noncanonical_chat_group_channel_key | 100% | 1 |
| JP | fleet_chat_group | activity_ins_chat_group | 200 | None | system / `CHANNEL:FLEET_CHAT:200` | resolved | noncanonical_chat_group_channel_key | 100% | 1 |
| JP | fleet_chat_group | activity_ins_chat_group | 201 | None | system / `CHANNEL:FLEET_CHAT:201` | resolved | noncanonical_chat_group_channel_key | 100% | 1 |
| JP | juustagram | activity_ins_npc_template | 10121 | None | unresolved / `UNRESOLVED_SOCIAL:JUUSTAGRAM:10121` | unresolved | no_supported_identity_rule | 0% | 5 |
| JP | juustagram | activity_ins_npc_template | 10122 | None | unresolved / `UNRESOLVED_SOCIAL:JUUSTAGRAM:10122` | unresolved | no_supported_identity_rule | 0% | 6 |
| JP | juustagram | activity_ins_npc_template | 10990 | None | unresolved / `UNRESOLVED_SOCIAL:JUUSTAGRAM:10990` | unresolved | no_supported_identity_rule | 0% | 5 |
| JP | juustagram | activity_ins_npc_template | 10991 | None | unresolved / `UNRESOLVED_SOCIAL:JUUSTAGRAM:10991` | unresolved | no_supported_identity_rule | 0% | 4 |
| JP | juustagram | activity_ins_npc_template | 10992 | None | unresolved / `UNRESOLVED_SOCIAL:JUUSTAGRAM:10992` | unresolved | no_supported_identity_rule | 0% | 4 |
| JP | juustagram | activity_ins_npc_template | 10993 | None | unresolved / `UNRESOLVED_SOCIAL:JUUSTAGRAM:10993` | unresolved | no_supported_identity_rule | 0% | 4 |
| JP | juustagram | activity_ins_npc_template | 10994 | None | unresolved / `UNRESOLVED_SOCIAL:JUUSTAGRAM:10994` | unresolved | no_supported_identity_rule | 0% | 4 |
| JP | juustagram | activity_ins_npc_template | 10995 | None | unresolved / `UNRESOLVED_SOCIAL:JUUSTAGRAM:10995` | unresolved | no_supported_identity_rule | 0% | 5 |
| JP | juustagram | activity_ins_npc_template | 301541 | None | unresolved / `UNRESOLVED_SOCIAL:JUUSTAGRAM:301541` | unresolved | no_supported_identity_rule | 0% | 1 |
| JP | juustagram | activity_ins_npc_template | 30187 | None | unresolved / `UNRESOLVED_SOCIAL:JUUSTAGRAM:30187` | unresolved | no_supported_identity_rule | 0% | 6 |
| JP | juustagram | activity_ins_npc_template | 900939 | None | unresolved / `UNRESOLVED_SOCIAL:JUUSTAGRAM:900939` | unresolved | no_supported_identity_rule | 0% | 1 |
| JP | juustagram | activity_ins_template | 0 | 2 | system / `SYSTEM:JUUSTAGRAM_PORT_NEWS` | resolved | juustagram_type_2_official_account | 100% | 4 |
| JP | juustagram | activity_ins_template | 10121 | 1 | npc / `SOCIAL_NPC:10121` | resolved | named_noncanonical_social_profile | 75% | 1 |
| JP | juustagram | activity_ins_template | 10122 | 1 | npc / `SOCIAL_NPC:10122` | resolved | named_noncanonical_social_profile | 75% | 1 |
| JP | juustagram | activity_ins_template | 10990 | 1 | npc / `SOCIAL_NPC:10990` | resolved | named_noncanonical_social_profile | 75% | 1 |
| JP | juustagram | activity_ins_template | 10991 | 1 | npc / `SOCIAL_NPC:10991` | resolved | named_noncanonical_social_profile | 75% | 1 |
| JP | juustagram | activity_ins_template | 10992 | 1 | npc / `SOCIAL_NPC:10992` | resolved | named_noncanonical_social_profile | 75% | 1 |
| JP | juustagram | activity_ins_template | 10993 | 1 | npc / `SOCIAL_NPC:10993` | resolved | named_noncanonical_social_profile | 75% | 1 |
| JP | juustagram | activity_ins_template | 10994 | 1 | npc / `SOCIAL_NPC:10994` | resolved | named_noncanonical_social_profile | 75% | 1 |
| JP | juustagram | activity_ins_template | 10995 | 1 | npc / `SOCIAL_NPC:10995` | resolved | named_noncanonical_social_profile | 75% | 1 |
| JP | juustagram | activity_ins_template | 30187 | 1 | npc / `SOCIAL_NPC:30187` | resolved | named_noncanonical_social_profile | 75% | 1 |
| KR | dorm3d_chat | dorm3d_ins_chat_language | 0 | 1 | player_role / `COMMANDER` | resolved | chat_type_1_player_option_semantics | 100% | 144 |
| KR | dorm3d_chat | dorm3d_ins_chat_language | 0 | 4 | system / `SYSTEM:DORM3D_CHAT:CONTROL` | resolved | auxiliary_chat_control_record | 95% | 2 |
| KR | fleet_chat | activity_ins_chat_language | 0 | 1 | player_role / `COMMANDER` | resolved | chat_type_1_player_option_semantics | 100% | 1922 |
| KR | fleet_chat | activity_ins_chat_language | 0 | 4 | system / `SYSTEM:FLEET_CHAT:CONTROL` | resolved | auxiliary_chat_control_record | 95% | 92 |
| KR | fleet_chat | activity_ins_chat_language | 0 | 5 | system / `SYSTEM:FLEET_CHAT:CONTROL` | resolved | auxiliary_chat_control_record | 95% | 8 |
| KR | fleet_chat | activity_ins_chat_language | 1 | 5 | system / `SYSTEM:FLEET_CHAT:CONTROL` | resolved | auxiliary_chat_control_record | 95% | 41 |
| KR | fleet_chat_group | activity_ins_chat_group | 101 | None | system / `CHANNEL:FLEET_CHAT:101` | resolved | noncanonical_chat_group_channel_key | 100% | 2 |
| KR | fleet_chat_group | activity_ins_chat_group | 102 | None | system / `CHANNEL:FLEET_CHAT:102` | resolved | noncanonical_chat_group_channel_key | 100% | 1 |
| KR | fleet_chat_group | activity_ins_chat_group | 103 | None | system / `CHANNEL:FLEET_CHAT:103` | resolved | noncanonical_chat_group_channel_key | 100% | 3 |
| KR | fleet_chat_group | activity_ins_chat_group | 104 | None | system / `CHANNEL:FLEET_CHAT:104` | resolved | noncanonical_chat_group_channel_key | 100% | 1 |
| KR | fleet_chat_group | activity_ins_chat_group | 105 | None | system / `CHANNEL:FLEET_CHAT:105` | resolved | noncanonical_chat_group_channel_key | 100% | 1 |
| KR | fleet_chat_group | activity_ins_chat_group | 106 | None | system / `CHANNEL:FLEET_CHAT:106` | resolved | noncanonical_chat_group_channel_key | 100% | 1 |
| KR | fleet_chat_group | activity_ins_chat_group | 107 | None | system / `CHANNEL:FLEET_CHAT:107` | resolved | noncanonical_chat_group_channel_key | 100% | 2 |
| KR | fleet_chat_group | activity_ins_chat_group | 108 | None | system / `CHANNEL:FLEET_CHAT:108` | resolved | noncanonical_chat_group_channel_key | 100% | 1 |
| KR | fleet_chat_group | activity_ins_chat_group | 109 | None | system / `CHANNEL:FLEET_CHAT:109` | resolved | noncanonical_chat_group_channel_key | 100% | 1 |
| KR | fleet_chat_group | activity_ins_chat_group | 110 | None | system / `CHANNEL:FLEET_CHAT:110` | resolved | noncanonical_chat_group_channel_key | 100% | 1 |
| KR | fleet_chat_group | activity_ins_chat_group | 200 | None | system / `CHANNEL:FLEET_CHAT:200` | resolved | noncanonical_chat_group_channel_key | 100% | 1 |
| KR | fleet_chat_group | activity_ins_chat_group | 201 | None | system / `CHANNEL:FLEET_CHAT:201` | resolved | noncanonical_chat_group_channel_key | 100% | 1 |
| KR | juustagram | activity_ins_npc_template | 10121 | None | unresolved / `UNRESOLVED_SOCIAL:JUUSTAGRAM:10121` | unresolved | no_supported_identity_rule | 0% | 5 |
| KR | juustagram | activity_ins_npc_template | 10122 | None | unresolved / `UNRESOLVED_SOCIAL:JUUSTAGRAM:10122` | unresolved | no_supported_identity_rule | 0% | 6 |
| KR | juustagram | activity_ins_npc_template | 10990 | None | unresolved / `UNRESOLVED_SOCIAL:JUUSTAGRAM:10990` | unresolved | no_supported_identity_rule | 0% | 5 |
| KR | juustagram | activity_ins_npc_template | 10991 | None | unresolved / `UNRESOLVED_SOCIAL:JUUSTAGRAM:10991` | unresolved | no_supported_identity_rule | 0% | 4 |
| KR | juustagram | activity_ins_npc_template | 10992 | None | unresolved / `UNRESOLVED_SOCIAL:JUUSTAGRAM:10992` | unresolved | no_supported_identity_rule | 0% | 4 |
| KR | juustagram | activity_ins_npc_template | 10993 | None | unresolved / `UNRESOLVED_SOCIAL:JUUSTAGRAM:10993` | unresolved | no_supported_identity_rule | 0% | 4 |
| KR | juustagram | activity_ins_npc_template | 10994 | None | unresolved / `UNRESOLVED_SOCIAL:JUUSTAGRAM:10994` | unresolved | no_supported_identity_rule | 0% | 4 |
| KR | juustagram | activity_ins_npc_template | 10995 | None | unresolved / `UNRESOLVED_SOCIAL:JUUSTAGRAM:10995` | unresolved | no_supported_identity_rule | 0% | 5 |
| KR | juustagram | activity_ins_npc_template | 301541 | None | unresolved / `UNRESOLVED_SOCIAL:JUUSTAGRAM:301541` | unresolved | no_supported_identity_rule | 0% | 1 |
| KR | juustagram | activity_ins_npc_template | 30187 | None | unresolved / `UNRESOLVED_SOCIAL:JUUSTAGRAM:30187` | unresolved | no_supported_identity_rule | 0% | 6 |
| KR | juustagram | activity_ins_npc_template | 900939 | None | unresolved / `UNRESOLVED_SOCIAL:JUUSTAGRAM:900939` | unresolved | no_supported_identity_rule | 0% | 1 |
| KR | juustagram | activity_ins_template | 0 | 2 | system / `SYSTEM:JUUSTAGRAM_PORT_NEWS` | resolved | juustagram_type_2_official_account | 100% | 4 |
| KR | juustagram | activity_ins_template | 10121 | 1 | npc / `SOCIAL_NPC:10121` | resolved | named_noncanonical_social_profile | 75% | 1 |
| KR | juustagram | activity_ins_template | 10122 | 1 | npc / `SOCIAL_NPC:10122` | resolved | named_noncanonical_social_profile | 75% | 1 |
| KR | juustagram | activity_ins_template | 10990 | 1 | npc / `SOCIAL_NPC:10990` | resolved | named_noncanonical_social_profile | 75% | 1 |
| KR | juustagram | activity_ins_template | 10991 | 1 | npc / `SOCIAL_NPC:10991` | resolved | named_noncanonical_social_profile | 75% | 1 |
| KR | juustagram | activity_ins_template | 10992 | 1 | npc / `SOCIAL_NPC:10992` | resolved | named_noncanonical_social_profile | 75% | 1 |
| KR | juustagram | activity_ins_template | 10993 | 1 | npc / `SOCIAL_NPC:10993` | resolved | named_noncanonical_social_profile | 75% | 1 |
| KR | juustagram | activity_ins_template | 10994 | 1 | npc / `SOCIAL_NPC:10994` | resolved | named_noncanonical_social_profile | 75% | 1 |
| KR | juustagram | activity_ins_template | 10995 | 1 | npc / `SOCIAL_NPC:10995` | resolved | named_noncanonical_social_profile | 75% | 1 |
| KR | juustagram | activity_ins_template | 30187 | 1 | npc / `SOCIAL_NPC:30187` | resolved | named_noncanonical_social_profile | 75% | 1 |
| TW | dorm3d_chat | dorm3d_ins_chat_language | 0 | 1 | player_role / `COMMANDER` | resolved | chat_type_1_player_option_semantics | 100% | 144 |
| TW | dorm3d_chat | dorm3d_ins_chat_language | 0 | 4 | system / `SYSTEM:DORM3D_CHAT:CONTROL` | resolved | auxiliary_chat_control_record | 95% | 2 |
| TW | fleet_chat | activity_ins_chat_language | 0 | 1 | player_role / `COMMANDER` | resolved | chat_type_1_player_option_semantics | 100% | 1474 |
| TW | fleet_chat | activity_ins_chat_language | 0 | 4 | system / `SYSTEM:FLEET_CHAT:CONTROL` | resolved | auxiliary_chat_control_record | 95% | 72 |
| TW | fleet_chat | activity_ins_chat_language | 0 | 5 | system / `SYSTEM:FLEET_CHAT:CONTROL` | resolved | auxiliary_chat_control_record | 95% | 7 |
| TW | fleet_chat | activity_ins_chat_language | 1 | 5 | system / `SYSTEM:FLEET_CHAT:CONTROL` | resolved | auxiliary_chat_control_record | 95% | 27 |
| TW | fleet_chat_group | activity_ins_chat_group | 101 | None | system / `CHANNEL:FLEET_CHAT:101` | resolved | noncanonical_chat_group_channel_key | 100% | 2 |
| TW | fleet_chat_group | activity_ins_chat_group | 102 | None | system / `CHANNEL:FLEET_CHAT:102` | resolved | noncanonical_chat_group_channel_key | 100% | 1 |
| TW | fleet_chat_group | activity_ins_chat_group | 103 | None | system / `CHANNEL:FLEET_CHAT:103` | resolved | noncanonical_chat_group_channel_key | 100% | 2 |
| TW | fleet_chat_group | activity_ins_chat_group | 104 | None | system / `CHANNEL:FLEET_CHAT:104` | resolved | noncanonical_chat_group_channel_key | 100% | 1 |
| TW | fleet_chat_group | activity_ins_chat_group | 105 | None | system / `CHANNEL:FLEET_CHAT:105` | resolved | noncanonical_chat_group_channel_key | 100% | 1 |
| TW | fleet_chat_group | activity_ins_chat_group | 106 | None | system / `CHANNEL:FLEET_CHAT:106` | resolved | noncanonical_chat_group_channel_key | 100% | 1 |
| TW | fleet_chat_group | activity_ins_chat_group | 107 | None | system / `CHANNEL:FLEET_CHAT:107` | resolved | noncanonical_chat_group_channel_key | 100% | 1 |
| TW | fleet_chat_group | activity_ins_chat_group | 108 | None | system / `CHANNEL:FLEET_CHAT:108` | resolved | noncanonical_chat_group_channel_key | 100% | 1 |
| TW | fleet_chat_group | activity_ins_chat_group | 109 | None | system / `CHANNEL:FLEET_CHAT:109` | resolved | noncanonical_chat_group_channel_key | 100% | 1 |
| TW | fleet_chat_group | activity_ins_chat_group | 110 | None | system / `CHANNEL:FLEET_CHAT:110` | resolved | noncanonical_chat_group_channel_key | 100% | 1 |
| TW | fleet_chat_group | activity_ins_chat_group | 200 | None | system / `CHANNEL:FLEET_CHAT:200` | resolved | noncanonical_chat_group_channel_key | 100% | 1 |
| TW | fleet_chat_group | activity_ins_chat_group | 201 | None | system / `CHANNEL:FLEET_CHAT:201` | resolved | noncanonical_chat_group_channel_key | 100% | 1 |
| TW | juustagram | activity_ins_npc_template | 10990 | None | unresolved / `UNRESOLVED_SOCIAL:JUUSTAGRAM:10990` | unresolved | no_supported_identity_rule | 0% | 5 |
| TW | juustagram | activity_ins_npc_template | 10991 | None | unresolved / `UNRESOLVED_SOCIAL:JUUSTAGRAM:10991` | unresolved | no_supported_identity_rule | 0% | 4 |
| TW | juustagram | activity_ins_npc_template | 10992 | None | unresolved / `UNRESOLVED_SOCIAL:JUUSTAGRAM:10992` | unresolved | no_supported_identity_rule | 0% | 4 |
| TW | juustagram | activity_ins_npc_template | 10993 | None | unresolved / `UNRESOLVED_SOCIAL:JUUSTAGRAM:10993` | unresolved | no_supported_identity_rule | 0% | 4 |
| TW | juustagram | activity_ins_npc_template | 10994 | None | unresolved / `UNRESOLVED_SOCIAL:JUUSTAGRAM:10994` | unresolved | no_supported_identity_rule | 0% | 4 |
| TW | juustagram | activity_ins_npc_template | 10995 | None | unresolved / `UNRESOLVED_SOCIAL:JUUSTAGRAM:10995` | unresolved | no_supported_identity_rule | 0% | 5 |
| TW | juustagram | activity_ins_npc_template | 301541 | None | unresolved / `UNRESOLVED_SOCIAL:JUUSTAGRAM:301541` | unresolved | no_supported_identity_rule | 0% | 1 |
| TW | juustagram | activity_ins_npc_template | 30187 | None | unresolved / `UNRESOLVED_SOCIAL:JUUSTAGRAM:30187` | unresolved | no_supported_identity_rule | 0% | 6 |
| TW | juustagram | activity_ins_npc_template | 900939 | None | unresolved / `UNRESOLVED_SOCIAL:JUUSTAGRAM:900939` | unresolved | no_supported_identity_rule | 0% | 1 |
| TW | juustagram | activity_ins_template | 0 | 2 | system / `SYSTEM:JUUSTAGRAM_PORT_NEWS` | resolved | juustagram_type_2_official_account | 100% | 3 |
| TW | juustagram | activity_ins_template | 10990 | 1 | npc / `SOCIAL_NPC:10990` | resolved | named_noncanonical_social_profile | 75% | 1 |
| TW | juustagram | activity_ins_template | 10991 | 1 | npc / `SOCIAL_NPC:10991` | resolved | named_noncanonical_social_profile | 75% | 1 |
| TW | juustagram | activity_ins_template | 10992 | 1 | npc / `SOCIAL_NPC:10992` | resolved | named_noncanonical_social_profile | 75% | 1 |
| TW | juustagram | activity_ins_template | 10993 | 1 | npc / `SOCIAL_NPC:10993` | resolved | named_noncanonical_social_profile | 75% | 1 |
| TW | juustagram | activity_ins_template | 10994 | 1 | npc / `SOCIAL_NPC:10994` | resolved | named_noncanonical_social_profile | 75% | 1 |
| TW | juustagram | activity_ins_template | 10995 | 1 | npc / `SOCIAL_NPC:10995` | resolved | named_noncanonical_social_profile | 75% | 1 |
| TW | juustagram | activity_ins_template | 30187 | 1 | npc / `SOCIAL_NPC:30187` | resolved | named_noncanonical_social_profile | 75% | 1 |

## Unresolved and affected surfaces

- Unresolved entities in the current normalized eight-character corpus: **0**.
- Source-wide special-ID records still conservatively unresolved: **214**.
- Affected current character corpora: `BALTIMORE_10316` (10316), `ENTERPRISE_10706` (10706), `TAKAO_30311` (30311), `ATAGO_30312` (30312), `NAGATO_30505` (30505), `TAIHOU_30707` (30707).
- Taihou raw-zero rows: **26**; resolved as Commander: **26**; regression: **PASS**.

## Special secretary applicability

Not applicable to social actor resolution: secretary_special_ship records are character-bound dialogue rows and do not use the polymorphic social participant ID field.
