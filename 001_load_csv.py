# -*- coding: utf-8 -*-
"""
Created by Gabe for practice
"""

import os, sys
import tkFileDialog
import unicodecsv
import pandas as pd



def readfile(fpath):
    with open(fpath) as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)

def readwithpandas(fpath):
    passengers = pd.read_csv(fpath)
    headers = list(passengers.columns.values)
    #print passengers.head(10)\

    p2 = passengers[passengers['Sex'] == 'male']
    print p2[['Name', 'PassengerId', 'Pclass', 'Sex'] ].head(20)

    #print passengers[passengers['Sex'] == 'male'].head(10)
    #print passengers[passengers['Sex'] == 'male'].head(10)


def countgender(data):
    males = []
    females = []
    unknowncount = 0

    for r in data:
        if r['Sex'] == 'male':
            males.append(r['Name'])
        elif r['Sex'] == 'female':
            females.append(r['Name'])
        else:
            unknowncount += 1

    print str(len(males)) + str(' Males')
    print str(len(females)) + str(' Females')
    print str(unknowncount) + str(' Unknown')

    print '\n'.join(males)



def main():

    fpath = tkFileDialog.askopenfilename(filetypes=[('csv files', '.csv'),('text files', '.txt')],
                                        initialdir=[('/home/gm/Desktop/Data_Science_Course/01_Classes/C02_intro_to_data_analysis')])
    if fpath == '':
        exit()


    '''
    print 'basename: ' + os.path.basename(fpath)
    print 'dirname: ' + os.path.dirname(fpath)

    (fpath, fname) = os.path.split(fpath)
    (fnameshort, fnameext) = os.path.splitext(fname)
    '''

    readwithpandas(fpath)
    #data = readfile(fpath)
    #print data[0].keys()
    #countgender(data)

    '''
    names = []
    for row in data:
        names.append(row['Name'])
    print '\n'.join(names)
    print len(names)
    '''

    # for k, v in data.iteritems():
    #     print str(k) + ' ' + str(v)




# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
