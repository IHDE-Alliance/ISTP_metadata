**Appendix A- Examples**


Examples of data and support_data variables commonly found in ISTP/IACG investigations are shown in the image below. They are mapped to their corresponding dimensions and sizes in CDF.

![image](https://user-images.githubusercontent.com/94626382/163575651-588e8af0-d722-4235-ae49-9d2a9c8b6bca.png)


- Density and Temperature (**data**) in this example are scalars; in CDF they are associated with zero dimension and no size.

- Plasma velocity, electric and magnetic fields (**data**) are vectors, i.e., three
orthogonal components in some coordinate system, stored in one-dimension of size 3.

- Particle flux, for this example, has values at eight energy channels. Flux (**data**) and Energy (**support_data**) are stored as one-dimensional variables of size 8.

- The image array (**data**) maps into a two-dimensional variable with sizes 256 and 256. Latitude and longitude (**support_data**) are one-dimensional variables of size 256, providing the necessary coordinate indices for the image array.

***Data***
# ***Example of a simple scalar data variable***

We show here the variable, Ion number density, as it would appear in a CDF Skeleton table. We include all required variable attributes. Some recommended variable attributes are also shown. See the [Display](https://spdf.gsfc.nasa.gov/istp_guide/variables.html#Scalar%20(0D)%20Time%20Series) of this variable.

```
! Variable       Data             Number                              Record          Dimension
! Name           Type             Elements      Dims      Sizes       Variance        Variances
! --------       ----             --------      ----      -----       --------        ---------

"SW_P_Den"      CDF_REAL4           1            0                       T

! Attribute       Data
! Name            Type          Value 
! --------        ----          -----

 "CATDESC"       CDF_CHAR       { "Ion number density (Solar Wind " -"Analyzer), scalar" }
 "DEPEND_0"      CDF_CHAR       { "Epoch" }
 "DICT_KEY"      CDF_CHAR       { "density>ion_number" }
 "DISPLAY_TYPE"  CDF_CHAR       { "time_series" }
 "FIELDNAM"      CDF_CHAR       { "Ion Number Density (CPI/SWA)" }
 "FILLVAL"       CDF_REAL4      { -1.0e+31 }
 "FORMAT"        CDF_CHAR       { "f8.3" }
 "LABLAXIS"      CDF_CHAR       { "Ion N" }
 "UNITS"         CDF_CHAR       { "#/cc" }
 "VALIDMIN"      CDF_REAL4      { 0.01 }
 "VALIDMAX"      CDF_REAL4      { 1000.0 }
 "VAR_NOTES"     CDF_CHAR       { "Assuming no helium (0.3 - several " - "hundred) if the density is less than " -
                                   "0.3/cc the higher moments (VEL,TEMP) " - "shall not be used because of the poor "
                                   - "counting statistics." }

 "VAR_TYPE"      CDF_CHAR       { "data" }.
```

***Example of a vector magnetic field data variable***

We show here the variable, Vector Magnetic Field, as it would appear in a CDF Skeleton table. We include all required variable attributes. Some recommended variable attributes are also shown. See the [Display](https://spdf.gsfc.nasa.gov/istp_guide/variables.html#1D%20Time%20Series) of this variable.

(Magnetic Field does not need a DEPEND_1 because it does not depend on any support_data. In past versions of the ISTP/IACG Guidelines we tied vectors to their coordinate system, but this is not really needed and so we have dropped the requirement. It is still allowable to include the tie via DEPEND_1.)

To see the LABL_PTR_1 values referenced below, see the label_B_GSE variable definition [below](https://spdf.gsfc.nasa.gov/istp_guide/variables.html#Metadata_eg1).

```
! Variable        Data        Number                            Record         Dimension
! Name            Type        Elements        Dims    Sizes     Variance       Variances
! --------        ----        --------        ----    -----     --------       ---------

"BGSE"           CDF_REAL4        1              1      3         T                 T

 ! Attribute       Data
 ! Name            Type         Value
 ! --------        ----         -----

 "FIELDNAM"      CDF_CHAR      { "Magnetic field vector in GSE " - "coordinates (1 min)" }
 "VALIDMIN"      CDF_REAL4     { -65534.0 }
 "VALIDMAX"      CDF_REAL4     { 65534.0 }
 "UNITS"         CDF_CHAR      { "nT" }
 "FORMAT"        CDF_CHAR      { "E13.6" }
 "SCALETYP"      CDF_CHAR      { "linear" }
 "CATDESC"       CDF_CHAR      { "Magnetic field vector in GSE" - "cartesian coordinates (1 min)" }
 "FILLVAL"       CDF_REAL4     { -1.0e+31 }
 "LABL_PTR_1"    CDF_CHAR      { "label_B_GSE" }
 "DEPEND_0"      CDF_CHAR      { "Epoch" }
 "VAR_TYPE"      CDF_CHAR      { "data" }.

```
***Example of a 1D flux data variable***

We show here the variable, Ion Differential Intensity, as it would appear in a CDF Skeleton table. We include all required variable attributes. Some recommended variable attributes are also shown. See the [Display](https://spdf.gsfc.nasa.gov/istp_guide/variables.html#1D%20Spectrogram) of this variable.

```
! Variable             Data        Number                          Record      Dimension
! Name                 Type        Elements      Dims    Sizes     Variance    Variances
! --------             ----        --------      ----    -----     --------    ---------

 "IDiffI_I"            CDF_REAL4      1            1      12         T            T

 ! Attribute        Data
 ! Name             Type           Value
 ! --------         ----           -----

 "FIELDNAM"         CDF_CHAR       { "Spin-avg Ion Diff Inten (EPIC/ICS)" }
 "CATDESC"          CDF_CHAR       { "Ion Diff. Intensity, at 12 energies " - "67-1361 keV (EPIC/ICS)" }
 "VALIDMIN"         CDF_REAL4      { 1.000000e-04 }
 "VALIDMAX"         CDF_REAL4      { 1.000000e+10 }
 "SCALETYP"         CDF_CHAR       { "log" }
 "UNITS"            CDF_CHAR       { "1/[cm**2-s-sr-keV]" }
 "LABLAXIS"         CDF_CHAR       { "dJ/dE" }
 "FORMAT"           CDF_CHAR       { "E9.3" }
 "DEPEND_0"         CDF_CHAR       { "Epoch" }
 "DEPEND_1"         CDF_CHAR       { "IDiffI_I_Energy" }
 "DELTA_PLUS_VAR"   CDF_CHAR       { "IDiffI_I_Uncert" }
 "DELTA_MINUS_VAR"  CDF_CHAR       { "IDiffI_I_Uncert" }
 "DICT_KEY"         CDF_CHAR       { "particle_flux>ion_differential" }
 "VAR_TYPE"         CDF_CHAR       { "data" }
 "FILLVAL"          CDF_REAL4      { -1.000000e+31 }
 "DISPLAY_TYPE"     CDF_CHAR       { "spectrogram" } .

```
***Example of a 2D sizes 28,12 data variable***

We show here the variable, H+ number flux, as it would appear in a CDF Skeleton table. We include all required variable attributes. Some recommended attributes are also shown. See the [Display](https://spdf.gsfc.nasa.gov/istp_guide/variables.html#2D%20Spectrogram) of this variable.

```
! Variable             Data             Number                       Record       Dimension
! Name                 Type             Elements    Dims    Sizes    Variance     Variances
! --------             ----             --------    ----    -----    --------     ---------

 "Flux_H"              CDF_REAL4          1           2     28 12      T             T T

 ! Attribute          Data
 ! Name               Type           Value
 ! --------           ----           -----

 "FIELDNAM"           CDF_CHAR       { "H+ number flux" }
 "VALIDMAX"           CDF_REAL4      { 1.0e+08 }
 "UNITS"              CDF_CHAR       { "#/(cm^2-s-keV/e-sr)" }
 "FORMAT"             CDF_CHAR       { "e12.4" }
 "LABL_PTR_1"         CDF_CHAR       { "H_energy_of_flux" }
 "LABL_PTR_2"         CDF_CHAR       { "H_angle_of_flux" }
 "MONOTON"            CDF_CHAR       { "FALSE " }
 "FILLVAL"            CDF_REAL4      { -1.0e+31 }
 "CATDESC"            CDF_CHAR       { "H+ number flux for for 28 energy and " - "3 selected angle bins." }
 "VAR_TYPE"           CDF_CHAR       { "data" }
 "DICT_KEY"           CDF_CHAR       { "particle_flux>number_species_proton" }
 "DEPEND_0"           CDF_CHAR       { "Epoch_H" }
 "DEPEND_1"           CDF_CHAR       { "energy" }
 "DEPEND_2"           CDF_CHAR       { "angle" }
 "AVG_TYPE"           CDF_CHAR       { "standard" }
 "DISPLAY_TYPE"       CDF_CHAR       { "spectrogram>y=energy,z=Flux_H(*,1),z=F" -  "lux_H(*,7),z=Flux_H(*,12)" }
 "SCALETYP"           CDF_CHAR       { "log" }
 "VAR_NOTES"          CDF_CHAR       { "Negative values reflect low counting " - "rates and background subtraction. " } .

```

**Support_Data**

***Example of Epoch time***

We show here the variable, Epoch as it would appear in a CDF Skeleton table. We include all required variable attributes. Some recommended attributes are also shown. Epoch is time varying and is attached to all time varying data variables via DEPEND_0. It is used for the x-axis in all displays below.

```
!Variable          Data      Number                          Record        Dimension
!Name              Type      Elements      Dims    Sizes     Variance      Variances
!--------          ----      --------      ----    -----     --------      ---------

 "Epoch"           CDF_EPOCH     1           0                  T

 ! Attribute         Data
 ! Name              Type              Value
 ! --------          ----              -----

 "FIELDNAM"          CDF_CHAR          { "Time since 0 AD" }
 "VALIDMIN"          CDF_EPOCH         { 01-Jan-1994 00:00:00.000 }
 "VALIDMAX"          CDF_EPOCH         { 01-Jan-2020 00:00:00.000 }
 "LABLAXIS"          CDF_CHAR          { "Epoch" }
 "UNITS"             CDF_CHAR          { "ms" }
 "FILLVAL"           CDF_REAL8         { -1.0e+31 }
 "VAR_TYPE"          CDF_CHAR          { "support_data" }
 "DICT_KEY"          CDF_CHAR          { "time>Epoch" }
 "SCALETYP"          CDF_CHAR          { "linear" }
 "MONOTON"           CDF_CHAR          { "INCREASE" }
 "CATDESC"           CDF_CHAR          { "Interval centered time tag rounded to " -  "nearest msecond "}.

```
 ! RV values were not requested.

***Another Example of "Epoch" is shown below.***

```
! Variable        Data      Number                               Record      Dimension
! Name            Type      Elements     Dims      Sizes         Variance    Variances
! --------        ----      --------     ----      -----         --------    ---------

 "Epoch"          CDF_TIME_  TT2000       1         0               T

 ! VAR_COMPRESSION: None
 ! (Valid compression: None, GZIP.1-9, RLE.0, HUFF.0, AHUFF.0)
 ! VAR_SPARSERECORDS: None
 ! (Valid sparserecords: None, sRecords.PAD, sRecords.PREV)
 ! VAR_PADVALUE: 0000-01-01T00:00:00.000000000

 ! Attribute        Data
 ! Name             Type             Value
 ! --------         ----             -----

 "CATDESC"          CDF_CHAR        { "Interval centered time tag (TBC)" }
 "FIELDNAM"         CDF_CHAR        { "Time since Jan 1, 1958" }
 "FILLVAL"          CDF_TIME_TT2000 { 9999-12-31T23:59:59.999999999 }
 "LABLAXIS"         CDF_CHAR        { "Epoch" }
 "UNITS"            CDF_CHAR        { "ns" }
 "VALIDMIN"         CDF_TIME_TT2000 { 2010-01-01T00:00:00.000000000 }
 "VALIDMAX"         CDF_TIME_TT2000 { 2029-12-31T23:59:58.999000000 }
 "VAR_TYPE"         CDF_CHAR        { "support_data" }
 "SCALETYP"         CDF_CHAR        { "linear" }
 "MONOTON"          CDF_CHAR        { "INCREASE" }
 "DICT_KEY"         CDF_CHAR        { "time>Epoch" }
 "TIME_BASE"        CDF_CHAR        { "J2000" }
 "TIME_SCALE"       CDF_CHAR        { "Terrestrial Time" }.

```
 ! RV values were not requested.

***Example of a simple 1D size 12 time varying support_data variable - energy.***

We show here the variable, Ion Energy, as it would appear in a CDF Skeleton table. We include all required variable attributes. Some recommended attributes are also shown. This support_data variable is attached to a data variable (Ion Diff. Intensity, at 12 energies 67-1361 keV) of the same dimensionality and size. See this variable used in a [Display](https://spdf.gsfc.nasa.gov/istp_guide/variables.html#1D%20Spectrogram).

```
! Variable         Data     Number                        Record     Dimension
! Name             Type     Elements    Dims    Sizes     Variance   Variances
! --------         ----     --------    ----    -----     --------   ---------

 "IDiffI_I_Energy"
                   CDF_REAL4    1         1      12         T            T

 ! Attribute          Data
 ! Name               Type          Value
 ! --------           ----          -----

 "CATDESC"            CDF_CHAR      { "Ion Energy, at 12 channels energies " -  "67-1361 keV (EPIC/ICS) " }
 "DELTA_PLUS_VAR"     CDF_CHAR      { "IDiffI_I_Eplus" }
 "DELTA_MINUS_VAR"    CDF_CHAR      { "IDiffI_I_Eminus" }
 "DEPEND_0"           CDF_CHAR      { "Epoch" }
 "DICT_KEY"           CDF_CHAR      { "energy>ion" }
 "FIELDNAM"           CDF_CHAR      { "Ion Energy (EPIC/ICS)" }
 "FILLVAL"            CDF_REAL4     { -1.000000e+31 }
 "FORMAT"             CDF_CHAR      { "F7.1" }
 "LABLAXIS"           CDF_CHAR      { "Ion Energy" }
 "UNITS"              CDF_CHAR      { "keV" }
 "VALIDMIN"           CDF_REAL4     { 67.3 }
 "VALIDMAX"           CDF_REAL4     { 1361.0 }
 "VAR_TYPE"           CDF_CHAR      { "support_data" }.

```
***Metadata***

***Example of a 1D size 3 metadata variable***

This metadata variable labels the cartesian GSE magnetic field (1D size 3) data variable. See this variable used in a [Display](https://spdf.gsfc.nasa.gov/istp_guide/variables.html#1D%20Time%20Series)<u><span>.</span></u>
Character metadata must define the number of elements to be the same as the number of characters used in its value.

```
! Variable         Data         Number                        Record      Dimension
! Name             Type         Elements    Dims    Sizes     Variance    Variances
! --------         ----         --------    ----    -----     --------    ---------

 "label_B_GSE"     CDF_CHAR      6            1       3         F            T

 ! Attribute       Data
 ! Name            Type         Value
 ! --------        ----         -----

 "CATDESC"         CDF_CHAR     { "Label cartesian B" }
 "FIELDNAM"        CDF_CHAR     { "Label cartesian B" }
 "VAR_TYPE"        CDF_CHAR     { "metadata" }.

```
 ! NRV values follow...

 [ 1 ] = { "Bx GSE" }

 [ 2 ] = { "By GSE" }

 [ 3 ] = { "Bz GSE" }





Return to Table of Contents: [Table of Contents](00_Table_of_Contents.md)
