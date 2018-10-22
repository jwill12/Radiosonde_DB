# Radiosonde Project

Parsing and Querying tool to identify NOAA/ERSL/GSD RAOB radiosonde data

[To visit main site](https://www.ncdc.noaa.gov/data-access/weather-balloon/integrated-global-radiosonde-archive)

[For FTP link to Data](ftp://ftp.ncdc.noaa.gov/pub/data/igra)

[For HTTP link to Data](https://www1.ncdc.noaa.gov/pub/data/igra/)

[Station list](ftp://ftp.ncdc.noaa.gov/pub/data/igra/igra2-station-list.txt)


## FILE DESCRIPTIONS & USAGE
see readME.txt within /test directory

### FOR COMPLETE HEADER FORMATTING [link](ftp://ftp.ncdc.noaa.gov/pub/data/igra/data/igra2-data-format.txt)

COL | DESCRIPTION
--- | :---:
ID | station identification code. [For Complete List](ftp://ftp.ncdc.noaa.gov/pub/data/igra/data/igra2-data-format.txt)
YEAR | is the year of the sounding
MONTH | is the month of sounding
DAY | is the day of the sounding
NUMLEV | is the number of levels in the sounding
PSRC | is the data source code for pressure levels
NPSRC | is the data source code for non-pressure levels
LAT | is the Latitude at which the sounding was taken
LON | is the Longitude at which the sounding was taken


Var | Col | Type|
----| :----:| ----|
ID | 2-12 | CHAR|
YEAR | 14-17 | INT|
MONTH | 19-20 | INT|
DAY | 22-23 | INT|
NUMLEV | 33-36 | INT|
PSRC | 38-45 | CHAR|
NPSRC | 47-54 | CHAR|
LAT | 56-62 | INT|
LON | 64-71 | INT|


### FOR DATA FORMATTING [link](ftp://ftp.ncdc.noaa.gov/pub/data/igra/data/igra2-data-format.txt)

COL | DESCRIPTION
--- | ---
LVLTYP1 | is the major level type indicator. `1 = Standard Pressure Level, 2 = Other Pressure Level, 3 = Non-pressure level` [For Complete List](ftp://ftp.ncdc.noaa.gov/pub/data/igra/data/igra2-data-format.txt)
LVLTYP2 | is the minor level type indicator. `1 = Surface, 2 = Tropopause, 0 = Other` [For Complete List](ftp://ftp.ncdc.noaa.gov/pub/data/igra/data/igra2-data-format.txt)
ETIME | is the elapsed time since launch. `format is in MMMSS; MMM represents minutes & SS represents seconds. -8888 = Value removed, -9999 = Value is missing` [For Complete List](ftp://ftp.ncdc.noaa.gov/pub/data/igra/data/igra2-data-format.txt)
PRESSURE | is the reported pressure. `Pa or mb * 100, -9999 = missing value` [For Complete List](ftp://ftp.ncdc.noaa.gov/pub/data/igra/data/igra2-data-format.txt)
GPH | is the reported geopotential height `meters above sea level. -8888 = value removed, -9999 = value missing` [For Complete List](ftp://ftp.ncdc.noaa.gov/pub/data/igra/data/igra2-data-format.txt)
TEMP | is the reported temperature. `degrees C to tenths, -8888 = value removed by IGRA, -9999 = value is missing` 
RH | is the reported relative humidity `percent to nearest tenths, -8888 = value removed, -9999 = value missing` [For Complete List](ftp://ftp.ncdc.noaa.gov/pub/data/igra/data/igra2-data-format.txt)
DPDP | is the reported dewpoint depression `degrees to nearest tenths. -8888 = value removed, -9999 = value missing`  [For Complete List](ftp://ftp.ncdc.noaa.gov/pub/data/igra/data/igra2-data-format.txt)
WDIR | is the reported wind direction `degrees to nearest tenths. -8888 = vale removed, -9999 = value missing`  [For Complete List](ftp://ftp.ncdc.noaa.gov/pub/data/igra/data/igra2-data-format.txt)
WSPD | is the reported wind speed `meters per second to the tenths. -8888 = value removed, -9999 = vale missing`  [For Complete List](ftp://ftp.ncdc.noaa.gov/pub/data/igra/data/igra2-data-format.txt)


Var | Col | Type|
--- | :---:| ---|
LVLTYP1 | 1-1 | INT|
LVLTYP2 | 2-2 | INT|
ETIME | 4-8 | INT|
PRESSURE | 10-15 | INT|
GPH | 17-21 | INT|
TEMP | 23-27 | INT|
RH | 29-33 | INT|
DPDP | 35-39 | INT|
WDIR | 41-45 | INT|
WSPD | 47-51 | INT|




