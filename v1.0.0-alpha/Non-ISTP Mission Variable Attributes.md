# Non-ISTP Mission Variable Attributes 


- M - mandatory by mission
- R - recommended by mission
- O - optional for mission



| Attributes | ISTP alternative | Cluster | Arase (ERG) | GOLD | ICON | MMS | PDS | PRBEM | PSP | Solar Orbiter |
| ---------- | ---------------- | ------- | --- | ---- | ---- | --- | --- | ----- | --- | ------------- |
| _ChunkingSizes (NetCDF Internal) | | | | | M |
| Coordinate_System | | | | | | R |
| Data |                            | M|
| _DeflateLevel (NetCDF Internal) | | | | | M |
| Delta_Minus | DELTA_MINUS_VAR | O | | | | | | | | 
| Delta_Plus | DELTA_PLUS_VAR | O | | | | | | | | 
| _FillValue (NetCDF) | | | | | M |
| FLUX_PTR | | | | | | | | | M |
| Frame | | M | | | | | | | | 
| Long_name | | | | | R |
| Operator_Type | | | | | | M |
| Representation_i | | M | | | | M | | | | 
| SI_Conversion | | M | | | | | | | | R |
| _Shuffle (NetCDF) | | | | | M |
| Sizes | | M |
| SPECIES | | | | | | | | | M |
| Tensor_Frame | | M | | | | | | | | 
| Tensor Order | | M | | | | M | | | | 
| Valid_Max (NetCDF) | | | | | M |
| Valid_Min (NetCDF) | | | | | M |
| Valid_Range (NetCDF) | | | | | M |
| Value Type  | | M | | | | | | | | 
 

**Descriptions**


_ChunkingSizes- NetCDF attribute which controls the data arrangement.

COORDINATE_SYSTEM- For nonscalar data, contains coordinate system name, e.g. ‘HCI’ or ‘RTN.’ Note representation is no longer included.

Data- Used to provide the values of variables which are fixed for all records of a dataset.

_DeflateLevel- ZLIB compression level from 0 to 9. ICON uses deflate level 6 by default. 

Delta_Minus-  Describes the range over which the data are integrated, representative, etc. and locate the position of the time tag or value within this range.

Delta_Plus- Describes the range over which the data are integrated, representative, etc. and locate the position of the time tag or value within this range.

_FillValue- Used by NetCDF to fill in data that was not explicitly set. This is typed data.

Frame-  Optional and partially redundant with the more powerful description provided by the three concepts TENSOR_ORDER, REPRESENTATION, AND TENSOR_FRAME.

Long_Name- A description of the data item in string format similar to the ISTP CatDesc.

L_value- (Dipole) L value of the location of station.

REPRESENTATION_i- Pointer to a support variable that gives the representation (['x','y','z'] for Cartesian; ['r','p','t'] for spherical polar; ['r','p','z'] for cylindrical polar) of the ith dimension of the variable.

_Shuffle- Enables byte shuffling in NetCDF data set for optimized compression performance.

SI_CONVERSION- A string that defines the conversion needed to base SI units, e.g. "1.0E-9>T" for DC Magnetic field data in nT.

Sizes-  Essential for any variable that has more than one element, such as arrays and vectors.

Tensor_Frame- 

TENSOR_ORDER- Contains the rank or order of a tensor, i.e. 1 for a vector, 2 for a 3x3 tensor.

Valid_Max- The NetCDF maximum valid value which is of the same type as the variable. Skip this for strings or double/floats that are unlimited. 

Valid_Min- The NetCDF minimum valid value which is of the same type as the variable. Skip this for strings or double/floats that are unlimited. 

Valid_Range- The NetCDF two length vector containing the minimum and maximum valid values. 

Value Type-  This identifies the data type and is necessary for conversion from the ascii entry. 

