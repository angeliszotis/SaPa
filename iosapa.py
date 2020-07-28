# -*- coding: utf-8 -*-
# *-* coding: iso-8859-1 *-*
import Acc
import fileinput
import glob
import os
from array import *

class IoSapa:
    def __init__(self):
        pass
    
    def writeF(self,filename,username,password):
        with open('./data/{}.txt'.format(filename),'w') as fo:
            account = Acc.Acc(filename,username,password)
            fo.write(account.toString())

    def readF(self):
        x=0
        y=0
        filename = glob.glob("data/*.txt")
        arrprint = []
        for i in filename:
            with open(str(filename[x]),"r+") as fo:
                x+=1
                for line in fo:
                    print (line) 
                    arrprint.insert(x,[x,line])
                    y+=1
        return arrprint

    def removeF(self,path):

        print (path)
        if os.path.isfile('./data/{}.txt'.format(path)):
            os.remove('./data/{}.txt'.format(path))
        else:
            print("Δεν υπαρχει ο παροχος");

p1 = IoSapa()
p1.readF()
