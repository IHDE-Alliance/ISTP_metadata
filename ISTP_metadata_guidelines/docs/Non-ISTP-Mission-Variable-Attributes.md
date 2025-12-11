# Non-ISTP Mission Variable Attributes 


- M - mandatory by mission
- R - recommended by mission
- O - optional for mission



| Attributes | ISTP alternative | Cluster | Arase (ERG) | GOLD | ICON | MMS | PDS | PRBEM | PSP | Solar Orbiter |
| ---------- | ---------------- | ------- | --- | ---- | ---- | --- | --- | ----- | --- | ------------- |
| `_ChunkingSizes` <br> (netCDF Internal) | | | | | M |
| `COORDINATE_SYSTEM` | | | | | | R |
| `DATA`  <br> (Cluster CEF only) |  | M  |
| `_DeflateLevel` <br> (netCDF Internal) | | | | | M |
| `DELTA_MINUS` | `DELTA_MINUS_VAR` | O | | | | | | | | 
| `DELTA_PLUS` | `DELTA_PLUS_VAR` | O | | | | | | | | 
| `_FillValue` <br> (netCDF) | `FILLVAL`| | | | M |
| `FLUX_PTR` | | | | | | | | | M |
| `FRAME` | | O | | | | | | | | 
| `long_name` | | | | | R |
| `Operator_Type` | | | | | | M |
| `REPRESENTATION_i` | | M | | | | M | | | | 
| `SI_CONVERSION` | | M | | | | | | | | R |
| `_Shuffle` <br> (netCDF) | | | | | M |
| `SIZES`   <br> (Cluster CEF only)| | M |
| `SPECIES` | | | | | | | | | M |
| `TENSOR_FRAME` | | M | | | | | | | | 
| `TENSOR_ORDER` | | M | | | | M | | | | 
| `valid_max` <br> (netCDF) | `VALIDMAX` | | | | M |
| `valid_min` <br> (netCDF) | `VALIDMIN`| | | | M |
| `valid_range` <br> (netCDF) | | | | | M |
| `VALUE_TYPE`   <br> (Cluster CEF only) | | M | | | | | | | | 
 

**Descriptions**


`_ChunkingSizes`  &mdash; netCDF attribute which controls the data arrangement.

`COORDINATE_SYSTEM`  &mdash; For nonscalar data, contains coordinate system name, e.g. `"HCI"` or `"RTN"`.

`DATA`  &mdash; (Cluster CEF only.) Used to provide the values of variables which are fixed for all records of a dataset.

`_DeflateLevel`  &mdash; ZLIB compression level from `0` to `9`. ICON uses deflate level `6` by default. 

`DELTA_MINUS` &mdash;  Describes the range over which the data are integrated, representative, etc. and locate the position of the time tag or value within this range.

`DELTA_PLUS` &mdash; Describes the range over which the data are integrated, representative, etc. and locate the position of the time tag or value within this range.

`_FillValue` &mdash; Used by netCDF to fill in data that was not explicitly set. This is typed data.

`FRAME` &mdash;  Optional and partially redundant with the more powerful description provided by the three concepts TENSOR_ORDER, REPRESENTATION, AND TENSOR_FRAME.

`long_name` &mdash; A description of the data item in string format similar to the ISTP `CATDESC`.

`L_value` &mdash; (Dipole) L value of the location of station.

`REPRESENTATION_i`- Pointer to a support variable that gives the representation ([`"x"`,`"y"`,`"z"`] for Cartesian; [`"r"`,`"p"`,`"t"`] for spherical polar; [`"r"`,`"p"`,`"z"`] for cylindrical polar) of the i-th dimension of the variable.

`_Shuffle` &mdash; Enables byte shuffling in netCDF data set for optimized compression performance.

`SI_CONVERSION` &mdash; A string that defines the conversion needed to base SI units, e.g. `"1.0E-9>T"` for DC Magnetic field data in nT.

`SIZES` &mdash; (Cluster CEF only.) Essential for any variable that has more than one element, such as arrays and vectors.

`TENSOR_FRAME` &mdash; Contains the frame of a tensor. 

`TENSOR_ORDER` &mdash; Contains the rank or order of a tensor, i.e. `1` for a vector, `2` for a 3x3 tensor.

`valid_max` &mdash; The netCDF maximum valid value which is of the same type as the variable. Skip this for strings or double/floats that are unlimited. 

`valid_min` &mdash; The netCDF minimum valid value which is of the same type as the variable. Skip this for strings or double/floats that are unlimited. 

`valid_range` &mdash; The netCDF two-element vector containing the minimum and maximum valid values. 

`VALUE_TYPE` &mdash; (Cluster CEF only.) This identifies the data type and is necessary for conversion from the ascii entry. 

---
Return to [Table of Contents](../README.md)
