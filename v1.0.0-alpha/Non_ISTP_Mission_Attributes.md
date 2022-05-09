# Non-ISTP Attributes Used by Missions

- M - mandatory by mission
- R - recommended by mission
- O - optional for mission

| Attributes | ISTP alternative | Cluster | ERG | GOLD | ICON | MMS | PDS | PRBEM | PSP | Solar Orbiter |
| ---------- | ---------------- | ------- | --- | ---- | ---- | --- | --- | ----- | --- | ------------- |
| ACCESS_FORMAT | 
| Alpha |                            
| Alpha_Eq |    
| B_Calc| 
| B_Eq |
| CAVEATS | | | | | | | | | | O |
| Channel_ID |
| _ChunkingSizes |
| Coordinate_System |                                                                    | R |
| CountRate |
| Data |                            | M|
| Data_coordinates |
| Data_cycle |
| Data_level |
| Data_product |                                                                        | R |
| DATAPRODUCT_TYPE |
| Data_resolution | 
| Data_revision |
| Data_sampling_type |
| Dataset_ID |
| Data_type_2 |
| D_conversion_factor |
| _DeflateLevel
| D_unit |
| Delta_Minus | DELTA_MINUS_VAR | O | | | | | | | | 
| Delta_Plus | DELTA_PLUS_VAR | O | | | | | | | | 
| Elevation |
| _FillValue |
| FLUX_PTR |
| Free_field |
| Frame | | M | | | | | | | | 
| FRAME_ORIGIN |
| FRAME_VELOCITY |
| Geographic_coordinates |
| Geographic_latitude |
| Geographic_longitude |
| Geomagnetic_coordinates |
| Geomagnetic_latitude |
| Geomagnetic_longitude |
| I | 
| Job_ID |
| Known_problems |
| K9_limit |
| L |
| L_star |
| Last_obs_count_in_ file |
| LEVEL |
| L_value |
| Long_name |
| Magnetometer_type |
| Maximum_PHD |
| Minimum_PHD |
| Mirror_hemisphere |
| MLT |
| Number_of_channels |
| Observation_complete |
| Observation_end |
| Observation_start |
| Observation_type |
| OBS_ID |
| OBS_TYPE |
| Operator_Type |
| Position |
| Process_ID |
| REFERENCE | | | | | | | | | | | | | | O |
| Representation_i | | M | | | | | | | | 
| SI_Conversion | | M | | | | | | | | R |
| _Shuffle |
| Sizes |
| SOOP_TYPE |
| spase_DatasetResource | | | | | | | | | | O |
| spase_DatasetResourceID | | | | | | | | | O |
| spase_GranuleResource | | | | | | | | | | O |
| spase_GranuleResourceID | | | | | | | | | O |
| SPECIES |
| Station_code |
| Station_name |
| TARGET_CLASS |
| TARGET_NAME | | | | | | | | | | | | | R |
| TARGET_REGION |
| Tensor_Frame | | M | | | | | | | | 
| Tensor Order | | M | | | | | | | | 
| Text_supplement |
| Time_calibration_method |
| TIME_MAX |
| TIME_MIN |
| UCD |
| Valid_Max |
| Valid_Min |
| Valid_Range | | |
| Value Type  | | | | | | | | | | 

**Descriptions**

ACCESS_FORMAT- Format of the file.

COORDINATE_SYSTEM- For nonscalar data, contains coordinate system name, e.g. ‘HCI’ or ‘RTN’. Note representation is no longer included.

Data_product-  Type of data product. It shall use the ISTP format "PREFIX>Suffix" (e.g., "HIST1D>1D histogram"). 

DATAPRODUCT_TYPE- High level scientific organization of the data.

Dataset_ID- Data set identifier.

Free_field- Description of the free field in the filename. It shall use the ISTP format "PREFIX>Suffix" (e.g., "NORM>Normal mode"), where the value of the prefix shall correspond to the "free" field in the file naming convention.

FRAME_ORIGIN- gives the origin of the reference frame where this is not implicit in the value of COORDINATE_SYSTEM.

FRAME_VELOCITY- can take either the value 'Observatory' where no corrections have been applied to the data or 'Inertial' where quantities (e.g. electric 
field or plasma flow velocity) have been corrected for spacecraft motion relative to an inertial frame (HCI).

Job_ID- Process job identifier.

LEVEL- Data processing level as defined in the Solar Orbiter conventions. It shall use the ISTP format "PREFIX>Suffix" (e.g., "L1>Level 1 data processing"), where the value of the prefix shall correspond to the "level" field in the file naming convention.

SI_CONVERSION- A string that defines the conversion needed to base SI units, e.g. "1.0E-9>T" for DC Magnetic field data in nT.

spase_DatasetResource- The SPASE XML description of the dataset that corresponds to the SPASE ResourceID.

spase_DatasetResourceID- The SPASE ResourceID assigned of the NumericalData resource the data file is part of.

spase_GranuleResource- The SPASE XML description of the dataset that corresponds to the SPASE Granule ResourceID.

spase_GranuleResourceID- The Granule ResourceID assigned to the data file.

OBS_ID- A unique identifier for the observation that is associated with the data acquisition and includes identifying information about: the SOOP; planning period; instrument; and instrument’s observation mode. The format of OBS_ID is defined in [IOR-ICD], and shall be included in the IORs delivered by the Instrument Teams to SOC.

Process_ID- Process identifier.

REFERENCE- Bibcode, DOI or URL.

REPRESENTATION_i- Pointer to a support variable that gives the representation (['x','y','z'] for Cartesian; ['r','p','t'] for spherical polar; ['r','p','z'] for cylindrical polar) of the ith dimension of the variable.

SOOP_TYPE-  SOOP campaign identifier, following the SOOP naming convention.

TARGET_CLASS- Class of the target.

TARGET_NAME- Name of the target. 

TARGET_REGION- Region where the target is observed.

TENSOR_ORDER- Contains the rank or order of a tensor, i.e. 1 for a vector, 2 for a 3x3 tensor.

TIME_MAX- The date and time of the end of the last acquisition for the data contained in the file.

TIME_MIN- The date and time of the beginning of the first acquisition for the data contained in the file.

UCD- UCD keywords as defined by the IVOA.
