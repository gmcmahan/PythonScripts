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




def main():

    fpath = tkFileDialog.askopenfilename(filetypes=[('csv files', '.csv'),('text files', '.txt')],
                                        initialdir=[('/home/')])
    if fpath == '':
        exit()


    readwithpandas(fpath)
    #data = readfile(fpath)
    #print data[0].keys()



# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
