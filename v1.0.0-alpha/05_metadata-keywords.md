**ISTP/IACG Dictionary Keywords**

A project data dictionary contains information required to make the data independently useable to a wide community. For ISTP/IACG the CDF, chosen as the data exchange format for key parameter and event data, carries much (but not all) of the data dictionary information using a set of standard global attributes describing the overall CDF content and a set of standard attributes for each variable in the CDF. The variable attributes contain descriptions, data types, minimum and maximum values, labels, units, time tags, and if required, dependencies, uncertainties, and offsets. However, there is little consistency in variable names nor in the descriptions that are tied to each variable, to help other users of the data find and use the variables of interest. We have extended the ISTP/IACG project data dictionary to include dictionary keywords that identify variables as being a certain type such as time or magnetic_field regardless of the naming convention adopted by the investigators. Each variable in a CDF has defined dictionary keywords (class and subclass) that are stored in its associated DICT_KEY attribute.

**List of Class Keywords**

We provide a standard set of class keywords that include 'sensor (science)' and 'supporting' class words and their meanings, to be used to categorize the data variables of primary interest to investigators, among the several ISTP/IACG satellites and experiments. ISTP/IACG class keywords will be restricted to the approved values shown below. Sets of subclass keywords, with each set used to modify one of the class keywords, are also adopted and listed with the associated information below. Lists of common subclass keywords, valid for any variable, can also be found below.
		
		
| Class Word    | Description    |   Subclass Word/s |		
| ------------- | ---------------| -------------   |	
| Anisotropy	|The variation of physical properties with direction, usually expressed as a ratio |  parallel
| Angle 	|The geometric figure formed by two lines diverging from a point or two planes diverging from a common line or the space between two such lines or surfaces| antenna, elevation, pitch, aspect, fov, pointing, axis, geometric, polar, azimuth, inclination, rotation, phase, sector
| Current | 	The rate of flow of electricity | hall, primary, load, secondary	
| Energy | 	The property of a system that is a measure of its capacity for doing work| band, channel, incident, reflected	
| Density | The mass per unit volume of a substance, or the number of items per unit volume | partial, mass, number
| Flag | An entity that signals the occurance of an event, or that indicates a particular status of a spacecraft or instrument or software program. The flag can be a number, letter, or word, and may have any of a variety of encoded meanings | number, quality, post_gap, status
| Electric_Field | The space surrounding an electric charge within which it is capable of exerting a perceptible force on another electric charge. The strength of an electric field at a given point is given in terms of the force exerted by the field on unit charge at that point | AC, amplitude, angle, antenna, calibration, DC, potential
| Frequency | The number of cycles completed by a periodic function in unit time | band, channel
| Magnetic_Field | The field of force surrounding a magnetic pole or a current flowing through a conductor, in which there is a magnetic flux | AC, amplitude, angle, antenna, calibration, DC, potential
| Label| A term or phrase attached by way of classification or characterization | All other class words are also possible sub-class words
| Particle_Flux | The number of particles passing through a specified area or volume in a specified time interval (and possibly in a specified energy range or in a specified range of directions) | differential, number, rate, directional, omni-directional, sample, integral, parallel, spectral, mass, perpendicular, thermal
| Number | A symbol or word, or a group of either of these, showing how many or what place in a sequence | direction, frame, target, event, image, telescope, exposure, mode, filter, sequence
| Photon_Flux | The number of photons passing through a specified area or volume in a specified time interval (and possibly in a specified energy or wavelength range or in a specified range of directions) | brightness, integral, differential, incident, directional, omni-directional, filtered, reflected
| Ratio | The quotient of one quantity divided by another of the same kind, and usually expressed as a fraction | albedo, electric_field, power, beta, energy, pressure, anisotropy, particle_flux, temperature, current, photon_flux, velocity, density, magnetic_field, spectral
| Position | A location, distance, or direction with respect to some particular reference. The reference can be moving or fixed, such as the geographic coordinate system or a spacecraft body | altitude, distance, radial, angle, elevation, range, antenna, height, RA, attitude, horizontal, row, azimuth, inclination, surface, column, latitude, target, declination, longitude, vertical, direction, projection 
| Significance | |  correlation
| Potential | Electrostatic, magnetostatic, or gravitational potential, at a point in the field: the work done in bringing unit positive charge, unit positive pole, or unit mass respectively from infinity (i.e., a place infinitely distant from the causes of the field) to the point | antenna, Hall, bias, magnetic, electric, polar_cap, gravity, surface
| Source | The origin (mission, spacecraft, instrument, ground observatory, or other observing platform) of the data in question | experiment, ground-based, campaign, investigation
| Power | The rate at which energy is expended or work is done | amplitude, electric, radiant, antenna, emission, reflected, bandwidth, field, spectral, calibration, flux, transmittance, density, poynting 
| Species | The identity of a particle or class of particles in detail, such as common name, chemical name, mass, charge state, atomic number, atomic weight, degree of ionization, mass per charge, etc. |  electron, oxygen, ion, Z>3, proton, neutral, helium, particle, nitrogen, dust 
| Pressure | Force per unit area |  atmosphere, magnetic, derived, solar, dynamic, surface 
| Time | The period between two events or measurements; a measurable interval, usually between a fixed reference (instant of time) such as 0 AD and the subject event or measurement | bin, GMT, minute, clock, hour, PB5, cycle, interval, reference, date, Julian, relative, elapsed, local, second, epoch, magnetic, spacecraft, event, millisecond, UT

**Sensor Words Supporting Words**








[pressure](https://spdf.gsfc.nasa.gov/istp_guide/data_dictionary.html#pressure) [time](https://spdf.gsfc.nasa.gov/istp_guide/data_dictionary.html#time)

[temperature](https://spdf.gsfc.nasa.gov/istp_guide/data_dictionary.html#temperature) [uncertainty](https://spdf.gsfc.nasa.gov/istp_guide/data_dictionary.html#uncertainty)

[velocity](https://spdf.gsfc.nasa.gov/istp_guide/data_dictionary.html#velocity) [wavelength](https://spdf.gsfc.nasa.gov/istp_guide/data_dictionary.html#wavelength)

**Implementation**

The syntax for populating the Dictionary Keyword attribute DICT_KEY is class>subclass_subclass_subclass. Click here for [examples](https://spdf.gsfc.nasa.gov/istp_guide/data_dictionary.html#Examples).

**Associated information: More on Class words**

The dictionary keywords and definitions (along with the other global and variable attributes) comprise the primary content of the ISTP/IACG project data dictionary. The class keywords were selected to be, as much as possible, a complete and orthogonal set. In the realm of space physics there are three broad classes of sensor data words:
electric and magnetic field (DC values for vectors, AC values for power spectra), particle distributions (e.g., densities, flow speeds, flow direction angles, thermal speeds, temperatures, anisotropy, fluxes), images (e.g., remote sensing of the aurora, ionosphere and sun at various wavelength ranges measuring e.g., electromagnetic waves, temperatures, pressures). In addition, there are time words, orbit/attitude words, and flags of various types (e.g.,instrument mode). We choose the measured quantities such as magnetic_field, density, temperature, to be the sensor (science) class keywords that are of primary science interest. Supporting keywords are of secondary science interest such as the energy or time at which a measurement was made, or the label or flag associated with a measured quantity. The sensor (science) class words are
listed separately from the supporting class words below. It is envisioned that the usage of the sensor (science) and supporting class keywords will be different. Sensor Words make up a short, standard list that enables automated searching for data of interest at a fairly high level. Supporting Words are at a lower level of interest, but may still be used for some types of searches. In the CDF model every variable must have one and only one class keyword defined, but may have any number of subclass keywords defined.

**Class Word definitions and associated subclass words**

ANGLE The geometric figure formed by two lines diverging from a point or two planes
diverging from a common line or the space between two such lines or surfaces.

Subclass Words antenna elevation pitch

 aspect fov pointing

 axis geometric polar

 azimuth inclination rotation

 phase sector

ANISOTROPY The variation of physical properties with direction, usually expressed as a ratio.

Subclass Words: parallel

CURRENT The rate of flow of electricity.

Subclass Words: Hall primary

 load secondary

DENSITY The mass per unit volume of a substance, or the number of items per unit volume.

Subclass Words: partial mass number

ELECTRIC_FIELD The space surrounding an electric charge within which it is capable of exerting a perceptible force on another electric charge. The strength of an electric field at a given point is given in terms of the force exerted by the field on unit charge at that point.

Subclass Words: AC calibration

 amplitude DC

 angle potential

 antenna 

ENERGY The property of a system that is a measure of its capacity for doing work.

Subclass Words band channel 

 incident reflected 

FLAG An entity that signals the occurrence of an event, or that indicates a particular status of a spacecraft or instrument or software program. The flag can be a number, letter, or word, and may have any of a variety of encoded meanings.

Subclass Words number post_gap 

 quality status 

FREQUENCY The number of cycles completed by a periodic function in unit time.

Subclass Words band 

 channel 

LABEL A term or phrase attached by way of classification or characterization.

Subclass Words  [All other class words are also possible sub-class words]

 alias 

 name(s) 

 source 

MAGNETIC_FIELD The field of force surrounding a magnetic pole or a current flowing through a conductor, in which there is a magnetic flux.

Subclass Words AC calibration 

 amplitude DC 

 angle potential 

 antenna 

NUMBER A symbol or word, or a group of either of these, showing how many or what place in a sequence.

Subclass Words direction frame target

 event image telescope

 exposure mode 

 filter sequence 

PARTICLE_FLUX The number of particles passing through a specified area or volume in a specified time interval (and possibly in a specified energy range or in a specified range of directions).

Subclass Words differential number rate

 directional omni-directional sample

 integral parallel spectral

 mass perpendicular thermal

PHOTON_FLUX The number of photons passing through a specified area or volume in a specified time interval (and possibly in a specified energy or wavelength range or in a specified range of directions).

Subclass Words brightness integral

 differential incident

 directional omni-directional

 filtered reflected

POSITION A location, distance, or direction with respect to some particular reference. The reference can be moving or fixed, such as the geographic coordinate system or a spacecraft body.

Subclass Words altitude distance radial

 angle elevation range

 antenna height RA

 attitude horizontal row

 azimuth inclination surface

 column latitude target

 declination longitude vertical

 direction projection 

POTENTIAL Electrostatic, magnetostatic, or gravitational potential, at a point in the field: the work done in bringing unit positive charge, unit positive pole, or unit mass
respectively from infinity (i.e., a place infinitely distant from the causes of the field) to the point.

Subclass Words antenna Hall

 bias magnetic

 electric polar_cap

 gravity surface

POWER The rate at which energy is expended or work is done.

Subclass Words amplitude electric radiant

 antenna emission reflected

 bandwidth field spectral

 calibration flux transmittance

 density poynting 

PRESSURE Force per unit area.

Subclass Words atmosphere magnetic

 derived solar

 dynamic surface

RATIO The quotient of one quantity divided by another of the same kind, and usually expressed as a fraction.

Subclass Words albedo electric_field power

 beta energy pressure

 anisotropy particle_flux temperature

 current photon_flux velocity

 density magnetic_field spectral

SIGNIFICANCE

Subclass Words correlation 

SOURCE The origin (mission, spacecraft, instrument, ground observatory, or other observing platform) of the data in question.

Subclass Words experiment ground-based 

 campaign investigation 

SPECIES The identity of a particle or class of particles in detail, such as common name, chemical name, mass, charge state, atomic number, atomic weight, degree of ionization, mass per charge, etc.

Subclass Words electron oxygen

 ion Z>3

 proton neutral

 helium particle

 nitrogen dust

TEMPERATURE The degree or intensity of heat or cold as measured on a thermometric scale. Also the equivalent temperature corresponding to the energy of thermal motion of plasma particles, or the equivalent temperature as computed in radio measurements.

Subclass Words characteristic parallel

 isotropic perpendicular

 operational threshold

TIME The period between two events or measurements; a measurable interval, usually between a fixed reference (instant of time) such as 0 AD and the subject event or measurement.

Subclass Words bin GMT minute

 clock hour PB5

 cycle interval reference

 date Julian relative

 elapsed local second

 epoch magnetic spacecraft

 event millisecond UT

UNCERTAINTY An estimate of the lack of precision in an observed or calculated value.

Subclass Words  [All other class words are also possible sub-class words] 

 percent 

VELOCITY The rate of increase of distance traversed by a body in a particular direction (linear velocity) or the rate at which a body rotates about an axis (angular velocity). Speed is similarly defined with the omission of reference to direction.

Subclass Words doppler horizontal speed

 drift phase thermal

 group rotation vertical

WAVELENGTH The distance from a particular point of a wave to that same point in the next oscillation cycle of the wave. Also a range of wavelengths, such as infra-red, visible, radio, x-ray.

Subclass Words radio band primary

 IR bin scan

 visible channel resolution

 UV characteristic 

 x-ray filter 

 gamma
ray nominal 

**Common Subclass Words**

The following lists of words are valid for more than one class word. Note that some species and wavelength subclass keywords are also considered to be common because they can be used in conjunction with several of the class words.

GENERAL Subclass Words absolute instrument mean

 average interval offset

 center maximum spacecraft

 component measured vector

 derived minimum total

COORDINATE SYSTEM Subclass Words cartesian GSM

 geographic HDZ

 geomagnetic HGI

 GCI NEV

 GSE polar

SOURCE Subclass Words electron oxygen

 ion Z>3

 proton neutral

 helium particle

 nitrogen dust

WAVELENGTH Subclass Words radio 

 IR

 visible

 UV

 x-ray 

 gamma ray 


Return to Table of Contents: [Table of Contents](00_Table_of_Contents.md)
