**Mission Metadata Usage**

Table of Contents

MMS (#MMS)

Cluster

ERG

PRBEM

Solar Orbiter


**MMS**

Global attributes are used to provide information about the data set as an entity.
Together with variables and variable attributes, the global attributes make the data correctly and independently usable by someone not connected with the instrument team, and hence, a good archive product.




1. Required-
   The following global attributes are required with MMS data products. MMS-specific values are provided where applicable.
  
   1.1  Data_type-
     This attribute is used by CDF file writing software to create a filename. It is a combination of the following filename components: mode, data level, and optional data product descriptor. 

    1.2  Data_version- 
   This attribute identifies the version (vX.Y.Z) of a particular CDF data file.
   
    1.3  Descriptor- 
   This attribute identifies the name of the instrument or sensor that collected the data. Both a long name and a short name are given. For any data file, only a single value is allowed. For MMS, the following are valid values:
-    FIELDS>Electric and Magnetic Fields Investigation
-    ADP>Axial Double Probe
-    SDP>Spin-plane Double Probe
-    EDP->Electric Double Probe
-    AFG>Analog Flux Gate Magnetometer
-    DFG>Digital Flux Gate Magnetometer
-    AFG-DFG
-    AFG-DFG-SCM
-    SCM>Search Coil Magnetometer
-    EDI>Electron Drift Instrument
-    FPI>Fast Plasma Instrument
-    DIS>Dual Ion Spectrometers
-    DES>Dual Electron Spectrometers
-    HPCA> Hot Plasma Composition Analyzer
-    EPD>Energetic Particle Detector
-    EIS>Energetic Ion Spectrometer
-    FEEPS>Fly’s Eye Energetic Particle Sensor 
-    EIS-FEEPS
-    ASP1>Active Spacecraft Potential Control - sensor 1
-    ASP2>Active Spacecraft Potential Control - sensor 2
-    ASP>Active Spacecraft Potential Control – sensors 1 and 2
-    EPH>Ephemeris
-    ATT>Attitude
-    MEC>Magnetic Ephemeris and Coordinates


1.4  Discipline-
This attribute describes both the science discipline and sub discipline. For MMS, this 
value should always be “Space Physics>Magnetospheric Science.”

1.5 Generation_date- 
Date stamps the creation of the file using the syntax yyyymmdd, e.g., "20150923". This 
is distinct from the date in "validate" below which records the times of later validation 
processes. 

1.6 Instrument_type-
This attribute is used to facilitate making choices of instrument type. More than one entry is allowed. Valid values for MMS include:
- Electric Fields (space)
- Magnetic Fields (space)
- Particles (space)
- Plasma and Solar Wind
- Spacecraft Potential Control
- Ephemeris

1.7 Logical_file_id-
This attribute stores the name of the CDF file but without the  file extension (e.g. ".cdf"). This attribute is required to avoid loss of the original source  in the case of accidental (or intentional) renaming. This attribute must be manually set by  the user during creation. 

1.8 Logical_source- 
This attribute determines the file naming convention in the SKT Editor and is used by 
CDA Web. It is composed of the following values:
- source_name - (e.g. spacecraft identifier)
- descriptor - (e.g. instrument identifier)
- data_type - (e.g. mode, data level, and optional data product descriptor - value)

For instance, the following examples are valid "Logical_source" attributes: 
- mms1_edi_slow_ql_ambient
- mms2_edi_brst_l2_ambient
- mms3_edi_fast_l2_efield
- mms4_dsp_slow_ql_lfe
- mms1_dsp_fast_ql_mfe
- mms2_dsp_slow_ql_lfb
- mms3_sdp_fast_ql_swd
- mms4_brst_l2_efield 
- mms1_brst_l2_bfield
- mms1_fpi_fast_sitl_1h
- mms1_des_slow_l1A_cnts-1h
- mms1_dis_slow_l1A_cnts-1h

1.9 Logical_source_description-
This attribute writes out the full words associated with the encrypted Logical_source 
above, e.g., "Level 1 Dual Electron Spectrometer Survey Data". Users on CDAWeb see 
this value on their website.

1.10 Mission_group-
This attribute has a single value and is used to facilitate making choices of source through CDAWeb. This value should be “MMS.”

1.11 PI_affiliation- 
This attribute value should include the MMS mission PI affiliation followed by a comma separated list of any Co-I affiliations that are responsible for this particular dataset. The
following are valid MMS values, of which the abbreviations should be used exclusively 
within this attribute value, and the full text of the affiliation included in the general text 
attribute as it is used solely in plot labels.
- JHU/APL – Applied Physics Laboratory
- GSFC – Goddard Space Flight Center
- IRFU - Institutet för rymdfysik, Uppsala
- IWF - Institut für Weltraumforschung
- KTH - Kungliga Tekniska Högskolan (Swedish Royal Institute of Technology)
- LANL - Los Alamos National Laboratory
- LASP - Laboratory for Atmospheric and Space Physics
- LPP - Laboratoire de Physique des Plasmas
- SWRI – Southwest Research Institute
- UCLA - University of California Los Angeles
- UNH – University of New Hampshire

1.12 PI_name- 
This attribute value should include first initial and last name of the MMS mission PI 
followed by a comma-separated list of any Co-Is that are responsible for this particular 
dataset. For example, a single PI entry in this attribute would be: J. Burch. The attribute 
inclusive of Co-Is would be: J. Burch, C. Pollock, S. Fuselier, R. Torbert, B. Mauk, K.Torkar. 

1.13 Project- 
This attribute identifies the name of the project and indicates ownership. For MMS, this 
value should be “STP>Solar-Terrestrial Physics”. 

1.14 Source_name-
This attribute identifies the observatory where the data originated. The following are 
valid values for MMS:
- MMS1>MMS Satellite Number 1
- MMS2>MMS Satellite Number 2
- MMS3>MMS Satellite Number 3
- MMS4>MMS Satellite Number 4
- MMS>MMS Constellation

1.15 TEXT-
This attribute is an SPDF standard global attribute, which is a text description of the 
experiment whose data is included in the CDF. A reference to a journal article(s) or to a 
World Wide Web page describing the experiment is essential, and constitutes the 
minimum requirement. A written description of the data set is also desirable. This 
attribute can have as many entries as necessary to contain the desired information. 
Typically, this attribute is about a paragraph in length and is not shown on CDAWeb.

1.16 HTTP_LINK- 
This attribute stores the URL for with a description of this dataset at the SDC. This 
attribute is used in conjunction with "LINK_TEXT" and "LINK_TITLE". There can be 
up to 5 entries for each - there MUST be a corresponding entry of "LINK_TEXT" and 
"LINK_TITLE" for each "HTTP_LINK" entry. CDAWeb will then link to the URL 
given by "HTTP_LINK" using the "LINK_TITLE" and the description in 
"LINK_TEXT", on the CDAWeb Data Explorer page. For example:
- "LINK_TEXT" = 5-minute dual electron fast spectrometer data starting at 1 Feb 
- 2015 13:15 available at 
- "LINK_TITLE" = MMS1 DES
- "HTTP_LINK" = http://lasp.colorado.edu/mms1/des/fast/l2/ will create the following link:

5-minute dual electron fast spectrometer data starting at 1 Feb 2015 13:15 available at 
MMS1 DES Multiple HTTP_LINK (as well as LINK_TEXT and LINK_TITLE) attributes may be  included. It is suggested that each data set includes links to the MMS project web page, the relevant instrument page, and finally the web-services link to the data product itself. Thus the HTTP_LINK, LINK_TEXT, and LINK_TITLE attributes would read as follows:

- “HTTP_LINK” 1: CDF_CHAR {“ http://mms.gsfc.nasa.gov/”}
- 2: CDF_CHAR {“ http://mms.space.swri.edu/index.html”}
- 3: CDF_CHAR {“ https://lasp.colorado.edu/mms/sdc/” }
- “LINK_TEXT” 1: CDF_CHAR {“MMS home page”}
- 2: CDF_CHAR {“SMART package home page”}
- 3: CDF_CHAR {“Science Data Center”}
- “LINK_TITLE” 1: CDF_CHAR {“At GSFC”}
- 2: CDF_CHAR {“AT SWRI”}
- 3: CDF_CHAR {“LASP SDC”}

1.17 LINK_TEXT- 
If text is not needed, use: ""

1.18 LINK_TITLE 

1.19 MODS- 
This attribute is an SPDF standard global attribute, which is used to denote the history of modifications made to the CDF data set. The MODS attribute should contain a description of all significant changes to the data set, essentially capturing a log of high-level release notes. This attribute can have as many entries as necessary and should be 
updated if the "X" value of the version number changes. 

1.2 Recommended-
The following global attributes are recommended but not required with MMS data products. MMS-specific values are provided where applicable.

1.2.1 Acknowledgement-
This field indicates how the data should be cited.

1.2.2 Generated_by- 
This attribute indicates where users can get more information about this data and/or 
check for new versions. 

1.3 Optional

1.3.1 Parents- 
This attribute lists the parent data files for files of derived and merged data sets. The 
syntax for a CDF parent is: "CDF>logical_file_id". Multiple entry values are used for 
multiple parents. This attribute is required for any MMS data products that are derived 
from 2 or more data sources and the file names of parent data should be clearly identified.
CDF parents may include source files with non-cdf extensions. 

1.3.2 Skeleton_version- 
This is a text attribute containing the skeleton file version number. 

1.3.3 Rules_of_use- 
Text containing information on citability and/or PI access restrictions. This may point to 
a World Wide Web page specifying the rules of use. Rules of Use are determined on both a mission and instrument basis, at the discretion of the PI. 

1.3.4 Time_resolution-
Specifies time resolution of the file, e.g., "3 seconds."

2. Variables- There are three types of variables that should be included in CDF files: data, support data, and metadata. Additionally, required attributes are listed with each variable type listed below. To facilitate data exchange and software development, variable names should be consistent across the MMS instruments and four spacecraft. Additionally, it is preferable that data types are consistent throughout all MMS data products (e.g. all real variables are CDF_REAL4, all integer variables are CDF_INT2, and flag/status variables are UINT2). This is not to imply that only these data types are allowable within MMS CDF files. All CDF supported data types are available for use by MMS.

2.1 Data- 
These are variables of primary importance (e.g., density, magnetic field, particle flux). 
Data is always time (record) varying, but can be of any dimensionality or CDF supported  data type. Real or Integer data are always defined as having one element.

2.1.1 Naming- 
MMS data variables must adhere to the following naming convention scId_instrumentId_paramName
An underscore is used to separate different fields in the variable name. It is strongly 
recommended that variable names employ further fields, qualifiers and information 
designed to identify unambiguously the nature of the variable, instrument mode and data processing level, with sufficient detail to lead the user to the unique source file which  contains the variable. It is recommended that these follow the order shown below:
scId_instrumentId_paramName[_coordSys][_paramQualifier][_subModeLevel][_mode][
_dataLevel]
Note the following caveats:
- CDF variable names must begin with a letter and can contain numbers and 
- underscores, but no other special characters.
- In general, the instrumentId field follows the convention used for file names. However, since variable names cannot contain a hyphen, an underscore should be used instead of a hyphen when needing to separateinstrument components. For instance, "afg-dfg" is a valid instrumentId in a filename but when used in a variable name, "afg_dfg" should be used instead. 
- To ensure software compatibility between disparate systems, parameter names will consist of all lowercase characters.

2.1.2 Required Epoch Variable-
All MMS CDF data files must contain at least one variable of data type 
CDF_TIME_TT2000, typically named "Epoch". This variable should normally 
be the first variable in each CDF data set. All time varying variables in the CDF 
data set will depend on either this "Epoch" variable or on another variable of 
type CDF_TIME_TT2000 (e.g. mms1_afg_epoch). More than one 
CDF_TIME_TT2000 type variable is allowed in a data set to allow for more 
than one time resolution, using the required DEPEND_0 attribute (5.1.3.2) to 
associate a time variable to a given data variable. It is recommended that all 
such time variables use “epoch” within their variable name.
For ISTP, but not necessarily for all MMS data, the time value of a record 
refers to the center of the accumulation period for the record if the 
measurement is not an instantaneous one. All MMS time variables used as 
DEPEND_0 are strongly recommended to have DELTA_PLUS_VAR and 
DELTA_MINUS_VAR attributes (see section 5.1.4.3 below) which delineate 
the time interval over which the data was sampled, integrated, or otherwise 
representative of. This also locates the timetag within that interval.
The datatype, CDF_TIME_TT2000, is defined as an 8-byte signed integer with the 
following characteristics:

- Time_Base=J2000 (Julian date 2451545.0 TT or 2000 January 1, 12h TT)
Resolution=nanoseconds
- Time_Scale=Terrestrial Time (TT)
Units=nanoseconds
Reference_Position=rotating Earth Geoid

Given a current list of leap seconds, conversion between TT and UTC is straightforward 
(TT = TAI + 32.184s; TT = UTC + deltaAT + 32.184s, where deltaAT is the sum of the 
leap seconds since 1960; for example, for 2009, deltaAT = 34s). Pad values of -
9223372036854775808 (0x8000000000000000) which corresponds to 1707-09-
22T12:13:15.145224192; recommended FILLVAL is same.
It is proposed that the required data variables VALIDMIN and VALIDMAX (5.1.3.14 
and 5.1.3.15, respectively) are given values corresponding to the dates 1990-01-
01T00:00:00 and 2100-01-01T00:00:00 as these are well outside any expected valid 
times.

2.1.3 Attributes: Data Variables-
Data variables require the following attributes:
- CATDESC
- DEPEND_0
- DEPEND_i [for dimensional data variables]
- DISPLAY_TYPE
- FIELDNAM
- FILLVAL
- FORMAT or FORM_PTR
- LABLAXIS or LABL_PTR_i
- SI_CONVERSION
- UNITS or UNIT_PTR
- VALIDMIN and VALIDMAX
- VAR_TYPE

In addition, the following attributes are strongly recommended for vectors, tensors and 
quaternions which are held in or relate to a particular coordinate system:
- COORDINATE_SYSTEM
- TENSOR_ORDER
- REPRESENTATION_i
- OPERATOR_TYPE [for quaternions]

2.1.3.1 CATDESC-
This is a human readable description of the data variable. Generally, this is an 80-
character string which describes the variable and what it depends on. 

2.1.3.2 DEPEND_0- 
Explicitly ties a data variable to the time variable on which it depends. All variables 
which change with time must have a DEPEND_0 attribute defined.

2.1.3.3 DEPEND_i-
Ties a dimensional data variable to a SUPPORT_DATA variable on which the i-th 
dimension of the data variable depends. The number of DEPEND attributes must match the dimensionality of the variable, i.e., a one-dimensional variable must have a 
DEPEND_1, a two-dimensional variable must have a DEPEND_1 and a DEPEND_2 
attribute, etc. The value of the attribute must be a variable in the same CDF data set. It is strongly recommended that DEPEND_i variables hold values in physical units. 
DEPEND_i variables also require their own attributes.

2.1.3.4 DISPLAY_TYPE- (e.g. time_series, spectrogram, stack_plot,image)
This tells automated software, such as CDAWEB, how the data should be displayed. 
Examples of valid values include:
- time_series
- spectrogram
- stack_plot
- image

2.1.3.5 FIELDNAM-
A shortened version of CATDESC which can be used to label a plot axis or as a data 
listing heading. This is a string, up to ~30 characters in length.

2.1.3.6 FILLVAL-
Identifies the fill value used where data values are known to be bad or missing. 
FILLVAL is required for time-varying variables. Fill data are always non-valid data. The 
ISTP standard fill values are listed below:
- BYTE ---- -128
- INTEGER*2 ---- -32768
- INTEGER*4 ---- -2147483648
- INTEGER*8 ---- -9223372036854775808
- Unsigned INTEGER*1 ---- 255
- Unsigned INTEGER*2 ---- 65535
- Unsigned INTEGER*4 ---- 4294967295
- REAL*4 ---- -1.0E31
- REAL*8 ---- -1.0E31
- EPOCH ---- -1.0E31 (9999-12-31:23:59:59.999)
- EPOCH16 ---- -1.0E31 (9999-12-31:23:59:59.999999999999)
- TT2000 ---- -9223372036854775808LL (9999-12-31:23:59:59.999999999999)

2.1.3.7 FORMAT- (required if not using FORM_PTR)
This field allows software to properly format the associated data when displayed on a 
screen or output to a file. Format can be specified using either Fortran or C format codes. 
For instance, "F10.3" indicates that the data should be displayed across 10 characters 
where 3 of those characters are to the right of the decimal.

2.1.3.8 FORM_PTR- (required if not using FORMAT)
The value of this field is a variable which stores the character string that represents the 
desired output format for the associated data. 

2.1.3.9 LABLAXIS- (required if not using LABL_PTR_i)
Used to label a plot axis or to provide a heading for a data listing. This field is generally 
6-10 characters. Only one of LABLAXIS or LABL_PTR_i should be present.

2.1.3.10 LABL_PTR_i- (required if not using LABLAXIS)
Used to label a dimensional variable when one value of LABLAXIS is not sufficient to 
describe the variable or to label all the axes. LABL_PTR_i is used instead of 
LABLAXIS, where i can take on any value from 1 to n where n is the total number of 
dimensions of the original variable. The value of LABL_PTR_1 is a variable which will 
contain the short character strings which describe the first dimension of the original 
variable. The value of the attribute must be a variable in the same CDF data set and is 
generally 6-10 characters. Only one of LABLAXIS or LABL_PTR_i should be present.

2.1.3.11 SI_CONVERSION-
The conversion factor to SI units. This is the factor that the variable must be multiplied 
by in order to convert it to generic SI units. This parameter contains two text fields 
separated by the ">" delimiter. The first component is the conversion factor and the 
second is the standard SI unit. Units are defined according to their standard SI symbols 
(ie. Tesla = T, Newtons = N, Meters = m, etc.) For data variables that are inherently 
unitless, and thus lack a conversion factor, this data attribute will be “☐>☐” where ☐ is a blank space and the quotation marks are not included. Units which are not convenientlytransformed into SI should follow the blank syntax “☐>☐” described above. For example, the magnetic field for FGM will be in nT, and to convert to Tesla the value  of SI_CONVERSION will be "1.0e-9>T". The use of text allows this attribute to be parsed and the value must be extracted in software. An active list of MMS standard UNITS and their SI_CONVERSIONs is maintained on the mission web-pages at 
https://lasp.colorado.edu/galaxy/display/mms/Units+of+Measure, accessible via the 
MMS Science Working Team pages. SI_CONVERSION strings must adhere to a strict, 
machine-parseable format that is fully described on the “Units of Measure” web page 
found by following the above link.

2.1.3.12 UNITS- (required if not using UNIT_PTR)
A 6-20 character string that identifies the units of the variable (e.g. nT for magnetic 
field). Use a blank character, rather than "None" or "unitless", for variables that have no units (e.g., a ratio or a direction cosine). An active list of MMS standard UNITS and their SI_CONVERSIONs is maintained on the mission web-pages at
https://lasp.colorado.edu/galaxy/display/mms/Units+of+Measure, accessible via the 
MMS Science Working Team pages. Those pages also lay out the rules for formatting the UNITS string.

2.1.3.13 UNIT_PTR- (required if not using UNITS)
The value of this field is a variable which stores short character strings which identify the units of the variable. Use a blank character, rather than "None" or "unitless", for variables that have no units (e.g., a ratio or a direction cosine). The value of this attribute must be a variable in the same CDF data set.

**Cluster**

1. Global Metadata-
   Global attributes are used to provide informational metadata associated with all the variables in the file, and as a means of attaching information that may be carried along with the data.
   START META This parameter starts a block of metadata supplying the entries associated with a global attribute (in cdf terminology). This block is closed by an END META parameter. They are described more fully below. The value associated with these parameters is the name of the global attribute. No defaults are provided, and no global attributes are required by this syntax. The CAA requires metadata as specified in the CAA Metadata Dictionary, CAA-CDPP-TN-0002.
   The Global attribute block starts with a line
   START META = name
   and ends with the line
   END META = name
   where the value name is the name of the global attribute. The name is not restricted to the Global Attributes used by CSDS for the Prime and Summary Parameter files. Specification of a named metadata block implies creation of metadata with that name. This name is case insensitive. The global metadata block contains the following entries:

ENTRY- The value associated with this entry is the next entry in the global attribute. Space characters are valid within a text entry, and text entries must be enclosed in double quotes. This parameter may be repeated, with each successive value providing the next entry in the attribute.

VALUE TYPE- The VALUE TYPE of a global attribute may be used to convert the ascii text entry in each ENTRY into the appropriate type of the value in the data structure. The default value for each global metadata block independently is text. This parameter allows changing of type for each subsequent ENTRY within a block until reset with another VALUE TYPE parameter, or the end of the attribute block is reached. Allowed values are:
- ISO TIME
- FLOAT
- DOUBLE
- INT
- CHAR
- BYTE
- ISO standard date/time strings are used in the same format as used in data records.

2. Variable Metadata-
   Blocks of information describing the variables start with a line
   START VARIABLE = name
   and end with the line
   END VARIABLE = name
   where the value name is the name to be used for the variable. The variable name is not in quotes. These blocks are required for variable description and headers are not valid without one describing each variable. Variable entries must appear within the header in the same order as the variable themselves within each data record. Variable names are case sensitive, and are an exception to the usual rule of case insensitivity.
   
   2.1 Mandatory Variable Metadata-
   These metadata provide formatting information specific to the named variable. There is no preferred order for parameters within a variable metadata block.
   Each block of variable metadata takes the form,
   START VARIABLE = name
   parameter = value
   .
   .
   END VARIABLE = name
   Where data in science units are provided it is required that metadata sufficient to describe that data for science use is provided. The following metadata are
   required whenever meaningful.
   VALUE TYPE This identifies the data type and is necessary for conversion from the ascii
   entry. Allowed values are:
   ISO TIME
   FLOAT
   DOUBLE
   
   INT
   CHAR
   BYTE
   SIZES This is essential for any variable that has more than one element, such as arrays and vectors. The value string must comprise as many comma-separated integer values as there are array indices in the variable with the number giving the size of the array over that index. Thus an 8 by 54 array would have the entry
   SIZES = 8,54
   It is not required for scalars.
   DATA The concept of a variable that is fixed for all records is supported for cef files. Data for these ‘non-record-varying’ variables must be supplied within the header variable metadata segment, and no entry is then allowed in the data records. The presence of a parameter ‘DATA’ will be taken to indicate that this is a non-record-varying variable. The value(s) associated with this parameter are the data for that variable. These are particularly useful for label variables. They are comma separated. For array data elements will appear in the natural C ordering - last index varies fastest, and data lines for arrays may be continued using ‘\’ as a continuation marker following one of the commas separating the list of values.
   REPRESENTATION i This is a rigorous generalisation of the ISTP FRAME attribute for
   CAA, and allowed values are enumerated in the Metadata Dictionary, CAA-CDPP-TN0002. It is only used for tensor types (vectors and tensors). There are as many of these attributes as there are indices i in the tensor. A vector takes only REPRESENTATION 1. This should have the same number of entries as the dimension of index i. For example, a cartesian pressure tensor takes
   REPRESENTATION 1 = "x", "y", "z"
   REPRESENTATION 2 = "x", "y", "z"
   indicating that the components are
   "Pxx","Pxy","Pxz","Pyx","Pyy","Pyz","Pzx","Pzy","Pzz"
   A complete tensor in real 3-space will have three components in each index. An incomplete tensor may be specified where the dimension of one or more indices are less than three. For example a vector measured in the xy-plane will have
   REPRESENTATION 1 = "x", "y"
   and this in turn implies it may be rotated in the xy-plane but not around any other axis. This will often duplicate LABEL i, and is provided distinctly as it identifes TENSOR type data explicitly, and this has science processing connotations - ability to rotate, for example.
   TENSOR ORDER This is the number of indices for a tensor data type. Vectors have rank 1.
   SI CONVERSION Required for all data in science units. Text string of the form
   number>SI unit
   where number is the conversion factor to SI units. It is the factor that the variable must be multiplied by in order to turn it into SI units. The string SI unit is the standard unit that it converts to. For example the magnetic field for FGM may be in nT, and to convert to Tesla the value of “SI CONVERSION” should be ‘1.0e-9>T’. For compound units the grammar will be of a standard form: distinct unit dimensions will be separated by space characters and powers (signed) will be preceded by the carat, ∧. Non-dimensional qualifiers, which do not appear in the SI units list, are to be enclosed in braces ‘()’. For example, ‘m s∧−1’ or ‘(number electrons) m∧−3’. Similarly ‘(percent)’ and ‘(ratio)’ would provide user information on dimensionless quantities. Non-integer powers are permitted, e.g.‘Hz∧−0.5’. SI units should be one of:
   s second
   kg kilogram
   m metre
   Hz hertz
   A ampere
   K kelvin
   J joule
   V volt
   T tesla
   Pa pascal
   C coulomb
   H henry [needed for mu o]
   F farad [needed for eps o]
   W watt
   N newton
   ohm
   mho
   rad radian
   sr steradian
   degree [alternative angle measure, not SI, but convenient and often used].
   unitless [added for compliance with the MDD documentation, and used only when no units can
   be specified, e.g. Tpar/Tperp]
   FIELDNAM Name for the field, generally not as short as LABLAXIS
   LABLAXIS Short name suitable for labelling the data. The units need not be included as they are supplied separately in UNITS. In the case of vectors and arrays this will be the common stem applicable for all dimensions, for example, a cartesian velocity might have LABLAXIS “V” with the component specifiel by LABEL 1 (see below). 
   
   DEPEND i and LABEL i These contain information identifying the ith dimension in an array variable. Either one or the other of these attributes must exist for each index of an array, but never both. The LABEL i attribute is used when it is sufficient to provide a text label for each entry for this index. For example a vector such as a velocity in cartesian gse coordinates will take a LABEL 1 attribute such as
   LABEL 1 = "x", "y", "z" and the stem "V" is provided by the LABLAXIS (see above). Similarly, a pressure tensor in cartesians would have 
   
   LABEL 1 = "x", "y", "z"
   
   LABEL 2 = "x", "y", "z"
   and stem "P" provided by LABLAXIS. This permits construction of labels for individual components from the stem plus appropriate entry under LABEL i.
   
   By contrast, DEPEND i will normally point to another variable as it is used when arrays need descriptions that are more complex than labels. Vectors, tensors, and non-ordered arrays, such as Status have LABEL i attributes rather than DEPEND i. Quantities such as power spectra and particle spectra will require DEPEND i attributes to describe numerical quantities such as bin boundaries and other metadata describing the physical quantities associated with that array index (see below). DEPEND i attributes will in general take a LABLAXIS attribute themselves to provide a label stem for the numerical bin descriptions, but they do not normally require LABEL i or DEPEND i attributes themselves. 
   
   There must be as many of these parameters as there are entries in the Sizes value. Thus a 3-D array would require three parameters, DEPEND 1, DEPEND 2 and DEPEND 3 (or equivalently LABEL i for one or more of the indices). The variables identified may be either non-record-varying or supplied for each record to allow for changing bin boundaries such as variable energy sweeps. Each of the identified dimension variables must have a defining variable block in the header as normal. 
   
   Depend variables should be 1-D arrays of the same size as the dimension for that array index. Thus for an array with the first index varying over azimuthal angular bins, a Depend 1 variable describing these N azimuthal angular bins might point to a variable Dimension phi of size N, giving the centre of each bin. 
   
   Where DEPEND i is providing information on binning (e.g. angle, energy and frequency ranges) then DEPEND i will itself also have a DELTA PLUS and a DELTA MINUS attribute providing bin edge offsets. The lower bin boundary is given by the appropriate element in DEPEND i - DELTA MINUS and the upper boundary by DEPEND i + DELTA PLUS. The bin width is given by DELTA PLUS + DELTA MINUS.
   
   If binning is regular so that all bins have the same width then a single value may be provided for the DELTA attributes, otherwise they must each have the same number of entries, N, as the dimension of index i. Where bins are open ended, e.g. ”above 100MeV”, then either DEPEND i and DELTA PLUS (MINUS) should represent an estimate of the instrument responsiveness to give an effective location and width, or they should fit a logical progression from lower bins. Descriptive attributes should be provided to explain this to the user.
   
   The syntax does not permit the use of N+1 elements to describe a dimension of size N, even though this would be more efficient for uniform touching bins (i.e. just specifying the N+1 bin boundaries).
   
   Complex data values are represented by an extra dimension taking a LABEL i indicating either "Re" or "Im". If this is the last index then the real and imaginary parts of a value are successive entries in the record.
   
   DELTA PLUS and DELTA MINUS DEPEND i variables, including the time tags which are DEPEND 0 for the data, may have these. They describe the range over which the data are integrated, representative, etc, and locate the position of the time tag or value within this range. In the case of time, DELTA PLUS and DELTA MINUS are the number of seconds corresponding to the sampling interval or other representative time interval, given in seconds as a float. Alternatively, DELTA PLUS and DELTA MINUS for time variables could themselves be variables, e.g., if they are record-varying, in which case they require their own metadata. For an array of energies used as dependencies for array data, DELTA PLUS and DELTA MINUS used together with the energy value provide a complete description of the energy bin over which the measurement was made or is representative.
   
   It is also advisable to supply extra information to describe the relationships between the DEPEND variables with the parent variable, such as the method required to construct the volume of the bin. No syntax is prescribed for these parameters which should be text, but examples of possible descriptors are listed below.
   
   For some data it will be necessary to specify different area and volume factors depending on the slice to be taken through the data. Added parameters may be specified to cover any integration or processing factors appropriate.
   
   For example, consider a 2-D array of phase space densities calculated at centre energies Ei and starting polar angles and over a constant azimuthal angular range of 15◦. A suitable description parameter and described DEPEND variables could take the value
   
   DEPEND 1 = E
   and the variable E block would contain metadata
   DELTA PLUS = WE
   DELTA MINUS = WE
   
   where WE is another variable (or a single constant entry or a comma separated list of the right length) and
   
   DEPEND 2 = theta
   and the variable theta block would contain metadata
   DELTA PLUS = Wth
   DELTA MINUS = 0
   
   Other attributes may be defined to show the use of these form factors in calculating quantities associated with the binning, such as
   
   Theta Factor = "TFactor[j] is cos(theta[j])-cos(theta[j]+Wth[j])"
   Energy Factor = "EFactor[i] for volume is E[i]^2 *2*WE[i] + (2/3)WE[i]^3"
   Volume Factor = "V[i][j] = EFactor[i]*TFactor[j]* pi * 15/180"
   
   In this example the energy dimension is tagged by an array giving the mid energies for each energy bin, and another for the bin half-width. The extra attributes then describe constructing the volume element of the [i][j] element in the data array. Thus, if the data array is in partial densities, then the phase space density is found by dividing the data dn[i][j] by V[i][j]. (In practice, the partial density would probably be an integration in velocity and require converting from energy to velocity, with a different V[i][j].

For fixed bin widths of 100 eV, say, the subscript would be removed from the WE[i] in the above, and a separate WE variable would not be used.

2.2 Extra Metadata for Depend variables
Depend variables require the SIZES and VALUE TYPE parameters to be set, and should take the UNITS, SI CONVERSION and DATA parameters in the same way as a data variable. They should take a LABLAXIS attribute to provide labelling information specific to that index. A DELTA PLUS and DELTA MINUS attribute is also required to establish bin boundaries for DEPEND i.

Depend variables do not, themselves, take Depend variables to describe the arrays.
For example, an array whose first dimension is energy in 7 bins might have
DEPEND 1 = EnergyBins
and the associated variable, EnergyBins takes the form
START VARIABLE = EnergyBins
DELTA PLUS = 0.05
DELTA MINUS = 0.05
SCALING = “linear”
DATA = 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7
UNITS = “keV”
LABLAXIS = “E”
SI CONVERSION = “1.602e-16>J”
END VARIABLE = EnergyBins

2.3 Optional Variable Metadata
All CSDS variable attributes may be specified within the variable metadata block, but are not required. The following subset of the standard CSDS attributes are currently used by science tools and recommended.

CATDESC The ISTP Catdesc as used by, e.g., CSDS
SCALMIN Hint to plotting software giving the minimum for a plot scale
SCALMAX Hint to plotting software giving the maximum for a plot scale
FILLVAL Value to be treated as not physically meaningful, indicating a value which is missing or unavailable.
SCALETYP Takes a text value of linear, logarithmic or inhomogeneous as plotting hint
SIG DIGITS Gives the number of significant digits in the data measurement.

Other descriptive metadata in the same syntax may be supplied as deemed appropriate to describe the data adequately for scientific use.

**ERG**

The next task was to design what metadata and data variables are needed to well accommodate the  scientific data and metadata of each observation. As for the metadata, there has already existed  the standard metadata list released from the CDF 
website, called the International Solar-Terrestrial Physics/Inter-Agency Consultative Group (ISTP/IACG) CDF guidelines, which are suitable to  describe the general information on various data and observation. We adopted them as the base of  metadata for our data files and further sought to supplement them with some specific information necessary for actual data analyses. Naturally these data analysis-oriented metadata are different for different types of observational data. Thus we discussed what kind of information, parameter, description would be needed for each data and 
summarized them as the self-sufficient set of metadata which could be commonly used for each type of data. In contrast to the metadata, the design of data variables is more or less straightforward. Basically we designed data variables for CDF files 
as they were stored in the original data files. In addition to data quantities readily used for research, we included some engineering data associated with the instrument operation so that data users can use them to check the validity of the observed data to 
some degree by themselves. In the present paper, we show the typical set of metadata and data variables for ground magnetometer data in Tables 2a and 2b and for all sky image data in Tables 3a and 3b, respectively. As for radar data, the metadata/data variable set for the SuperDARN data has already been provided in a separate publication 8). Tables 2a and 2b show the metadata (also referred to as the global attributes in the CDF framework) and data variable lists, respectively, for 1-minute resolution geomagnetic field data of the 210MM magnetometer chain. The metadata set consists of the ISTP/IACG-standard metadata and those added by ERG-SC. The former are labeled with asterisks in Table 2a. They provide general information on the data set, such as the observation project name, brief description of the observation, 
instrument(s), data, and contact information of the PI. The data policy statement is stored in the “Rules_of_use” or “Text” attribute. The latter, namely, ERG-SC original metadata include more detailed information which is useful or further necessary for actual data analyses. For example, “Geographic_latitude”, “Geographic_longitude”, 
and “Elevation” provide the exact location of a magnetometer and data users can easily know the location in geomagnetic coordinates by referring to “Geomagnetic_latitude”, “Geomagnetic_longitude”, and “L_value”. We also added “Data_sampling_type” and “Time_calibration_method” so that users can know how the raw data were sampled and averaged and how accurate the given time labels for observed data are. “Known_problem” provides a quick summary about, for instance, unavailable time periods, data caveats, and other problems on data to be shared with users. These metadata sets have been used commonly for CDF data files of the 210MM, STEL magnetometer, and MAGDAS data. 

| Attribute Name                                                                                                                                                 | Description                                                                                                                                   |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Project*                                                                                                                                                       | Name of the project holding the ownership of data. "210 MM Magnetic Observation" is set.                                                      |
| Discipline*                                                                                                                                                    | Science discipline/subdiscipline in the ISTP/IACG standards. "Space Physics>Magnetospheric Science" is set.                                   |
| Source_name*                                                                                                                                                   | Name of the mission or investigation under which data are obtained.                                                                           |
| Data_type*                                                                                                                                                     | Type of the data in CDF file. "1min>1 min Resolution" is set.                                                                                 |
| Descriptor*                                                                                                                                                    | Name of instrument that collects data. "210MM>210 Magnetic Meridian Ground-Based Magnetometer Network" is set.                                |
| Data_version*                                                                                                                                                  | Version number of data stored in CDF file.                                                                                                    |
| Title*                                                                                                                                                         | Title for the data set. "210 MM Ground-Based Magnetometer Network 1 min Resolution Data" is set.                                              |
| Text*                                                                                                                                                          | Description for the data set.                                                                                                                 |
| Generated_by*                                                                                                                                                  | The generating data center/group. "Solar-Terrestrial Environment Laboratory, Nagoya University" is set.                                       |
| Generation_date*                                                                                                                                               | Date on which a data file was created.                                                                                                        |
| Mods*                                                                                                                                                          | The history of modifications made to the CDF data set.                                                                                        |
| ADID_ref*                                                                                                                                                      | The control authority identifier, currently being left blank.                                                                                 |
| Logical_file_id*                                                                                                                                               | Name of the CDF file using the ISTP naming convention. "MM210_1MIN_(STN)_                                                                     |
| (YYYYMMDD)_V(??)" is set. STN is 3-letter station code, YYYYMMDD is the date in the 8-digit format, and "??" corresponds to the version number of a data file. |                                                                                                                                               |
| Logical_source*                                                                                                                                                | Source_name, data_type, and descriptor information, originally used by NASA/CDAWeb. "MM210_1MIN_(STN)" is set.                                |
| Logical_source_description*                                                                                                                                    | The full words associated with the Logical_source.                                                                                            |
| PI_name*                                                                                                                                                       | Name of the principal investigator (PI) of an instrument.                                                                                     |
| PI_affiliation*                                                                                                                                                | Affiliations of the PI.                                                                                                                       |
| Mission_group*                                                                                                                                                 | Data source name originally used in NASA/CDAWeb. "210MM" is set.                                                                              |
| Instrument_type*                                                                                                                                               | Type of instrument generating the data set. Following the CDAWeb naming convection, "Ground-Based Magnetometers, Riometers, Sounders" is set. |
| Rules_of_use*                                                                                                                                                  | Rules of the road on using the data is set.                                                                                                   |
| Link_text*                                                                                                                                                     | Text describing on-line data available at PI or Co-Investigator (CoI) web sites, to be combined with the following two attributes.            |
| Link_title*                                                                                                                                                    | Title of the PI or CoI website.                                                                                                               |
| Http_link*                                                                                                                                                     | URL of the PI or CoI websites.                                                                                                                |
| Time_resolution*                                                                                                                                               | Typical time resolution of the data set.                                                                                                      |

**PRBEM**

Global attributes 
Global attributes are used to provide information about the data set as an entity. Together with variables and variable attributes, the global attributes make the data correctly and independently usable by someone not connected with the instrument team, and hence, a good archive product. The global attributes can also be used by any software, one popular example being the CDAWeb Display and Retrieval system (http://cdaweb.gsfc.nasa.gov/cdaweb/). A list of global attributes is provided below, note that it is not limited, one can decide to add more global attributes if needed for his own applications.

Acknowledgement--- (recommended) 
Text string at PI disposal allowing for information on expected acknowledgment if data is citable.

ADID_ref --- (recommended) 
This attribute stores the control authority identifier associated with the detached SFDU label. If no control authority identifier has been assigned, then the identifier associated with the ISTP/IACG Guidelines (NSSD0241) or with CDF (NSSD0110) can be used. 

Data_type --- (required) 
This attribute identifies the data type of the CDF data set. Both a long name and a short name are given. For ISTP exchangeable data products the values are "Kn>Key Parameter" for approximately minute averaged survey data, and "Hn>High Resolution data" for certified data of higher resolution than Key Parameters.$n$ can run from 0 to 9 to allow for more than one kind of data product. For Cluster/CSDS this can either be "SP>Summary Parameter" or "PP>Prime Parameter". Other possible data types may be defined in future. If any of these data sets are modified or used to produce derived products, the data type should be, e.g., "Mn>Modified Data n", where n is from 0 to 9. 

Data_version --- (required) 
This attribute identifies the version of a particular CDF data file for a given date, e.g., the file POLAR_H0_CEPPAD_19960923_V01 is the first version of data for 1996 September 23. Each time this particular data file is reproduced - for recalibration or other reasons - the Data_version is incremented by 1. Data_version always starts at `1'. 

Descriptor --- (required) 
This attribute identifies the name of the instrument or sensor that collected the data. Both a long name and a short name are given. An example for ISTP is "EPI>Energetic Particles and Ion Composition". The short name should be limited to from 2 to 4 characters for consistency with ISTP. This attribute should be single valued. 

Discipline --- (required) 
This attribute describes both the science discipline and subdiscipline. More than one entry is allowed. The list for space physics is: 
- "Space Physics>Magnetospheric Science" 
- "Space Physics>Interplanetary Studies" 

Generated_by --- (recommended) 
This attribute allows for the generating data center/group to be identified. 

Generated_with_software – (recommended) 
This attribute describes the software and its version being used for processing the data as well as the library and its version for computing magnetic coordinates (e.g. IRBEM-SVN 231) 

Generation_date --- (recommended) 
Date stamps the creation of the file using the syntax yyyymmdd, e.g., "19920923". This is distinct from the date in "validate" below which records the times of later validation processes. 

HTTP_LINK, LINK_TEXT and LINK_TITLE --- (recommended)

This attribute stores the URL for the PI or CoI web site holding on-line data. This attribute is used in conjunction with "LINK_TEXT" and "LINK_TITLE". There can be up to 5 entries for each - there MUST be a corresponding entry of "LINK_TEXT" and "LINK_TITLE" for each "HTTP_LINK" entry. As an example CDAWeb will then link to the URL given by "HTTP_LINK" using the "LINK_TITLE" and the description in "LINK_TEXT", on the CDAWeb Data Explorer page. For example 
- "LINK_TEXT" = 3-sec MGF magnetic field 1 Sep 1993 through 30 Sep 1997  
- "LINK_TITLE" = ISAS DARTS 
- "HTTP_LINK" = http://www.darts.isas.ac.jp/spdb/index.html 

will give the following link: 
3-sec MGF magnetic field 1 Sep 1993 through 30 Sep 1997 available at ISAS DARTS 

Instrument_type --- (required) 
This attribute is used to facilitate making choices of instrument type. More than one entry is allowed. The following list contains the valid values. 
• Particles (space) 
• Plasma and Solar Wind 

Logical_file_id --- (required) 
This attribute stores the name of the CDF file using the ISTP naming convention 
(source_name / data_type / descriptor / date / data_version), e.g., 
POLAR_H0_CEPPAD_19960923_V01. This attribute is required (1) to allow storage of the 
full name on IBM PCs, and (2) to avoid loss of the original source in the case of accidental (or intentional) renaming. For CDFs created on the ISTP CDHF, the correct Logical_file_id will be filled in by an ICSS support routine. 

Logical_source --- (required) 
This attribute carries source_name, data_type, and descriptor information. 

Logical_source_description --- (required) 
This attribute writes out the full words associated with the encrypted Logical_source above, e.g., "POLAR CEPPAD High resolution particle data". 

Mission_group --- (required) 
This attribute has a single value and is used to facilitate making choices of source. Valid 
values include (but are not restricted to): 
• Geotail 
• IMP8 
• Wind 
• Geosynchronous Investigations 

MODS --- (recommended) 
This attribute is an NSSDC standard global attribute which is used to denote the history of modifications made to the CDF data set. The MODS attribute should contain a description of all significant changes to the data set. This attribute is not directly tied to Data_version, but each version produced will contain the relevant modifications. This attribute can have as many entries as necessary to contain the desired information. 

Parents --- (optional) 
This attribute lists the parent CDF(S) for files of derived and merged data sets. Subsequent entry values are used for multiple parents. The syntax for a CDF parent would be e.g. "CDF>logical_file_id". 

PI_affiliation --- (required) 
This attribute value should include a recognizable abbreviation. 

PI_name --- (required) 
This attribute value should include first initial and last name. 

Planet --- (recommended) 
This attribute value indicate from which planet the data are (e.g. "Earth" or "Jupiter"). 

Project --- (required) 
This attribute identifies the name of the project and indicates ownership. For ISTP missions and investigations, the value used is "ISTP>International Solar-Terrestrial Physics". For the Cluster mission, the value is "STSP Cluster>Solar Terrestrial Science Programmes, Cluster". 

Rules_of_use --- (recommended) 
Text containing information on, e.g. citability and PI access restrictions. This may point to a World Wide Web page specifying the rules of use. 

Skeleton_version --- (optional) 
This is a text attribute containing the skeleton file version number. This is a required attribute for Cluster, but for IACG purposes it exists if experimenters want to track it. 

Software_version --- (optional) 
This is a required attribute for Cluster, but for IACG purposes it exists if experimenters want to track it. 

Source_name --- (required) 
This attribute identifies the mission or investigation that contains the sensors. For ISTP, this is the mission name for spacecraft missions or the investigation name for ground-based or theory investigations. Both a long name and a short name are provided. This attribute should be single valued. Examples: 
- "GEOTAIL>Geomagnetic Tail" 
- "WIND>Wind Interplanetary Plasma Laboratory" 
- "GOES_7>Geostationary Operational Environmental Satellite 7" 
- "IMP-8>Interplanetary Monitoring Platform" 
- "LANL1989_046>Los Alamos National Laboratory 1989" 
- "C1>Cluster Satellite No 1". 

TEXT --- (required)
This attribute is an NSSDC standard global attribute which is a text description of the 
experiment whose data is included in the CDF. A reference to a journal article(s) or to a 
World Wide Web page describing the experiment is essential, and constitutes the minimum requirement. A written description of the data set is also desirable. This attribute can have as many entries as necessary to contain the desired information. 

Time_resolution --- (required) 
specifies time resolution of the file in seconds, e.g., "3 seconds". 

TITLE --- (optional) 
This attribute is an NSSDC standard global attribute which is a title for the data set, e.g., " POLAR CEPPAD High Resolution Data". 

Validate --- (optional) 
Details to be specified. This attribute is written by software for automatic validation of 
features such as the structure of the CDF file on a simple pass/fail criterion. The software will test that all expected attributes are present and, where possible, have reasonable values. The syntax is likely to be of the form "test>result>where-done>date". It is not the same as data validation. 

Variables- 
In this section we define data variables, support_data variables, and metadata variables including their dimensionality and what is needed for their correct display. The list of variables is provided below, note that one can decide to add more variables if needed for particular data sets or applications (e.g., housekeeking). We have identified three types of variables to be included in ISTP/IACG CDF files: data variables of primary importance (e.g., particle_flux), support_data variables of secondary importance (e.g., time, energy_bands associated with particle_flux) and metadata variables (e.g., a variable holding "xGEO,yGEO,xGEO" to label spacecraft position). Variables are defined with CDF specifications and required attributes. Data variables also have attached variables for time and dependencies (support_data) and labels (metadata). The support_data variables can be attached to data variables via DEPEND_i variable attributes. Metadata variables can be attached to data variables via LABL_PTR_i variable attributes (see below). NOTE: ISTP/IACG now encourages the use of zVariables which carry their own dimensionality. The complete variable description is provided next. 

Data- 
These are variables of primary importance (e.g., particle_count_rates). Data variables are completely defined with the combination of CDF specifications, variable attributes, and attached variables such as time and dependencies (support_data) and labels (metadata).

One of the goals of these guidelines is to use the same variable names across spacecraft/instruments to ease data exchange and software development. Note that having the same data type throughout all spacecraft/instrument is highly recommended, i.e. all real variables are CDF_REAL4 and all integer variables are CDF_INT2. This variable types guarantee enough precision for the quantities stored in the cdf files. The following CDF variable specifications are required. Data is always either Real or Integer type. Data is always time (record) varying, but can be of 
any dimensionality. Real or Integer data are always defined as having one element. In order to not make huge files, requiring large data space or large memory we suggest using only REAL4 and INT2 data type. This provides enough precision for particle measurements and associated geographic and magnetic parameters. 
The following variable attributes are required: 
- AVG_TYPE 
- CATDESC (see http://spdf.gsfc.nasa.gov/istp_guide/vattributes.html#CATDESC)
- DEPEND_0 = Epoch 
- DEPEND_i 
- DICT_KEY 
- DISPLAY_TYPE (time_series, spectrogram, stack_plot,image) 
- FIELDNAM 
- FILLVAL 
- FORMAT/FORM_PTR 
- LABLAXIS/LABL_PTR_i 
- UNITS/UNIT_PTR 
- VALIDMIN 
- VALIDMAX 
- VAR_TYPE = data 
- RESPONSE_FUNCTION (provides the cdf file where the response function for each count rates can be found at, assuming it is in the same directory as the count rates cdf files are). 

The need for DEPEND_i (other than DEPEND_0) and either LABLAXIS or LABL_PTR_i depends on the data itself and how it will be displayed. The following variable attributes are recommended: 
• SCALETYP (linear or log)

• VAR_NOTES

**Solar Orbiter**

Global attributes-
Global attributes are used to provide information about the data set as an entity. Global attributes for Solar Orbiter CDF data sets are 
divided into 4 categories:
- Attributes defined by the ISTP (http://spdf.gsfc.nasa.gov/sp_use_of_cdf.html)
- Attributes associated to the Space Physics Archive Search and Extract dictionary (SPASE, http://www.spase-group.org/)
- Attributes derived from the Virtual European Solar and Planetary Access dictionary (VESPA, http://voparis-europlanetnew.obspm.fr/planetary/data/epn/query/all/)
- Additional attributes specific to Solar Orbiter CDF data sets.

ISTP attributes
The following table provides the list of ISTP global attributes that should be used for Solar Orbiter CDF data sets.

| Name                       | Description                                                                                                                                                                                                                                                              | Type | Default Value                          | Comment                                                                                                                                                                                                                              |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---- | -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Project                    | The name of the project.                                                                                                                                                                                                                                                 | M    | “SOLO>Solar Orbiter”                   | It can allow more than one entry                                                                                                                                                                                                     |
| Source_name                | The mission or investigation that contains the sensors. It shall use the ISTP format "PREFIX>Suffix" (e.g., "SOLO>Solar Orbiter"), where the value of the prefix shall correspond to the "source" field in the file naming convention.                                   | M    | "SOLO>Solar Orbiter"                   |                                                                                                                                                                                                                                      |
| Discipline                 | The science discipline and subdiscipline.                                                                                                                                                                                                                                | M    | "Space Physics>Interplanetary Studies" |                                                                                                                                                                                                                                      |
| Data_type                  | ISTP defined exchangeable data product type.                                                                                                                                                                                                                             | M    |                                        | For Solar Orbiter This will be the same as the processing level of the data. See also http://spdf.gsfc.nasa.gov/istp_guide/gattributes.html#Data_type                                                                                |
| Descriptor                 | The name of the instrument and sensor or detector, separated by a hyphen, that collected the data. (e.g., “RPW-TDS>Radio and Plasma Waves, Time Domain Sampler”, "SWA>Solar Wind Analyzer", ...) It shall use the ISTP format "PREFIX>Suffix" (e.g., "MAG>Magnetometer") | M    |                                        | Note that the descriptor field in the file name is in fact the combination of the ISTP descriptor attribute and the Solar Orbiter data_product attribute                                                                             |
| Data_version               | This attribute identifies the version of a particular CDF data file for a given date. The value of the version shall be consistent with the "version" field in the filename.                                                                                             | M    |                                        | It shall be an integer increment starting at 01                                                                                                                                                                                      |
| Software_version           | The version of the software that generated the CDF.                                                                                                                                                                                                                      | P    |                                        |                                                                                                                                                                                                                                      |
| Skeleton_version           | The skeleton file version number.                                                                                                                                                                                                                                        | O    |                                        | It shall be an integer increment starting at 01.                                                                                                                                                                                     |
| PI_name                    | First initial and last name of the PI.                                                                                                                                                                                                                                   | M    |                                        | e.g., "M.Maksimovic"                                                                                                                                                                                                                 |
| PI_affiliation             | A recognizable abbreviation of the PI affiliation.                                                                                                                                                                                                                       | M    |                                        | e.g., "LESIA, Observatoire de Paris-CNRS".                                                                                                                                                                                           |
| TEXT                       | Description of the experiment.                                                                                                                                                                                                                                           | M    |                                        | It shall be used to describe the instrument and to provide references. The first entry shall be reserved for the description, followed by as many entries as references. Reference entries shall be sorted by decreasing importance. |
| Instrument_type            | The ISTP defined instrument type. Multi-valued.                                                                                                                                                                                                                          | M    |                                        | See http://spdf.gsfc.nasa.gov/istp_guide/gattributes.html#Instrument_type                                                                                                                                                            |
| Mission_group              | The assigned name of the mission or project.                                                                                                                                                                                                                             | M    | “Solar Orbiter"                        |                                                                                                                                                                                                                                      |
| Logical_source             | Source_name, data_type, and descriptor information.                                                                                                                                                                                                                      | M    |                                        | See http://spdf.gsfc.nasa.gov/istp_guide/gattributes.html#Logical_source                                                                                                                                                             |
| Logical_file_id            | The name of the CDF file using the ISTP naming convention.                                                                                                                                                                                                               | M    |                                        | See http://spdf.gsfc.nasa.gov/istp_guide/gattributes.html#Logical_file_id                                                                                                                                                            |
| Logical_source_description | Full words associated with the Logical_source.                                                                                                                                                                                                                           | M    |                                        | See http://spdf.gsfc.nasa.gov/istp_guide/gattributes.html#Logical_source_description                                                                                                                                                 |
| File_naming_convention     | Description of the file naming convention.                                                                                                                                                                                                                               | O    |                                        | It shall be consistent with the file naming convention                                                                                                                                                                               |
| Rules_of_use               | Citability and PI access restrictions. This may point to a World Wide Web page specifying the rules of use.                                                                                                                                                              | M    |                                        |                                                                                                                                                                                                                                      |
| Generated_by               | The generating data center/group.                                                                                                                                                                                                                                        | M    |                                        | The name of the Institute that produce the data file. (TBC)                                                                                                                                                                          |
| Generation_date            | Date stamp for the creation of the file.                                                                                                                                                                                                                                 | M    |                                        | It shall be the data file creation date in ISO8601 format ("YYYY-MMDDTHH:MN:SS") (TBC)                                                                                                                                               |
| Acknowledgement            | Text string at PI disposal allowing for information on expected acknowledgment if data is citable.                                                                                                                                                                       | M    |                                        |                                                                                                                                                                                                                                      |
| MODS                       | History of modifications made to the CDF data set.                                                                                                                                                                                                                       | P    |                                        | A new entry shall be added each time a modification is made to the CDF data set. Each entry has to specify the date of the modifications, the person responsible and a summary of the changes. (TBC)                                 |
| LINK_TEXT                  | Text describing on-line data available at PI or Co-I web sites.                                                                                                                                                                                                          | O    |                                        | TBD                                                                                                                                                                                                                                  |
| LINK_TITLE                 | The title of the web site holding on-line data available at PI or Co- I web sites.                                                                                                                                                                                       | O    |                                        | TBD                                                                                                                                                                                                                                  |
| HTTP_LINK                  | The URL for the PI or Co-I web site holding on-line data.                                                                                                                                                                                                                | P    |                                        | TBD                                                                                                                                                                                                                                  |
| TEXT_supplement_1          | An attribute that can be used for providing additional information about dataset.                                                                                                                                                                                        | O    |                                        |                                                                                                                                                                                                                                      |
| Parents                    | This attribute lists the parent CDF(S) for files of derived and merged data sets. Subsequent entry values are used for multiple parents. The syntax for a CDF parent would be e.g.                                                                                       |      |                                        |                                                                                                                                                                                                                                      |
| "CDF>logical_file_id"      | O                                                                                                                                                                                                                                                                        |      |                                        |                                                                                                                                                                                                                                      |
