

Multi-Mission Use of Attributes

|                                       | Description                                                                                             | Examples                                                | ISTP/IACG    | Cluster | ERG | GOLD | ICON | MMS | PSP | PRBEM | RBSP (Van Allen Probes) | Solar Orbiter |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- | ------------ | ------- | --- | ---- | ---- | --- | --- | ----- | ----------------------- | ------------- |
| **Global Attribute**                  |                                                                                                         |                                                         |              |         |     |      |      |     |     |       |                         |               |
| Data_Type                             | Identifies the data type of the CDF data set                                                            | { "K0>Key Parameter" }.                                 | M            | M       | M   | M    | M    |     |     | M     |                         | M             |
| Data_Version                          | Identifies the version of a particular CDF data file for a given date                                   | { "1" }.                                                | M            |         | M   | M    | M    |     |     | M     |                         | M             |
| Descriptor                            | Identifies name of the instrument or sensor that collected the data                                     | { "EPI>Energetic Particles" -"and Ion Composition" }.   | M            |         | M   |      | M    |     |     | M     |                         | M             |
| Discipline                            | Describes both science discipline and subdiscipline                                                     | { "Space Physics>Magnetospheric Science" }.             | M            |         | M   | M    | M    |     |     | M     |                         | M             |
| Instrument_Type                       | Used to facilitate making choices of instrument type                                                    | { "Magnetic Fields (space)" }.                          | M            | M       | M   | M    | M    |     |     | M     |                         | M             |
| Logical_File_ID                       | Stores name of the CDF file using the ISTP naming convention                                            | { "GE_K0_EPI_19920908_V01" }.                           | M            | M       | M   | M    | M    |     |     | M     |                         | M             |
| Logical_Source                        | Carries source_name, data_type, and descriptor information                                              | { "GE_K0_EPI" }.                                        | M            |         | M   | M    | M    |     |     | M     |                         | M             |
| Logical_Source_Description            | Writes out full words associated with encrypted Logical_source                                          | { "Geotail Magnetic Field Key Parameters" }.            | M            |         | M   | M    | M    |     |     | M     |                         | M             |
| Mission_Group                         | Has a single value and is used to facilitate making choices of source through CDAWeb                    | { "Geotail" }.                                          | M            |         | M   | M    | M    |     |     | M     |                         | M             |
| PI_Affiliation                        | Should include a recognizable abbreviation                                                              | { "JHU/APL" }.                                          | M            |         | M   | M    | M    |     |     | M     |                         | M             |
| PI_Name                               | Should include first initial and last name                                                              | { "D. Williams" }.                                      | M            |         | M   | M    | M    |     |     | M     |                         | M             |
| Project                               | Identifies project name and indicates ownership                                                         | { "ISTP>International" - "Solar-Terrestrial Physics" }. | M            |         | M   | M    | M    |     |     | M     |                         | M             |
| Source_Name                           | Identifies mission or investigation that contains the sensors                                           | { "GEOTAIL>Geomagnetic Tail" }.                         | M            |         | M   | M    | M    |     |     | M     |                         | M             |
| TEXT                                  | A text description of the experiment whose data is included in the CDF                                  | { "reference to journal article, URL address" }.        | M            |         | M   | M    | M    |     |     | M     |                         | M             |
| Acknowledgement | Text string at PI disposal                                                                              |                                                         | R            | M       |     |      | M    |     |     | R     |                         | M             |
| Generated_By                          | Allows for generating data center/group to be identified                                                |                                                         | R            |         | M   | M    | M    |     |     | R     |                         | M             |
| Generation_Date                       | Date stamps the creation of the file                                                                    |                                                         | R            | M       | M   |      | M    |     |     | R     |                         | M             |
| HTTP_LINK                             | Stores URL for the PI or CoI web site holding on-line data                                              |                                                         | R            |         |     | M    | M    |     |     | R     |                         | M             |
| Link_Text                             | Stores text describing on-line data available at PI or CoI web sites                                    |                                                         | R            |         | M   | M    | M    |     |     | R     |                         | M             |
| Link_Title                            | Stores title of the web site holding on-line data available at PI or CoI web sites                      |                                                         | R            |         | M   | M    | M    |     |     | R     |                         | M             |
| MODS                                  | An NSSDC standard global attribute used to denote the history of modifications made to the CDF data set |                                                         | R            |         | M   |      | M    |     |     | R     |                         | M             |
| Rules_of_use                          | Text containing information on citability and PI access restrictions                                    |                                                         | R            |         | M   | M    | M    |     |     | R     |                         | M             |
| Time_Resolution                       | Specifies time resolution of the file                                                                   |                                                         | R            | M       |     |      | M    |     |     | M     |                         |               |
| TITLE                                 | An NSSDC standard global attribute which is a title for the data set                                    |                                                         | O            |         | M   | M    | M    |     |     | O     |                         |               |
| Validate                              | Written by software for automatic validation of features                                                |                                                         | O            |         |     |      |      |     |     | O     |                         |               |
| Software_Version                      | Exists if experimenters want to track it                                                                |                                                         | O            |         |     | M    | M    |     |     | O     |                         | M             |
| Skeleton_Version                      | Contains the skeleton file version number                                                               |                                                         | O            |         |     |      |      |     |     | O     |                         | M             |
| Parents                               | Lists parent CDF(S) for files of derived and merged data sets                                           |                                                         | O            |         |     |      | M    |     |     | O     |                         | M             |
| ADID_ref                              | Stores the control authority identifier                                                                 |                                                         | Not relevant |         | M   |      | M    |     |     | R     |                         |               |

|                        | Description                                                                        | Examples                                                              | ISTP/IACG | Cluster | ERG | GOLD | ICON | MMS | PSP | PRBEM | RBSP (Van Allen Probes) | Solar Orbiter |
| ---------------------- | ---------------------------------------------------------------------------------- | --------------------------------------------------------------------- | --------- | ------- | --- | ---- | ---- | --- | --- | ----- | ----------------------- | ------------- |
| **Variable Attribute** |                                                                                    |                                                                       |           |         |     |      |      |     |     |       |                         |               |
| CATDESC                | A textual description of the variable                                              | { "Ion Diff. Intensity, at 12 energies " - "67-1361 keV (EPIC/ICS)" } | M         | M       |     |      |      | M   | M   |       | M                       |               |
| DEPEND_0               | Ties a data variable to the time variable on which it depends                      | { "Epoch" }                                                           | M         |         |     |      |      | M   |     |       | M                       |               |
| DISPLAYTYPE            | Tells automated software what type of plot to make                                 | { "spectrogram" }                                                     | M         | M       |     |      |      |     |     |       | M                       |               |
| FIELDNAM               | Holds a character string which describes the variable                              | { "Spin-avg Ion Diff Inten (EPIC/ICS)" }                              | M         | M       |     |      |      | M   |     |       | M                       |               |
| FILLVAL                | Number inserted in CDF in place of data values known to be bad or missing          | { -1.000000e+31 }                                                     | M         | M       |     |      |      | M   |     |       | M                       |               |
| FORMAT                 | Output format used when extracting data values out to a file or screen             |                                                                       | M         |         |     |      |      | M   |     |       | M                       |               |
| FORM_PTR               | Has as its value a variable which stores the character strings                     |                                                                       | M         |         |     |      |      | M   |     |       | M                       |               |
| UNITS                  | A character string representing units of the variable                              |                                                                       | M         |         |     |      |      |     | M   |       | M                       |               |
| UNIT_PTR               | Has as its value a variable which stores the character strings                     |                                                                       | M         |         |     |      |      |     | M   |       | M                       |               |
| VALIDMAX               | Maximum values for a particular variable expected over the lifetime of the mission |                                                                       | M         |         |     |      |      |     | M   |       | M                       |               |
| VALIDMIN               | Minimum values for a particular variable expected over the lifetime of the mission |                                                                       | M         |         |     |      |      |     | M   |       | M                       |               |
| VAR_TYPE               | Identifies a variable as either data, support_data, metadata or ignore_data        |                                                                       | M         |         |     |      |      | M   |     |       | M                       |               |
| VAR_NOTES              | Holds ancilliary information about the variable and can be any length              |                                                                       | O         |         |     |      |      |     | M   |       | M                       |               |
| DELTA_MINUS_VAR        | Points to a variable which stores uncertainty in original variable's value         | { "IDiffI_I_Uncert" }                                                 | O         | M       |     |      |      |     | M   |       | M                       |               |
| DELTA_PLUS_VAR         | Value of the attribute must be a variable in the same CDF data set                 | { "IDiffI_I_Uncert" }                                                 | O         | M       |     |      |      |     | M   |       | M                       |               |

Legend

M-Mandatory

R-Recommended

O-Optional

### Attribute Descriptions


### Acknowledgement

Text string at PI disposal allowing for information on expected acknowledgement if data is citable.

### ADID_ref

This attribute stores the control authority identifier associated with the detached SFDU label. If no control authority identifier has been assigned, then the identifier associated with the ISTP/IACG Guidelines (NSSD0241) or with CDF (NSSD0110) can be used.

### Calibration_File

The name of the calibration file used when generating this data.

### CATDESC

An approximately 80-character string which is a textual description of the variable and includes a description of what the variable depends on. This information needs to be complete enough that users can select variables of interest based only on this value.

### Conventions

This is standard for NetCDF files and is required for ICON.

### Data_Level

The data product level as specified in the DPID. This is required and should follow the format “L#.#”. 

### Data_Revision

The data revision normally gets incremented during reprocessing. 

### Data_Type

This attribute identifies the data type of the CDF data set. Both a long name and a short name are given. For ISTP exchangeable data products the values are "Kn>Key Parameter" for approximately minute averaged survey data, and "Hn>High Resolution data" for certified data of higher resolution than Key Parameters can run from 0 to 9 to allow for more than one kind of data product. For Cluster/CSDS this can either be "SP>Summary Parameter" or "PP>Prime Parameter". Other possible data types may be defined in future. If any of these data sets are modified or used to produce derived products, the data type should be, *e.g.,* "Mn>Modified Data n", where n is from 0 to 9.

### Data_Version

This attribute identifies the version of a particular CDF data file for a given date, *e.g.,* the file GE_K0_MGF_19920923_V01 is the first version of data for 1992 September 23. **Each time** this particular data file is reproduced - for recalibration or other reasons - the Data_version is incremented by 1. Data_version always starts at '1'.

### Data_VersionMajor

The major version normally only changes for a software change significant enough to alter the data format produced. The major version should be between 1 and 99 while the revision should be between 0 and 999 as shown below. 

### Date_End

The time of the last data point. 

### Date_Start

The time of the first data point. 

### DELTA_MINUS_VAR

Included to point to a variable (or variables) which stores the uncertainty in (or range of) the original variable's value. The uncertainty (or range) is stored as a (+/-) on the value of the original variable. For many variables in ISTP/IACG, the original variable will be at the center of the interval so that only one value (or one set of values) of uncertainty (or range) will need to be defined. In this case, DELTA_PLUS_VAR, and DELTA_MINUS_VAR will point to the same variable. The value of the attribute must be a variable in the same CDF data set.

### DELTA_PLUS_VAR

Included to point to a variable (or variables) which stores the uncertainty in (or range of) the original variable's value. The uncertainty (or range) is stored as a (+/-) on the value of the original variable. For many variables in ISTP/IACG, the original variable will be at the center of the interval so that only one value (or one set of values) of uncertainty (or range) will need to be defined. In this case, DELTA_PLUS_VAR, and DELTA_MINUS_VAR will point to the same variable. The value of the attribute must be a variable in the same CDF data set.

### DEPEND_0

Explicitly ties a data variable to the time variable on which it depends. All variables which change with time must have a DEPEND_0 attribute defined. The value of DEPEND_0 is *'Epoch'*, the time ordering parameter for ISTP/IACG. Different time resolution data can be supported in a single CDF data set by defining the variables Epoch, Epoch_1, Epoch_2, etc. each representing a different time resolution. These are "attached" appropriately to the variables in the CDF data set via the attribute DEPEND_0. **The value of the attribute must be a variable in the same CDF data set.**

### Description

A description of the data set which may be the same as the title attribute or contain extra information.

### Descriptor

This attribute identifies the name of the instrument or sensor that collected the data. Both a long name and a short name are given. An example for ISTP is "EPI>Energetic Particles and Ion Composition". The short name should be limited to from 2 to 4 characters for consistency with ISTP. This attribute should be single valued.

### Discipline

This attribute describes both the science discipline and subdiscipline. More than one entry is allowed. The list for space physics is:

- "Space Physics>Magnetospheric Science"
- `Space Physics>Interplanetary Studies"
- `Space Physics>Ionospheric Science"

### DISPLAYTYPE

Tells automated software what type of plot to make and what associated variables in the CDF are required in order to do so. Some valid values are listed below:

- time_series
- spectrogram
- stack_plot
- image
- no_plot

### FIELDNAM

Holds a character string (up to 30 characters) which describes the variable. It can be used to label a plot either above or below the axis, or can be used as a data listing heading. Therefore, consideration should be given to the use of upper and lower case letters where the appearance of the output plot or data listing heading will be affected.

### File

This is supplementary data indicating the expected full file name similar to the logical source name global attribute but including the extension.

### File_Date

Listed in UTC time.

### File_naming_convention

Description of the file naming convention.

### FILLVAL

The number inserted in the CDF in place of data values that are known to be bad or missing. Fill data are always non-valid data. The ISTP standard fill values are listed below. Fill values are automatically supplied in the ISTP CDHF ICSS environment (ICSS_KP_FILL_VALUES.INC) for key parameters produced at the CDHF. The FILLVAL data type must match the data type of the variable. For key parameters produced outside of the CDHF, the values below should be used.

- REAL*4 ---- -1.0E31
- REAL*8 ---- -1.0E31
- BYTE ---- -128
- INTEGER*2 ---- -32768
- INTEGER*4 ---- -2147483648
- Unsigned INTEGER*1 ---- 255
- Unsigned INTEGER*2 ---- 65535
- Unsigned INTEGER*4 ---- 4294967295
- Signed INTEGER*8 ---- -9223372036854775808LL

### FORMAT

The output format used when extracting data values out to a file or screen (using CDFlist). The magnitude and the number of significant figures needed should be carefully considered. A good check is to consider it with respect to the values of VALIDMIN and VALIDMAX attributes. The output should be in Fortran format.

### FORM_PTR

Has as its value a variable which stores the character strings (up to 20 characters per character string) representing the desired output format for the original variable. FORM_PTR is used instead of FORMAT. The value of the attribute must be a variable in the same CDF data set.

### Generated_By

This attribute allows for the generating data center/group to be identified.

### Generated_with_software

This attribute describes the software and its version being used for processing the data as well as the library and its version for computing magnetic coordinates.

### Generation_Date

Date stamps the creation of the file using the syntax yyyymmdd, *e.g.,* "19920923". This is distinct from the date in "validate" below which records the times of later validation processes.

### History

Recommended global attribute for NSSDC indicating file modification state. This should be duplicated in the NetCDF history. 

### HTTP_LINK

This attribute stores the URL for the PI or CoI web site holding on-line data. This attribute is used in conjunction with "LINK_TEXT" and "LINK_TITLE". There can be up to 5 entries for each - there MUST be a corresponding entry of "LINK_TEXT" and "LINK_TITLE" for each "HTTP_LINK" entry. CDAWeb will then link to the URL given by "HTTP_LINK" using the "LINK_TITLE" and the description in "LINK_TEXT", on the CDAWeb Data Explorer page.

### Instrument

This should exist for all data associated with a single instrument.

### Instrument_Type

This attribute is used to facilitate making choices of instrument type through [CDAWeb](https://cdaweb.gsfc.nasa.gov/istp_public/). More than one entry is allowed. The following list contains the valid values.

- Electric Fields (space)
- Ephemeris
- Imagers (space)
- Magnetic Fields (space)
- Particles (space)
- Plasma and Solar Wind
- Radio and Plasma Waves (space)
- Ground-Based HF-Radars
- Ground-Based Imagers
- Ground-Based Magnetometers, Riometers, Sounders
- Ground-Based VLF/ELF/ULF, Photometers

### Link_Text

This attribute stores text describing on-line data available at PI or CoI web sites. This attribute is used in conjunction with "LINK_TITLE" and "HTTP_LINK". There can be up to 5 entries for each - there MUST be a corresponding entry of "LINK_TITLE" and "HTTP_LINK" for each "LINK_TEXT" entry. CDAWeb will then link to the URL given by "HTTP_LINK" using the "LINK_TITLE" and the description in "LINK_TEXT", on the CDAWeb Data Explorer page.

### Link_Title

This attribute stores the title of the web site holding on-line data available at PI or CoI web sites. This attribute is used in conjunction with "LINK_TEXT" and "HTTP_LINK". There can be up to 5 entries for each - there MUST be a corresponding entry of "LINK_TEXT" and "HTTP_LINK" for each "LINK_TITLE" entry. CDAWeb will then link to the URL given by "HTTP_LINK" using the "LINK_TITLE" and the description in "LINK_TEXT", on the CDAWeb Data Explorer page.

### Logical_File_ID

This attribute stores the name of the CDF file using the ISTP naming convention (source_name / data_type / descriptor / date / data_version), *e.g.,* GE_K0_MGF_19920923_V01. This attribute is required (1) to allow storage of the full name on IBM PCs, and (2) to avoid loss of the original source in the case of accidental (or intentional) renaming. For CDFs created on the ISTP CDHF, the correct Logical_file_id will be filled in by an ICSS support routine.

### Logical_Source

This attribute carries source_name, data_type, and descriptor information. Used by [CDAWeb](https://cdaweb.gsfc.nasa.gov/istp_public/).

### Logical_Source_Description

This attribute writes out the full words associated with the encrypted Logical_source above, *e.g.,* "Geotail Magnetic Field Key Parameters". Used by [CDAWeb](https://cdaweb.gsfc.nasa.gov/istp_public/).

### Mission_Group

This attribute has a single value and is used to facilitate making choices of source through [CDAWeb](https://cdaweb.gsfc.nasa.gov/istp_public/). Valid values include (but are not restricted to) :

- Geotail
- IMP8
- Wind
- Geosynchronous Investigations
- Ground-Based Investigations

### MODS

This attribute is an NSSDC standard global attribute which is used to denote the history of modifications made to the CDF data set. The MODS attribute should contain a description of all significant changes to the data set. This attribute is not directly tied to Data_version, but each version produced will contain the relevant modifications. This attribute can have as many entries as necessary to contain the desired information.

### Parents

This attribute lists the parent CDF(S) for files of derived and merged data sets. Subsequent entry values are used for multiple parents. The syntax for a CDF parent would be *e.g.* "CDF>logical_file_id".

### PI_Affiliation

This attribute value should include a recognizable abbreviation.

### PI_Name

This attribute value should include first initial and last name.

### Planet

This attribute value indicate from which planet the data are from.

### Project

This attribute identifies the name of the project and indicates ownership. For ISTP missions and investigations, the value used is "ISTP>International Solar-Terrestrial Physics". For the Cluster mission, the value is "STSP Cluster>Solar Terrestrial Science Programmes, Cluster". Other acceptable values are "IACG>Inter-Agency Consultative Group", "CDAWxx>Coordinated Data Analysis Workshop xx", and "SPDS>Space Physics Data System". Others may be defined in future. This attribute can be multi-valued if the data has been supplied to more than one project.

### Rules_of_Use

Text containing information on {\it e.g.} citability and PI access restrictions. This may point to a World Wide Web page specifying the rules of use.

### Skeleton_version

This is a text attribute containing the skeleton file version number. This is a required attribute for Cluster, but for IACG purposes it exists if experimenters want to track it.

### Software_Version

This is a required attribute for Cluster, but for IACG purposes it exists if experimenters want to track it.

### Source_Name

This attribute identifies the mission or investigation that contains the sensors. For ISTP, this is the mission name for spacecraft missions or the investigation name for ground-based or theory investigations. Both a long name and a short name are provided. This attribute should be single valued.

### Spacecraft_ID

This must exist for all data files and is fixed for ICON. 

### TEXT

This attribute is an NSSDC standard global attribute which is a text description of the experiment whose data is included in the CDF. A reference to a journal article(s) or to a World Wide Web page describing the experiment is essential, and constitutes the minimum requirement. A written description of the data set is also desirable. This attribute can have as many entries as necessary to contain the desired information.

### Text_Supplement

Extra descriptive text.

### TEXT_Supplement_1

An attribute that can be used for providing additional information about a dataset.

### Time_Resolution

Specifies time resolution of the file, *e.g.,* "3 seconds".

### TITLE

This attribute is an NSSDC standard global attribute which is a title for the data set, *e.g.,* "Geotail EPIC Key Parameters".

### UNITS

A character string (no more than 20 characters, but preferably 6 characters) representing the units of the variable,*e.g.,* nT for magnetic field. If the standard abbreviation used is short then the units value can be added to a data listing heading or plot label. Use a blank character, rather than "None" or "unitless", for variables that have no units (e.g., a ratio or a direction cosine). For CDF_TIME_TT2000: SI measurement unit: s, ms(milliseconds for EPOCH variables), ns(nanoseconds for CDF_TIME_TT2000), ps(picoseconds for EPOCH16).

### UNIT_PTR

Has as its value a variable which stores the character strings (up to 20 characters per character string) representing the units of the original variable, which can be added to a data listing heading or plot label. Use a blank character, rather than "None" or "unitless", for variables that have no units (e.g., a ratio or a direction cosine). If this attribute is used, then UNITS is not used. **The value of the attribute must be a variable in the same CDF data set.**

### Validate

Details to be specified. This attribute is written by software for automatic validation of features such as the structure of the CDF file on a simple pass/fail criterion. The software will test that all expected attributes are present and, where possible, have reasonable values. The syntax is likely to be of the form "test>result>where-done>date". It is not the same as data validation.

### VALID_MAX

Hold values which are, respectively, the minimum and maximum values for a particular variable that are expected over the lifetime of the mission. The values must match the data type of the variable.

### VALID_MIN

Hold values which are, respectively, the minimum and maximum values for a particular variable that are expected over the lifetime of the mission. The values must match the data type of the variable.

### VAR_NOTES

Holds ancilliary information about the variable and can be any length.

### VAR_TYPE

Identifies a variable as either

- **data** integer or real numbers that are plottable
- **support_data** integer or real "attached" variables
- **metadata** (labels or character variables)
- **ignore_data** placeholders
