# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 05:46:41 2016

@author: gabe mcmahan
"""
# Reads a MapSource Text file, reformats, and saves as CSV.

import os,sys
import Tkinter,tkFileDialog #GUI
import re


def deal_with_lat_lon(position):
    #print position
    pos = position.split(' ')
    lat = pos[0].replace("N","")
    lon = pos[1].replace("W","-")
    return lat, lon

def splitwaypointname(name):
    namesplit = name.split()
    wpt = namesplit[0]
    try:
        animalcount = namesplit[1]
    except:
        animalcount = ""
        pass

    return wpt, animalcount

def splitdatemodified(datetime):
    datetimesplit = datetime.split()
    date = datetimesplit[0]
    try:
        time = datetimesplit[1] + " " + datetimesplit[2]
    except:
        time = ""
        pass

    return date, time


def parse_file(datafile):
    data = []
    with open(datafile, "rb") as f:

        for i, line in enumerate(f):
            #linedata = line.strip().split('\t')
            linedata = line.split('\t')

            if linedata[0] == "Header":
                header = linedata
                linedata[len(linedata) - 1] = linedata[len(linedata) - 1].strip()  #removes line break from end of Categories key

            if linedata[0] == "Waypoint":
                entry = {}  #this is a new dictionary for each line
                for i, value in enumerate(linedata):
                    if header[i] == 'Name':
                        wpt, animalcount = splitwaypointname(value.strip())
                        entry["Waypoint"] = wpt
                        entry["animalcount"] = animalcount

                    if header[i] == 'Position': #This takes the position field and splits it in to lat and lon fields
                        latitude, longitude = deal_with_lat_lon(value.strip())
                        entry["latitude"] = latitude
                        entry["longitude"] = longitude

                    if header[i] == 'Date Modified':
                        dt, tm = splitdatemodified(value.strip())
                        entry["Date"] = dt
                        entry["Time"] = tm

                    if header[i] == 'Description':
                        match = re.search(r'^\d\d-\w\w\w-\d\d\s\d\d:\d\d$', value.strip())
                        if match:
                            #print match.group()
                            entry[header[i]] = ""
                            continue

                    entry[header[i]] = value.strip()
                data.append(entry)

    return data


def data_out(data, outfile):
    print outfile
    with open(outfile, 'wb') as outfile:
        # header - Remember to change this if changing output format
        outfile.write('Animal,Space,DATE,Space2,LATITUDE,LONGITUDE,GROUPSIZE,Space3,DESCRIPTION' + '\n')  #write header


        for line in data:
            Animal = line['Name'].split()[0]
            DateModified = line['Date']
            latitude = line['latitude']
            longitude = line['longitude']
            GroupSize = str(line['Name'].split()[-1])
            try:
                GroupSize = int(filter(str.isdigit, GroupSize)) #pulls digit from string
            except:
                pass
            try:
                GroupSize = int(filter(str.isdigit, GroupSize))
            except:
                pass

            Desc = line['Description']

            # When changing fields, make sure to change header fields at beginnin of this function
            outLine = Animal + ",," + DateModified + ",," + latitude + "," + longitude + "," + str(GroupSize) + ",," + Desc
            #print outLine
            outfile.write(outLine + '\n')


def main():
    initialdir = os.path.dirname(os.path.realpath(__file__))
    datafile = tkFileDialog.askopenfilename(initialdir=[(initialdir)], filetypes=[('text files', '.txt')])       #Opens File Dialog
    #print datafile
    (inFilePath, inFileName) = os.path.split(datafile)
    (inFileBaseName, inFileExtension)=os.path.splitext(inFileName)
    outFile = inFilePath + '/' +inFileBaseName + '_mod' + '.csv'         #inFileExtension   #specifies new file
    #print outFile
    if datafile != '':
        d = parse_file(datafile)
        data_out(d, outFile)


main()
