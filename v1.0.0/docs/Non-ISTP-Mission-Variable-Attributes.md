# Non-ISTP Mission Variable Attributes 


- M - mandatory by mission
- R - recommended by mission
- O - optional for mission



| Attributes | ISTP alternative | Cluster | Arase (ERG) | GOLD | ICON | MMS | PDS | PRBEM | PSP | Solar Orbiter |
| ---------- | ---------------- | ------- | --- | ---- | ---- | --- | --- | ----- | --- | ------------- |
| `_ChunkingSizes` (NetCDF Internal) | | | | | M |
| `Coordinate_System` | | | | | | R |
| `Data` |                            | M|
| `_DeflateLevel` (NetCDF Internal) | | | | | M |
| `DELTA_MINUS` | `DELTA_MINUS_VAR` | O | | | | | | | | 
| `DELTA_PLUS` | `DELTA_PLUS_VAR` | O | | | | | | | | 
| `_FillValue` (NetCDF) | | | | | M |
| `FLUX_PTR` | | | | | | | | | M |
| `Frame` | | O | | | | | | | | 
| `Long_name` | | | | | R |
| `Operator_Type` | | | | | | M |
| `Representation_i` | | M | | | | M | | | | 
| `SI_Conversion` | | M | | | | | | | | R |
| `_Shuffle` (NetCDF) | | | | | M |
| `SIZES` | | M |
| `SPECIES` | | | | | | | | | M |
| `TENSOR_FRAME` | | M | | | | | | | | 
| `TENSOR_ORDER` | | M | | | | M | | | | 
| `Valid_Max` (NetCDF) | `VALIDMAX` | | | | M |
| `Valid_Min` (NetCDF) | `VALIDMIN`| | | | M |
| `Valid_Range` (NetCDF) | | | | | M |
| `Value_Type`  | | M | | | | | | | | 
 

**Descriptions**


`_ChunkingSizes`  &mdash; netCDF attribute which controls the data arrangement.

`COORDINATE_SYSTEM`  &mdash; For nonscalar data, contains coordinate system name, e.g. `"HCI"` or `"RTN"`. Note representation is no longer included.

`Data`  &mdash; Used to provide the values of variables which are fixed for all records of a dataset.

`_DeflateLevel`  &mdash; ZLIB compression level from `0` to `9`. ICON uses deflate level `6` by default. 

`DELTA_MINUS` &mdash;  Describes the range over which the data are integrated, representative, etc. and locate the position of the time tag or value within this range.

`DELTA_PLUS` &mdash; Describes the range over which the data are integrated, representative, etc. and locate the position of the time tag or value within this range.

`_FillValue` &mdash; Used by netCDF to fill in data that was not explicitly set. This is typed data.

`Frame` &mdash;  Optional and partially redundant with the more powerful description provided by the three concepts TENSOR_ORDER, REPRESENTATION, AND TENSOR_FRAME.

`Long_Name` &mdash; A description of the data item in string format similar to the ISTP `CATDESC`.

`L_value` &mdash; (Dipole) L value of the location of station.

`REPRESENTATION_i`- Pointer to a support variable that gives the representation ([`"x"`,`"y"`,`"z"`] for Cartesian; [`"r"`,`"p"`,`"t"`] for spherical polar; [`"r"`,`"p"`,`"z"`] for cylindrical polar) of the ith dimension of the variable.

`_Shuffle` &mdash; Enables byte shuffling in netCDF data set for optimized compression performance.

`SI_CONVERSION` &mdash; A string that defines the conversion needed to base SI units, e.g. `"1.0E-9>T"` for DC Magnetic field data in nT.

`SIZES` -  Essential for any variable that has more than one element, such as arrays and vectors.

`TENSOR_FRAME` &mdash; Contains the frame of a tensor. 

`TENSOR_ORDER` &mdash; Contains the rank or order of a tensor, i.e. `1` for a vector, `2` for a 3x3 tensor.

`Valid_Max` &mdash; The netCDF maximum valid value which is of the same type as the variable. Skip this for strings or double/floats that are unlimited. 

`Valid_Min` &mdash; The netCDF minimum valid value which is of the same type as the variable. Skip this for strings or double/floats that are unlimited. 

`Valid_Range` &mdash; The netCDF two-element vector containing the minimum and maximum valid values. 

`Value_Type` &mdash;  This identifies the data type and is necessary for conversion from the ascii entry. 

---
Return to [Table of Contents](../README.md)
