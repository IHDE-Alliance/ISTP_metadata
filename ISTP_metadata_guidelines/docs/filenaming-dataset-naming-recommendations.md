# Recommended File and Data Collection Naming Practices

Summary
-------  

Use data file and directory names that express the information that researchers need to locate data collections of interest and to indicate the differences between collections (both current and possible future ones). The following are some hands-on practices for naming your data collections and data filenames, and adding information to a data collection Readme file (hopefully without being too legalistic). All data files should be made publicly available and in FTPS or HTTPS directories for easy access, even if also available through other services and databases. These directories have the advantage of allowing easy download (using wget for instance) of whole directories. Each instrument team should strive to capture the full scientific content of their instrument in a self-describing scientific format (CDF, netCDF, HDF, FITS) with full documentation and metadata, sufficient for someone in the far future to be able to fully apply its scientific value without the need for specialized software.

The following sections provide recommendations for laying out the directory hierarchy, naming the dataset or collection, naming the data files, and finally creating a Readme file for the collection. In general, use **all lowercase text**, except for specific files and subdirectories, and use a limited character set, to ensure maximum compatibility across computer platforms and processing languages. Use times in one of the ISO 8601 formats, such as 20160215T050357.123, or 2016046T050357.123, with or without the T, or standard internal time formats such as CDF\_TIME\_TT2000 (ns from J2000 in Terrestrial Time). Use well-known extensions, spacecraft and instrument short names, and datatypes when available.

Directory Hierarchy Conventions
-------------------------------

Directory hierarchy should flow from high level to specific: **project/mission/spacecraft, instrument, data collections, time ranges**. Time range directories (yearly, monthly, daily) should be chosen to keep the number of files per directory below 1000 to avoid delays in directory display. In general, avoid the use of levels (L0, L1, L2) as directories, but instead include them if needed as a subfactor in distinguishing between datasets in the data collection directory level names, perhaps prepended to make sorting easier (l2\_gms\_62ms).

So a typical data URL would be something like  

        https://repositoryURL/pub/data/spacecraft_dir/instrument_dir/general_product_dir/specific_product/date/file.format

For instance, a data file in the ISEE-1 plasma wave spectrum analyzer dataset on SPDF's archive is at  

        https://spdf.gsfc.nasa.gov/pub/data/isee/isee1/waves_pwi/sa_pwi/1982/isee1_pwi_sa_19820101_v01.cdf  

A researcher can follow from the ISEE mission to ISEE-1 spacecraft to the Plasma Wave Instrument to the spectrum analyzer data stored as CDF files in yearly directories.

Instrument Directory Naming Conventions
---------------------------------------

Instrument directories can be the instrument\_acronym (and perhaps add institution if needed), but if possible expanded to include the instrument type for users not familiar with the specific spacecraft. For examples, waves\_pwi or particles\_epact. [SPASE Measurement Types](https://spase-group.org/data/model/spase-2.6.0/index.html) are recommended. Datasets from multiple instruments can be named with combinations, such as magnetic\_electric\_fields, or  "combined" or "merged" if they involve a number of instruments. Composite/combined/merged data collections are best stored in directories at the instrument level (de/de2/combined\_magnetic\_electric\_fields/ and de/de2/combined\_plasma\_neutrals/). Data collections for housekeeping, engineering, ephemeris, orbits, attitude or combinations go at the same level as the instruments. Directory names should be meaningful to the wide community, and use written-out words and underscores if abbreviations are too cryptic or easily confused with other uses of the same.

Include a readme file (perhaps named 00readme.txt to appear first in directory listings, see below) with brief explanations of the data collections and their relationships. 00readme.txt may be placed in every directory for navigation and content identification (perhaps aliased to the top-level one). Connect data collections across several instruments with links in the 00readme.txt files and web pages.  Combined data collections at the higher level can have place-holder directories under each instrument involved, that includes a 00readme.txt pointing to the actual data directory. Instrument directories contain data collections directories, and may also include other directories, such as software, documents, catalogs, attributes. Archived web sites may be stored under the documents directory, perhaps with the name website.

Data Collection Directory Naming Conventions
--------------------------------------------

Data collection names should include info on parameters, temporal and spatial resolution, compression and file format with enough specificity to allow other variations later (so we can later add other data collections only differing by one of these), using the order:  project\_instrument\_parameters\_resolution\_format\_compression

These fields or sections are separated by underscores, and parts of a section can use hyphens to improve readability. Use English words where meaningful, except for short forms listed below. If desired, the level (L0, L1, L2 or kp (key parameter), sp (summary parameter), etc.) may be prepended to the data collection name to sort by these levels.

Data File Naming Conventions
----------------------------

Filenames contain the data collection name and add time and version information and file extension, such as **project\_instrument\_dataform\_time\_version.fileformat**

Alternatively, the ISTP format uses a slightly different ordering: project\_dataform\_instrument\_time\_version.fileformat, but we don't recommend this format anymore. 

Filenames must carry the project and instrument for uniqueness and clarity. Use **only alphabet characters, numbers, hyphens, underscores, and periods**, so the names are valid on all common file systems. Use **all lower case filenames** unless absolutely necessary, to avoid confusion with files that differ only by case.

### Field descriptions used in file naming and data collection naming

**(1) project/source/mission/spacecraft**

Shortest string that clearly describes and distinguishes from other spacecraft and projects (Metadata dictionary names: ISTP: "Source", SPASE: "Observatory")

Unless a hyphen is clearly needed, missions and instrument names with numbers should be put together; for instance, RBSP-B should be encoded as rbspb.

**(2) instrument**

Instrument name, 'all' for all instruments of a project, "combined" or "merged" for subsets (Metadata dictionary names: ISTP: "Descriptor", SPASE: "Instrument")

**(3) dataform/datatype**

Characteristics of the dataset that distinguish it from others (including plausible ones created later) using some meaningful combination of parameters, resolution, format, compression (Metadata dictionary names: ISTP: "Datatype", SPASE: "ProviderResourceName", "ProviderProcessingLevel")

*   Parameters: AC vs DC, AVG for average, or ISTP K0, K1, H0, etc. 
*   If desired, the **level** (L0, L1, L2 or kp (key parameter), sp (summary parameter), etc.) may be prepended to the data collection name to sort by these levels (such as l2-gms-62ms).
*   Resolution: temporal resolution using time codes: ms, min, s, hr, day, week, month; round off resolutions for varying resolutions; preferably note all time resolutions in the data collection. Examples: 500ms for 0.5sec resolution, 6s for 6sec, 5min for 5 minutes, 2hr for 2 hour, 1day for daily
*   Format: ascii, cdf (include in data collection directory name, but data files use this as file extension)
*   Compression: zip, gz, tar.gz (include in data collection directory name, but data files use this as file extension)

**(4) time**

begin time (or begin and end time if required) in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format ("t" between day and hour if desired) and always 4-digit years. Time preferably uses month and day (MMDD) rather than day of year (DDD) for consistency. Avoid using too much time resolution that could possibly change the begin time (and thus the file name) in tiny ways when the file is reprocessed. 

*   YYYYMMDDTHHMMSS (truncating where sensible)
*   YYYYDDDTHHMMSS (where DDD is day of year, with 001 = Jan 1)
*   YYYYqx (for quarter year: q1, q2, q3, q4, but discouraged)

**(5) version**

reprocessing version; preferably uses a format of "vNN" where NN=01, 02, 03, etc. Some projects use a more complicated versioning scheme, such as Release, Major, Minor (v02.13.004). (Metadata dictionary names: ISTP: "Data Version", SPASE: "")

**(6) file format**

(Metadata dictionary names: SPASE: "Format") usually in the file extension, including these:

*   standard science format: ".cdf", ".hdf", ".fits"
*   ASCII data format: ".asc" (not ".txt" which is reserved for text descriptions)
*   binary data format: ".vmsbin", ".os2bin", ".idl", ".xdr", ".ieeebin" (reserve ".dat" for unknown or uncommon binary data files)
*   software: ".for", ".c", ".pro", ".class", ".pas", ".pl"
*   document text format: ".txt" (".doc" for MS Word files only!)
*   graphics format: ".gif", ".jpeg", ".ps", ".png", ".tiff"
*   appended compression/collection: ".gz", ".tar.gz", ".tar.Z", ".zip", ".sit" (".bin" is MacBinary format or WordPerfect)  (Metadata dictionary names: SPASE: "Encoding")

It is important to distinguish text files from binary ones when the user is transferring them via FTP or the user wants to examine them. EBCDIC, BCD and 36bit file formats are discouraged. The varying fields of filenames can be described with the [Heliophysics URI Template Standard](https://github.com/hapi-server/uri-templates/wiki/Specification).


Appendix: 00readme.txt template
-------------------------------

00readme.txt file in each directory describes the directory contents and points to directories below and back to higher directories and other info.

*   Keep short (point to 00readme\_long.txt when longer file required to contrast various instruments or datasets).
*   Use < > around URLs and "/" at end for directories.
*   Use URLs to point to software and documentation.
*   Users may come into hierarchy at any level so each 00readme.txt should stand alone and place the user in hierarchy.

### Example 00readme.txt
_(1-line title)_  

Dynamics Explorer-2 (DE 2) Magnetometer Instrument (MAGB) Data  

_(location of this file)_  

 Data Directory
 :   
 [https://spdf.gsfc.nasa.gov/pub/data/de/de2/magnetic_fields_magb/00readme.txt](https://spdf.gsfc.nasa.gov/pub/data/de/de2/magnetic_fields_magb/00readme.txt)  

_(short description of directory)_  

This directory gathers data for the MAG-B instrument that flew on the DE 2 spacecraft   
which was launched on 3 August 1981 into an elliptical orbit with an altitude range   
of 300 km to 1000 km and re-entered the atmosphere on 19 February 1983.   

_(one line for each sub-directory name and short descriptive title)_   

Subdirectories:
    /gms\_62ms\_vmsbin/  High resolution magnetic field in VMS binary files (NSSDC ID: 81-070B-01G)

These high-resolution (16 samples per second) MAGnetometer (MAG-B) data are provided 
in GMS coordinates in VAX binary fixed-length format as daily files including orbit 
information. The data are for the time period from Aug 10, 1981 to Feb 16, 1983. 

The following documentation files are included in this directory:   
<pre><code>
    magb\_instrument\_data.txt: A description of the MAG-B instrument and data   
    data\_format\_description.txt: A description of the MAG-B GMS data format and software    
    read\_data.pro: An IDL program to read data into arrays   
    read\_and\_average\_data.pro: An IDL program to read and average the data    
    read\_requiring\_VAX\_UNIX\_conversion.pro: An IDL program to read data, requires VAX to UNIX conversion subroutine   
    VAX\_UNIX\_conversion.pro:  IDL subroutine for VAX to UNIX conversion 
</code>
</pre>

_(Any other pointers to documentation and software)_

Additional related information and data services: 
   NSSDC's DE-1 magnetometer Master Catalog: <http://nssdc.gsfc.nasa.gov/nmc/experimentDisplay.do?id=1981-070B-01>
   Heliophysics Data Portal <http://heliophysicsdata.gsfc.nasa.gov/websearch/dispatcher?action=RESULT\_LIST\_PANE\_ACTION&command=ProductViewCmd&pid=1143>

   Merged VEFI-MAGB data set: MAGB data are also available online in the form of merged VEFI 
   and MAG-B data sets (1/2-second and 1/16-second resolution) in directory magnetic\_electric\_fields\_vefi\_mag 
   and the 1/2-second data also for plotting at <https://omniweb.gsfc.nasa.gov/ftpbrowser/ftphelper.html>

Please acknowledge the NASA Space Physics Data Facility and the instrument's 
Principal Investigator for data usage.

_(short list of keywords for search engines)_ 
Keywords: Sun-Earth Connections, space physics, magnetosphere, ionosphere

Data contact:  [NASA-SPDF-Support@nasa.onmicrosoft.com]( NASA-SPDF-Support@nasa.onmicrosoft.com)

* * *

Document Version 1.5  
Original: 2015 November 13 by Robert Candey  
Revised: 2016 February 16 by Robert Candey  
Revised: 2019 June 14 by Robert Candey  
Revised: 2019 Nov. 5 by Robert Candey   
Revised: 2024 February 23 by Lan Jian
