# ISTP Global Attributes

Global attributes are used to provide information about the dataset as an entity and about the individual files composing the datasets. Together with the variables and variable attributes, the global attributes make the data correctly and independently usable by someone not connected with the instrument team, and hence a good archive product. The global attributes are also used by the Coordinated Data Analysis Web ([CDAWeb)](https://cdaweb.gsfc.nasa.gov/) data browsing and retrieval system hosted by SPDF, and by other data display and analysis software such as [AutoPlot](https://autoplot.org) and [SPEDAS](https://spedas.org/). 

The required, recommended, and optional global attributes are listed in the table below. See [Global Attribute Definitions](#global-attribute-definitions) for the full set of defined global attributes in alphabetical order; however, note that global attributes in a file can be listed in any order. Also note that the attribute names are case sensitive, and the names of the ISTP global attributes must match the case **exactly as shown**. Additional global attributes may be defined, but their **names must start with a letter and contain letters, numbers, and underscore character but no other special characters.** Though attribute names are case-sensitive, the names must not be distinguished by case only.

All ISTP global attributes are of character data type (CDF_CHAR) in the CDF file format. Since the CDF format allows multiple entries for global attributes, with each ISTP global attribute entry being a 1-D array of CDF_CHAR (a string), this allows storing a 1-D array of strings in a global attribute. **Note** that these multiple entries for an ISTP global attribute in the CDF format correspond to a 1-D array of string data type in the **netCDF-4** format.

```{eval-rst}
.. tabularcolumns:: |\X{20}{100}|\X{15}{100}|\X{35}{100}|\X{30}{100}|
```

| **Attribute Name** | **Requirement** | **Example Value** | **Notes** |
| -------------- | ---------------------------- | -------- | --------- |
| [`Data_type`](#data_type) | **Required** | `"L2-Summary>level 2 summary"`  | Identifies the data type of the dataset. Both the short and long names, separated by `>`, are included. |
| [`Data_version`](#data_version) | **Required** |  `"1"` | Identifies the version of a particular data file. |
| [`Descriptor`](#descriptor) | **Required** |  `"ISOIS>Integrated Science Investigation of the Sun"` | Identifies both the short and long names, separated by `>`, of the instrument or sensor that collected the data. |
| [`Instrument_type`](#instrument_type) | **Recommended, required by CDAWeb** (allows multiple entries; five  entries allowed by **CDAWeb**)  | `"Particles (space)"` <br> `"Plasma and Solar Wind"` | Combines types of instruments and regions as a simple way to quickly separate types of datasets for search through [CDAWeb](https://cdaweb.gsfc.nasa.gov/). [CDAWeb](https://cdaweb.gsfc.nasa.gov/) allows up to five entries from **[`controlled list`](#instrument_type)** (two entries are shown in the example). |
| [`Logical_file_id`](#logical_file_id) | **Required** | `"psp_isois_l2-summary_20180928_v07"`  | Stores the name of the file using the ISTP naming convention `Source_name`\_`Descriptor`\_`Data_type`\_Date\_v`Data_version`, with short names for `Source_name`, `Descriptor`, and `Data_type`.  |
| [`Logical_source`](#logical_source) | **Required** | `"psp_isois_l2-summary"`  | Carries `Source_name`, `Descriptor`, and `Data_type` short names. Used by [CDAWeb](https://cdaweb.gsfc.nasa.gov/) as the dataset ID. |
| [`Logical_source_description`](#logical_source_description) | **Required** | `"Parker Solar Probe ISOIS level 2 summary"`  | Writes out the full names associated with the encrypted `Logical_source`. Used by [CDAWeb](https://cdaweb.gsfc.nasa.gov/) as the dataset full name.|
| [`Mission_group`](#mission_group) | **Recommended, required by CDAWeb** |  `"Parker Solar Probe (PSP)"` | Has a single value and is used to facilitate making choices of source through [CDAWeb](https://cdaweb.gsfc.nasa.gov/). |
| [`PI_affiliation`](#pi_affiliation) | **Required** |  `"Princeton University"` | Lead organization, usually that of the Principal Investigator (PI); should include a recognizable abbreviation. |
| [`PI_name`](#pi_name) | **Required** |  `"David McComas"` | Lead person, usually Principal Investigator (PI); should at least include first initial and last name. |
| [`Source_name`](#source_name) | **Required** | `"PSP>Parker Solar Probe"` | Identifies the mission or investigation that contains the sensors. Both the short and long names, separated by `>`, are included. |
| [`TEXT`](#text) | **Required** (allows multiple entries) | `"EPI-Hi HET 3600 second rates cdf. Time tags indicate midpoint of integration."`<br> `"Instrument paper: Integrated Science Investigation of the Sun (ISIS): Design of the Energetic Particle Investigation. McComas, D. J. et al (2016). Space Sci. Rev., doi:10.1007/s11214-014-0059-1"` | Contains description of the key measurements provided by the dataset. A short description of the experiment, with reference to a journal paper and/or web page describing the experiment in detail, is also essential. This attribute can have multiple entries (two entries are shown in the example). Used by [CDAWeb](https://cdaweb.gsfc.nasa.gov/) as the dataset description.|
| [`Date_Start`](#date_start-date_end) <br> (**netCDF only**) | **Required** | `"2025-11-01T00:00:00"` | Start UTC date/time (in yyyy-mm-ddThh:mm:ss format) of the data in the file.|
| [`Date_End`](#date_start-date_end)  <br> (**netCDF only**) | **Required** | `"2025-11-01T23:59:59"` | End UTC date/time (in yyyy-mm-ddThh:mm:ss format) of the data in the file. | |
| [`Acknowledgement`](#acknowledgement)  | **Recommended**  | `"Cite McComas et al (2016),doi:10.1007/s11214-014-0059-1"` | Specifies the expected acknowledgement text if the dataset is cited. |
| [`Discipline`](#discipline) | **Recommended** (allows multiple entries) | `"Solar Physics>Heliospheric Physics"`  | Describes both the science discipline and subdiscipline. This attribute allow multiple entries. |
| [`Data_processing_level`](#data_processing_level) (**PROPOSAL ONLY**)| **Recommended** | `"L2>Level 2"`  | Describes the dataset processing level. Both the short and long names, separated by `>`, are included.|
| [`DOI`](#doi) | **Recommended**  |  `"https://doi.org/10.48322/mede-7j02"`  | Digital Object Identifier (DOI) as a persistent identifier for the dataset. |
| [`File_naming_convention`](#file_naming_convention) | **Recommended**  |  `source_descriptor_datatype_yyyyMMdd`  | Describes the dataset file naming convention based on combination of `Source_name`, `Descriptor`, and `Data_type` attribute short names and a date/time format. |
| [`Generated_by`](#generated_by) | **Recommended**  | `"ISOIS SOC, University of New Hampshire"` | Allows for the generating data center/group to be identified. |
| [`Generation_date`](#generation_date) | **Recommended**  |  `"20210329"` | Date of the file creation using yyyymmdd format.  |
| [`HTTP_LINK`](#link_text-link_title-http_link) | **Recommended** (allows multiple entries; five  entries allowed by **CDAWeb**)  |  `"http://spp-isois.sr.unh.edu/ISOIS_Terms_of_Use.html"` <br> `"https://link.springer.com/article/10.1007%2Fs11214-014-0059-1"` <br> `"http://fields.ssl.berkeley.edu/"` <br> `"https://www2.mps.mpg.de/homes/fraenz/systems/"` <br> `"http://spp-isois.sr.unh.edu/data_public/ISOIS_Data_Glossary.pdf"` | Stores the URL for the link. Used with `LINK_TEXT` and `LINK_TITLE` attributes. This attribute allows multiple entries, with [CDAWeb](https://cdaweb.gsfc.nasa.gov/) allowing five entries (five entries are shown in the example). |
| [`LINK_TEXT`](#link_text-link_title-http_link) | **Recommended** (allows multiple entries; five  entries allowed by **CDAWeb**) | `"Data "` <br> `"Instrument paper at "` <br> `"Magnetic field data for pitch angle calculation courtesy of "` <br> `"Coordinate systems according to definitions of "` <br> `"Detailed information in "` | Stores the text describing online data or documents. Used with `LINK_TITLE` and `HTTP_LINK` attributes. This attribute allows multiple entries, with [CDAWeb](https://cdaweb.gsfc.nasa.gov/) allowing five entries (five entries are shown in the example).|
| [`LINK_TITLE`](#link_text-link_title-http_link) | **Recommended** (allows multiple entries; five  entries allowed by **CDAWeb**) |  `"Rules of Use"` <br> `"Space Science Reviews"` <br> `"the FIELDS team"` <br>  `"Fraenz and Harper, PSS, 2002."` <br> `"ISOIS Data Glossary"`  | Stores the title of the web page holding online data or documents. Used with `LINK_TEXT` and `HTTP_LINK` attributes. This attribute allows multiple entries, with [CDAWeb](https://cdaweb.gsfc.nasa.gov/) allowing five entries (five entries are shown in the example). |
| [`MODS`](#mods) | **Recommended** (allows multiple entries) |  `"Version 1.0 Jan. 1, 2020"`  | Stores the history of modifications made to the dataset. This attribute can have multiple entries.|
| [`Project`](#project) | **Recommended**  (allows multiple entries) |  `"LWS>Living With a Star"`  | Identifies the name of the project, and indicates ownership. Both the short and long names, separated by `>`, are included. This attribute can have multiple entries.|
| [`Rules_of_use`](#rules_of_use)  | **Recommended**  | `"See http://spp-isois.sr.unh.edu/ISOIS_Terms_of_Use.html"` | Text containing information on citability and PI access restrictions. This may point to a web page specifying the rules of use. |
| [`spase_DatasetResourceID`](#spase_datasetresourceid) | **Recommended**  | "spase://NASA/NumericalData/ParkerSolarProbe/PT1M" | Unique dataset identifier assigned by a [SPASE](https://spase-group.org/) naming authority. |
| [`Time_resolution`](#time_resolution) | **Recommended**  | `"1 min"`  | Specifies time resolution of the data. |
| [`Parents`](#parents) | **Optional** (allows multiple entries) | `"RDM>0012081A"`  | Lists the parent files of derived and merged datasets. This attribute allows multiple entries. |
| [`Skeleton_version`](#skeleton_version) | **Optional, required by Cluster** | `"2.0.0"` | Version of the skeleton file used to create the data file.  |
| [`Software_version`](#software_version) | **Optional, required by Cluster** |  `"1.3.0"` | Version of the software that generated the data file.  |
| [`TITLE`](#title) | **Optional** | `"Parker Solar Probe ISOIS level 2 summary"` | Dataset title.  |
| [`Validate`](#validate) | **Optional** | `"ISTP_skel>pass>CDHF>19951107"` | Written by software for automatic validation of features such as the structure of the data file on a simple pass/fail criterion. |


## Global Attribute Definitions

### Acknowledgement
(**_Recommended_**.) Specifies the expected acknowledgement text if the dataset is cited.

### ADID_ref
(**_No longer relevant_**.) This attribute stores the control authority identifier associated with the detached SFDU label. If no control authority identifier has been assigned, then the identifier associated with the ISTP/IACG Guidelines (NSSD0241) or with CDF (NSSD0110) can be used.

### Data_processing_level
(**_Recommended. PROPOSAL ONLY_**.) Processing level of the dataset. Both a short name  and a long name, separated by `>`, are required. For example, `Data_processing_level = "L2>Level 2"`

### Data_type
(**_Required_**.) This attribute identifies the data type of the dataset, generally the characteristics of the dataset that distinguish it from other datasets from the same instrument (including plausible ones created later) using some meaningful combination of parameters, resolution, format, compression. Both a short name (used in `Logical_source` and in the filename) and a long name (used in `Logical_source_description`), separated by `>`, are required. 

If desired, the level (`L0`, `L1`, `L2`, key parameter `kp`, summary parameter `sp`, etc.) may be prepended to the data collection name to sort by these levels (such as `l2-gms-62ms`). Temporal resolution uses time codes such as: ms, min, s, hr, day, week, month; for example, `500ms` for 0.5sec resolution, `6s` for 6sec, `5min` for 5 minutes, `2hr` for 2 hour, `1day` for daily.

Originally, for ISTP exchangeable data products, the values of `Data_type` were `"Kn>Key Parameter"` for approximately minute averaged survey data, `"Hn>High Resolution data"` for certified data of higher resolution than Key Parameters, and `"Mn>Modified Data"` for modified or derived datasets, where`n` is from `0` to `9`. For Cluster/Cluster Science Data System (CSDS), the allowed values were either `"SP>Summary Parameter"` or `"PP>Prime Parameter"`. For new datasets, data providers are not restricted to these original definitions, and can define data types individually for each mission or instrument to capture relevant information. For example, `Data_type = "L2-Summary>level 2 summary"` indicates both the processing level (`L2`) and that the dataset contains summary data, as two subfields separated by hyphen. 

### Data_version
(**_Required_**.) This attribute identifies the version of a particular data file for a given date, e.g., file ge_k0_mgf_19920923_v01.cdf is the first version of data for 1992 September 23. `Data_version` generally starts at `"1"`. **Each time** the data file is reproduced - for recalibration or other reasons - the `Data_version` is incremented by unity. Some projects use a more complex versioning scheme, such as Release, Major, Minor versions separated by period (e.g., `Data_version = "2.13.004"`). 

**Note** that the version, in case of a simple versioning, or the major version, in case of a more complex scheme, should be consistent across all files in the dataset (same version number have the same meaning for all files). This enables easy and unambiguous identification of major processing version for each data file. Description of all significant changes corresponding to each major processing version (up to, and including, the file current version) should also be included as a `MODS` global attribute entry (one entry per major version).

### Date_Start, Date_End
(**_Required for netCDF only_**.) The two attributes, always used together, describe the start and end UTC date/time (in yyyy-mm-ddThh:mm:ss format) of the data in the file. Required for netCDF since netCDF does not have a standard or defined variable for epoch/time values. Used by [CDAWeb](https://cdaweb.gsfc.nasa.gov/istp_public/).

### Descriptor
(**_Required_**.) This attribute identifies the name of the instrument or sensor that collected the data. Both a short name (used in `Logical_source` and in the filename) and a long name (used in `Logical_source_description`), separated by `>`, are required. For example,  `Descriptor = "ISOIS>Integrated Science Investigation of the Sun"`. This attribute should have single entry.

### Discipline
(**_Recommended_**.) This attribute describes both the science discipline and subdiscipline. Multiple entries are allowed. The list for space physics is:
- `"Solar Physics>Heliospheric Physics"`
- `"Space Physics>Interplanetary Studies"`
- `"Space Physics>Magnetospheric Science"`
- `"Space Physics>Ionospheric Science"`
- `"Space Physics>Astrophysics Science"`

### DOI
(**_Recommended_**.) Digital Object Identifier (DOI) as a persistent identifier for the dataset, of the form
`https://doi.org/PREFIX/SUFFIX` with the `PREFIX` identifying the DOI registration authority and the `SUFFIX` identifying the dataset. The DOI should point to a landing page for additional information about the dataset. DOIs are typically created by the [SPASE](https://spase-group.org/) naming authority or archive.

### File_naming_convention

(**_Recommended_**.) Describes the dataset file naming convention using combination of `"source"`, `"descriptor"`, and `"datatype"` (correspond to short names in `Source_name`, `Descriptor`, and `Data_type` attributes) and a date/time format, all separated by `"_"`, e.g., `File_naming_convention = "source_descriptor_datatype_yyyyMMdd"`. **Note** that  `"source_descriptor_datatype"` is the recommended order for new datasets, while `"source_datatype_descriptor"` may be common for older datasets. Date/time format includes a date format, either `"yyyyMMdd"` (recommended) or `"yyyyDDD"`, possibly followed by a time format (`"HHmmss"`, `"HHmm"`, or `"HH"`) with optional `"t"` separating them . E.g., `File_naming_convention = "source_descriptor_datatype_yyyyMMddtHHmmss"`.


### Generated_by
(**_Recommended_**.) This attribute allows for the generating data center/group to be identified.

### Generation_date
(**_Recommended_**.) File creation date using *yyyymmdd* syntax, e.g., `Generation_date = "19920923"`. This is distinct from the date in `Validate` below which records the times of later validation processes.

### Instrument_type
(**_Recommended, required by CDAWeb_**.) Combines types of instruments and regions as a simple way to quickly separate types of datasets for search through [CDAWeb](https://cdaweb.gsfc.nasa.gov/). Up to five entries are allowed. The following list contains allowed values:

- `"Activity Indices"`
- `"Dust and Debris"`
- `"Electric Fields (space)"`
- `"Engineering"`
- `"Ephemeris/Attitude/Ancillary"`
- `"Ground-Based HF-Radars"`
- `"Ground-Based Imagers"`
- `"Ground-Based Magnetometers, Riometers, Sounders"`
- `"Ground-Based VLF/ELF/ULF, Photometers"`
- `"Housekeeping"`
- `"Imaging and Remote Sensing (ITM/Earth)"`
- `"Imaging and Remote Sensing (Magnetosphere/Earth)"`
- `"Imaging and Remote Sensing (Sun)"`
- `"Magnetic Fields (Balloon)"`
- `"Magnetic Fields (space)"`
- `"Particles (space)"`
- `"Plasma and Solar Wind"`
- `"Radio and Plasma Waves (space)"`


### LINK_TEXT, LINK_TITLE, HTTP_LINK
(**_Recommended_**.) These attributes are used together to store the text (in `LINK_TEXT`, optional, even if the other two attributes are present), the title (in `LINK_TITLE`), and the URL (in `HTTP_LINK`)  of the link to the related and useful resources and documents, including links to the online data available at the PI or Co-I web site. The links will be displayed on the [CDAWeb](https://cdaweb.gsfc.nasa.gov/) Data Explorer page for the dataset. For example, if all three attributes are used (and each attribute includes one entry):
  
```
LINK_TEXT = "3-sec MGF magnetic field 1 Sep 1993 through 30 Sep 2015 available at "
LINK_TITLE = "ISAS DARTS"
HTTP_LINK = "https://www.darts.isas.jaxa.jp/stp/geotail/"
```
[CDAWeb](https://cdaweb.gsfc.nasa.gov/) Data Explorer page for the dataset will display:

_3-sec MGF magnetic field 1 Sep 1993 through 30 Sep 2015 available at [ISAS DARTS](https://www.darts.isas.jaxa.jp/stp/geotail/)_

If only `LINK_TITLE` and `HTTP_LINK` are used:
```
LINK_TITLE = "ISAS DARTS"
HTTP_LINK = "https://www.darts.isas.jaxa.jp/stp/geotail/"
```
[CDAWeb](https://cdaweb.gsfc.nasa.gov/) Data Explorer page for the dataset will display:

_[ISAS DARTS](https://www.darts.isas.jaxa.jp/stp/geotail/)_


These attributes can have multiple entries (up to five entries allowed by [CDAWeb](https://cdaweb.gsfc.nasa.gov/)), but exactly the same number of entries is required for each of the included attributes, with empty strings allowed. This will result in multiple lines of text displayed on the [CDAWeb](https://cdaweb.gsfc.nasa.gov/) Data Explorer page for the dataset.

### Logical_file_id
(**_Required_**.) This attribute stores the name of the data file, without extension, using the ISTP naming convention (`Source_name`\_`Descriptor`\_`Data_type`\_Date\_v`Data_version`), with short names for `Source_name`, `Descriptor`, and `Data_type`, e.g., `Logical_file_id = "psp_isois_l2-summary_20180928_v07"`. This attribute stores the filename in case of an inadvertent filename change.

### Logical_source
(**_Required_**.) This attribute carries dataset ID (used by [CDAWeb](https://cdaweb.gsfc.nasa.gov/istp_public/)) in the form `Source_name`\_ `Data_type`\_`Descriptor`, e.g., `Logical_source = "psp_isois_l2-summary"`.

### Logical_source_description
(**_Required_**.) This attribute writes out the full names associated with the encrypted `Logical_source`, e.g., `Logical_source_description = "Parker Solar Probe ISOIS level 2 summary"`. Used by [CDAWeb](https://cdaweb.gsfc.nasa.gov/) as the dataset full name.

### Mission_group
(**_Recommended, required by CDAWeb_**.) This attribute has a single value and is used to facilitate making choices of source through [CDAWeb](https://cdaweb.gsfc.nasa.gov/istp_public/). Examples:

- `"Geotail"`
- `"GOLD"`
- `"ICON"`
- `"IMP8"`
- `"Parker Solar Probe"`
- `"Solar Orbiter"`
- `"THEMIS"`
- `"Wind"`
- `"Van Allen Probes (RBSP)"`
- `"Geosynchronous Investigations"`
- `"Ground-Based Investigations"`
- `"Helio ephemeris"`
- `"OMNI (Combined 1AU IP Data; Magnetic and Solar Indices)"`
- `"Smallsats/Cubesats"`
- `"Sounding Rockets"`

### MODS
(**_Recommended_**.) This attribute is used to store the description of all significant changes to the dataset. The attribute is not directly tied to `Data_version`, but each version produced will contain relevant modifications, and description of each major version (including version change date and all significant changes) should be included as a `MODS` attribute entry (one entry per major version). This attribute can have unlimited number of entries to store the complete history of modifications made to the dataset.

### Parents
(**_Optional_**.) This attribute lists the parent files (in CDF or other format) for derived or merged datasets. Multiple entries are used to include multiple parents. The `Parents` entry syntax, e.g., for a CDF parent file, is of the form`"CDF>logical_file_id"`. Alternatively, the whole file name, including extension, can be included as a `Parents` attribute entry.

### PI_affiliation
(**_Required_**.) Affiliation of the lead person, usually Principal Investigator (PI). This attribute value should include a recognizable abbreviation.

### PI_name
(**_Required_**.) Lead person, usually Principal Investigator (PI). This attribute value should at least include first initial and last name.

### Project
(**_Recommended_**.) This attribute identifies the name of the project and indicates ownership and funding project. For the original ISTP missions and investigations, the value used is `"ISTP>International Solar-Terrestrial Physics"`. For the Cluster mission, the value is `"STSP Cluster>Solar Terrestrial Science Programmes, Cluster"`. Other acceptable values are:

  - `"LWS>Living With a Star"`
  - `"STP>Solar Terrestrial Probes"`
  - `"IACG>Inter-Agency Consultative Group"`
  - `"CDAWxx>Coordinated Data Analysis Workshop xx"`
  - `"SPDS>Space Physics Data System"`

  Others may be defined in the future. This attribute can have multiple entries if the data has been supplied to more than one project.

### Rules_of_use
(**_Recommended_**.) Text containing information on, e.g., citability or use restrictions. This may point to a web page specifying the rules of use.

### Skeleton_version
(**_Optional, required by Cluster_**.) Version of the skeleton file used to create the data file.

### Software_version
(**_Optional, required by Cluster_**.) Version of the software that generated the data file.

### Source_name
(**_Required_**.) This attribute identifies the mission or investigation that contains the sensors. For ISTP, this is the mission name for spacecraft missions or the investigation name for ground-based or theory investigations. Both a short name (used in `Logical_source` and in the filename) and a long name (used in `Logical_source_description`) separated by `>` are required. This attribute should be single valued. Examples:

- `"GEOTAIL>Geomagnetic Tail"`
- `"WIND>Wind Interplanetary Plasma Laboratory"`
- `"DARN>Dual Auroral Radar Network"`
- `"GOES_7>Geostationary Operational Environmental Satellite 7"`
- `"IMP-8>Interplanetary Monitoring Platform"`
- `"LANL1989_046>Los Alamos National Laboratory 1989"`
- `"C1>Cluster Satellite No 1"`

### spase_DatasetResourceID
(**_Recommended_**.) Unique dataset identifier assigned by a [SPASE](http://www.spase-group.org/) naming authority, of the form `spase://NAMING_AUTHORITY/UNIQUE_ID`, where `UNIQUE_ID` is the ID assigned by the `NAMING_AUTHORITY`. The SPASE resource record provides metadata about the dataset, including pointers to locations holding the data.

### TEXT
(**_Required_**.) This attribute should contain description of the key measurements provided by the dataset. A short description of the experiment, with reference to a journal paper and/or web page describing the experiment in detail, is also essential. The attribute allows multiple entries. It is used by [CDAWeb](https://cdaweb.gsfc.nasa.gov/) as the dataset description, and it is also included when data is requested as an ASCII listing.


### Time_resolution
(**_Recommended_**.) Specifies time resolution of the data, e.g., `"1 min"`

### TITLE
(**_Optional_**.) Dataset title, e.g., `TITLE = "Parker Solar Probe ISOIS level 2 summary"`.

### Validate
(**_Optional_**.) Details to be specified. This attribute is written by software for automatic validation of features such as the structure of the data file on a simple pass/fail criterion. The software will test that all expected attributes are present and, where possible, have reasonable values. The syntax is likely to be of the form `"test>result>where done>date"`. It is not the same as data validation.
