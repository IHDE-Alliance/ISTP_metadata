# International Solar-Terrestrial Physics (ISTP) Metadata Guidelines

## Introduction

In the 1990s, collaborations between NASA, the European Space Agency (ESA), the Institute of Space and Astronautical Science (ISAS) of Japan, and the Academy of Sciences (Russia)/Rosaviakosmos resulted in the International Solar-Terrestrial Physics ([ISTP](https://pwg.gsfc.nasa.gov)) science initiative to combine resources and scientific communities to obtain coordinated, simultaneous investigations of the Sun-Earth space environment over an extended period of time. ISTP was the flagship mission for the space physics scientific community, the "great observatory" of the 1990's. It was later adopted by the Interagency Consultative Group (IACG), and now by most heliophysics missions.

This document describes the required and optional types of metadata that provide a definitive description of what the data in each variable represents, and enable building generalized analysis and display applications. The goal is to make each scientific dataset correctly and independently usable and accessible by the science community into the future, and enables analysis and display by generalized software applications such as Coordinated Data Analysis Web display and retrieval system ([CDAWeb](https://cdaweb.gsfc.nasa.gov)), [Autoplot](https://autoplot.org) and [SPEDAS](https://spedas.org). Using a common set of metadata also enables cross-comparison of different data sets. Global attributes, variable attributes and types of variables are defined, as well as examples of each type.

A Common Data Format ([CDF](https://cdf.gsfc.nasa.gov)) or [netCDF](https://www.unidata.ucar.edu/software/netcdf/) dataset using the ISTP guidelines forms a logically complete and self-sufficient whole (data and descriptions). CDF and netCDF data files are platform-independent and can be read by various programming languages and commercial software.

Metadata is information which describes a dataset. It should contain all the information required to read and interpret the bits (syntactic description), and to understand what the resulting numerical values (or bit strings) represent (semantic description), including how the data was obtained, enhancing the scientific significance of the data.

Global attributes, variable attributes, and variables are included in the metadata. Global attributes are used to provide information about the data set as an entity. Variable attributes are linked with each individual variable, and provide additional information about each variable.

## History

Ramona L. Kessel and Robert E. McGuire at the NASA Space Physics Data Facility ([SPDF](https://spdf.gsfc.nasa.gov)) and others began coordinating development of the ISTP Guidelines in the early 1990's as part of the ISTP project and used by the Polar, Wind, Geotail, and Cluster missions initially and then adopted by later missions, including MMS, Van Allen Probes, Parker, and Solar Orbiter.

The ISTP Guidelines were adopted internationally, and are used by most major heliophysics missions because they provide critical value in understanding the data by researchers outside the specific teams. The ISTP Guidelines fall between Specification and International Standard, and are accepted as a best practice.

## Why Standardized Metadata
- Standardized self-describing data formats, metadata for datasets and parameters, time conventions, and dataset and filenaming conventions enable effective data analysis and browsing using generic easy-to-use software and web services
- Restricting metadata representations limits the number of equivalent possibilities with which software must deal, and thus fosters interoperability
- Conventions standardize ways to name things, represent relationships, and locate data in space and time
- Enables developing applications with powerful extraction, regridding, analysis, visualization, and processing capabilities
- Abstracts general data models to represent data semantics
- Embodies the provider’s experience and capture the meaning in data and make data semantics accessible to humans as well as programs
- Provide higher-level abstractions such as coordinate systems, standard names for physical quantities for comparing different data, and distinguish variables

## Self-describing Scientific Data Formats
- [FITS](https://fits.gsfc.nasa.gov/) is used in astronomy and solar physics with FITS and WCS metadata
- [HDF](https://www.hdfgroup.org/) is used in Earth sciences with [HDF-EOS](https://hdfeos.org) metadata]
- [netCDF](https://www.unidata.ucar.edu/software/netcdf/) in atmosphere with [Climate and Forecast](https://cfconventions.org) metadata], and in Ionosphere, Thermosphere, and Mesosphere (ITM) with ISTP metadata. Development started in 1988. netCDF compression requires careful block size determination.
-- ISTP Guidelines use the netCDF4 Classic model with no groups or user-defined variable types, and time as the unlimited dimension
- [CDF](https://cdf.gsfc.nasa.gov/) is used in the rest of Heliophysics with ISTP Guidelines metadata. CDF started in 1984 on a Modcomp computer and converted to C in 1990, and now available via libraries in many programming languages.
--  PDS added CDF-A as standard format (in addition to PDS-3, PDS-4, JPEG) and defined as CDFs with ISTP Guidelines and two SPASE attributes, but no compression or sparse variables

## ISTP Guidelines Structure and Concepts
- Data is time-ordered and time-identified; times vary by record
- Set of required and suggested metadata (as defined in this document)
– Variables can carry metadata (e.g. labels for dimensional variables)
- Variable attributes can point to other variables by name and carry arguments, and thus carry information about relationships among variables
- Skeleton CDF is a CDF with structure and metadata defined but no data, so it can be used as a template from which to build a data file
- General dataset and file naming conventions
- ISTP conventions allow more than one time variable in a file
- Carry slowly-varying data as variables rather than in attributes (CDF includes a sparse=sRecords.PREV key that only store the numbers when changed)

### Defining a Dataset
- What are the key data quantities?
- What is their definition/meaning?
- How are they going to be named?
- Understand (at the dataset level) the dimensionality and dependencies, and variance with time and dimension

The general rule is to capture the relationships in the structure and in the variable attributes. The relationships should be logically-structured and machine-readable, and available for general-purpose codes to understand. Let the CDF or netCDF file structure deal with the mechanics of efficient data storage. Essentially, lay out the data by what is scientifically logical and useful.

## CDF/netCDF Files and Components

### Naming of files and datasets

CDF files should have the file name extension ".cdf", and netCDF files should end in ".nc". [Recommended file and data
    collection naming practices](https://spdf.gsfc.nasa.gov/guidelines/filenaming_recommendations.html).

### Naming Conventions

Variable, dimension, attribute and group names should begin with a letter and be composed of letters, digits, and underscores. Attributes with leading underscores in names are reserved for system use.

Case is significant in variable and attribute names, but it is recommended that names should not be distinguished purely by case, i.e., if case is disregarded, no two names should be the same. It is also recommended that names should be obviously meaningful, if possible, as this renders the file more effectively self-describing.

This convention does not standardize any variable or dimension names, although other conventions do. Attribute names and their contents, where standardized, are given in English in this document and should appear in English in conforming files for the sake of portability. Languages other than English are permitted for variables, dimensions, and non-standardized attributes. The content of standardized attributes should be in English.

### Dimensions

Dimensions 

### Variable attributes

In particular, the following variable attributes are often required for automated processing:
- CATDESC for longer variable description
- DEPEND_0 points to time variables
- DEPEND_1, 2, 3 point to variables that describe other dimensions
- FIELDNAM short variable name for plots
- FILLVAL values indicating missing or bad data
- LABLAXIS/LABL_PTR for axis and column titles
- UNITS/UNIT_PTR for units
- VALIDMIN/VALDMAX for valid data range



Return to Table of Contents: [Table of Contents](00_Table_of_Contents.md)
