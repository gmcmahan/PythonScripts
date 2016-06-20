# -*- coding: utf-8 -*-
"""
Created by Gabe for practice
"""

import os, sys
import tkFileDialog as tk
from os import listdir
from os.path import isfile, join
import re




def dostuff(fdir):
    fileList = [f for f in listdir(fdir) if isfile(join(fdir, f))]

    months = ["Jan","Feb","March","April","May","June","July","August","Sept","Oct","Nov","Dec"]
    month_lookup = {"Jan":"01","Feb":"02","March":"03","April":"04","May":"05"
                    ,"June":"06","July":"07","August":"08","Sept":"09","Oct":"10"
                    ,"Nov":"11","Dec":"12"}

    for f in fileList:
        #Get year
        match = re.search(r'\s\d{4}\.txt', f)
        if match:
            year = match.group().replace('.txt', '').strip()
        else:
            continue

        #convert month
        for m in months:
            if m in f:
                month = month_lookup[m]
                break

        #Get day
        match = re.search(r'\s\d{1,2}\,', f)
        if match:
            day = match.group().replace(',', '').strip()


        #Rename File
        if f[-4:] == '.txt':
            newname = '%s_%s_%s_%s' % (year, month, day, f)
            orig = fdir + '/' + f
            new = fdir + '/' + newname
            os.rename(orig,new)



def main():
    root = tk.Tk()
    root.withdraw()
    initialdir = os.path.dirname(os.path.realpath(__file__))
    #initialdir = os.path.dirname(os.path.dirname(initialdir))
    fdir = tk.askdirectory(initialdir=[(initialdir)])
    root.destroy()
    # fpath = tkFileDialog.askopenfilename(filetypes=[('csv files', '.csv'),('text files', '.txt')],
    #                                     initialdir=[('')])
    if fdir == '':
        exit()

    dostuff(fdir)






# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
