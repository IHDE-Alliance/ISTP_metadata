***Example of Time\_PB5***

Time_PB5 is the second variable in an ISTP KP CDF data set. It is not required for IACG or ISTP higher resolution or event data. Time_PB5 is another way of presenting time which allows for easy recognition of the time value when looking at the data, for instance in a data dump. For ISTP the time value of a record refers to the center of the accumulation period for the record if the measurement is not an instantaneous one.
Time_PB5 is given in YEAR (4 digit), DAY OF YEAR (note: January 1 is Day 1), and MSEC OF DAY (elapsed ms). These are all signed integer*4 numbers and are stored as the three elements of the one-dimensional variable named "Time\_PB5", e.g. 1992, 214, 0 would be August 1, 1992 at midnight.

"Time\_PB5" has three "attached" variables which provide labels units and formats for the three components. These are called "label\_time", "unit\_time", and "format\_time", respectively, and are shown in the example below.

```
! Variable      Data        Number                          Record        Dimension
! Name          Type        Elements     Dims     Sizes     Variance      Variances
! --------      ----        --------     ----     -----     --------      ---------

 "Time_PB5"     CDF_INT4       1          0                    T

 ! Attribute    Data
 ! Name         Type        Value
 ! --------     ----        -----

 "FIELDNAM"     CDF_CHAR    { "Time PB5" }
 "VALIDMIN"     CDF_INT4    { 1997, 237, 0 }
 "VALIDMAX"     CDF_INT4    { 2020, 366, 0 }
 "VAR_TYPE"     CDF_CHAR    { "support_data" }
 "FORM_PTR"     CDF_CHAR    { "format_time" }
 "LABL_PTR_1"   CDF_CHAR    { "label_time" }
 "UNIT_PTR"     CDF_CHAR    { "unit_time" } 
 "FILLVAL"      CDF_INT4    { -2147483648 }
 "DEPEND_0"     CDF_CHAR    { "Epoch" }
 "DICT_KEY"     CDF_CHAR    { "time>PB5" }
 "CATDESC"      CDF_CHAR    { "Time of observation in Year, Day, & " -  "milliseconds (5 min)" }
 "SCALETYP"     CDF_CHAR    { "LINEAR" } .
```
 ! RV values were not requested.

```
! Variable        Data      Number                        Record          Dimension
! Name            Type      Elements    Dims    Sizes     Variance        Variances
! --------        ----      --------    ----    -----     --------        ---------

 "unit_time"      CDF_CHAR      4         0                 F

 ! Attribute          Data
 ! Name               Type          Value
 ! --------           ----          -----

 "FIELDNAM"           CDF_CHAR      { "Units for Time_PB5" }
 "VAR_TYPE"           CDF_CHAR      { "metadata" }
 "DICT_KEY"           CDF_CHAR      { "label>" }
 "CATDESC"            CDF_CHAR      { "Units for Time_PB5" } .

 ! NRV values follow...

 [1] = { "year" }
 [2] = { "day " }
 [3] = { "msec" }

```
! Variable       Data     Number                    Record      Dimension
! Name           Type     Elements   Dims   Sizes   Variance    Variances
! -------- ---- -------- ---- ----- -------- ---------

 "label_time" CDF_CHAR 27 0 F

 ! Attribute Data

 ! Name Type Value

 ! -------- ---- -----

 "FIELDNAM" CDF_CHAR { "Label for Time_PB5" }

 "VAR_TYPE" CDF_CHAR { "metadata" }

 "DICT_KEY" CDF_CHAR { "label>" }

 "CATDESC" CDF_CHAR { "Label for Time_PB5" } .

 ! NRV values follow...

 [1] = { "Year " }

 [2] = { "Day of Year
(Jan 1 = Day 1)" }

 [3] = { "Elapsed milliseconds of day" }

! Variable Data Number Record Dimension

! Name Type Elements Dims Sizes Variance Variances

! -------- ---- -------- ---- ----- -------- ---------

 "format_time" CDF_CHAR 2 0 F

 ! Attribute Data

 ! Name Type Value

 ! -------- ---- -----

 "FIELDNAM" CDF_CHAR { "Format for Time_PB5" }

 "VAR_TYPE" CDF_CHAR { "metadata" }

 "DICT_KEY" CDF_CHAR { "label>" }

 "CATDESC" CDF_CHAR { "Format for Time_PB5" } 

 ! NRV values follow...

 [1] = { "I4" }

 [2] = { "I3" }

 [3] = { "I8" }


Return to Table of Contents: [Table of Contents](00_Table_of_Contents.md)
