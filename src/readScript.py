# -*- coding: utf-8 -*-
import os
import sqlite3

print(os.getcwd())

sqlite3_file = 'reCast.sqlite'

conn = sqlite3.connect(sqlite3_file,timeout=10)
c = conn.cursor()

with open("biggertest.txt", 'r') as f:
    data = f.readlines()

with open('testSCRIPTparse.txt', 'w') as f:

    # testing purposes
    header_data = ()
    psrc_data = []
    npsrc_data = []
    lat_lon_data = ()

    rec_count = 0

    '''
        listing out all of the HEADER columns
    
        STATION, YEAR, MONTH, DAY, NUMLEV, PSRC, NPSRC, LAT, LON, LVLTYPE1, LVLTYPE2,
        ETIME, PRESSURE, GPH, TEMP, RH, DPDP, WDIR, WSPD
    '''

    c.execute('''CREATE TABLE IF NOT EXISTS RADIOSONDE_HEADER(STATION TEXT, YEAR TEXT, MONTH TEXT, DAY TEXT, NUMLEV INT, 
    PSRC TEXT, NPSRC TEXT,LAT INT, LON INT)''')

    c.execute('''CREATE TABLE IF NOT EXISTS RADIOSONDE_DATA(LVLTYPE1 INT, LVLTYPE2 INT, ETIME INT, PRESSURE INT, GPH INT, 
    TEMP INT, DPDP INT, WDIR INT, WSPD INT)''')

    for icounter,ivalue in enumerate(data):
        testsplitlines = ivalue.splitlines()

        for line in testsplitlines:
            words = line.split()

            if (line[0] == '#'):
                rec_count += 1
                if(len(words) == 10):

                    header_data = tuple(words[:7])
                    psrc_data.append(words[7])
                    npsrc_data.append('NULL')
                    lat_lon_data = tuple(words[8:])

                    # testing purposes
                    # npsrc header differences
                    #print(npsrc_data)

                    f.write(line)
                    for x in range(int(words[6])):
                        c.execute('''INSERT OR IGNORE INTO RADIOSONDE_HEADER(STATION, YEAR,
                                MONTH, DAY, NUMLEV, PSRC, NPSRC, LAT, LON) VALUES(?,?,?,?,?,?,?,?,?)''',
                                (words[0].strip('#'),words[1],words[2],words[3],words[6],words[7],'NULL',
                                int(words[8])/10000.,int(words[9])/10000.))
                if(len(words) == 11):

                    #header_data = tuple(words[:7])
                    psrc_data.append(words[7])
                    npsrc_data.append(words[8])

                    # testing purposes
                    # npsrc header differences
                    #print(npsrc_data)
                    for x in range(int(words[6])):
                        c.execute('''INSERT OR IGNORE INTO RADIOSONDE_HEADER(STATION, YEAR,
                                    MONTH, DAY, NUMLEV, PSRC, NPSRC, LAT, LON) VALUES(?,?,?,?,?,?,?,?,?)''',
                                    (words[0].strip('#'), words[1], words[2], words[3], words[6], words[7], words[8],
                                    int(words[9]) / 10000., int(words[10]) / 10000.))
            else:

                '''
                        listing out all of DATA columns

                        LVLTYPE1, LVLTYPE2, ETIME, PRESSURE, GPH, TEMP, RH, DPDP, WDIR, WSPD
                '''
                if (len(words) == 9):
                    c.execute('''INSERT OR IGNORE INTO RADIOSONDE_DATA(LVLTYPE1,LVLTYPE2,
                        ETIME, PRESSURE, GPH, TEMP, DPDP, WDIR, WSPD) VALUES (?,?,?,?,?,?,?,?,?)''', (line[0],
                        line[1], words[1], words[2].strip('AB'), words[3].strip('B'), words[4][:4].strip('B'),
                        words[6], words[7], words[8]))
                if (len(words) == 8):
                    c.execute('''INSERT OR IGNORE INTO RADIOSONDE_DATA(LVLTYPE1,LVLTYPE2,
                        ETIME, PRESSURE, GPH, TEMP, DPDP, WDIR, WSPD) VALUES (?,?,?,?,?,?,?,?,?)''', (line[0],
                        line[1], words[1], words[2].strip('AB'), words[3].strip('B'), words[4][:4].strip('B'),
                        words[5], words[6], words[7]))

# spits out how many headers are executed
print("There are", str(rec_count), "recordings")
conn.commit()
conn.close()