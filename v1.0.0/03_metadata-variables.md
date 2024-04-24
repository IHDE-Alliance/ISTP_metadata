# **Variables**

[Introduction](#Introduction)

[Complete Variable Description](#Complete-Variable-Description)

[Data](#Data)
- [General](#General)
- [Example - simple scalar density](https://github.com/IHDE-Alliance/ISTP_metadata/blob/main/v1.0.0/07_example-variables.md)
- [Example - vector magnetic field](https://github.com/IHDE-Alliance/ISTP_metadata/blob/main/v1.0.0/07_example-variables.md)
- [Example - 1D flux](https://github.com/IHDE-Alliance/ISTP_metadata/blob/main/v1.0.0/07_example-variables.md)
- [Example - 2D flux](https://github.com/IHDE-Alliance/ISTP_metadata/blob/main/v1.0.0/07_example-variables.md)

[Support_data](#Support_data)
- [General](#General)
- [Example - Epoch time](https://spdf.gsfc.nasa.gov/istp_guide/variables.html#support_data_eg1)
- [Example - 1D Energy](https://spdf.gsfc.nasa.gov/istp_guide/variables.html#support_data_eg2)
 
[Metadata](#Metadata)
- [General](#General)
- [Example - vector magnetic field labels](https://spdf.gsfc.nasa.gov/istp_guide/variables.html#Metadata_eg1)
 
[Variable Display](#Variable-Display)
- [Scalar (0D) Time Series, e.g., Solar Wind Proton Number Density, scalar](https://spdf.gsfc.nasa.gov/istp_guide/variables.html#Scalar%20(0D)%20Time%20Series)
- [1D - size 3 Time Series, e.g., Magnetic Field, cartesian GSE](https://spdf.gsfc.nasa.gov/istp_guide/variables.html#1D%20Time%20Series)
- [1D - size 12 Spectrogram , e.g., Ion Diff. Intensity, at 12 energies 67-1361 keV](https://spdf.gsfc.nasa.gov/istp_guide/variables.html#1D%20Spectrogram)
- [1D - size 7 Stack_plot, e.g., Electron Flux at 7 energies (0.1-225keV)](https://spdf.gsfc.nasa.gov/istp_guide/variables.html#1D%20Stack_plot)
- [1D - sizes 28, 12 Spectrogram , e.g., H+ number flux for selected energy and angle bins](https://spdf.gsfc.nasa.gov/istp_guide/variables.html#2D%20Spectrogram)
 
[Required support_data variables](#Required-support_data_variables)
- [Epoch (required)](#Epoch-(required))
- [Quality Flag (recommended)](#Quality-Flag-(recommended))
- [Time_PB5](#Time_PB5)
- [Post Gap Flag](#Post-Gap-Flag)

# **Introduction**

Three types of variables have been identified to be included in ISTP/IACG CDF files: **data** variables of primary importance (e.g., density, magnetic_field, particle_flux), **support_data** variables of secondary importance (e.g., time, energy_bands associated with particle_flux) and **metadata** variables (e.g., a variable holding "Bx,By,Bz" to label magnetic field). Variables are defined with CDF specifications and required attributes. Data variables also have attached variables for time and dependencies (support_data) and labels (metadata). The support_data variables can be attached to data variables via DEPEND_i variable attributes. A variable’s dimension sizes should stay static, in a data set, for the life of the mission. They should be defined as the maximum size and fill the unused dimensions with the defined fill value. Any details about the modes and associated sizes, etc. should be documented in the variable attribute var_notes or in the global attribute text. Having a variable that shows the number of steps in a sweep is benefical, so users can list/plot that along with the data. Variables should not be added or removed, or have their dimension sizes changed, for a given data set over the life of the mission. If it is necessary to do so, the user will need to reprocess all files to have a consistent structure for the life of the mission. When defining a variable’s “record variance”, consider if the values could change throughout the mission, not just for a given file. If it can change, it should be defined as “record varying.” If the values change very slowly, e.g. once every year or two, they can be defined as “PREV_SPARSERECORDS” (see the [CDF User Guide](https://cdf.gsfc.nasa.gov/html/cdf_docs.html) or programming guides for further details). Metadata variables can be attached to data variables via LABL_PTR_i variable attributes (see below).


**NOTE:** ISTP/IACG now encourages the use of zVariables which carry their own dimensionality. (The old style rVariables carry the dimensionality of the entire CDF and are intrinsically more complicated.) For more information about zVariables and rVariables consult the [CDF home page](https://cdf.gsfc.nasa.gov/).

# **Complete Variable Description**

# ***Data***

These are variables of primary importance (e.g., density, magnetic_field, particle_flux). Data variables are completely defined with the combination of CDF specifications, variable attributes, and attached variables such as time and dependencies (support_data) and labels (metadata).

***Naming***

**CDF Variable names must begin with a letter and can contain numbers and underscores, but no other special characters.**

# ***General***

The following CDF variable specifications are required. Data is always either Real or Integer type. Data is always time (record) varying, but can be of any dimensionality. Real or Integer data are always defined as having one element.

The need for DEPEND_i (other than DEPEND_0) and either LABLAXIS or LABL_PTR_i depends on the data itself and how it will be displayed. This is illustrated in examples in [Variable Display](https://spdf.gsfc.nasa.gov/istp_guide/variables.html#Variable%20Display).

# **Support_Data**

These are variables of secondary importance (e.g., time, energy_bands associated with
particle_flux).

***Naming***

**CDF Variable names must begin with a letter and can contain numbers and undercores, but no other special characters.**

# ***General***

The following CDF variable specifications are required.

Support_data is always either Real or Integer type. Support_data is usually time invariant, but can be time varying.

If a support_data variable is attached to a data variable via DEPEND_i, then it must be of the same size as the dimension i. See example below. Real or Integer data are always defined as having one element.

# **Metadata**

These are variables of secondary importance e.g., a variable holding "Bx,By,Bz" to label magnetic field).

***Naming***

**CDF Variable names must begin with a letter and can contain numbers and underscores, but no other special characters.**

# ***General***

The following CDF variable specifications are required. Metadata is always character type. Metadata is always time invariant if it is used to label a data variable. Metadata can be time varying if it is NOT used as a label. If a metadata variable is attached to a data variable via LABL_PTR_i, then it must be of the same size as the dimension i. Character metadata must define the number of elements to be the same as the number of characters used in its value.

# **Variable Display**

The dependencies and labels that need to be included with a data variable depend both on the data variable's dimensionality and on how the data variable will be displayed. They point out which attributes and associated support_data and metadata variables are used to label the display.

# **Required support_data variables**

For IACG use (expanded international community with missions outside the core ISTP) and for ISTP higher resolution definitive data or for event data, **only Epoch is now required.** A quality flag is still recommended.

# **Epoch (required)**
CDF Time variable types
- CDF_TIME_TT2000 nanoseconds from J2000 in Terrestrial Time in 8 byte integer handles leap seconds and is well-defined; UTC conversion requires up-to-date leap second table (last value stored in CDF header as a check)
- EPOCH milliseconds from 0AD in 8byte float; usually UTC but not leap seconds
- EPOCH16 picoseconds from 0AD in two 8byte float; usually UTC but not leap seconds

"Epoch" should be the first variable in each CDF data set. All time varying variables in the CDF data set will depend on the "Epoch" variable (or on a CDF_TIME_TT2000 (or CDF_EPOCH or CDF_EPOCH16) type variable) - more than one CDF_TIME_TT2000/EPOCH/EPOCH16 type variable is allowed in a data set to allow
for more than one time resolution. For ISTP the time value of a record refers to the center of the accumulation period for the record if the measurement is not an instantaneous one.

Epoch allows for a scalar representation of time which provides for seamless crossings of day and year boundaries. Epoch time is simply the time in milliseconds A.D. CDF toolkit programs will display and expect CDF_EPOCH values in the format dd-mmm-yyyy hh:mm:ss.ccc where dd is the day of the month, mmm is the month, yyyy is the year, hh is the hour, mm is the minute, ss is the second and ccc is the millisecond (e.g., 01-Aug-1992 10:30:05.025). "Epoch" will be monotonically increasing so that the attribute MONOTON should be defined as "INCREASE."

**(Note: All CDF data sets using the Epoch variable should use the subroutines provided in the CDF toolkit for making the conversion between this value and year, month, day, etc. These routines are available as black boxes from SPDF.**) To determine Epoch time it is only necessary to call the subroutine compute_Epoch (year, month, day, hour, minute, second, msec, Epoch) with arguments as shown.for making the conversion between this value and year, month, day, etc. This ensures that all users use the same conversion when generating their CDF data sets and will therefore have the same view of the effects of the various calendar changes that have occurred over the last two thousand years.)

# **Quality Flag (recommended)**

Each ISTP/IACG CDF data set should contain at least one quality or status flag which is record varying. The CDF data set designer may choose to have more than one if the data warrants this.

# **Time_PB5**

Time_PB5 is the second variable in an ISTP KP CDF data set. It is not required for IACG or ISTP higher resolution or event data. Time_PB5 is another way of presenting time
which allows for easy recognition of the time value when looking at the data, for instance in a data dump. For ISTP the time value of a record refers to the center of the accumulation period for the record if the measurement is not an instantaneous one. Time_PB5 is given in YEAR (4 digit), DAY OF YEAR (note: January 1 is Day 1), and MSEC OF DAY (elapsed ms). These are all signed integer*4 numbers and are stored as the three elements of the one-dimensional variable named "Time\_PB5", e.g. 1992, 214, 0 would be August 1, 1992 at midnight.

# **Post Gap Flag**

At the May 1992 ISTP SWG it was decided that a record varying "Post Gap" Quality
Flag would also be included in each KP record.

(Note: This I*4 Flag is included in every record and is defined in the following way: 0 - no gap occurred immediately prior to this record [thus most of the time this Flag would be set to 0]; 1 - the gap occurred because the instrument was not in a mode that allowed for the production of KPs; 2 - the gap occurred because Level Zero or SIRIUS data were missing; 3 - the gap occurred because Level Zero or SIRIUS data were too noisy to compute KPs. Integer numbers above 9 can be used by the PI team to define other gap conditions, as required.)

A variable similar to this is recommended for inclusion in CDFs to indicate real and substantial data gaps. The detailed definition of this flag should appear in the CDF metadata in the VAR_NOTES attribute.


Return to Table of Contents: [Table of Contents](00_Table_of_Contents.md)
