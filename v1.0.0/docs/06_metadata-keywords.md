# Dictionary Keywords

A project data dictionary contains information required to make the data independently useable to a wide community. For ISTP, the CDF format carries much (but not all) of the data dictionary information using a set of standard global attributes describing the overall CDF content and a set of standard attributes for each variable in the CDF. The variable attributes contain descriptions, variable types, minimum and maximum values, labels, units, time tags, and if required, dependencies, uncertainties, and offsets. However, there is little consistency in variable names nor in the descriptions that are tied to each variable, to help other users of the data find and use the variables of interest. 

## ISTP Dictionary Keywords 

We have extended the ISTP project data dictionary to include dictionary keywords that identify variables as being a certain type such as *time* or *magnetic field* regardless of the naming convention adopted by the investigators. Each variable in a CDF has defined dictionary keywords (class and subclass) that are stored as a string value in its associated `DICT_KEY` attribute. The syntax for populating the Dictionary Keyword attribute `DICT_KEY` is `class>subclass_subclass_subclass`. See  [examples of use](#examples-of-subclass-words).

### List of Class and Subclass Keywords

We provide a standard set of class keywords that include both sensor (science) and supporting class words and their meanings, to be used to categorize the data variables of primary interest to investigators, among the several ISTP satellites and experiments. ISTP class keywords are restricted to the values shown below. Sets of subclass keywords, with each set used to modify one of the class keywords, are also adopted and listed with the associated information below. Lists of common subclass keywords, valid with any class keywords, can also be found below.

| Sensor Class Word    | Description    |   Subclass Words |		
| ------------- | ---------------| -------------   |
| `anisotropy`	|The variation of physical properties with direction, usually expressed as a ratio |  `parallel` |
| `current` | 	The rate of flow of electricity | `Hall`, `load`, `primary`,  `secondary`	|
| `density` | The mass per unit volume of a substance, or the number of items per unit volume | `partial`, `mass`, `number` |
| `electric_field` | The space surrounding an electric charge within which it is capable of exerting a perceptible force on another electric charge. The strength of an electric field at a given point is given in terms of the force exerted by the field on unit charge at that point | `AC`, `amplitude`, `angle`, `antenna`, `calibration`, `DC`, `potential` |
| `magnetic_field` | The field of force surrounding a magnetic pole or a current flowing through a conductor, in which there is a magnetic flux | `AC`, `amplitude`, `angle`, `antenna`, `calibration`, `DC`, `potential` |
| `particle_flux` | The number of particles passing through a specified area or volume in a specified time interval (and possibly in a specified energy range or in a specified range of directions) | `differential`, `directional`, `integral`, `mass`, `number`, `omni-directional`, `parallel`, `perpendicular`, `rate`, `sample`, `spectral`, `thermal` |
| `photon_flux` | The number of photons passing through a specified area or volume in a specified time interval (and possibly in a specified energy or wavelength range or in a specified range of directions) | `brightness`, `differential`, `directional`, `filtered`, `integral`, `incident`, `omni-directional`, `reflected` |
| `position` | A location, distance, or direction with respect to some particular reference. The reference can be moving or fixed, such as the geographic coordinate system or a spacecraft body | `altitude`, `angle`, `antenna`, `azimuth`, `column`, `declination`, `direction`, `distance`, `elevation`, `height`, `horizontal`, `inclination`, `latitude`, `longitude`, `projection`, `radial`, `range`, `RA`, `attitude`, `row`, `surface`, `target`, `vertical` |
| `potential` | Electrostatic, magnetostatic, or gravitational potential, at a point in the field: the work done in bringing unit positive charge, unit positive pole, or unit mass respectively from infinity (i.e., a place infinitely distant from the causes of the field) to the point | `antenna`, `bias`, `electric`, `gravity`, `Hall`, `magnetic`, `polar_cap`, `surface` |
| `power` | The rate at which energy is expended or work is done | `amplitude`, `antenna`, `bandwidth`, `calibration`, `density`, `electric`, `emission`, `field`, `flux`, `poynting`, `radiant`, `reflected`, `spectral`, `transmittance` |
| `pressure` | Force per unit area |  `atmosphere`, `derived`, `dynamic`, `magnetic`, `solar`, `surface` |
| `temperature` | The degree or intensity of heat or cold as measured on a thermometric scale. Also the equivalent temperature corresponding to the energy of thermal motion of plasma particles, or the equivalent temperature as computed in radio measurements | `characteristic`, `isotropic`, `operational`, `parallel`, `perpendicular`, `threshold` |
| `velocity` | The rate of increase of distance traversed by a body in a particular direction (linear velocity) or the rate at which a body rotates about an axis (angular velocity). Speed is similarly defined with the omission of reference to direction | `doppler`, `drift`, `group`, `horizontal`, `phase`, `rotation`, `speed`, `thermal`, `vertical` |



| Supporting Class Word    | Description    |   Subclass Words |		
| ------------- | ---------------| -------------   |
| `angle` 	|The geometric figure formed by two lines diverging from a point or two planes diverging from a common line or the space between two such lines or surfaces| `antenna`, `aspect`, `axis`, `azimuth`, `elevation`, `fov`, `geometric`, `inclination`, `phase`, `pitch`, `pointing`, `polar`, `rotation`, `sector` |
| `energy` | 	The property of a system that is a measure of its capacity for doing work| `band`, `incident`, `channel`, `reflected`	|
| `flag` | An entity that signals the occurance of an event, or that indicates a particular status of a spacecraft or instrument or software program. The flag can be a number, letter, or word, and may have any of a variety of encoded meanings | `number`, `quality`, `post_gap`, `status` |
| `frequency` | The number of cycles completed by a periodic function in unit time | `band`, `channel` |
| `label`| A term or phrase attached by way of classification or characterization | All other class words are also possible subclass words, `alias`, `name(s)`, `source` |
| `number` | A symbol or word, or a group of either of these, showing how many or what place in a sequence | `direction`, `event`, `exposure`, `filter`, `frame`, `image`, `mode`, `sequence`, `target`, `telescope` |
| `ratio` | The quotient of one quantity divided by another of the same kind, and usually expressed as a fraction | `albedo`, `anisotropy`, `beta`, `current`, `density`, `electric_field`, `energy`, `magnetic_field`, `particle_flux`, `photon_flux`, `power`, `pressure`, `spectral`, `temperature`, `velocity` |
| `significance` | |  `correlation` |
| `source` | The origin (mission, spacecraft, instrument, ground observatory, or other observing platform) of the data in question | `experiment`, `campaign`, `ground-based`, `investigation` |
| `species` | The identity of a particle or class of particles in detail, such as common name, chemical name, mass, charge state, atomic number, atomic weight, degree of ionization, mass per charge, etc. |  `electron`, `ion`, `proton`, `helium`, `nitrogen`, `oxygen`, `Z>3`, `neutral`, `particle`, `dust` |
| `time` | The period between two events or measurements; a measurable interval, usually between a fixed reference (instant of time) such as 0 AD and the subject event or measurement | `bin`, `clock`, `cycle`, `date`, `elapsed`, `epoch`, `event`, `GMT`, `hour`, `interval`, `Julian`, `local`, `magnetic`, `millisecond`, `minute`, `PB5`, `reference`, `relative`, `second`, `spacecraft`, `UT` |
| `uncertainty` | An estimate of the lack of precision in an observed or calculated value | All other class words are also possible subclass words, `percent` |
| `wavelength` | The distance from a particular point of a wave to that same point in the next oscillation cycle of the wave. Also a range of wavelengths, such as infra-red, visible, radio, x-ray |  `radio`, `IR`, `visible`, `UV`, `x-ray`, `gamma`, `band`, `bin`, `channel`, `characteristic`, `filter`, `nominal`, `primary`, `scan`, `resolution`|





### Associated information: More on Class words

The dictionary keywords and definitions (along with the other global and variable attributes) comprise the primary content of the ISTP project data dictionary. The class keywords were selected to be, as much as possible, a complete and orthogonal set. In the realm of space physics there are three broad classes of sensor data words:
electric and magnetic field (DC values for vectors, AC values for power spectra), particle distributions (e.g., densities, flow speeds, flow direction angles, thermal speeds, temperatures, anisotropy, fluxes), images (e.g., remote sensing of the aurora, ionosphere and sun at various wavelength ranges measuring e.g., electromagnetic waves, temperatures, pressures). In addition, there are time words, orbit/attitude words, and flags of various types (e.g., instrument mode). We choose the measured quantities such as magnetic_field, density, temperature, to be the sensor (science) class keywords that are of primary science interest. Supporting keywords are of secondary science interest such as the energy or time at which a measurement was made, or the label or flag associated with a measured quantity. The sensor (science) class words are
listed separately from the supporting class words below. It is envisioned that the usage of the sensor (science) and supporting class keywords will be different. Sensor Words make up a short, standard list that enables automated searching for data of interest at a fairly high level. Supporting Words are at a lower level of interest, but may still be used for some types of searches. In the CDF model every variable must have one and only one class keyword defined, but may have any number of subclass keywords defined.

### Common Subclass Words

The following lists of words are valid with any class word. Note that some species and wavelength subclass keywords are also considered to be common because they can be used in conjunction with several of the class words.

GENERAL Subclass Words &mdash; `absolute`, `average`, `center`, `component`, `derived`, `instrument`, `interval`, `maximum`, `measured`, `minimum`, `mean`, `offset`, `spacecraft`, `vector`, `total`

COORDINATE SYSTEM Subclass Words &mdash; `cartesian`, `geographic`, `geomagnetic`, `GCI`, `GSM`, `GSE`, `HDZ`, `HGI`, `NEV`, `polar`   

SOURCE Subclass Words &mdash; `electron`, `ion`, `proton`, `helium`, `nitrogen`, `oxygen`, `Z>3`, `neutral` , `particle`, `dust`

WAVELENGTH Subclass Words &mdash; `radio`, `IR`, `visible`, `UV`, `x-ray`, `gamma` `ray`

### Examples of Subclass Words

| Source | Instrument | Variable | DICT_KEY  |
| ------ | --- | -------- | ------------------|
|All     | All |Epoch     |`"time>Epoch_center_range"` |
|IMP 8    |MAG |Time_PB5  |`"time>PB5_center_range"` |
|IMP 8    |MAG |B_GSE_c   |`"magnetic_field>GSE_cartesian_vector"` |
|IMP 8    |MAG |B_GSM_p   |`"magnetic_field>GSM_polar_vector"` |
|IMP 8    |MAG |Rad_dist  |`"position>radial_distance"` |
|IMP 8    |MAG |SC_pos_se |`"position>GSE_cartesian"` |
|IMP 8    |MAG |Mode      |`"flag>mode"` |
|IMP 8    |MAG |DQF       |`"flag>quality"` |
|DARN     |GBAY |vel      |`"velocity>drift_components"` |
|DARN     |GBAY |post_flag |`"flag>post_gap"` |
|DARN     |GBAY |label_time |`"label>time"` |
|DARN     |GBAY |label_unit |`"label>unit"` |
|Geotail  |EPIC |IDiffI_I    |`"particle_flux>ion_differential"` |
|Geotail  |EPIC |IDiffI_I_Uncert |`"uncertainty>ion_differential"` |
|Geotail  |EPIC |IDiffI_I_Energy |`"energy>ion_center_channel"` |
|Geotail  |EPIC |IDiffI_I_Ch     |`"label>ion_energy_channel"` |
|Geotail  |EPIC |IDiffI_I_Eplus  |`"energy>ion_energy_plus"` |
|Geotail  |EPIC |IDiffI_I_Eminus |`"energy>ion_energy_minus"` |



## SPASE Dictionary Keywords
Alternatively, `DICT_KEY` variable attribute can be used with values from controlled lists of the Space Physics Archive Search and Extract [(SPASE)](https://spase-group.org) data model, enabling both accurate description of parameters and full compatibility with the SPASE model. For compliance with the SPASE model requirements for Level 2 (L2) and higher level datasets archived at NASA SPDF, `DICT_KEY` attribute using SPASE controlled lists must be included for all **_data_**  and **_support_data_** ISTP variables. `DICT_KEY` is not required for **_metadata_** variables.

See format and examples below (depending on described parameter type in SPASE model: Field, Particle, Wave, Mixed, or Support) for filling the `DICT_KEY` attribute string value. Note that the SPASE parameter type is independent from the ISTP variable type (identified by `VAR_TYPE` attribute value). `Key:VALUE` pairs in bold are always required, other `Key:VALUE` pairs are required if applicable. `VALUE[_VALUE...]` means multiple `VALUEs` are allowed, separated by underscores. **If a parameter cannot be described in any other way, use** `DICT_KEY = “SPASE>Support>SupportQuantity:Other”`.

In the `DICT_KEY` formats for various SPASE parameter types below, replace `VALUE` with a value from a linked list corresponding to `Key`:
- [FieldQuantity](https://spase-group.org/data/model/spase-latest/spase-latest_xsd.htm#FieldQuantity)
- [ParticleType](https://spase-group.org/data/model/spase-latest/spase-latest_xsd.htm#ParticleType)
- [ParticleQuantity](https://spase-group.org/data/model/spase-latest/spase-latest_xsd.htm#ParticleQuantity)
- [WaveType](https://spase-group.org/data/model/spase-latest/spase-latest_xsd.htm#WaveType)
- [WaveQuantity](https://spase-group.org/data/model/spase-latest/spase-latest_xsd.htm#WaveQuantity)
- [MixedQuantity](https://spase-group.org/data/model/spase-latest/spase-latest_xsd.htm#MixedQuantity)
- [SupportQuantity](https://spase-group.org/data/model/spase-latest/spase-latest_xsd.htm#SupportQuantity)
- [Qualifier](https://spase-group.org/data/model/spase-latest/spase-latest_xsd.htm#Qualifier)
- [CoordinateSystemName](https://spase-group.org/data/model/spase-latest/spase-latest_xsd.htm#CoordinateSystemName)
- [CoordinateRepresentation](https://spase-group.org/data/model/spase-latest/spase-latest_xsd.htm#CoordinateRepresentation)


### Field (Magnetic or Electric) Parameter

**Format:**
```
DICT_KEY = “SPASE>Field>FieldQuantity:VALUE,Qualifier:VALUE[_VALUE...],CoordinateSystemName:VALUE,CoordinateRepresentation:VALUE”
```

**Examples:**
```
DICT_KEY = “SPASE>Field>FieldQuantity:Magnetic,Qualifier:Magnitude”
```
```
DICT_KEY = “SPASE>Field>FieldQuantity:Magnetic,Qualifier:Vector,CoordinateSystemName:GSM,CoordinateRepresentation:Cartesian”
```

### Particle Parameter

**Format:**
```
DICT_KEY = “SPASE>Particle>ParticleType:VALUE[_VALUE...],ParticleQuantity:VALUE,Qualifier:VALUE[_VALUE...],CoordinateSystemName:VALUE,CoordinateRepresentation:VALUE”
```

**Examples:**
```
DICT_KEY = “SPASE>Particle>ParticleType:Electron,ParticleQuantity:NumberDensity,Qualifier:Moment”
```
```
DICT_KEY = “SPASE>Particle>ParticleType:Proton,ParticleQuantity:FlowVelocity,Qualifier:Vector_Moment,CoordinateSystemName:GSE,CoordinateRepresentation:Cartesian”
```

### Wave Parameter

**Format:**
```
DICT_KEY = “SPASE>Wave>WaveType:VALUE,WaveQuantity:VALUE,Qualifier:VALUE[_VALUE...],CoordinateSystemName:VALUE,CoordinateRepresentation:VALUE”
```

**Examples:**
```
DICT_KEY = “SPASE>Wave>WaveType:Electrostatic,WaveQuantity:Intensity”
```

### Mixed Parameter

**Format:**
```
DICT_KEY = “SPASE>Mixed>MixedQuantity:VALUE,ParticleType:VALUE[_VALUE...],Qualifier:VALUE[_VALUE...],CoordinateSystemName:VALUE,CoordinateRepresentation:VALUE”
```

**Examples:**
```
DICT_KEY = “SPASE>Mixed>MixedQuantity:AlfvenMachNumber”
```

### Support Parameter

**Format:**
```
DICT_KEY = “SPASE>Support>SupportQuantity:VALUE,Qualifier:VALUE[_VALUE...],CoordinateSystemName:VALUE,CoordinateRepresentation:VALUE”
```

**Examples:**

For all Time/Epoch variables:
```
DICT_KEY = “SPASE>Support>SupportQuantity:Temporal”
```
For various other Support parameters:
```
DICT_KEY = “SPASE>Support>SupportQuantity:Positional,Qualifier:Vector,CoordinateSystemName:GSE,CoordinateRepresentation:Cartesian”
```
```
DICT_KEY = “SPASE>Support>SupportQuantity:Orientation,Qualifier:DirectionAngle.AzimuthAngle,CoordinateSystemName:GSE,CoordinateRepresentation:Spherical”
```
```
DICT_KEY = “SPASE>Support>SupportQuantity:DataQuality”
```
```
DICT_KEY = “SPASE>Support>SupportQuantity:Other”
```

---
Return to [Table of Contents](../README.md)
