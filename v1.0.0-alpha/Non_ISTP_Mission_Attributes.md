# Non-ISTP Attributes Used by Missions

- M - mandatory by mission
- R - recommended by mission
- O - optional for mission

| Attributes | ISTP alternative | Cluster | ERG | GOLD | ICON | MMS | PDS | PRBEM | PSP | Solar Orbiter |
| ---------- | ---------------- | ------- | --- | ---- | ---- | --- | --- | ----- | --- | ------------- |
| ACCESS_FORMAT | | | | | | | | | | O |
| CAVEATS | | | | | | | | | | O |
| Channel_ID | | | | M |
| _ChunkingSizes | | | | | M |
| Coordinate_System | | | | | | R |
| Data |                            | M|
| Data_coordinates | | | M |
| Data_cycle | | | | M |
| Data_level | | | | M |
| Data_product |                                                                        | R |
| DATAPRODUCT_TYPE | | | | | | | | | | O |
| Data_resolution | | | M |
| Data_revision | | | | M |
| Data_sampling_type | | | M |
| Dataset_ID |
| Data_type_2 | | | M |
| D_conversion_factor | | | M |
| _DeflateLevel | | | | | M |
| D_unit | | | M |
| Delta_Minus | DELTA_MINUS_VAR | O | | | | | | | | 
| Delta_Plus | DELTA_PLUS_VAR | O | | | | | | | | 
| Elevation | | | M |
| _FillValue | | | | | M |
| FLUX_PTR |
| Free_field |
| Frame | | M | | | | | | | | 
| FRAME_ORIGIN |
| FRAME_VELOCITY |
| Geographic_coordinates | | | M |
| Geographic_latitude | | | M |
| Geographic_longitude | | | M |
| Geomagnetic_coordinates | | | M |
| Geomagnetic_latitude | | | M |
| Geomagnetic_longitude | | | M |
| Generated_with_software | | | | | | | M |
| Job_ID |
| Known_problems | | | M |
| K9_limit | | | M |
| Last_obs_count_in_ file | | | | M |
| LEVEL |
| L_value | | | M |
| Long_name | | | | | R |
| Magnetometer_type | | | M |
| Maximum_PHD | | | | M |
| Minimum_PHD | | | | M |
| Mirror_hemisphere | | | | M |
| Number_of_channels | | | M |
| Observation_complete | | | | M |
| Observation_end | | | M |
| Observation_start | | | M |
| Observation_type | | | | M |
| OBS_ID | | | | M |
| OBS_TYPE | | | | M |
| Operator_Type | | | | | | M |
| Planet | | | | | | | | M |
| Process_ID |
| REFERENCE | | | | | | | | | | O |
| Representation_i | | M | | | | M | | | | 
| SI_Conversion | | M | | | | | | | | R |
| _Shuffle | | | | | M |
| Sizes |
| SOOP_TYPE |
| spase_DatasetResource | | | | | | |M | | | O |
| spase_DatasetResourceID | | | | | | | O| | |O |
| spase_GranuleResource | | | | | | | O| | | O |
| spase_GranuleResourceID | | | | | | |O | | | O |
| SPECIES |
| Station_code | | | M |
| Station_name | | | M |
| TARGET_CLASS | | | | | | | | | | R |
| TARGET_NAME | | | | | | | | | | R |
| TARGET_REGION | | | | | | | | | | R |
| Tensor_Frame | | M | | | | | | | | 
| Tensor Order | | M | | | | M | | | | 
| Text_supplement | | | M |
| Time_calibration_method | | | M |
| TIME_MAX | | | | | | | | | | O |
| TIME_MIN | | | | | | | | | | O |
| UCD |
| Valid_Max | | | | | M |
| Valid_Min | | | | | M |
| Valid_Range | | | | | M |
| Value Type  | | | | | | | | | | 

**Descriptions**

ACCESS_FORMAT- Format of the file.

Channel_ID- 0 = CHANNEL A 1 = CHANNEL B.

_ChunkingSizes- NetCDF attribute which controls the data arrangement.

COORDINATE_SYSTEM- For nonscalar data, contains coordinate system name, e.g. ‘HCI’ or ‘RTN.’ Note representation is no longer included.

Data_coordinates- Coordinate system used for observed magnetic field vector. "Other" means that an instrument-specific coordinate system is used.

Data_Cycle- Data cycle sequence number.

Data_Level- L1B.

Data_product-  Type of data product. It shall use the ISTP format "PREFIX>Suffix" (e.g., "HIST1D>1D histogram"). 

DATAPRODUCT_TYPE- High level scientific organization of the data.

Data_resolution- Typical resolution of data values. 

Data_Revision- Revision sequence number.

Data_sampling_type- What kind of time bin for averaging or sampling is used to obtain data values.

Dataset_ID- Data set identifier.

Data_type_2- Type of observed vector values, e.g., Absolute field, Variation. 

D_conversion_factor- Factor used to convert the unit of D-component from degree to nT.

_DeflateLevel- ZLIB compression level from 0 to 9. ICON uses deflate level 6 by default. 

D_unit- Physical unit of the D-component of the geomagnetic field. 

Elevation- Elevation of the location of station. 

_FillValue- Used by NetCDF to fill in data that was not explicitly set. This is typed data.m

Free_field- Description of the free field in the filename. It shall use the ISTP format "PREFIX>Suffix" (e.g., "NORM>Normal mode"), where the value of the prefix shall correspond to the "free" field in the file naming convention.

FRAME_ORIGIN- gives the origin of the reference frame where this is not implicit in the value of COORDINATE_SYSTEM.

FRAME_VELOCITY- can take either the value 'Observatory' where no corrections have been applied to the data or 'Inertial' where quantities (e.g. electric 
field or plasma flow velocity) have been corrected for spacecraft motion relative to an inertial frame (HCI).

Geographic_coordinates- What kind of geographic coordinate system is used for the following latitude and longitude. Usually either of geodetic or geographic. 

Geographic_latitude - Geographic or geodetic latitude of the location of station. 

Geographic_longitude- Geographic or geodetic longitude of the location of station. 

Geomagnetic_coordinates- What kind of geomagnetic coordinate system and what epoch and time are used for the following geomagnetic coordinate values. 

Geomagnetic_latitude- Geomagnetic latitude of the location of station. 

Geomagnetic_longitude- Geomagnetic longitude of the location of station. 

Job_ID- Process job identifier.

K9_limit- Threshold of K-index for K = 9. (for WDC data).

Known_problems- Known problems regarding the data set, such as data glitches and gaps.

Last_obs_Count_In_File- Identifies the number of packets in the current science observation type.

LEVEL- Data processing level as defined in the Solar Orbiter conventions. It shall use the ISTP format "PREFIX>Suffix" (e.g., "L1>Level 1 data processing"), where the value of the prefix shall correspond to the "level" field in the file naming convention.

Long_Name- A description of the data item in string format similar to the ISTP CatDesc.

L_value- (Dipole) L value of the location of station.

Magnetometer_type- Type of magnetometer instrument. Usually "Fluxgate" or "Induction." 

Maximum_PHD- Upper limit for the pulse height filter (typical values range from 200 to 254).

Minimum_PHD- Lower limit for the pulse height filter (typical value = 2).

Mirror_Hemisphere- Either ‘N’ (north) or ‘S’ (south) for the observed hemisphere.

Number_of_channels- Number of channels of magnetometer. 

OBS_ID- A unique identifier for the observation that is associated with the data acquisition and includes identifying information about: the SOOP; planning period; instrument; and instrument’s observation mode. The format of OBS_ID is defined in [IOR-ICD], and shall be included in the IORs delivered by the Instrument Teams to SOC.

Observation_Complete- 1 if this is the last l1b file in the current observation type otherwise 0 to continue.

Observation_end- The termination date of instrument operation. This is left blank if the instrument is currently in operation.

Observation_start- The start date of instrument operation.

Observation_Type- DAY_DISK, LIMB, NIGHT_DISK_ARCS, or STELLAR_OCCULTATION.

OBS_TYPE- 1 (DAY_DISK), 2 (LIMB), 8 (NIGHT_DISK) or 3 (OCCULTATION).

Process_ID- Process identifier.

REFERENCE- Bibcode, DOI or URL.

REPRESENTATION_i- Pointer to a support variable that gives the representation (['x','y','z'] for Cartesian; ['r','p','t'] for spherical polar; ['r','p','z'] for cylindrical polar) of the ith dimension of the variable.

_Shuffle- Enables byte shuffling in NetCDF data set for optimized compression performance.

SI_CONVERSION- A string that defines the conversion needed to base SI units, e.g. "1.0E-9>T" for DC Magnetic field data in nT.

spase_DatasetResource- The SPASE XML description of the dataset that corresponds to the SPASE ResourceID.

spase_DatasetResourceID- The SPASE ResourceID assigned of the NumericalData resource the data file is part of.

spase_GranuleResource- The SPASE XML description of the dataset that corresponds to the SPASE Granule ResourceID.

spase_GranuleResourceID- The Granule ResourceID assigned to the data file.

SOOP_TYPE-  SOOP campaign identifier, following the SOOP naming convention.

Station_code- 3-letter station code. 

Station_name- The full spelling of station name. 

TARGET_CLASS- Class of the target.

TARGET_NAME- Name of the target. 

TARGET_REGION- Region where the target is observed.

TENSOR_ORDER- Contains the rank or order of a tensor, i.e. 1 for a vector, 2 for a 3x3 tensor.

Time_calibration_method- Time recording method for observation, e.g., "GPS." 

TIME_MAX- The date and time of the end of the last acquisition for the data contained in the file.

TIME_MIN- The date and time of the beginning of the first acquisition for the data contained in the file.

UCD- UCD keywords as defined by the IVOA.

Valid_Max- The NetCDF maximum valid value which is of the same type as the variable. Skip this for strings or double/floats that are unlimited. 

Valid_Min- The NetCDF minimum valid value which is of the same type as the variable. Skip this for strings or double/floats that are unlimited. 

Valid_Range- The NetCDF two length vector containing the minimum and maximum valid values. 

Value Type-  This identifies the data type and is necessary for conversion from the ascii entry. 
