# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 07:11:08 2016

@author: gm
"""


import os#, sys
import Tkinter as tk
from tkFileDialog import askdirectory




def listPaths(indir):
    fList = []
    for path, subdirs, files in os.walk(indir):
        for name in files:
            fList.append(os.path.join(path, name))
    return fList


def main():
    root = tk.Tk()
    root.withdraw() #Hide blank dialog    
    #get directory of the full path of this python file
    initialdir = os.path.dirname(os.path.realpath(__file__))
    fdir = askdirectory(initialdir=([initialdir]))    
    root.destroy() #kill Tkinter
    #print fdir

    fList =  listPaths(fdir)
    print "\n".join(fList)






if __name__ == "__main__":
    main()