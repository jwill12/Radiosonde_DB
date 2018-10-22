class ScrubberRadio():

    def __init__(self,
                 year=None,
                 month=None,
                 day=None):

        '''
                    Class that extracts necessary dates for the parser.
                    (DOES NOT SEND DATA TO DATABASE)

                    Args:
                    year(str): year of recording
                    month(str): month of recording
                    day(str): day of recording
        '''

        self.year = year
        self.month = month
        self.day = day

    def scrubber(self):

        '''
                    function simply parses the file &
                    writes to a txt file
        '''

        with open("test2.txt", 'r') as f:
            data = f.readlines()

        with open('testCLASSparse.txt', 'w') as f:

            for_header = []
            for_year = []
            for_month = []
            for_day = []
            for_lat = []
            for_lon = []
            for_numlev = []
            for_psrc = []
            for_npsrc = []

            '''
                            listing out all of them columns

                            STATION, YEAR, MONTH, DAY, NUMLEV, PSRC, NPSRC, LAT, LON, LVLTYPE1, LVLTYPE2,
                            ETIME, PRESSURE, GPH, TEMP, RH, DPDP, WDIR, WSPD
            '''

            for icounter, ivalue in enumerate(data):
                testsplitlines = ivalue.splitlines()

                for line in testsplitlines:
                    words = line.split()

                    if (line[0] == '#'):

                        if (len(words) == 10):
                            if (words[1] >= self.year and words[2] <= self.month and words[3] <= self.day):
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
                        if (len(words) == 11):
                            if (words[1] >= self.year and words[2] <= self.month and words[3] <= self.day):
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

                    for ic, iv in enumerate(for_day):
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
                                    if (int(words[2].strip('AB')) <= 100000):
                                        # print(words[2]) correct
                                        f.write(line)
                                        print(line)
                            if (line[0] == '2'):
                                if (line[1] == '0' or line[1] == '1' or line[1] == '2'):
                                    if (int(words[2].strip('AB')) <= 100000):
                                        # print(words[2]) correct
                                        f.write(line)
                                        print(line)
                            if (line[0] == '3'):
                                if (line[1] == '0' or line[1] == '1' or line[1] == '2'):
                                    if (int(words[2].strip('AB')) <= 100000):
                                        # print(words[2]) correct
                                        f.write(line)
                                        print(line)
                        if (len(words) == 8):
                                if (line[0] == '1'):
                                    if (line[1] == '0' or line[1] == '1' or line[1] == '2'):
                                        if (int(words[2].strip('AB')) <= 100000):
                                            # print(words[2]) correct
                                            f.write(line)
                                            print(line)
                                if (line[0] == '2'):
                                    if (line[1] == '0' or line[1] == '1' or line[1] == '2'):
                                        if (int(words[2].strip('AB')) <= 100000):
                                            # print(words[2]) correct
                                            f.write(line)
                                            print(line)
                                if (line[0] == '3'):
                                    if (line[1] == '0' or line[1] == '1' or line[1] == '2'):
                                        if (int(words[2].strip('AB')) <= 100000):
                                            # print(words[2]) correct
                                            f.write(line)
                                            print(line)