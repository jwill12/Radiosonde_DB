# -*- coding: utf-8 -*-
import os
import sqlite3

print(os.getcwd())

sqlite3_file = 'testclasssql.sqlite'

conn = sqlite3.connect(sqlite3_file,timeout=10)
c = conn.cursor()

with open("test2.txt", 'r') as f:
    data = f.readlines()

with open('testivalue', 'w') as f:

    for_header = []
    for_year = []
    for_month = []
    for_day = []
    for_lat = []
    for_lon = []
    for_numlev = []
    for_psrc = []
    for_npsrc = []

    for_lvl1 = []
    for_lvl2 = []
    for_etime = []
    for_press = []

    for_gph = []
    for_temp = []
    for_rh = []
    for_dpdp = []
    for_wdir = []
    for_wspd = []

    '''
        listing out all of them columns
    
        STATION, YEAR, MONTH, DAY, NUMLEV, PSRC, NPSRC, LAT, LON, LVLTYPE1, LVLTYPE2,
        ETIME, PRESSURE, GPH, TEMP, RH, DPDP, WDIR, WSPD
    '''

    c.execute('''CREATE TABLE RADIOSONDE(STATION TEXT, YEAR TEXT, MONTH TEXT, DAY TEXT, NUMLEV INT, 
    PSRC TEXT, NPSRC TEXT,LAT INT, LON INT, LVLTYPE1 INT, LVLTYPE2 INT, ETIME INT, PRESSURE INT, GPH INT, 
    TEMP INT, RH TEXT, DPDP INT, WDIR INT, WSPD INT)''')
    for icounter,ivalue in enumerate(data):
        testsplitlines = ivalue.splitlines()

        for line in testsplitlines:
            words = line.split()

            if (line[0] == '#'):

                if(len(words) == 10):
                    if (words[1] >= '1947' and words[2] <= '07' and words[3] <= '23'):
                        for_header.append(words[0][1:])

                        for_year.append(words[1])

                        for_month.append(words[2])

                        for_day.append(words[3])

                        for_numlev.append(words[6])

                        for_psrc.append(words[7])

                        for_npsrc.append("NULL")

                        for_lat.append(words[8])
                        for_latDeg = int(for_lat[0]) / 10000.

                        for_lon.append(words[9])
                        for_lonDeg = int(for_lon[0]) / 10000.

                        f.write(line)
                        print(line)
                    else:
                        break
                if(len(words) == 11):
                    if (words[1] >= '1947' and words[2] <= '07' and words[3] <= '23'):
                        for_header.append(words[0][1:])

                        for_year.append(words[1])

                        for_month.append(words[2])

                        for_day.append(words[3])

                        for_numlev.append(words[6])

                        for_psrc.append(words[7])

                        # no changes until after words[8],
                        # where npsrc can only be derived from a header w/ a length of 11
                        for_npsrc.append(words[8])

                        f.write(line)
                        print(line)
                    else:
                        break
                else:
                    break
            for ic, iv in enumerate(for_header):
                header_split = iv.split()

            for ic, iv in enumerate(for_year):
                year_split = iv.split()

            for ic, iv in enumerate(for_month):
                month_split = iv.split()

            for ic,iv in enumerate(for_day):
                day_split = iv.split()

            for ic, iv in enumerate(for_numlev):
                numlev_split = iv.split()

            for ic, iv in enumerate(for_psrc):
                psrc_split = iv.split()

            for ic, iv in enumerate(for_npsrc):
                nsrc_split = iv.split()

            else:
                if (len(words) == 9):
                    if (line[0] == '1'):
                        if (line[1] == '0' or line[1] == '1' or line[1] == '2'):
                            if (int(words[2].strip('B')) <= 100000):
                                # print(words[2]) correct
                                print(line)
                                c.execute('''INSERT OR IGNORE INTO RADIOSONDE(STATION, YEAR,
                                MONTH, DAY, NUMLEV, PSRC, NPSRC,LAT, LON, LVLTYPE1, LVLTYPE2, ETIME, PRESSURE, GPH,TEMP,
                                RH, DPDP, WDIR, WSPD) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(header_split[0],
                                year_split[0],month_split[0],day_split[0],numlev_split[0],psrc_split[0],nsrc_split[0],for_latDeg,
                                for_lonDeg, line[0], line[1],words[1],words[2].strip('B'),words[3].strip('B'),
                                words[4].strip('B'),words[5],words[6],words[7],words[8]))
                    if (line[0] == '2'):
                        if (line[1] == '0' or line[1] == '1' or line[1] == '2'):
                            if (int(words[2].strip('B')) <= 100000):
                                # print(words[2]) correct
                                print(line)
                                c.execute('''INSERT OR IGNORE INTO RADIOSONDE(STATION, YEAR,
                                MONTH, DAY, NUMLEV, PSRC, NPSRC,LAT, LON, LVLTYPE1, LVLTYPE2, ETIME, PRESSURE, GPH,TEMP,
                                RH, DPDP, WDIR, WSPD) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                                (header_split[0],year_split[0], month_split[0], day_split[0], numlev_split[0],
                                psrc_split[0], nsrc_split[0], for_latDeg,
                                for_lonDeg, line[0], line[1], words[1], words[2].strip('B'),
                                words[3].strip('B'),words[4].strip('B'), words[5], words[6], words[7], words[8]))
                    if (line[0] == '3'):
                        if (line[1] == '0' or line[1] == '1' or line[1] == '2'):
                            if (int(words[2].strip('B')) <= 100000):
                                # print(words[2]) correct
                                print(line)
                                c.execute('''INSERT OR IGNORE INTO RADIOSONDE(STATION, YEAR,
                                MONTH, DAY, NUMLEV, PSRC, NPSRC,LAT, LON, LVLTYPE1, LVLTYPE2, ETIME, PRESSURE, GPH,TEMP,
                                RH, DPDP, WDIR, WSPD) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                                (header_split[0], year_split[0], month_split[0], day_split[0],
                                numlev_split[0],psrc_split[0], nsrc_split[0], for_latDeg,
                                for_lonDeg, line[0], line[1], words[1], words[2].strip('B'),
                                words[3].strip('B'), words[4].strip('B'), words[5], words[6],words[7], words[8]))
                if (len(words) == 8):
                    if (line[0] == '1'):
                        if (line[1] == '0' or line[1] == '1' or line[1] == '2'):
                            if (int(words[2].strip('B')) <= 100000):
                                # print(words[2]) correct
                                print(line)
                                c.execute('''INSERT OR IGNORE INTO RADIOSONDE(STATION, YEAR,
                                MONTH, DAY, NUMLEV, PSRC, NPSRC,LAT, LON, LVLTYPE1, LVLTYPE2, ETIME, PRESSURE, GPH,TEMP,
                                RH, DPDP, WDIR, WSPD) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                                (header_split[0],year_split[0], month_split[0], day_split[0], numlev_split[0],
                                psrc_split[0],nsrc_split[0], for_latDeg,
                                for_lonDeg, line[0], line[1], words[1], words[2].strip('B'),
                                words[3].strip('B'),words[4][:5].strip('B'), words[4][5:].strip('B'),
                                 words[5], words[6], words[7]))
                    if (line[0] == '2'):
                        if (line[1] == '0' or line[1] == '1' or line[1] == '2'):
                            if (int(words[2].strip('B')) <= 100000):
                                # print(words[2]) correct
                                print(line)
                                c.execute('''INSERT OR IGNORE INTO RADIOSONDE(STATION, YEAR,
                                MONTH, DAY, NUMLEV, PSRC, NPSRC,LAT, LON, LVLTYPE1, LVLTYPE2, ETIME, PRESSURE, GPH,TEMP,
                                RH, DPDP, WDIR, WSPD) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(
                                header_split[0], year_split[0], month_split[0], day_split[0], numlev_split[0],
                                psrc_split[0], nsrc_split[0], for_latDeg,
                                for_lonDeg, line[0], line[1], words[1], words[2].strip('B'),
                                words[3].strip('B'), words[4][:5].strip('B'), words[4][5:].strip('B'),
                                words[5], words[6], words[7]))
                    if (line[0] == '3'):
                        if (line[1] == '0' or line[1] == '1' or line[1] == '2'):
                            if (int(words[2].strip('B')) <= 100000):
                                # print(words[2]) correct
                                print(line)
                                c.execute('''INSERT OR IGNORE INTO RADIOSONDE(STATION, YEAR,
                                MONTH, DAY, NUMLEV, PSRC, NPSRC,LAT, LON, LVLTYPE1, LVLTYPE2, ETIME, PRESSURE, GPH,TEMP,
                                RH, DPDP, WDIR, WSPD) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(
                                header_split[0], year_split[0], month_split[0], day_split[0], numlev_split[0],
                                psrc_split[0], nsrc_split[0], for_latDeg,
                                for_lonDeg, line[0], line[1], words[1], words[2].strip('B'),
                                words[3].strip('B'), words[4][:5].strip('B'), words[4][5:].strip('B'),
                                words[5], words[6], words[7]))

conn.commit()
conn.close()