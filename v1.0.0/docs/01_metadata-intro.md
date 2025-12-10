# Introduction

In the 1990s, collaborations between the National Aeronautics and Space Administration (NASA), European Space Agency (ESA), Institute of Space and Astronautical Science (ISAS) of Japan, and Academy of Sciences (Russia)/Rosaviakosmos resulted in the International Solar-Terrestrial Physics ([ISTP](https://pwg.gsfc.nasa.gov)) science initiative to combine resources and scientific communities for coordinated, simultaneous investigations of the Sun-Earth space environment over an extended period of time.

As part of the ISTP initiative in the early 1990's,  Ramona L. Kessel and Robert E. McGuire at the NASA Space Physics Data Facility ([SPDF](https://spdf.gsfc.nasa.gov)) and others in the science community began coordinated development of the ISTP Metadata Guidelines for  use by the Polar, Wind, Geotail, and Cluster missions. The ISTP Guidelines were later adopted by the Interagency Consultative Group (IACG) for Space Science, and are now used by most of the major heliophysics missions, including MMS, Van Allen Probes, Parker Solar Probe, and Solar Orbiter. The ISTP Guidelines fall between *Specification* and *International Standard*, and are accepted as a *best practice*. 

A dataset in a self-describing scientific data format, e.g., Common Data Format ([CDF](https://cdf.gsfc.nasa.gov)) or [netCDF](https://www.unidata.ucar.edu/software/netcdf/), using the ISTP Guidelines forms a logically complete and self-sufficient whole (data and descriptions). This document describes the required and optional types of metadata that provide definitive description of the data in each variable and the dataset as a whole. The goal is to make each scientific dataset correctly and independently usable and accessible by the science community into the future, and to enable analysis and display by generalized software applications such as Coordinated Data Analysis Web display and retrieval system ([CDAWeb](https://cdaweb.gsfc.nasa.gov)), [Autoplot](https://autoplot.org), and [SPEDAS](https://spedas.org). Using a common set of metadata also enables cross-comparison of different datasets. The document defines global attributes (information about the dataset as an entity), variable attributes (information about individual variables), types of ISTP variables, and provide their examples.

The most common practice in the heliophysics in-situ community is currently to use the CDF standard file format for disseminating heliophysics observations. For this reason, this document describes how to include the metadata content through attributes inside CDF files, but that does not preclude the  use of other file formats such as netCDF. In many ways, this document simply uses CDF notation as a language to express the underlying metadata requirements. There are many attributes that are not mentioned in this document which have established definitions in various mission documents, other references, and existing or past projects. As far as possible, such attributes should be used when appropriate, and should not be used in conflict with that definition. New attributes should not be invented if there is already an attribute in established use that covers the needs. In general, see the [Non-ISTP Mission Global Attributes](Non-ISTP-Mission-Global-Attributes.md) and [Non-ISTP Mission Variable Attributes](Non-ISTP-Mission-Variable-Attributes.md) appendices before inventing new attributes. Please propose changes and new attributes as tickets on the [Github](https://github.com/IHDE-Alliance/ISTP_metadata/tree/main) site if they are appropriate for other missions to use.

Some missions that adopted the ISTP metadata guidelines have their own documents describing their requirements. Some of these are stored at [SPDF](https://spdf.gsfc.nasa.gov/pub/documents/metadata/istp-guidelines/).

## Why Standardize Metadata
- Standardized self-describing data formats, metadata for datasets and parameters, time conventions, and dataset and filenaming conventions enable effective data analysis and browsing using generic easy-to-use software and web services.
- Restricting metadata representations limits the number of equivalent possibilities with which software must deal, and thus fosters interoperability.
- Conventions standardize ways to name things, represent relationships, and locate data in space and time.
- Enables developing applications with powerful extraction, regridding, analysis, visualization, and processing capabilities.
- Abstracts general data models to represent data semantics.
- Embodies the data provider’s experience and capture the meaning in data and make data semantics accessible to humans as well as programs.
- Provides higher-level abstractions such as coordinate systems, standard names for physical quantities for comparing different data, and distinguish variables.


## ISTP Guidelines Structure and Concepts
- Data is time-ordered and time-identified; in CDF, times vary by record.
- Multiple time variables in a file, allowing data variables with different time cadences.
- Set of required and recommended metadata (as defined in this document).
- Structure of each variable (variable data type, number of its dimensions, and the dimension sizes) stays unchanged throughout the entire mission (all dataset files).
- Variables can carry metadata, e.g., labels for dimensional variables.
- Variable attributes can point to other variables by name and carry arguments, thus providing information about relationships among variables.
- Slowly-varying data should be stored as variables rather than in attributes (CDF variables can be defined with record sparseness set to previous record, allowing storing only records that changed).
- Skeleton CDF is a CDF with structure and metadata defined but no data, so it can be used as a template from which to build a data CDF file. [NetCDF Common Data Language (CDL)](https://docs.unidata.ucar.edu/nug/2.0-draft/cdl.html) is the netCDF equivalent.
- General dataset and file naming conventions.

## Defining a Dataset
General guidelines for defining a dataset may include answering the following questions:
- How were the measurements obtained?
- What information would future users need to fully understand these data?
- What are the key data quantities?
- What is their definition/meaning?
- How will they be named?
- Understand (at the dataset level) the dimensionality, dependencies, and variance with time and dimensions.

The overall purpose for the dataset and its connections to the missions, instruments, people, and organizations are provided in the [Global Attributes](./03_metadata-global-attributes.md). The data structure and relationships are captured in the variable structure and [Variable Attributes](./05_metadata-variable-attributes.md). The relationships should be logically structured, machine-readable, and available for general-purpose codes to understand. In particular, the following variable attributes are often required for automated processing:
- `FIELDNAM` short variable name for plots.
- `CATDESC` for longer variable description.
- `DEPEND_0` points to time variable describing time dimension (record dimension in CDF).
- `DEPEND_i` point to variables that describe higher dimensions.
- `LABLAXIS`/`LABL_PTR_i` for axis and column titles.
- `UNITS`/`UNIT_PTR` for units.
- `VALIDMIN`/`VALDMAX` for valid data range.
- `FILLVAL` values indicating missing or bad data.

---
Return to [Table of Contents](../README.md)
