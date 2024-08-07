**Variable Attributes**

***ISTP/IACG Variable Attributes***

Variable attributes are linked with each individual variable, and provide additional information about each variable. A standard set of these attributes is very important, for this is where the information can be stored in a commonly defined manner. Note that CDF attributes are case-sensitive and must **exactly** follow what is shown here **(ISTP attribute names must be capitalized)**. Additional Variable attributes can be defined but **they must start with a letter and can otherwise contain letters, numbers and the underscore character (no other special characters allowed).** The variable attributes can be listed in any order.

The following table lists all the attributes and the type of variables for which they are needed. If a type of variable is not listed, then that attribute need not be defined for that particular variable. However, if a given variable has an attribute that is not
needed, it will be ignored in most ISTP/IACG compliant applications. (RV is record or time varying)

See [Alphabetical list of Variable Attribute Definitions.](https://spdf.gsfc.nasa.gov/istp_guide/vattributes.html#variable)


| **Attribute** | **NASA Archive Requirement** | **Example** | **Notes** |
| -------------- | ---------------- | ------------- | --------- |
| [AVG_TYPE](#AVG_TYPE) | Optional | "standard" | Data or RV support_data |
| [CATDESC](#CATDESC) | Required | "HET Default time" | Required for all variables, 80 character string can be used  |
| [DELTA_MINUS](#DELTA_MINUS) | Optional |
| [DELTA_MINUS_VAR](#DELTA_MINUS_VAR)  | Optional |  "HET_Epoch_DELTA" | Data | [DELTA_PLUS](#DELTA_PLUS) | Optional  |
| [DELTA_PLUS_VAR](#DELTA_PLUS_VAR) | Optional |  "HET_Epoch_DELTA" | Data  |
| [DEPEND_0](#DEPEND_0) | Required |  "HET_Epoch"  | Data, RV support_data, and RV metadata  |
| [DEPEND_1](#DEPEND_1) | Required |  "Electron_ChanE_Energy" | Data of the following form:  1D spectrogram, 1D stack_plot, 2D spectrogram image |
| [DEPEND_2](#DEPEND_2) | Required |  "lat" | Data of the following form:  2D spectrogram image  |
| [DEPEND_3](#DEPEND_3) | Required | "TELESCOPE_index"  | Data of the following form:  3D spectrogram  |
| [DICT_KEY](#DICT_KEY) | Optional | "time"  | Optional for all variables, describes the variable |
| [DISPLAY_TYPE](#DISPLAY_TYPE) | Optional |  "time_series" | Recommended data plot type |
| [FIELDNAM](#FIELDNAM) | Required |  "HET_A_H_Rate_TS"  | Required for all variables, 30 character string can be used  |
| [FILLVAL](#FILLVAL) | Required |  -1.0e+31 | Data, RV support_data, and RV metadata  |
| [FORMAT](#FORMAT) | Required |  "F10.1"  | All not using [FORM_PTR](https://spdf.gsfc.nasa.gov/istp_guide/vattributes.html#FORM_PTR) |
| [FORM_PTR](#FORM_PTR) | Required |  "format_time" | Points to metadata string variable name for multidimensional data not using [FORMAT](https://spdf.gsfc.nasa.gov/istp_guide/vattributes.html#FORMAT) |
| [FRAME](#FRAME) | Optional |
| [LABLAXIS](#LABLAXIS) | Required | "Time" | Data of the following form:  image scalar time_series, 1D spectrogram, also needed for support_data that does not utilize LABL_PTR_X |
| [LABL_PTR_1](#LABL_PTR_1) | Required | "Electron_ChanE_Energy_LABL"  | Points to metadata string variable name for multidimensional data  without a LABLAXIS |
| [LABL_PTR_2](#LABL_PTR_1) | Required | "Telescope_Labl"  | Points to metadata string variable name for multidimensional data without a LABLAXIS  |
| [LABL_PTR_3](#LABL_PTR_1) | Required | "Sector_Label"  | Points to metadata string variable name for multidimensional data |
| [LIMITS_WARN_MIN](#LIMITS_WARN_MIN) | Optional |  0.0000 | Data  |
| [LIMITS_WARN_MAX](#LIMITS_WARN_MIN) | Optional | 9999.0000  | Data  |
| [LIMITS_NOMINAL_MIN](#LIMITS_NOMINAL_MIN) | Optional | 1990.0, 279.0, 0.0  | Data  |
| [LIMITS_NOMINAL_MAX](#LIMITS_NOMINAL_MAX) | Optional | 2001.0, 365.0, 86400000.0 | Data  |
| [MONOTON](#MONOTON) | Optional |  "INCREASE" | Epoch data |
| [REPRESENTATION_i](#REPRESENTATION_i) | Optional | "x", "y", "z" | Allowed values are enumerated in the Metadata Dictionary |
| [SCALEMAX](#SCALEMAX) | Optional | 10  | Data and RV support_data |
| [SCALEMIN](#SCALEMIN) | Optional | 100  | Data and RV support_data |
| [SCALETYP](#SCALETYP) | Recommended  |  "linear" | Data not using [SCALE_PTR](https://spdf.gsfc.nasa.gov/istp_guide/vattributes.html#SCALE_PTR) and support_data |
| [SCAL_PTR](#SCAL_PTR) | Recommended  |  "D_scale" | Points to metadata string variable name for multidimensional data not using SCALETYP  |
| [SI_CONVERSION](#SI_CONVERSION) | Optional | "1.0E-5>T"  | Expressed in terms of one of the SI units |
| [SIZES](#SIZES) | Optional | 1 for a scalar (default value) | Dimensions of the array required for any physical parameter represented by more than one component |
| [TENSOR_FRAME](#TENSOR_FRAME) | Optional | "gse" |
| [TENSOR_ORDER](#TENSOR_ORDER) | Optional | | Order of the vector or tensor which represents a non-scalar physical observable |
| [UNITS](#UNITS) | Required |  "counts s!E-1!N" | Data and support_data not using [UNIT_PTR](https://spdf.gsfc.nasa.gov/istp_guide/vattributes.html#UNIT_PTR) |
| [UNIT_PTR](#UNIT_PTR) | Required |  "unit_time" | Points to metadata string variable name for multidimensional data not using [UNITS](https://spdf.gsfc.nasa.gov/istp_guide/vattributes.html#UNITS)  |
| [VALIDMIN](#VALIDMIN) | Required | 0 | Data and RV support_data  |
| [VALIDMAX](#VALIDMAX) | Required | 200  | Data and RV support_data  |
| [VALUE_TYPE](#VALUE_TYPE) | Optional | "ISO_TIME" | Type of variable, used by Cluster Exchange Format (CEF) |
| [VAR_NOTES](#VAR_NOTES) | Recommended  | "Epoch is midpoint of integration" | Optional for all variables, any length of characters can be used |
| [VAR_TYPE](#VAR_TYPE) | Required | "support_data" | Required for all variables, describes the variable type |
| [VARIABLE_PURPOSE](#VARIABLE_PURPOSE) | Optional | "support_data"  | Data  |
| [V_PARENT](#V_PARENT) | Optional |  "A_Heavy_Rate_Parent"  | Data  |

**Variable attributes for time documentation (not needed for predefined CDF_TIME_TT2000)**


| **Attribute** | **NASA Archive Requirement** | **Example** | **Notes** |
| ------------- | ---------------- | ----------- | -------------- |
| [ABSOLUTE_ERROR](#Absolute_Error) | Optional | 0.3  | Absolute or systematic error, in same units as Units attribute. |
| [BIN_LOCATION](#Bin_Location) | Optional | 0.5  | Relative position of time stamp to the data measurement bin, with 0.0 at the beginning of time bin and 1.0 at the end. Default is 0.5 for the time at the center of the data measurement. |
| [LEAP_SECONDS_INCLUDED](#Leap_Seconds_Included) | Recommended for UTC only | "1961JAN01+1.42282s, ... ,2017JAN01+1s"  | Comma-delimited list (within brackets) of leap seconds  |
| [REFERENCE_POSITION](#Reference_Position) | Optional | "Geocenter" | Topocenter (local), Geocenter, rotating Earth geoid (used by CDF_TIME_TT2000) |
| [RELATIVE_ERROR](#Relative_Error) | Optional |  0,4 | Relative or random error, in same units as Units attribute - to specify the accuracy of the time stamps relative to each other. |
| [RESOLUTION](#Resolution) | Optional | "1ms"  | Using ISO8601 relative time format, for example: "1s" = 1 second. Resolution provides the smallest change in time that is measured. |
| [TIME_BASE](#Time_Base) | Recommended (Important for netCDF files and clarity) | "J2000" | Fixed (0AD, 1900, 1970 (POSIX), J2000 (used by CDF_TIME_TT2000), 4714 BC (Julian)) or flexible (provider-defined) |
| [TIME_SCALE](#Time_Scale) | Recommended  |  "TDT" | TT (same as TDT, used by CDF_TIME_TT2000), TAI (same as IAT, TT-32.184s), UTC (includes leap seconds), TDB (same as SPICE ET), EME1950 [default: UTC]  |
| [UNITS](#UNITS) | Optional |  "ns" | SI measurement unit: s, ms(milliseconds for EPOCH variables), ns(nanoseconds for CDF_TIME_TT2000), ps(picoseconds for EPOCH16)  |

**Variable Attribute Definitions in alphabetical order**

## ABSOLUTE_ERROR
(Optional) Absolute or systematic error, in same units as Units attribute.

## AVG_TYPE
(Optional) Sets up useful default conditions: different techniques appropriate to averaging different types of data. If this attribute is not present, **standard** average, i.e., simple arithmetic mean, is assumed. The value of this attribute can be used with application software. The valid options are listed below:

- standard -- simple arithmetic mean

- angle_degrees -- "direction" average over 360 deg e.g., average of 5 and 355 is 0 instead of 180.

- angle_radians -- "direction" average over 2 pi

- angle_hour -- "direction" average over local times (hours), e.g., average of 2 and 22 is 0 instead of 12.

- RMS -- square root of the average of the squares of the values.

- log -- logarithm of the average of the anti-logarithms of the values.

- decibel -- 10 times the logarithm of the average of the anti-logarithms of the
(values/10.).

- cosine -- cosine of the average of the arc-cosines of the values.

- none -- no meaningful averaging calculation is possible.

- Geometric -- anti-logarithm of the average of the logarithms of the values.

## BIN_LOCATION
(Optional) Relative position of time stamp to the data measurement bin, with 0.0 at the beginning of time bin and 1.0 at the end. Default is 0.5 for the time at the center of the data measurement. Since clock readings are usually truncated, the real value may be
closer to 0.0.

## CATDESC
(Required for all variables) (Catalog description) is an approximately 80-character string which is a textual description of the variable and includes a description of what the variable depends on. This information needs to be complete enough that users can select variables of interest based only on this value. (see [CDAWeb www-based interface](https://cdaweb.gsfc.nasa.gov/)). Examples:

- **Geotail Comprehensive Plasma Instrument (CPI):** Ion number density (Solar Wind Analyzer), scalar

- **Geotail EPI:** Ion Diff. Intensity, at 12 energies 67-1361 keV

- **Wind Magnetic Field Investigation (MFI):** Magnetic Field, Cartesian GSM coordinates

- **Geotail Electric Field Detector (EFD):** Electric Field from spherical probe, sunwd \ duskwd comp

- **Canopus MPA:** 42 values of 5577A Intensities from Geodetic Lat 46-67, Long=265

- **Canopus MARI:** Local Auroral Electrojet index, lower bound (CL), scalar

## DELTA_MINUS
(Optional)  Describes the range over which the data are integrated, representative, etc. and locate the position of the time tag or value within this range.

## DELTA_MINUS_VAR
(Optional) Are included to point to a variable (or variables) which stores the uncertainty in (or range of) the original variable's value. The uncertainty (or range) is stored as a (+/-) on the value of the original variable. For many variables in ISTP/IACG, the original variable will be at the center of the interval so that only one value (or one set of values) of uncertainty (or range) will need to be defined. In this case, DELTA_PLUS_VAR, and DELTA_MINUS_VAR will point to the same
variable. See [example](https://spdf.gsfc.nasa.gov/istp_guide/variables.html#data_eg3). **The value of the attribute must be a variable in the same CDF data set.**

## DELTA_PLUS
(Optional)  Describes the range over which the data are integrated, representative, etc. and locate the position of the time tag or value within this range.

## DELTA_PLUS_VAR
(Optional) Are included to point to a variable (or variables) which stores the uncertainty in (or range of) the original variable's value. The uncertainty (or range) is stored as a (+/-) on the value of the original variable. For many variables in ISTP/IACG, the original variable will be at the center of the interval so that only one
value (or one set of values) of uncertainty (or range) will need to be defined. In this case, DELTA_PLUS_VAR, and DELTA_MINUS_VAR will point to the same
variable. See [example](https://spdf.gsfc.nasa.gov/istp_guide/variables.html#data_eg3). **The value of the attribute must be a variable in the same CDF data set.**

## DEPEND_0
(Required for time-varying variables) Explicitly ties a data variable to the time variable on which it depends. All variables which change with time must have a DEPEND_0 attribute defined. The value of DEPEND_0 is *'Epoch'*, the time ordering parameter for ISTP/IACG. Different time resolution data can be supported in a single CDF data set by defining the variables Epoch, Epoch_1, Epoch_2, etc. each representing a different time resolution. These are
"attached" appropriately to the variables in the CDF data set via the attribute DEPEND_0. **The value of the attribute must be a variable in the same CDF data set.** See [example](https://spdf.gsfc.nasa.gov/istp_guide/variables.html#data_eg1).

## DEPEND_1
(Required for dimensional variables as shown in table above.) (1D time series data variables do not need a DEPEND_1 defined.) Ties a dimensional data variable to a support_data variable on which the i-th dimension of the data variable depends. The number of DEPEND attributes must match the dimensionality of the variable, i.e., a one-dimensional variable must have a DEPEND_1, a two-dimensional variable must have a DEPEND_1 and a DEPEND_2 attribute, etc. **The value of the attribute must be a variable in the same CDF data set.** See [example](https://spdf.gsfc.nasa.gov/istp_guide/variables.html#data_eg4).

## DEPEND_2
(Required for dimensional variables as shown in table above.) (1D time series data variables do not need a DEPEND_1 defined.) Ties a dimensional data variable to a support_data variable on which the i-th dimension of the data variable depends. The number of DEPEND attributes must match the dimensionality of the variable, i.e., a one-dimensional variable must have a DEPEND_1, a two-dimensional variable must have a DEPEND_1 and a DEPEND_2 attribute, etc. **The value of the attribute must be a variable in the same CDF data set.** See [example](https://spdf.gsfc.nasa.gov/istp_guide/variables.html#data_eg4).

## DEPEND_3
(Required for dimensional variables as shown in table above.) (1D time series data variables do not need a DEPEND_1 defined.) Ties a dimensional data variable to a support_data variable on which the i-th dimension of the data variable depends. The number of DEPEND attributes must match the dimensionality of the variable, i.e., a one-dimensional variable must have a DEPEND_1, a two-dimensional variable must have a DEPEND_1 and a DEPEND_2 attribute, etc. **The value of the attribute must be a variable in the same CDF data set.** See [example](https://spdf.gsfc.nasa.gov/istp_guide/variables.html#data_eg4).

## DERIVN
(Cluster required for derived variables) A text string identifying the derivation of the variable, possibly including a function/algorithm name or journal reference. Most derived variables will not be unique, and this information is essential if the product is to be compared/validated elsewhere.

## DICT_KEY
(Optional) Comes from a data dictionary keyword list and describes the variable to which it is attached. The ISTP/IACG standard dictionary keyword list is described in [ISTP/IACG Dictionary Keywords](https://spdf.gsfc.nasa.gov/istp_guide/data_dictionary.html).

## DISPLAY_TYPE
(Required for data variables) Tells automated software what type of plot to make and what associated variables in the CDF are required in order to do so. Some valid values are listed below:

- time_series

- spectrogram

- stack_plot

- image

- no_plot

## FIELDNAM
(Required for all variables) Holds a character string (up to 30 characters) which describes the variable. It can be used to label a plot either above or below the axis, or can be used as a data listing heading. Therefore, consideration should be given to the use of upper- and lower-case letters where the appearance of the output plot or data listing heading will be affected.

## FILLVAL
(Required for time varying variables) Is the number inserted in the CDF in place of data values that are known to be bad or
missing. Fill data are always non-valid data. The ISTP standard fill values are listed below. Fill values are automatically supplied in the ISTP CDHF ICSS environment (ICSS_KP_FILL_VALUES.INC) for key parameters produced at the CDHF. The FILLVAL data type must match the data type of the variable. For key parameters produced outside of the CDHF, the values below should be used.

- REAL*4
---- -1.0E31

- REAL*8
---- -1.0E31

- BYTE
---- -128

- INTEGER*2
---- -32768

- INTEGER*4
---- -2147483648

- Unsigned
INTEGER*1 ---- 255

- Unsigned
INTEGER*2 ---- 65535

- Unsigned
INTEGER*4 ---- 4294967295

- Signed
INTEGER*8 ---- -9223372036854775808LL

In addition, the CDF library has special cases for the FILLVAL and PADVALUE numbers for the three-time variable data types, where the display string is purposefully set to a recognizable string rather than the actual stored number:

| **Time data type** | **Variable type** | **Stored number**  | **Input/Output string**  |
| ------------------ | ----------------- | ---------------------- | -------------------------------- |
| TT2000 | FILLVAL | -9223372036854775808LL | 9999-12-31:23:59:59.999999999  |
|  | PADVALUE  | -9223372036854775807LL | 0000-01-01:00:00:00.000000000  |
| EPOCH  | FILLVAL | -1.0E31  | 9999-12-31:23:59:59.999  |
|  | PADVALUE  | 0.0  | 0000-01-01:00:00:00.000  |
| EPOCH16  | FILLVAL | -1.0E31, -1.0E31 | 9999-12-31:23:59:59.999999999999 |
|  | PADVALUE  | 0.0  | 0000-01-01:00:00:00.000000000000 |

## FORMAT
(Required if not using FORM_PTR) Is the output format used when extracting data values out to a file or screen (using CDFlist). The magnitude and the number of significant figures needed should be carefully considered. A good check is to consider it with respect to the values of VALIDMIN and VALIDMAX attributes. The output should be in Fortran format.

## FORM_PTR
(Required if not using FORMAT) Has as its value a variable which stores the character strings (up to 20 characters per
character string) representing the desired output format for the original variable. FORM_PTR is used *instead of* FORMAT. **The value of the attribute must be a variable in the same CDF data set.**

## LABLAXIS
(Required if not using LABL_PTR_1) Should be a short character string (approximately 10 characters, but preferably 6 characters - more only if absolutely required for clarity) which can be used to label a y-axis for a plot or to provide a heading for a data listing.

## FRAME
(Optional)  Optional and partially redundant with the more powerful description provided by the three concepts TENSOR_ORDER, REPRESENTATION, AND TENSOR_FRAME.

## LABL_PTR_1
(Required if not using LABLAXIS) Is used to label a dimensional variable when one value of LABLAXIS is not sufficient to describe the variable or to label all the axes. LABL_PTR_i is used *instead of* LABLAXIS, where *i* can take on any value from 1 to *n* where *n* is the total number of dimensions of the original variable. The value of LABL_PTR_1 is a variable which will contain the short character strings which describe the first dimension of the original variable. The actual labels should be short as described above for LABLAXIS. **The value of the attribute must be a variable in the same CDF data set.** See example (https://spdf.gsfc.nasa.gov/istp_guide/variables.html#data_eg2).

## LABL_PTR_2
(Required if not using LABLAXIS) Is used to label a dimensional variable when one value of LABLAXIS is not sufficient to describe the variable or to label all the axes. LABL_PTR_i is used *instead of* LABLAXIS, where *i* can take on any value from 1 to *n* where *n* is the total number of dimensions of the original variable. The value of LABL_PTR_1 is a variable which will contain the short character strings which describe the first dimension of the original variable. The actual labels should be short as described above for LABLAXIS. **The value of the attribute must be a variable in the same CDF data set.** See example (https://spdf.gsfc.nasa.gov/istp_guide/variables.html#data_eg2).

## LABL_PTR_3
(Required if not using LABLAXIS) Is used to label a dimensional variable when one value of LABLAXIS is not sufficient to describe the variable or to label all the axes. LABL_PTR_i is used *instead of* LABLAXIS, where *i* can take on any value from 1 to *n* where *n* is the total number of dimensions of the original variable. The value of LABL_PTR_1 is a variable which will contain the short character strings which describe the first dimension of the original variable. The actual labels should be short as described above for LABLAXIS. **The value of the attribute must be a variable in the same CDF data set.** See example (https://spdf.gsfc.nasa.gov/istp_guide/variables.html#data_eg2).

## LEAP_SECONDS_INCLUDED
(Recommended for UTC only) Comma-delimited list (within brackets) of leap seconds included in the form of a lists of ISO8601 times when each leap second was added, appended with the size of the leap second in ISO8601 relative time (+/- time, most commonly: "+1s") [default: standard list of leap seconds up to time of data]. Leap_Seconds_Included is needed to account for time scales that don't have all 37 (in 2022) leap seconds and for the clocks in various countries that started using leap seconds at different times. The full list is required to handle the equally or more common case where a time scale starts at a specific Universal Time Coordinate (UTC) but continues on without leap seconds in TAI mode; this is basically what missions that don't add leap seconds are doing.

$ cat tai-utc.dat | awk
'ORS="," { val = $7 - prev } {prev = $7} { print $1$2"01+"val "s" }'

LEAP_SECONDS_INCLUDED="1961JAN01+1.42282s,1961AUG01-0.05s,1962JAN01+0.47304s,1963NOV01+0.1s,1964JAN01+1.29427s,1964APR01+0.1s,1964SEP01+0.1s,1965JAN01+0.1s,1965MAR01+0.1s,1965JUL01+0.1s,1965SEP01+0.1s,1966JAN01+0.47304s,1968FEB010.1s,1972JAN01+5.78683s,1972JUL01+1s,1973JAN01+1s,1974JAN01+1s,1975JAN01+1s,1976JAN01+1s,1977JAN01+1s,1978JAN01+1s,1979JAN01+1s,1980JAN01+1s,1981JUL01+1s,1982JUL01+1s,1983JUL01+1s,1985JUL01+1s,1988JAN01+1s,1990JAN01+1s,1991JAN01+1s,1992JUL01+1s,1993JUL01+1s,1994JUL01+1s,1996JAN01+1s,1997JUL01+1s,1999JAN01+1s,2006JAN01+1s,2009JAN01+1s",2012JUL01+1s,2015JUL01+1s,2017JAN01+1s"

## LIMITS_WARN_MAX
(Optional) Values which define the limits where damage is likely to occur for values outside these values (often referred to as red limits). Visualization software can use these attributes for indicating limits on plots or other warnings. **The values data type must match the data type of the variable.**

## LIMITS_WARN_MIN
(Optional) Values which define the limits where damage is likely to occur for values outside these values (often referred to as red limits). Visualization software can use these attributes for indicating limits on plots or other warnings. **The values data type must match the data type of the variable.**

## LIMITS_NOMINAL_MAX
(Optional) Values which define the range of nominal operations and where values outside the range of these values should be flagged as warnings (often referred to as yellow
limits). Visualization software can use these attributes for indicating limits on plots or other warnings. The range of LIMITS_NOMINAL_MIN and LIMITS_NOMINAL_MAX fall within the range of LIMITS_WARN_MIN and LIMITS_WARN_MAX. Yellow limits are often set a certain percentage away from the red limits to give the operator a chance to respond before the red limits are reached. **The values data type must match the data type of the variable.**

## LIMITS_NOMINAL_MIN
(Optional) Values which define the range of nominal operations and where values outside the range of these values should be flagged as warnings (often referred to as yellow
limits). Visualization software can use these attributes for indicating limits on plots or other warnings. The range of LIMITS_NOMINAL_MIN and LIMITS_NOMINAL_MAX fall within the range of LIMITS_WARN_MIN and LIMITS_WARN_MAX. Yellow limits are often set a certain percentage away from the red limits to give the operator a chance to respond before the red limits are reached. **The values data type must match the data type of the variable.**

## MONOTON
(Optional) Indicates whether the variable is monotonically increasing or monotonically decreasing. Use of MONOTON is strongly recommended for the Epoch time variable, and can significantly increase the performance speed on retrieval of data. Valid values: INCREASE, DECREASE.

## RELATIVE_ERROR
(Optional) Relative or random error, in same units as Units attribute - to specify the accuracy of the time stamps relative to each other. This is usually much smaller than Absolute_Error.

## REFERENCE_POSITION
(Optional) Topocenter (local), Geocenter , rotating Earth geoid (used by CDF_TIME_TT2000).
Reference_Position is optional metadata to account for time variance with position in the gravity wells and with relative velocity. While we could use a combined TimeSystem attribute that defines mission-specific time scales where needed, such as UTC-at-STEREO-B, it's cleaner to keep them separate as Time_Scale=UTC and Reference_Position=STEREO-B.

## REPRESENTATION_i
(Required) Pointer to a support variable that gives the representation (['x','y','z'] for Cartesian; ['r','p','t'] for spherical polar; ['r','p','z'] for cylindrical polar) of the ith dimension of the variable.

## RESOLUTION
(Optional) Using ISO8601 relative time format, for example: "1s" = 1 second. Resolution provides the smallest change in time that is measured.

## SCALEMAX
(Optional) Are values which can be based on the actual values of data found in the CDF data set or on the probable uses of the data, em e.g., plotting multiple files at the same scale. Visualization software can use these attributes as defaults for plotting. The values must match the data type of the variable.

## SCALEMIN
(Optional) Are values which can be based on the actual values of data found in the CDF data set or on the probable uses of the data, em e.g., plotting multiple files at the same scale. Visualization software can use these attributes as defaults for plotting. The values must match the data type of the variable.

## SCALETYP
(Recommended for non-linear scales if not using SCAL_PTR) Indicates whether the variable should have a **linear** or a **log** scale as a default. If this attribute is not present, **linear** scale is assumed.

## SCAL_PTR
(Recommended for non-linear scales if not using SCALETYP) Is used for dimensional variables when one value of SCALTYP is not sufficient. SCAL_PTR is used \em instead of SCALTYP, and will point to a variable which will be of the same dimensionality as the original variable. The allowed values are linear and log. **The value of the attribute must be a variable in the same CDF data set.**

## sig_digits
(Cluster recommended) This attribute provides the number of significant digits or other measure of data accuracy in a TBD manner. It is to allow compression software to optimize the number of digits to retain, and users to assess the accuracy of products. This operation is subject to the deliberations of the 'network traffic report' Task Group, DS-CFC-TN-0001, on compression algorithms and implementation. Restrictions on data compression may also influence the format and choice of data type used by the CDF generation software.

## SI_CONVERSION
(Cluster recommended) The conversion factor to SI units as a text string of the form number>SI unit, using the SI units listed below. This is the factor that the variable must be multiplied by in order to turn it to generic SI units. It will contain two text fields separated by the delimiter >. The first is the conversion number and the second is the standard unit that it converts to. For example, for a magnetic field measured in nT, the SI_CONVERSION="1.0e-9>T". The format must be scrupulously respected because the information will be parsed by generic software. Two useful units which are not SI units are added: degree (angle), and unitless (no units).

For compound units, the grammar will be of a standard form: distinct unit dimensions will be separated by space characters and powers (signed) will be preceded by the carat, ^. Non-dimensional qualifiers, which do not appear in the SI units list, are to be enclosed in brackets “()” and will be ignored, for example, "m s^-1" or "(number electrons) m^-3" . Non-integer powers are permitted, e.g., “Hz^–0.5”. Similarly, brackets may be used to provide user information (e.g., for labelling axes) on dimensionless quantities, such as SI_CONVERSION="1.0E-2>(fraction) unitless" for a percentage. When the unit is unitless, unitless must be specified on the right-hand side.

For cases where there are multiple inhomogeneous units, such as representing a vector in polar coordinates, the syntax may be extended with commas between units, such as "1.e3>m, 1>degree, 1>degree" for spherical polar coordinates in [km, degrees, degrees]; or "1.e3>m, 1>rad, "1.e3>m" for cylindrical polar coordinates in [km, radian, km].

Other examples:

Magnetic field in γ : SI_CONVERSION="1.0E-5>T"

density in cm-3 : SI_CONVERSION="1.0E-6>(particles)m^-3"

unitless : SI_CONVERSION="1>unitless"

|SI Unit|Description|
|---|------|
|m|metre|
|N|newton|
|kg|kilogram| 
|Pa|pascal|
|s|second|
|Hz|hertz|
|A|ampere|
|V|volt|
|K|kelvin|
|W|watt|
|rad|radian| 
|J|joule|
|sr|steradian| 
|C|coulomb|
|T|tesla|
|ohm|ohm|
|mho|mho (siemens)|
|H|henry|
|F|farad|
|Celsius|celsius|
|degree|angle|
|unitless|no units|


## SIZES
(Required) Essential for any variable that has more than one element, such as arrays and vectors.

## TENSOR_FRAME
(Required) Contains the frame of a tensor.

## TENSOR_ORDER
(Required) Contains the rank or order of a tensor, i.e. 1 for a vector, 2 for a 3x3 tensor.

## TIME_BASE
(Recommended for Time variables [important for netCDF files and clarity]) Fixed (0AD, 1900, 1970 (POSIX), J2000 (used by CDF_TIME_TT2000), 4714 BC (Julian)) or flexible (provider-defined)

## TIME_SCALE
(Optional) TT (same as TDT, used by CDF_TIME_TT2000), TAI (same as IAT, TT-32.184s), UTC (includes leap seconds), TDB (same as SPICE ET), EME1950 [default: UTC]

## UNITS
(Required if not using UNIT_PTR [optional for time variables]) Is a character string (no more than 20 characters, but preferably 6 characters) representing the units of the variable, *e.g.,* nT for magnetic field. If the standard abbreviation used is short then the units value can be added to a data listing heading or plot label. Use a blank character, rather than "None" or "unitless", for variables that have no units (e.g., a ratio or a direction cosine). For CDF_TIME_TT2000: SI measurement unit: s, ms(milliseconds for EPOCH variables), ns(nanoseconds for CDF_TIME_TT2000), ps(picoseconds for EPOCH16)

## UNIT_PTR
(Required if not using UNITS) Has as its value a variable which stores the character strings (up to 20 characters per character string) representing the units of the original variable, which can be added to a data listing heading or plot label. Use a blank character, rather than "None" or "unitless", for variables that have no units (e.g., a ratio or a direction cosine). If this attribute is used, then UNITS is not used. **The value of the attribute must be a variable in the same CDF data set.**

## VALIDMAX
(Required for time varying data and support_data) Hold values which are, respectively, the minimum and maximum values for a particular variable that are expected over the lifetime of the mission, not values for the individual data files. The values must match the data type of the variable.

## VALIDMIN
(Required for time varying data and support_data) Hold values which are, respectively, the minimum and maximum values for a particular variable that are expected over the lifetime of the mission, not values for the individual data files. The values must match the data type of the variable.

## VALUE_TYPE
(Required) This identifies the data type and is necessary for conversion from the ascii entry.

## VAR_NOTES
(Optional) Holds ancillary information about the variable and can be any length.

## VAR_TYPE
(Required for all variables) Identifies a variable as either:

- **data** integer or real numbers that are plottable

- **support_data** integer or real "attached" variables

- **metadata** (labels or character variables)

- **ignore_data** placeholders

## VARIABLE_PURPOSE
(Optional) Are a list of tags/keywords separated by commas that indicate probable uses of the variable and its function. Software can use these attributes to find the primary variables in the dataset, find variables with a common function, indicate variables suitable for specific purposes such as summary plots or educational displays, etc. Tags could indicate a common geophysical quantity to enable matching several variables of the same kind. For instance, all magnetic field variables could be tagged with VARIABLE_PURPOSE="Magnetic_Field" even though they have different coordinate systems or cadences. Software could use this tag to identify variables with a common theme for easier distinguishing between groups of variables and selecting between them. The values are always in a character string. Suggested tags/keywords include:

- **"PRIMARY_VAR"**: one of the primary variables in the dataset

- **"EDUCATION"**: one of the variables suitable for displaying in an educational context

- **"SUMMARY"**: one the variables to display on automatic summary plots

- **"CARTESIAN", "ANGULAR"**: distinguish variables by coordinate system

- **"Magnetic_Field", "Electric_Field", etc.**: common instrument tag to relate similar variables

## V_PARENT
(Optional for use with derived variables) Identifies the "attached" variable which stores the parent variable(s) of a derived variable. The ''attached" variable can be dimensional and sized to hold as many parents as necessary. The syntax of each entry would be: logical_file_id>variable_name.


Return to Table of Contents: [Table of Contents](00_Table_of_Contents.md)
