# Non-ISTP Mission Global Attributes

- M - mandatory by mission
- R - recommended by mission
- O - optional for mission



| Attributes | ISTP alternative | Cluster | Arase (ERG) | GOLD | ICON | MMS | PDS | PRBEM | PSP | Solar Orbiter |
| ---------- | ---------------- | ------- | --- | ---- | ---- | --- | --- | ----- | --- | ------------- |
| `ACCESS_FORMAT` | | | | | | | | | | O |
| `CAVEATS` | | | | | | | | | | O |
| `Channel_ID` | | | | M |
| `Data_coordinates` | | | M |
| `Data_cycle` | | | | M |
| `Data_level` | | | | M |
| `Data_product` | |  | | | | | | | | R |
| `DATAPRODUCT_TYPE` | | | | | | | | | | O |
| `Data_resolution` | | | M |
| `Data_revision` | | | | M |
| `Data_sampling_type` | | | M |
| `Dataset_ID` | | | | | | | | | | O |
| `Data_type_2` | | | M |
| `D_conversion_factor` | | | M |
| `D_unit` | | | M |
| `Elevation` | | | M |
| `FLUX_PTR` | | | | | | | | | M |
| `Free_field` | | | | | | | | | | R | 
| `Geographic_coordinates` | | | M |
| `Geographic_latitude` | | | M |
| `Geographic_longitude` | | | M |
| `Geomagnetic_coordinates` | | | M |
| `Geomagnetic_latitude` | | | M |
| `Geomagnetic_longitude` | | | M |
| `Generated_with_software` | | | | | | | | M |
| `Job_ID` | | | | | | | | | | O |
| `Known_problems` | | | M |
| `K9_limit` | | | M |
| `Last_obs_count_in_file` | | | | M |
| `LEVEL` | | | | | | | | | | R |
| `L_value` | | | M |
| `Magnetometer_type` | | | M |
| `Maximum_PHD` | | | | M |
| `Minimum_PHD` | | | | M |
| `Mirror_hemisphere` | | | | M |
| `Number_of_channels` | | | M |
| `Observation_complete` | | | | M |
| `Observation_end` | | | M |
| `Observation_start` | | | M |
| `Observation_type` | | | | M |
| `OBS_ID` | | | | M | | | | | | R |
| `OBS_TYPE` | | | | M |
| `Planet` | | | | | | | | M |
| `Process_ID` | | | | | | | | | | O |
| `REFERENCE` | | | | | | | | | | O | 
| `SOOP_TYPE` | | | | | | | | | | R |
| `spase_DatasetResource` | | | | | | |M | | | O |
| `spase_DatasetResourceID` | | | | | | | O| | |O |
| `spase_GranuleResource` | | | | | | | O| | | O |
| `spase_GranuleResourceID` | | | | | | |O | | | O |
| `SPECIES` | | | | | | | | | M |
| `Station_code` | | | M |
| `Station_name` | | | M |
| `TARGET_CLASS` | | | | | | | | | | R |
| `TARGET_NAME` | | | | | | | | | | R |
| `TARGET_REGION` | | | | | | | | | | R |
| `Text_supplement` | | | M |
| `Time_calibration_method` | | | M |
| `TIME_MAX` | | | | | | | | | | O |
| `TIME_MIN` | | | | | | | | | | O |
 
 

## Descriptions

`ACCESS_FORMAT` &mdash; Format of the file.

`CAVEATS`  &mdash; Information which may be important in the avoidance of the misuse of the resource, for instance the assumptions or limitations on data processing, modeling or inversions.

`Channel_ID`  &mdash; `0` = CHANNEL A,  `1` = CHANNEL B.

`Data_coordinates`  &mdash; Coordinate system used for observed magnetic field vector. "Other" means that an instrument-specific coordinate system is used.

`Data_Cycle`  &mdash; Data cycle sequence number.

`Data_Level`  &mdash;  `L1B`.

`Data_product`  &mdash;  Type of data product. It shall use the ISTP format "PREFIX>Suffix" (e.g., `"HIST1D>1D histogram"`). 

`DATAPRODUCT_TYPE`  &mdash; High level scientific organization of the data.

`Data_resolution`  &mdash; Typical resolution of data values. 

`Data_Revision`  &mdash; Revision sequence number.

`Data_sampling_type`  &mdash; What kind of time bin for averaging or sampling is used to obtain data values.

`Dataset_ID`  &mdash; Data set identifier.

`Data_type_2`  &mdash; Type of observed vector values, e.g., `"Absolute field"`, `"Variation"`. 

`D_conversion_factor`  &mdash; Factor used to convert the unit of D-component from degree to nT.

`D_unit`  &mdash; Physical unit of the D-component of the geomagnetic field. 

`Elevation`  &mdash; Elevation of the location of station. 

`Free_field`  &mdash; Description of the free field in the filename. It shall use the ISTP format "PREFIX>Suffix" (e.g., `"NORM>Normal mode"`), where the value of the prefix shall correspond to the "free" field in the file naming convention.

`Geographic_coordinates`  &mdash; What kind of geographic coordinate system is used for the following latitude and longitude. Usually either of geodetic or geographic. 

`Geographic_latitude`   &mdash; Geographic or geodetic latitude of the location of station. 

`Geographic_longitude`  &mdash; Geographic or geodetic longitude of the location of station. 

`Geomagnetic_coordinates`  &mdash; What kind of geomagnetic coordinate system and what epoch and time are used for the following geomagnetic coordinate values. 

`Geomagnetic_latitude`  &mdash; Geomagnetic latitude of the location of station. 

`Geomagnetic_longitude`  &mdash; Geomagnetic longitude of the location of station. 

`Job_ID`  &mdash; Process job identifier.

`K9_limit`  &mdash; Threshold of K-index for K = 9. (for WDC data).

`Known_problems`  &mdash; Known problems regarding the data set, such as data glitches and gaps.

`Last_obs_Count_In_File`  &mdash; Identifies the number of packets in the current science observation type.

`LEVEL`  &mdash; Data processing level as defined in the Solar Orbiter conventions. It shall use the ISTP format "PREFIX>Suffix" (e.g., `"L1>Level 1 data processing"`), where the value of the prefix shall correspond to the "level" field in the file naming convention.

`L_value`  &mdash; (Dipole) L value of the location of station.

`Magnetometer_type`  &mdash; Type of magnetometer instrument. Usually `"Fluxgate"` or `"Induction"`. 

`Maximum_PHD`  &mdash; Upper limit for the pulse height filter (typical values range from `200` to `254`).

`Minimum_PHD`  &mdash; Lower limit for the pulse height filter (typical value = `2`).

`Mirror_Hemisphere`  &mdash; Either `"N"` (north) or `"S"` (south) for the observed hemisphere.

`Number_of_channels`  &mdash; Number of channels of magnetometer. 

`OBS_ID`  &mdash; A unique identifier for the observation that is associated with the data acquisition and includes identifying information about: the SOOP; planning period; instrument; and instrument’s observation mode. The format of OBS_ID is defined in [IOR-ICD], and shall be included in the IORs delivered by the Instrument Teams to SOC.

`Observation_Complete`  &mdash; `1` if this is the last l1b file in the current observation type otherwise `0` to continue.

`Observation_end`  &mdash; The termination date of instrument operation. This is left blank if the instrument is currently in operation.

`Observation_start`  &mdash; The start date of instrument operation.

`Observation_Type`  &mdash; `"DAY_DISK"`, `"LIMB"`, `"NIGHT_DISK_ARCS"`, or `"STELLAR_OCCULTATION"`.

`OBS_TYPE`  &mdash; `1` (DAY_DISK), `2` (LIMB), `8` (NIGHT_DISK) or `3` (OCCULTATION).

`Process_ID`  &mdash; Process identifier.

`REFERENCE`  &mdash; Bibcode, DOI or URL.

`spase_DatasetResource`  &mdash; The SPASE XML description of the dataset that corresponds to the SPASE ResourceID.

`spase_DatasetResourceID`  &mdash; The SPASE ResourceID assigned of the NumericalData resource the data file is part of.

`spase_GranuleResource`  &mdash; The SPASE XML description of the dataset that corresponds to the SPASE Granule ResourceID.

`spase_GranuleResourceID`  &mdash; The Granule ResourceID assigned to the data file.

`SOOP_TYPE`  &mdash;  SOOP campaign identifier, following the SOOP naming convention.

`Station_code`  &mdash; 3-letter station code. 

`Station_name`  &mdash; The full spelling of station name. 

`TARGET_CLASS`  &mdash; Class of the target.

`TARGET_NAME`  &mdash; Name of the target. 

`TARGET_REGION`  &mdash; Region where the target is observed.

`Time_calibration_method`  &mdash; Time recording method for observation, e.g., `"GPS"`. 

`TIME_MAX`  &mdash; The date and time of the end of the last acquisition for the data contained in the file.

`TIME_MIN`  &mdash; The date and time of the beginning of the first acquisition for the data contained in the file.

---
Return to [Table of Contents](../README.md)


