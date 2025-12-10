
# Multi-Mission Use of ISTP Attributes

- M - mandatory by mission
- R - recommended by mission
- O - optional for mission

| | ISTP  | Cluster | ERG | GOLD | ICON | MMS | PSP | PRBEM | RBSP (Van Allen Probes) | Solar Orbiter |
| ------------ | ----- | ------- | --- | ---- | ---- | --- | --- | ----- | ----- | ------- |
| **Global Attribute**  |  | | |  |  | | | | | |
| [`Data_type`](./03_metadata-global-attributes.md#data_type) | M  | M | M | M  | M  | | | M | | M |
| [`Data_version`](./03_metadata-global-attributes.md#data_version)  | M  | | M | M  | M  | | | M | | M |
| [`Descriptor`](./03_metadata-global-attributes.md#descriptor)  | M  | | M |  | M  | | | M | | M |
| [`Discipline`](./03_metadata-global-attributes.md#discipline)  | M  | | M | M  | M  | | | M | | M |
| [`Instrument_type`](./03_metadata-global-attributes.md#instrument_type) | M  | M | M | M  | M  | | | M | | M |
| [`Logical_file_id`](./03_metadata-global-attributes.md#logical_file_id) | M  | M | M | M  | M  | | | M | | M |
| [`Logical_source`](./03_metadata-global-attributes.md#logical_source)  | M  | | M | M  | M  | | | M | | M |
| [`Logical_source_description`](./03_metadata-global-attributes.md#logical_source_description)  |  M  | | M | M  | M  | | | M | | M |
| [`Mission_group`](./03_metadata-global-attributes.md#mission_group) | M  | | M | M  | M  | | | M | | M |
| [`PI_affiliation`](./03_metadata-global-attributes.md#pi_affiliation)  | M  | | M | M  | M  | | | M | | M |
| [`PI_name`](./03_metadata-global-attributes.md#pi_name) | M  | | M | M  | M  | | | M | | M |
| [`Project`](./03_metadata-global-attributes.md#project) | R  | | M | M  | M  | | | M | | M |
| [`Source_name`](./03_metadata-global-attributes.md#source_name) | M  | | M | M  | M  | | | M | | M |
| [`TEXT`](./03_metadata-global-attributes.md#text)  | M  | | M | M  | M  | | | M | | M |
| [`Acknowledgement`](./03_metadata-global-attributes.md#acknowledgement) | R  | M | |  | M  | | | R | | M |
| [`Generated_by`](./03_metadata-global-attributes.md#generated_by)  | R  | | M | M  | M  | | | R | | M |
| [`Generation_date`](./03_metadata-global-attributes.md#generation_date) | R  | M | M |  | M  | | | R | | M |
| [`HTTP_LINK`](./03_metadata-global-attributes.md#link_text-link_title-http_link) | R  | | | M  | M  | | | R | | M |
| [`LINK_TEXT`](./03_metadata-global-attributes.md#link_text-link_title-http_link) | R  | | M | M  | M  | | | R | | M |
| [`LINK_TITLE`](./03_metadata-global-attributes.md#link_text-link_title-http_link)  | R  | | M | M  | M  | | | R | | M |
| [`MODS`](./03_metadata-global-attributes.md#mods)  | R  | | M |  | M  | | | R | | M |
| [`Rules_of_use`](./03_metadata-global-attributes.md#rules_of_use)  | R  | | M | M  | M  | | | R | | M |
| [`Time_resolution`](./03_metadata-global-attributes.md#time_resolution) | R  | M | |  | M  | | | M | | |
| [`TITLE`](./03_metadata-global-attributes.md#title) | O  | | M | M  | M  | | | O | | |
| [`Validate`](./03_metadata-global-attributes.md#validate)  | O  | | |  |  | | | O | | |
| [`Software_version`](./03_metadata-global-attributes.md#software_version)  | O  | | | M  | M  | | | O | | M |
| [`Skeleton_version`](./03_metadata-global-attributes.md#skeleton_version)  | O  | | |  |  | | | O | | M |
| [`Parents`](./03_metadata-global-attributes.md#parents) | O  | | |  | M  | | | O | | M |
| [`ADID_ref`](./03_metadata-global-attributes.md#adid_ref)  | Not relevant | | M |  | M  | | | R | | |

|  | ISTP | Cluster | ERG | GOLD | ICON | MMS | PSP | PRBEM | RBSP (Van Allen Probes) | Solar Orbiter |
| -------- | --------- | ------- | --- | ---- | ---- | --- | --- | ----- | ----- | ----- |
| **Variable Attribute** |  | | | | |  |  | | | | | |
| [`CATDESC`](./05_metadata-variable-attributes.md#catdesc)  | M | M | |  |  | M | M | | M | |
| [`DEPEND_0`](./05_metadata-variable-attributes.md#depend_0) | M | | |  |  | M | | | M | |
| [`DISPLAY_TYPE`](./05_metadata-variable-attributes.md#display_type)  | M | M | |  |  | | | | M | |
| [`FIELDNAM`](./05_metadata-variable-attributes.md#fieldnam) | M | M | |  |  | M | | | M | |
| [`FILLVAL`](./05_metadata-variable-attributes.md#fillval)  | M | M | |  |  | M | | | M | |
| [`FORMAT`](./05_metadata-variable-attributes.md#format) | M | | |  |  | M | | | M | |
| [`FORM_PTR`](./05_metadata-variable-attributes.md#form_ptr) | M | | |  |  | M | | | M | |
| [`UNITS`](./05_metadata-variable-attributes.md#units)  | M | | |  |  | | M | | M | |
| [`UNIT_PTR`](./05_metadata-variable-attributes.md#unit_ptr) | M | | |  |  | | M | | M | |
| [`VALIDMAX`](./05_metadata-variable-attributes.md#validmin-validmax) | M | | |  |  | | M | | M | |
| [`VALIDMIN`](./05_metadata-variable-attributes.md#validmin-validmax) | M | | |  |  | | M | | M | |
| [`VAR_TYPE`](./05_metadata-variable-attributes.md#var_type) | M | | |  |  | M | | | M | |
| [`VAR_NOTES`](./05_metadata-variable-attributes.md#var_notes)  | O | | |  |  | | M | | M | |
| [`DELTA_MINUS_VAR`](./05_metadata-variable-attributes.md#delta_plus_var-delta_minus_var)  | O | M | |  |  | | M | | M | |
| [`DELTA_PLUS_VAR`](./05_metadata-variable-attributes.md#delta_plus_var-delta_minus_var) | O | M | |  |  | | M | | M | |

---
Return to [Table of Contents](../README.md)
