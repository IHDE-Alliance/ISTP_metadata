
# Best practices for creating a ISTP-compliant dataset in CDF and netCDF formats

## Dataset and filenaming recommmendations
Follow the SPDF [Recommended File and Data Collection Naming Practices](https://spdf.gsfc.nasa.gov/guidelines/filenaming_recommendations.html)

### note: perhaps move the above file into the ISTP Github and change SPDF pointer to it

## CDF-specific practices

## netCDF-specific practices
- Use time as the unlimited dimension
- Define variables to hold the values for each dimension
- Do not use netCDF groups, unsigned 64-bit integers, or user-defined variable types, since these are not widely supported by generalized science software
- Provide two global attributes `Data_Start` and `Data_End` with value = yyyy-mm-ddThh:mm:ss UTC

Recommend using the CDF_TIME_TT2000 variable type as 8-byte integers in netCDF, and using the CDF library routines for conversion to and from other time formats. Otherwise, time variables should be in seconds from some epoch, with `UNITS` of "seconds since 2000-01-01", for instance.

In addition to the ISTP-defined `FILLVAL`, `CATDESC` and `UNITS`, netCDF conventions call for also storing in `_FillValue`, `long_name`, and `units`, respectively.  See [netCDF Attribute Conventions](https://docs.unidata.ucar.edu/netcdf-c/4.9.2/attribute_conventions.html)


## Tools for laying out the dataset

## Metadata editors
- Browser--based [ISTP Metadata Editor](https://spdf.gsfc.nasa.gov/istp-metadata-editor/) 

- [SKTEditor](https://spdf.gsfc.nasa.gov/skteditor/), a Java downloadable program that aids the user with the creation of a Skeleton CDF.

## Adding Data to Skeleton CDFs

### Use IDLmakecdf program

produces a CDF file using IDL with a Skeleton CDF file and user-supplied IDL code to read user data.

- [IDLmakecdf](https://spdf.gsfc.nasa.gov/CDAWlib.html) (IDL software and on-line help)

### Use makeCDF program

produces a CDF file (using C) when given 3 input files: (1) data file, (2) translation file, (3) Skeleton CDF file.
- [On-line Tutorial](https://spdf.gsfc.nasa.gov/makecdf.html#help)
- [makeCDF program](https://spdf.gsfc.nasa.gov/makecdf.html)