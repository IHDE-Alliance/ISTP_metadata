# Global Attributes

Global attributes are used to provide information about the data set as an entity. Together with variables and variable attributes, the global attributes make the data correctly and independently usable by someone not connected with the instrument team, and hence, a good archive product. The global attributes are also used by the Coordinated Data Analysis Web ([CDAWeb)](https://cdaweb.gsfc.nasa.gov/) Display and Retrieval system. The required Global Attributes are listed here with example values. Note that Common Data Format (CDF) attributes are case-sensitive and must **exactly** follow what is shown here. Additional Global attributes can be defined but **they must start with a letter and can otherwise contain letters, numbers and the unscore character (no other special characters allowed).** See [Global Attribute Definitions](https://spdf.gsfc.nasa.gov/istp_guide/gattributes.html#gdefinitions) for the full set of defined Global Attributes.

| **Attribute**                                             | **NASA Archive Requirement** | **Example**                                              | **Notes**                                                                                                                                                                                                                                                                                                                                      |
| --------------------------------------------------------- | ---------------------------- | -------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Project](#project)                                       | Required                     | { "ISTP>International " - "Solar-Terrestrial Physics" }. | Identifies the name of the project and indicates ownership.                                                                                                                                                                                                                                                                                    |
| [Source_name](#source_name)                               | Required                     | { "GEOTAIL>Geomagnetic Tail" }.                          | Identifies the mission or investigation that contains the sensors.                                                                                                                                                                                                                                                                             |
| [Mission_group](#Mission_group)                           | Required                     | {< "Geotail" }.                                          | Has a single value and is used to facilitate making choices of source through [CDAWeb](https://cdaweb.gsfc.nasa.gov/istp_public/).                                                                                                                                                                                                             |
| [Instrument_type](#Instrument_type)                       | Required                     | { "Magnetic Fields (space)" }.                           | Used to facilitate making choices of instrument type through [CDAWeb](https://cdaweb.gsfc.nasa.gov/istp_public/).                                                                                                                                                                                                                              |
| [Logical_source_description](#Logical_source_description) | Required                     | { "Geotail Magnetic Field Key Parameters" }.             | Writes out the full words associated with the encrypted Logical_source above, *e.g.,* "Geotail Magnetic Field Key Parameters."                                                                                                                                                                                                                 |
| [Data_type](#Data_type)                                   | Required                     | { "K0>Key Parameter" }.                                  | Identifies the data type of the CDF data set. Both a long name and a short name are given.                                                                                                                                                                                                                                                     |
| [Data_version](#Data_version)                             | Required                     | { "1" }.                                                 | Identifies the version of a particular CDF data file for a given date, *e.g.,* the file GE_K0_MGF_19920923_V01 is the first version of data for 1992 September 23.                                                                                                                                                                             |
| [Descriptor](#Descriptor)                                 | Required                     | { "EPI>Energetic Particles" - " and Ion Composition" }.  | Example: "EPI>Energetic Particles and Ion Composition."                                                                                                                                                                                                                                                                                        |
| [Discipline](#Discipline)                                 | Required                     | { "Space Physics>Magnetospheric Science" }.              | Describes both the science discipline and subdiscipline.                                                                                                                                                                                                                                                                                       |
| [Logical_file_id](#Logical_file_id)                       | Required                     | { "GE_K0_EPI_19920908_V01" }.                            | Stores the name of the CDF file using the ISTP naming convention (source_name/data_type/ descriptor/date/data_version), *e.g.,* GE_K0_MGF_19920923_V01.                                                                                                                                                                                        |
| [Logical_source](#Logical_source)                         | Required                     | { "GE_K0_EPI" }.                                         | Carries source_name, data_type, and descriptor information. Used by [CDAWeb](https://cdaweb.gsfc.nasa.gov/istp_public/).                                                                                                                                                                                                                       |
| [PI_affiliation](#PI_affiliation)                         | Required                     | { "JHU/APL" }.                                           | Should include a recognizable abbreviation.                                                                                                                                                                                                                                                                                                    |
| [PI_name](#PI_name)                                       | Required                     | { "D. Williams" }.                                       | Should include first initial and last name.                                                                                                                                                                                                                                                                                                    |
| [TEXT](#TEXT)                                             | Required                     | { "reference to journal article, URL address" }.         | A standard global attribute which is a text description of the experiment whose data is included in the CDF.                                                                                                                                                                                                                                   |
| [Acknowledgment](#acknowledgement-----recommended)                                 | Recommended                  |                                                          | Text string at Particles and Ion (PI) disposal allowing for information on expected acknowledgment if data is citable.                                                                                                                                                                                                                         |
| [DOI](#DOI)                                               | Recommended                  |                                                          | Digital Object Identifier (DOI) as a persistent identifier for the dataset, of the formÂ https://doi.org/ with the identifying the DOI registration authority and the <SUFFIX> identifying the dataset.                                                                                                                                         |
| [Generated_by](#Generated_by)                             | Recommended                  |                                                          | Allows for the generating data center/group to be identified.                                                                                                                                                                                                                                                                                  |
| [Generation_date](#Generation_date)                       | Recommended                  |                                                          | Date stamps the creation of the file using the syntax yyyymmdd, *e.g.,* "19920923."                                                                                                                                                                                                                                                            |
| [HTTP_LINK](#HTTP_LINK)                                   | Recommended                  |                                                          | Stores the URL for the PI or CoI web site holding on-line data.                                                                                                                                                                                                                                                                                |
| [LINK_TEXT](#LINK_TEXT)                                   | Recommended                  |                                                          | Stores text describing on-line data available at PI or CoI web sites.                                                                                                                                                                                                                                                                          |
| [LINK_TITLE](#LINK_TITLE)                                 | Recommended                  |                                                          | Stores the title of the web site holding on-line data available at PI or CoI web sites.                                                                                                                                                                                                                                                        |
| [MODS](#MODS)                                             | Recommended                  |                                                          | A standard global attribute which is used to denote the history of modifications made to the CDF data set.                                                                                                                                                                                                                                     |
| [Rules_of_use](#Rules)                                    | Recommended                  |                                                          | Text containing information on, {\it e.g.} citability and PI access restrictions. This may point to a World Wide Web page specifying the rules of use.                                                                                                                                                                                         |
| [spase_DatasetResourceID](#spase_DatasetResourceID)       | Recommended                  |                                                          | Unique dataset identifier assigned by Space Physics Archive Search and Extract ([SPASE)](http://www.spase-group.org/), of the form spase://<NAMING_AUTHORITY>/<UNIQUE_ID>, where <UNIQUE_ID>Â is the ID assigned to the SPASE resource record for the dataset in the [SPASE system](http://www.spase-group.org/) by a SPASE <NAMING_AUTHORITY>. |
| [Time_resolution](#Time_resolution)                       | Recommended                  |                                                          | Specifies time resolution of the file, *e.g.,* "3 seconds."                                                                                                                                                                                                                                                                                    |
| [TITLE](#TITLE)                                           | Optional                     |                                                          | A standard global attribute which is a title for the data set, *e.g.,* "Geotail EPIC Key Parameters."                                                                                                                                                                                                                                          |
| [Parents](#Parents)                                       | Optional                     |                                                          | Lists the parent CDF(s) for files of derived and merged data sets.                                                                                                                                                                                                                                                                             |
| [Skeleton_version](#Skeleton_version)                     | Optional                     |                                                          | A text attribute containing the skeleton file version number.                                                                                                                                                                                                                                                                                  |
| [Software_version](#Software)                             | Optional                     |                                                          | Required attribute for Cluster, but for Inter-Agency Consultative Group (IACG) purposes it exists if experimenters want to track it.                                                                                                                                                                                                           |
| [Validate](#Validate)                                     | Optional                     |                                                          | Written by software for automatic validation of features such as the structure of the CDF file on a simple pass/fail criterion.                                                                                                                                                                                                                |

Global Attribute DefinitionsÂ in alphabetical order

## Acknowledgement 
  (Recommended) Text string at PI disposal allowing for information on expected acknowledgment if data is citable.

## ADID_ref 
  (No longer relevant)

This attribute stores the control authority identifier associated with the detached SFDU
label. If no control authority identifier has been assigned, then the identifier associated with the ISTP/IACG Guidelines (NSSD0241) or with CDF (NSSD0110) can be used.

### Data_type --- required

This attribute identifies the data type of the CDF data set. Both a long name and a short name are given. For ISTP exchangeable data products the values are "Kn>Key Parameter" for approximately minute averaged survey data, and "Hn>High Resolution data" for certified data of higher resolution than Key Parameters.$n$ can run from 0 to 9 to allow for more than one kind of data product. For Cluster/Cluster Science Data System (CSDS) this can either be "SP>Summary Parameter" or "PP>Prime Parameter." Other possible data types may be defined in the future. If any of these data sets are modified or used to produce derived products, the data type should be, *e.g.,* "Mn>Modified Data n", where n is from 0 to 9.

**Data_version --- required**

This attribute identifies the version of a particular CDF data file for a given date, *e.g.,* the file GE_K0_MGF_19920923_V01 is the first version of data for 1992 September23. **Each time** this particular data file is reproduced - for recalibration or other reasons - the Data_version is incremented by 1. Data_version always starts at `1'.

**Descriptor --- required**

This attribute identifies the name of the instrument or sensor that collected the data. Both a long name and a short name are given. An example for ISTP is "EPI>Energetic Particles and Ion Composition." The short name should be limited to from 2 to 4 characters for consistency with ISTP. This attribute should be single valued.

**Discipline --- required**

This attribute describes both the science discipline and subdiscipline. More than one entry is allowed. The list for space physics is:

Â· "Space Physics>Magnetospheric Science"

Â· ''Space Physics>Interplanetary Studies"

Â· ''Space Physics>Ionospheric Science"

**DOI --- recommended**

Digital Object Identifier (DOI) as a persistent identifier for the dataset, of the form
https://doi.org/<PREFIX>/<SUFFIX> with the <PREFIX> identifying the DOI registration authority and the <SUFFIX> identifying the dataset. The DOI should point to a landing page for additional information about the dataset. DOIs are typically created by the [SPASE](https://spase-group.org/) naming authority or archive.

**Generated_by --- recommended**

This attribute allows for the generating data center/group to be identified.

**Generation_date --- recommended**

Date stamps the creation of the file using the syntax yyyymmdd, *e.g.,* "19920923."
This is distinct from the date in "validate" below which records the times of later validation processes.

**HTTP_LINK --- recommended**

This attribute stores the URL for the PI or CoI web site holding on-line data. This attribute is used in conjunction with "LINK_TEXT" and "LINK_TITLE." There can be up to 5 entries for each - there MUST be a corresponding entry of "LINK_TEXT" and "LINK_TITLE" for each "HTTP_LINK" entry. CDAWeb will then link to the URL given by "HTTP_LINK" using the "LINK_TITLE" and the description in "LINK_TEXT," on the CDAWeb Data Explorer page. For example:

Â· "LINK_TEXT" = 3-sec MGF magnetic field 1 Sep 1993 through 30 Sep 2015 available at

Â· "LINK_TITLE" = Institute of Space and Astronautical Science (ISAS) Data ARchives and Transmission System (DARTS)

Â· "HTTP_LINK" = https://www.darts.isas.jaxa.jp/stp/geotail/ will give the following link:

3-sec MGF magnetic field 1 Sep 1993 through 30 Sep 2015 available at [ISAS DARTS](https://www.darts.isas.jaxa.jp/stp/geotail/)

**Instrument_type --- required**

This attribute is used to facilitate making choices of instrument type through [CDAWeb](https://cdaweb.gsfc.nasa.gov/istp_public/). More than one entry is allowed. The following list contains the valid values:

Â· Electric Fields (space)

Â· Ephemeris

Â· Imagers (space)

Â· Magnetic Fields (space)

Â· Particles (space)

Â· Plasma and Solar Wind

Â· Radio and Plasma Waves (space)

Â· Ground-Based High Frequency (HF)-Radars

Â· Ground-Based Imagers

Â· Ground-Based Magnetometers, Riometers, Sounders

Â· Ground-Based Very Low Frequency (VLF)/Extremely Low Frequency (ELF)/Ultralow Frequency (ULF), Photometers

**LINK_TEXT --- recommended**

This attribute stores text describing on-line data available at PI or CoI web sites. This attribute is used in conjunction with "LINK_TITLE" and "HTTP_LINK." There can be up to 5 entries for each - there MUST be a corresponding entry of "LINK_TITLE" and "HTTP_LINK" for each "LINK_TEXT" entry. CDAWeb will then link to the URL given by
"HTTP_LINK" using the "LINK_TITLE" and the description in "LINK_TEXT," on the CDAWeb Data Explorer page. For example:

Â· "LINK_TEXT" = 3-sec MGF magnetic field 1 Sep 1993 through 30 Sep 2015 available at

Â· "LINK_TITLE" = ISAS DARTS

Â· "HTTP_LINK" = https://www.darts.isas.jaxa.jp/stp/geotail/ will give the following link:

3-sec MGF magnetic field 1 Sep 1993 through 30 Sep 2015 available at [ISAS DARTS](https://www.darts.isas.jaxa.jp/stp/geotail/)

**LINK_TITLE --- recommended**

This attribute stores the title of the web site holding on-line data available at PI or CoI
web sites. This attribute is used in conjunction with "LINK_TEXT" and "HTTP_LINK." There can be up to 5 entries for each - there MUST be a corresponding entry of "LINK_TEXT" and "HTTP_LINK" for each "LINK_TITLE" entry. CDAWeb will then link to the URL given by "HTTP_LINK" using the "LINK_TITLE" and the description in "LINK_TEXT," on the CDAWeb Data Explorer page. For example:

Â· "LINK_TEXT" = 3-sec MGF magnetic field 1 Sep 1993 through 30 Sep 2015 available at

Â· "LINK_TITLE" = ISAS DARTS

Â· "HTTP_LINK" = https://www.darts.isas.jaxa.jp/stp/geotail/ will give the following link:

3-sec MGF magnetic field 1 Sep 1993 through 30 Sep 2015 available at [ISAS DARTS](https://www.darts.isas.jaxa.jp/stp/geotail/)

**Logical_file_id --- required**

This attribute stores the name of the CDF file using the ISTP naming convention (source_name / data_type / descriptor / date / data_version), *e.g.,* GE_K0_MGF_19920923_V01. This attribute is required (1) to allow storage of the full name on IBM PCs, and (2) to avoid loss of the original source in the case of accidental (or intentional) renaming. For CDFs created on the ISTP Central Data Handling Facilities (CDHF), the correct Logical_file_id will be filled in by an ICSS support routine.

**Logical_source --- required**

This attribute carries source_name, data_type, and descriptor information. Used by [CDAWeb](https://cdaweb.gsfc.nasa.gov/istp_public/).

**Logical_source_description --- required**

This attribute writes out the full words associated with the encrypted Logical_source
above, *e.g.,* "Geotail Magnetic Field Key Parameters." Used by [CDAWeb](https://cdaweb.gsfc.nasa.gov/istp_public/).

## Mission_group 
  required**

This attribute has a single value and is used to facilitate making choices of source through [CDAWeb](https://cdaweb.gsfc.nasa.gov/istp_public/). Valid values include (but are not restricted to):

- Geotail
- IMP8
- Wind
- Geosynchronous Investigations
- Ground-Based Investigations

**MODS --- recommended**

This attribute is a standard global attribute which is used to denote the history of modifications made to the CDF data set. The Metadata Object Description (MODS) attribute should contain a description of all significant changes to the data set. This attribute is not directly tied to Data_version, but each version produced will contain the relevant modifications. This attribute can have as many entries as necessary to contain the desired information.

**Parents --- optional**

This attribute lists the parent CDF(s) for files of derived and merged data sets. Subsequent entry values are used for multiple parents. The syntax for a CDF parent would be *e.g.* "CDF>logical_file_id."

**PI_affiliation --- required**

This attribute value should include a recognizable abbreviation.

**PI_name --- required**

This attribute value should include first initial and last name.

## Project

Required
This attribute identifies the name of the project and indicates ownership. For ISTP missions and investigations, the value used is "ISTP>International Solar-Terrestrial Physics." For the Cluster mission, the value is "STSP Cluster>Solar Terrestrial Science Programmes, Cluster." Other acceptable values are "IACG>Inter-Agency Consultative Group," "CDAWxx>Coordinated Data Analysis Workshop xx", and "SPDS>Space Physics Data System." Others may be defined in the future. This attribute can be multi-valued if the data has been supplied to more than one project.

**Rules_of_use --- recommended**

Text containing information on, {\it e.g.} citability and PI access restrictions. This may
point to a World Wide Web page specifying the rules of use.

**Skeleton_version --- optional**

This is a text attribute containing the skeleton file version number. This is a required
attribute for Cluster, but for IACG purposes it exists if experimenters want to track it.

**Software_version --- optional**

This is a required attribute for Cluster, but for IACG purposes it exists if experimenters want to track it.

## Source_name

Required
This attribute identifies the mission or investigation that contains the sensors. For ISTP,
this is the mission name for spacecraft missions or the investigation name for ground-based or theory investigations. Both a long name and a short name are provided. This attribute should be single valued. Examples:

Â· "GEOTAIL>Geomagnetic Tail"

Â· "WIND>Wind Interplanetary Plasma Laboratory"

Â· "DARN>Dual Auroral Radar Network"

Â· "GOES_7>Geostationary Operational Environmental Satellite 7"

Â· "IMP-8>Interplanetary Monitoring Platform"

Â· "LANL1989_046>Los Alamos National Laboratory 1989"

Â· "C1>Cluster Satellite No 1"

**spase_DatasetResourceID --- recommended**

Unique dataset identifier assigned by [SPASE](http://www.spase-group.org/), of the form spase://<NAMING_AUTHORITY>/<UNIQUE_ID>, where <UNIQUE_ID> is the ID assigned to the SPASE resource record for the dataset in the [SPASE system](http://www.spase-group.org/) by a SPASE <NAMING_AUTHORITY>. The SPASE resource record provides metadata about the dataset, including pointers to locations holding the data.

**TEXT --- required**

This attribute is a standard global attribute which is a text description of the
experiment whose data is included in the CDF. A reference to a journal article(s) or to a World Wide Web page describing the experiment is essential and constitutes the minimum requirement. A written description of the data set is also desirable. This attribute can have as many entries as necessary to contain the desired information.

**Time_resolution --- recommended**

specifies time resolution of the file, *e.g.,* "3 seconds."

**TITLE --- optional**

This attribute is a standard global attribute which is a title for the data set, *e.g.,* "Geotail EPIC Key Parameters."

**Validate --- optional**

Details to be specified. This attribute is written by software for automatic validation of features such as the structure of the CDF file on a simple pass/fail criterion. The software will test that all expected attributes are present and, where possible, have reasonable values. The syntax is likely to be of the form "test>result>where done>date." It is not the same as data validation.
