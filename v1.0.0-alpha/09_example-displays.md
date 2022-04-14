***Examples of Variable Displays***

**Scalar (0D) Time Series**

We display below the Ion Number Density from the example [simple scalar density](https://spdf.gsfc.nasa.gov/istp_guide/variables.html#data_eg1). The y-axis labels come from variable attributes LABLAXIS and UNITS. The x-axis if defined by the Epoch variable (time). Ion Number Density is tied to its time tag using the DEPEND_0 variable attribute. (Ion Number Density has 0 dimensions and does not need any other DEPEND_i defined.)

**1D - size 3 Time Series**

We display below the Magnetic Field from the example [vector magnetic field](https://spdf.gsfc.nasa.gov/istp_guide/variables.html#data_eg2). The y-axis
labels come from 2 places: (1) Bx, By, Bz from the metadata variable "label_B_GSE" (labeled in blue) which is attached to the Magnetic Field variable via LABL_PTR_1 and (2) nT from the UNITS variable attribute. The x-axis if defined by the Epoch variable (time). Ion Number Density is tied to its time tag using the DEPEND_0 variable attribute. See also the [metadata variable](https://spdf.gsfc.nasa.gov/istp_guide/variables.html#Metadata_eg1) "label_B_GSE."

**1D - size 12 Spectrogram**

We display below the Ion Diff. Intensity, at 12 energies (67-1361 keV) from the example [1D flux](https://spdf.gsfc.nasa.gov/istp_guide/variables.html#data_eg3). The z-axis labels come from variable attributes LABLAXIS and UNITS. The y-axis labels (labeled in green) come from the energy variable attached to Ion Diff. Intensity via the DEPEND_1 variable attribute, specifically the LABLAXIS (or FIELDNAM) and UNITS of the energy variable. The x-axis if defined by the Epoch variable (time). Ion Number Density is tied to its time tag using the DEPEND_0 variable attribute.

See also the [Support data variable](https://spdf.gsfc.nasa.gov/istp_guide/variables.html#support_data_eg2) "IDiffI_I_Energy."

**1D - size 7 Stacked Time Series**

We display below Electron Flux at 7 energies (0.1 - 222 keV). As opposed to the spectrogram above, the y-axis labels come from variable attributes LABLAXIS and UNITS. The z-axis labels (labeled in green) come from the energy variable attached to Electron Flux via the DEPEND_1 variable attribute, specifically the LABLAXIS
(or FIELDNAM) and UNITS of the energy variable. The x-axis if defined by the Epoch variable (time). Ion Number Density is tied to its time tag using the DEPEND_0 variable attribute.

**2D - sizes 28, 12 Spectrogram**

We display below H+ number flux using two different cuts through the 2D data. H+ number flux depends on energy (first dimension) and angle (second dimension). See [Example - 2D flux](https://spdf.gsfc.nasa.gov/istp_guide/variables.html#data_eg4).

**There are two ways to plot spectrograms with 2D data**:

- plot all energies (y-axis) and a few selected angle bins (in separate panels)

- plot all angles (y-axis) and a few selected energy bins (in separate panels).

These are both illustrated below. [H+ number flux needs two label variables to adequately label all possible spectrogram displays. LABL_PTR_1 points to a label (metadata) 1D variable of size 28; the label variable holds 28 H+ energy labels, e.g.,
"H+ Flux 4.4keV/e". LABL_PTR_2 points to a label (metadata) 1D variable of size 12; the label variable holds 12 H+ angle labels, e.g., "H+ Flux 7.5 deg".]

**H+ number flux for 28 energies and 3 selected angle bins**

The 3 selected angle bins appear as separate panels. The energy attribute values (either the LABLAXIS value or the FIELDNAM value, along with the UNITS value) are used to label the y-axis on each panel. The energy support_data variable is attached to the data variable via the DEPEND_1 attribute.

The z-axis (color bar) is labeled with selected values from the *H+ angle label variable* that is attached to the data variable via the LABL_PTR_2 attribute. The z-axis units come from the data variable UNITS attributes.

**H+ number flux for 12 angles and 3 selected energy bins**

The 3 selected energy bins appear as separate panels. The angle attribute values (either the LABLAXIS value or the FIELDNAM value, along with the UNITS value) are used to label the y-axis on each panel. The angle support_data variable is attached to the data variable via the DEPEND_2 attribute.

The z-axis (color bar) is labeled with selected values from the *H+ energy label variable* that is attached to the data variable via the LABL_PTR_1 attribute. The z-axis units come from the data variable UNITS attributes.


Return to Table of Contents: [Table of Contents](00_Table_of_Contents.md)
