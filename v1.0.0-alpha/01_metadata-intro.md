***International Solar-Terrestrial Physics (ISTP) Metadata Guidelines***

**Introduction**

This document addresses the required and optional types of metadata. Global attributes, variable attributes and types of variables are defined, as well as examples of each type. The examples are included in Appendix A. Data acquired in different countries/institutes/agencies are usually stored in various format (cdf, hdf, ascii, binary, idl 
saveset) more or less exotic with no standard header, information, description. This current status makes it difficult to cross-compare different data sets (it is always necessary to develop dedicated routines usually done several times throughout the world). Guidelines are needed from the worldwide community of developers of space radiation data bases to permit standardization of data file format and therefore minimize efforts for data users. 

Metadata is information which describes a dataset. It should be complete, that is, contain all the information required to read and interpret the bits (syntactic description), and to understand what the resulting numerical values (or bit strings) represent (semantic description), including how the data was obtained; the latter information impacts upon the scientific significance of the data. 


[Global Attributes](02_metadata-global-attributes.md)

[Variable Attributes](03_metadata-variable-attributes.md)

[Variables](04_metadata-variables.md)

[Keywords](05_metadata-keywords.md)

[Tools](06_metadata-tools.md)

[Example variables](07_example-variables.md)

[Example skeleton tables](08_example-skeletontables.md)

[Example displays](09_example-displays.md)

[Example PB5 times](10_example-PB5-times.md)

[Example subclass keywords](11_example-subclass-keywords.md)


# try hiding sections
<details><summary>Global attributes</summary>
  # Global Attributes

Global attributes are used to provide information about the data set as an entity. Together with variables and variable attributes, the global attributes make the data correctly and independently usable by someone not connected with the instrument team, and hence, a good archive product. The global attributes are also used by the Coordinated Data Analysis Web ([CDAWeb)](https://cdaweb.gsfc.nasa.gov/) Display and Retrieval system. The required Global Attributes are listed here with example values. Note that Common Data Format (CDF) attributes are case-sensitive and must **exactly** follow what is shown here. Additional Global attributes can be defined but **they must start with a letter and can otherwise contain letters, numbers and the unscore character (no other special characters allowed).** See [Global Attribute Definitions](https://spdf.gsfc.nasa.gov/istp_guide/gattributes.html#gdefinitions) for the full set of defined Global Attributes.
</details>


  ## failed attempts at including other markdown files:
  
  
Try as include:
@@include[02_metadata-global-attributes.md](02_metadata-global-attributes.md)

:(02_metadata-global-attributes.md)

!!!(02_metadata-global-attributes.md)!!!

@[:markdown](02_metadata-global-attributes.md)

{02_metadata-global-attributes.md}

{% include "02_metadata-global-attributes.md" %}

{% include "git+https://github.com/HDE-Alliance/ISTP_metadata/edit/main/v1.0.0-alpha/01_metadata-intro.md" %}

<iframe src="02_metadata-global-attributes.md" seamless></iframe>
