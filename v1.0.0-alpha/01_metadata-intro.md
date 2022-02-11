**International Solar-Terrestrial Physics (ISTP) Metadata Guidelines**

**Introduction**

This document addresses the required and optional types of metadata. Global attributes, variable attributes and types of variables are defined, as well as examples of each type. The examples are included in Appendix A. Data acquired in different countries/institutes/agencies are usually stored in various format (cdf, hdf, ascii, binary, idl 
saveset) more or less exotic with no standard header, information, description. This current status makes it difficult to cross-compare different data sets (it is always necessary to develop dedicated routines usually done several times throughout the world). Guidelines are needed from the worldwide community of developers of space radiation data bases to permit standardization of data file format and therefore minimize efforts for data users. 

A Common Data Format (CDF) data set using ISTP/Interagency Consultative Group (IACG) guidelines, by definition forms a logically complete and self-sufficient whole (data and descriptions). The goal is to make the resulting CDF data set correctly and independently usable by the science community and accessible through the CDAWeb Display and Retrieval system. A CDF file is composed of global attributes which provide descriptions of the whole data set, variables, and variable attributes. This file format can contain metadata and various types of data variables in a single file. Data files in CDF are endian-independent and can be read by various programming languages and commercial software on all of major operating systems because the library codes to read CDF files are made available for them by National Aeronautics and Space Administration/Goddard Space Flight Center (NASA/GSFC).

Metadata is information which describes a dataset. It should be complete, that is, contain all the information required to read and interpret the bits (syntactic description), and to understand what the resulting numerical values (or bit strings) represent (semantic description), including how the data was obtained; the latter information impacts upon the scientific significance of the data. Metadata is always character type. Metadata is always time invariant if it is used to label a data variable. Metadata can be time varying if it is NOT used as a label. If a metadata variable is attached to a data variable via LABL_PTR_i, then it must be of the same size as the dimension i. Character metadata must define the number of elements to be the same as the number of characters used in its value.


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
