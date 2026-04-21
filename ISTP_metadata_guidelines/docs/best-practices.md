
# Best Practices for Creating ISTP-compliant Datasets in CDF and netCDF Formats

## Dataset and File Naming Recommmendations
- Follow the SPDF [Recommended File and Dataset Naming Practices](./filenaming-dataset-naming-recommendations.md)

## CDF-Specific Practices
If extremely rare changes occur in the variable values over time, a CDF variable can be defined with **record sparseness set to previous record**. In this case, only records with changes need to be explicitly written into the CDF file, while reading any record will return the last explicitly written record before the requested one. Note that the first variable record in each CDF file still must be explicitly written with valid value. See the [CDF User's Guide](https://spdf.gsfc.nasa.gov/pub/software/cdf/doc/cdf_User_Guide.pdf) for details on CDF variable sparse records.

## netCDF-Specific Practices
- Use time as the unlimited dimension
- Define variables to hold the values for each dimension
- Do not use netCDF groups, unsigned 64-bit integers, or user-defined variable types, since these are not widely supported by generalized science software
- Provide two global attributes `Data_Start` and `Data_End` with value = yyyy-mm-ddThh:mm:ss UTC

Recommend using the CDF_TIME_TT2000 variable type as 8-byte integers in netCDF, and using the CDF library routines for conversion to and from other time formats. Otherwise, time variables should be in seconds from some epoch, with `UNITS` of "seconds since 2000-01-01", for instance.

In addition to the ISTP-defined `FILLVAL`, `CATDESC` and `UNITS`, netCDF conventions call for also storing in `_FillValue`, `long_name`, and `units`, respectively.  See [netCDF Attribute Conventions](https://docs.unidata.ucar.edu/netcdf-c/current/attribute_conventions.html).


## Tools for Laying out Datasets

### Metadata Editors
- Browser-based [ISTP Metadata Editor](https://spdf.gsfc.nasa.gov/istp-metadata-editor/) for creating and editing ISTP guideline compliant CDF, skeleton (SKT), and netCDF files

- Original Java based [ISTP CDF Skeleton Editor](https://spdf.gsfc.nasa.gov/skteditor/)

### Adding Data to Skeleton CDFs

#### Use IDLmakecdf Program

Produces a CDF file using IDL with a Skeleton CDF file and user-supplied IDL code to read user data.

- [IDLmakecdf](https://spdf.gsfc.nasa.gov/CDAWlib.html#IDLmakecdf) (IDL software and on-line help), part of [CDAWlib](https://spdf.gsfc.nasa.gov/CDAWlib.html)

#### Use makeCDF Program

Produces a CDF file (using C) when given 3 input files: (1) data file, (2) translation file, (3) Skeleton CDF file.
- [makeCDF program](https://spdf.gsfc.nasa.gov/makecdf.html)

### CDF Libraries
- [Quick start guides](https://cdf.gsfc.nasa.gov/quickstartguides/) for systems and programming languages
- [CDF software](https://cdf.gsfc.nasa.gov/html/sw_and_docs.html)
- [CDF homepage](https://cdf.gsfc.nasa.gov/)


---
Return to [Table of Contents](../README.md)
