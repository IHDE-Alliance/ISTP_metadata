# ISTP Global Attributes

Global attributes are used to provide information about the dataset as an entity and about the individual files composing the datasets. Together with variables and variable attributes the global attributes make the data correctly and independently usable by someone not connected with the instrument team, and hence, a good archive product. Global attributes provide informational metadata associated with all the variables in the file, and as a means of attaching information that may be carried along with the data. The global attributes are also used by the Coordinated Data Analysis Web ([CDAWeb)](https://cdaweb.gsfc.nasa.gov/) Display and Retrieval system. 

The required, recommended, and optional global attributes with example values are listed in the table below. See [Global Attribute Definitions](#global-attribute-definitions) for the full set of defined global attributes in alphabetical order. Global attributes can be listed in any order. Note that the attribute names are case-sensitive, and the names of the ISTP global attributes must match the case **exactly** as shown. Also, all ISTP global attributes are of **character data type** (string).

Additional global attributes may be defined, but their **names must start with a letter and can otherwise contain letters, numbers and the underscore character, but no other special characters.** Though attribute names are case sensitive, the names must never be distinguished by case only.



| **Attribute Name** | **NASA Archive Requirement** | **Example Value** | **Notes** |
| -------------- | ---------------------------- | -------- | --------- |
| [`Data_type`](#data_type) | Required | `"L2-Summary>level 2 summary"`  | Identifies the data type of the dataset. Both the short and long names are included. |
| [`Data_version`](#data_version) | Required |  `"07"` | Identifies the version of a particular data file |
| [`Descriptor`](#descriptor) | Required |  `"ISOIS>Integrated Science Investigation of the Sun"` |Identifies both the short and long names of the instrument or sensor that collected the data |
| [`Instrument_type`](#instrument_type) | Required | `"Particles (space)"` <br> `"Plasma and Solar Wind"` | Used to facilitate making choices of instrument type through [CDAWeb](https://cdaweb.gsfc.nasa.gov/istp_public/). This attribute can have up to five entries (two entries are shown). |
| [`Logical_file_id`](#logical_file_id) | Required | `"psp_isois_l2-summary_20180928_v07"`  | Stores the name of the file using the ISTP naming convention (`Source_name`\_`Descriptor`\_`Data_type`\_Date\_`Data_version`)  |
| [`Logical_source`](#logical_source) | Required | `"psp_isois_l2-summary"`  | Carries `Source_name`, `Descriptor`, and `Data_type` information. Used by [CDAWeb](https://cdaweb.gsfc.nasa.gov/istp_public/). |
| [`Logical_source_description`](#logical_source_description) | Required | `"Parker Solar Probe ISOIS level 2 summary"`  | Writes out the full words associated with the encrypted `Logical_source` above |
| [`Mission_group`](#mission_group) | Required |  `"Parker Solar Probe (PSP)"` | Has a single value and is used to facilitate making choices of source through [CDAWeb](https://cdaweb.gsfc.nasa.gov/istp_public/). |
| [`PI_affiliation`](#pi_affiliation) | Required |  `"Princeton University"` | Should include a recognizable abbreviation. |
| [`PI_name`](#pi_name) | Required |  `"David McComas"` | Should at least include first initial and last name. |
| [`Project`](#project) | Required |  `"LWS>Living With a Star"`  | Identifies the name of the project and indicates ownership. Both the short and long names are included. |
| [`Source_name`](#source_name) | Required | `"PSP>Parker Solar Probe"` | Identifies the mission or investigation that contains the sensors. Both the short and long names are included. |
| [`TEXT`](#text) | Required | `"EPI-Hi HET 3600 second rates cdf. Time tags indicate midpoint of integration."`<br> `"Instrument paper: Integrated Science Investigation of the Sun (ISIS): Design of the Energetic Particle Investigation. McComas, D. J. et al (2016). Space Sci. Rev., doi:10.1007/s11214-014-0059-1"` | A standard global attribute for description of the experiment whose data are included in the CDF.  A reference to a journal article(s) or web page describing the experiment is essential, and constitutes the minimum requirement. A written description of the dataset is also essential. This attribute can have unlimited number of entries (two entries are shown).|
| [`Acknowledgement`](#acknowledgement)  | Recommended  | `"Cite McComas et al (2016),doi:10.1007/s11214-014-0059-1"` | Text string at Principal Investigator's (PI) disposal allowing for information on expected acknowledgement if dataset is citable. |
| [`Discipline`](#discipline) | Recommended | `"Solar Physics>Heliospheric Physics"`  | Describes both the science discipline and subdiscipline. |
| [`Data_processing_level`](#data_processing_level-proposal-only) (PROPOSAL ONLY)| Recommended | `"L2>Level 2"`  | Describes dataset processing level. Both the short and long names are included.|
| [`DOI`](#doi) | Recommended  |  `"https://doi.org/10.48322/mede-7j02"`  | Digital Object Identifier (DOI) as a persistent identifier for the dataset. |
  | [`Generated_by`](#generated_by) | Recommended  | `"ISOIS SOC, University of New Hampshire"` | Allows for the generating data center/group to be identified. |
| [`Generation_date`](#generation_date) | Recommended  |  `"20210329"` | Date stamps the creation of the file using the yyyymmdd syntax.  |
| [`HTTP_LINK`](#link_text-link_title-http_link) | Recommended  |  `"http://spp-isois.sr.unh.edu/ISOIS_Terms_of_Use.html"` <br> `"https://link.springer.com/article/10.1007%2Fs11214-014-0059-1"` <br> `"http://fields.ssl.berkeley.edu/"` <br> `"https://www2.mps.mpg.de/homes/fraenz/systems/"` <br> `"http://spp-isois.sr.unh.edu/data_public/ISOIS_Data_Glossary.pdf"` | Stores the URL for the PI or CoI web site holding on-line data. Used with `LINK_TEXT` and `LINK_TITLE` attributes. This attribute can have up to five entries (five entries are shown). |
| [`LINK_TEXT`](#link_text-link_title-http_link) | Recommended  | `"Data "` <br> `"Instrument paper at "` <br> `"Magnetic field data for pitch angle calculation courtesy of "` <br> `"Coordinate systems according to definitions of "` <br> `"Detailed information in "` | Stores text describing on-line data available at PI or CoI web sites. Used with `LINK_TITLE` and `HTTP_LINK` attributes. This attribute can have up to five entries (five entries are shown).|
| [`LINK_TITLE`](#link_text-link_title-http_link) | Recommended  |  `"Rules of Use"` <br> `"Space Science Reviews"` <br> `"the FIELDS team"` <br>  `"Fraenz and Harper, PSS, 2002."` <br> `"ISOIS Data Glossary"`  | Stores the title of the web site holding on-line data available at PI or CoI web sites. Used with `LINK_TEXT` and `HTTP_LINK` attributes. This attribute can have up to five entries (five entries are shown). |
| [`MODS`](#mods) | Recommended  |  `"Version 1.0 Jan. 12, 1993"`  | A standard global attribute used to denote the history of modifications made to the dataset. This attribute can have unlimited number of entries.|
| [`Rules_of_use`](#rules_of_use)  | Recommended  | `"See http://spp-isois.sr.unh.edu/ISOIS_Terms_of_Use.html."` | Text containing information on citability and PI access restrictions. This may point to a web page specifying the rules of use. |
| [`spase_DatasetResourceID`](#spase_datasetresourceid) | Recommended  | `"spase://NASA/NumericalData/ParkerSolarProbe/ISOIS/Merged/Level2/Summary/PT1M"` | Unique dataset identifier assigned by Space Physics Archive Search and Extract (SPASE). |
| [`Time_resolution`](#time_resolution) | Recommended  | `"1 min"`  | Specifies time resolution of the data. |
| [`Parents`](#parents) | Optional | `"RDM>0012081A"`  | Lists the parent files of derived and merged datasets. |
| [`Skeleton_version`](#skeleton_version) | Optional | `"2.0.0"` | Version number of the skeleton file used to create the data file.  |
| [`Software_version`](#software_version) | Optional |  `"1.3.0"` | Used to document version of software that generated the file.  |
| [`TITLE`](#title) | Optional | `"Parker Solar Probe ISOIS level 2 summary"` | Dataset title.  |
| [`Validate`](#validate) | Optional | `"Compatible with the ISTP CDF Standards"` | Written by software for automatic validation of features such as the structure of the CDF file on a simple pass/fail criterion. |


## Global Attribute Definitions

### Acknowledgement
(*Recommended*) Text string at Principal Investigator's (PI) disposal allowing for information on expected acknowledgement if dataset is citable.

### Data_processing_level (PROPOSAL ONLY)

Processing level of the dataset. Both a short name (used in `Logical_source` and in the filename) and a long name (description used in `Logical_source_description`) separated by `>` are required. For example, `Data_processing_level = "L2>Level 2"`


### Data_type
(*Required*) This attribute identifies the data type of the CDF dataset. Both a short name (used in `Logical_source` and in the filename) and a long name (description used in `Logical_source_description`) separated by `>` are required. Originally, for ISTP exchangeable data products, the values were `"Kn>Key Parameter"` for approximately minute averaged survey data, `"Hn>High Resolution data"` for certified data of higher resolution than Key Parameters, and `"Mn>Modified Data"` for modified or derived datasets, where`n` is from `0` to `9`. For Cluster/Cluster Science Data System (CSDS) the allowed values were either `"SP>Summary Parameter"` or `"PP>Prime Parameter"`. For new datasets, data providers are not restricted to these original definitions, and can define data types individually for each mission or instrument to capture relevant information. For example, `Data_type = "L2-Summary>level 2 summary"` indicates both the processing level (`L2`) and that the dataset contains summary data, as two subfields separated by hyphen. 

### Data_version
(*Required*) This attribute identifies the version of a particular CDF data file for a given date, e.g., the file GE_K0_MGF_19920923_V01 is the first version of data for 1992 September 23. **Each time** this particular data file is reproduced - for recalibration or other reasons - the `Data_version` is incremented by unity. `Data_version` always starts at `"1"`.

### Descriptor
(*Required*) This attribute identifies the name of the instrument or sensor that collected the data. Both a short name (used in `Logical_source` and in the filename) and a long name (description used in `Logical_source_description`) separated by `>` are required. For example,  `Descriptor = "EPI>Energetic Particles and Ion Composition"`. The short name should be limited to from 2 to 4 characters for consistency with ISTP. This attribute should have single entry.

### Discipline
(*Recommended*) This attribute describes both the science discipline and subdiscipline. More than one entry is allowed. The list for space physics is:
- `"Solar Physics>Heliospheric Physics"`
- `"Space Physics>Interplanetary Studies"`
- `"Space Physics>Magnetospheric Science"`
- `"Space Physics>Ionospheric Science"`
- `"Space Physics>Astrophysics Science"`

### DOI
(*Recommended*) Digital Object Identifier (DOI) as a persistent identifier for the dataset, of the form
https://doi.org/PREFIX/SUFFIX with the PREFIX identifying the DOI registration authority and the SUFFIX identifying the dataset. The DOI should point to a landing page for additional information about the dataset. DOIs are typically created by the [SPASE](https://spase-group.org/) naming authority or archive.

### Generated_by
(*Recommended*) This attribute allows for the generating data center/group to be identified.

### Generation_date
(*Recommended*) Date stamps the creation of the file using the syntax *yyyymmdd*, e.g. `Generation_date = "19920923"`. This is distinct from the date in `Validate` below which records the times of later validation processes.

### Instrument_type
(*Required*) This attribute is used to facilitate making choices of instrument type through [CDAWeb](https://cdaweb.gsfc.nasa.gov/istp_public/). Up to five entries are allowed. The following list contains the valid values:

- `"Activity Indices"`
- `"Electric Fields (space)"`
- `"Electron Precipitation Bremsstrahlung"`
- `"Energetic Particle Detector"`
- `"Engineering"`
- `"Ephemeris/Attitude/Ancillary"`
- `"Gamma and X-Rays"`
- `"Ground-Based HF-Radars"`
- `"Ground-Based Imagers"`
- `"Ground-Based Magnetometers, Riometers, Sounders"`
- `"Ground-Based VLF/ELF/ULF, Photometers"`
- `"Housekeeping"`
- `"Imaging and Remote Sensing (ITM/Earth)"`
- `"Imaging and Remote Sensing (Magnetosphere/Earth)"`
- `"Imaging and Remote Sensing (Sun)"`
- `"Imagers (space)"`
- `"Linear Energy Transfer Spectrometer"`
- `"Magnetic Fields (Balloon)"`
- `"Magnetic Fields (space)"`
- `"Particles (space)"`
- `"Plasma and Solar Wind"`
- `"Pressure gauge (space)"`
- `"Radio and Plasma Waves (space)"`
- `"Spacecraft Potential Control"`
- `"UV Imaging Spectrograph (Space)"`


### LINK_TEXT, LINK_TITLE, HTTP_LINK
(*Recommended*) The three attributes are used together to store the text (`LINK_TEXT`, optional even if the other two are present) describing the on-line data available at the PI or Co-I web site and the title (`LINK_TITLE`) and URL (`HTTP_LINK`) of that web site. CDAWeb will link the attribute values into a line of text displayed at the CDAWeb Data Explorer page for the dataset. For example:
  
```
LINK_TEXT = "3-sec MGF magnetic field 1 Sep 1993 through 30 Sep 2015 available at "
LINK_TITLE = "ISAS DARTS"
HTTP_LINK = "https://www.darts.isas.jaxa.jp/stp/geotail/"
```
will display:

_3-sec MGF magnetic field 1 Sep 1993 through 30 Sep 2015 available at [ISAS DARTS](https://www.darts.isas.jaxa.jp/stp/geotail/)_

`LINK_TEXT`, `LINK_TITLE`, and `HTTP_LINK` can have multiple (up to five), but exactly the same, number of entries for each of the present attributes, with empty strings allowed. This will result in multiple lines of text displayed at the CDAWeb Data Explorer page.

### Logical_file_id
(*Required*) This attribute stores the name of the CDF file, without extension, using the ISTP naming convention (`Source_name`\_`Descriptor`\_`Data_type`\_Date\_v`Data_version`), e.g., `"psp_isois_l2-summary_20180928_v07"`.

### Logical_source
(*Required*) This attribute carries dataset ID (used by [CDAWeb](https://cdaweb.gsfc.nasa.gov/istp_public/)) in the form `Source_name`\_ `Data_type`\_`Descriptor`, e.g., `"psp_isois_l2-summary"`.

### Logical_source_description
(*Required*) This attribute writes out the full words associated with the encrypted `Logical_source`, e.g., `"Parker Solar Probe ISOIS level 2 summary"`. Used by [CDAWeb](https://cdaweb.gsfc.nasa.gov/istp_public/).

### Mission_group
(*Required*) This attribute has a single value and is used to facilitate making choices of source through [CDAWeb](https://cdaweb.gsfc.nasa.gov/istp_public/). Example values include, but not limited to:

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
(*Recommended*) This attribute is a standard global attribute which is used to denote the history of modifications made to the CDF dataset. The Metadata Object Description (`MODS`) attribute should contain a description of all significant changes to the dataset. This attribute is not directly tied to Data_version, but each version produced will contain the relevant modifications. This attribute can have as many entries as necessary to contain the desired information.

### Parents
(*Optional*) This attribute lists the parent files (in CDF or other format) for files of derived or merged datasets. Multiple entries are used to include multiple parents. The `Parents` entry syntax, e.g., for a CDF parent file is of the form`"CDF>logical_file_id"`. Alternatively, the whole file name, including extension, can be included as a `Parents` attribute entry.

### PI_affiliation
(*Required*) This attribute value should include a recognizable abbreviation.

### PI_name
(*Required*) This attribute value should at least include first initial and last name.

### Project
(*Required)* This attribute identifies the name of the project and indicates ownership. For ISTP missions and investigations, the value used is `"ISTP>International Solar-Terrestrial Physics"`. For the Cluster mission, the value is `"STSP Cluster>Solar Terrestrial Science Programmes, Cluster"`. Other acceptable values are:

  - `"LWS>Living With a Star"`
  - `"STP>Solar Terrestrial Probes"`
  - `"IACG>Inter-Agency Consultative Group"`
  - `"CDAWxx>Coordinated Data Analysis Workshop xx"`
  - `"SPDS>Space Physics Data System"`

  Others may be defined in the future. This attribute can be multi-valued if the data has been supplied to more than one project.

### Rules_of_use
(*Recommended*) Text containing information on, e.g., citability or use restrictions. This may point to web page specifying the rules of use.

### Skeleton_version
(*Optional*) This is a text attribute containing the skeleton file version number. This is a required
attribute for Cluster, but for IACG purposes it exists if experimenters want to track it.

### Software_version
(*Optional*) This is a required attribute for Cluster, but for IACG purposes it exists if experimenters want to track it.

### Source_name
(*Required*) This attribute identifies the mission or investigation that contains the sensors. For ISTP, this is the mission name for spacecraft missions or the investigation name for ground-based or theory investigations. Both a short name (used in `Logical_source` and in the filename) and a long name (description used in `Logical_source_description`) separated by `>` are required. This attribute should be single valued. Examples:

- `"GEOTAIL>Geomagnetic Tail"`
- `"WIND>Wind Interplanetary Plasma Laboratory"`
- `"DARN>Dual Auroral Radar Network"`
- `"GOES_7>Geostationary Operational Environmental Satellite 7"`
- `"IMP-8>Interplanetary Monitoring Platform"`
- `"LANL1989_046>Los Alamos National Laboratory 1989"`
- `"C1>Cluster Satellite No 1"`

### spase_DatasetResourceID
(*Recommended*) Unique dataset identifier assigned by [SPASE](http://www.spase-group.org/), of the form spase://NAMING_AUTHORITY/UNIQUE_ID, where UNIQUE_ID is the ID assigned to the SPASE resource record for the dataset in the [SPASE system](http://www.spase-group.org/) by a SPASE NAMING_AUTHORITY. The SPASE resource record provides metadata about the dataset, including pointers to locations holding the data.

### TEXT
(*Required*) This attribute is a standard global attribute which is a text description of the
experiment whose data is included in the CDF. A reference to a journal article(s) or to a web page describing the experiment is essential, and constitutes the minimum requirement. A written description of the dataset is also essential. This attribute can have as many entries as necessary.

### Time_resolution
(*Recommended*) Specifies time resolution of the file, e.g., `"1 min"`

### TITLE
(*Optional*) This attribute is a standard global attribute which is a title for the dataset, e.g., `"Parker Solar Probe ISOIS level 2 summary"`.

### Validate
(*Optional*) Details to be specified. This attribute is written by software for automatic validation of features such as the structure of the CDF file on a simple pass/fail criterion. The software will test that all expected attributes are present and, where possible, have reasonable values. The syntax is likely to be of the form `"test>result>where done>date"`. It is not the same as data validation.

---
Return to [Table of Contents](../README.md)
