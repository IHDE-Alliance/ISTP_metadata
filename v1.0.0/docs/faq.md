
# Frequently Asked Questions (FAQ)

This page covers many of the most common questions asked about the ISTP Guidelines.
If you have a question that isn't on this list, please open a ticket on the ISTP Guidelines Github site, so that the ISTP Guidelines community can respond.
We will use that list as the basis for additional content for this set of questions.

Some links in this FAQ may point to previously released versions of the ISTP Guidelines specification.

## ISTP Guidelines background
This section includes general background about the ISTP Guidelines.

### What are the ISTP Guidelines, and what do they include?

The ISTP Guidelines metadata are designed to promote the processing and sharing of Heliophysics non-solar data in self-describing scientific data formats (including CDF and netCDF files).
The Guidelines define metadata that provide a definitive description of what the data in each variable represents, and enable building generalized analysis and display applications.

### What are the principles of the ISTP Guidelines?
Principles of the ISTP Guidelines include self-describing data (no external tables needed for understanding); metadata equally readable by humans and software; minimum redundancy and maximum simplicity; and a development process focusing on existing needs.

### Who manages the ISTP Guidelines?

The ISTP Guidelines are maintained by volunteers in the Heliophysics community. [define a governance document and rules for changes, email list, Github issues?]

### How long have the ISTP Guidelines been around? Is it mature?

Ramona L. Kessel and Robert E. McGuire at the NASA Space Physics Data Facility ([SPDF](https://spdf.gsfc.nasa.gov)) began coordinating development of the ISTP Guidelines in 1991 as part of the International Solar-Terrestrial Physics Project ([ISTP](https://pwg.gsfc.nasa.gov)). It was used by the Polar, Wind, and Geotail missions initially and then adopted by later missions, including Cluster, MMS, Van Allen Probes.

### How does the ISTP Guidelines relate to other guidelines/specifications?
Earth sciences has a similar set of metadata guidelines in the [CF conventions](https://cfconventions.org/)

## Working with the ISTP Guidelines
Learning about and changing the ISTP Guidelines.

### How do I propose a change?

Changes to the ISTP Guidelines standard are generally proposed by opening an issue on the Github site.

### What is the process for accepting a change to the ISTP Guidelines?

The community discusses requests for changes proposed on the Github site. If no one raises objections or concerns about the change (modified as needed to address any issues), it is considered accepted.

## Common questions about the ISTP Guidelines details

### My file was written using an earlier version of the ISTP Guidelines. Is it still compliant?

As a general rule, tools that work with files following the ISTP Guidelines should support all versions of the Guidelines. Where possible, previously defined elements of the ISTP Guidelines are not invalidated by subsequent versions.

### How can I describe a file with multiple time coordinates?

Datasets can have multiple time variables, with some variables depending on one time variable or another.  This dependency is defined by the DEPEND_0 variable attribute, that contains a string giving the name of the associated time variable. Other dimensions should also point to associated variables using the DEPEND_1, DEPEND_2, etc. variable attributes.


---
This FAQ used as a template the one at the [CF Conventions](https://github.com/cf-convention/cf-convention.github.io).

Return to [Table of Contents](../README.md)
