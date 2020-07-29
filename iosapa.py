# -*- coding: utf-8 -*-
# *-* coding: iso-8859-1 *-*
import Acc
import fileinput
import glob
import os

class IoSapa:
    def __init__(self):
        pass
    
    def writeF(self,filename,username,password):
        with open('./data/{}.txt'.format(filename),'w') as fo:
            account = Acc.Acc(filename,username,password)
            fo.write(account.toString())

    def removeF(self,path):

        print (path)
        if os.path.isfile('./data/{}.txt'.format(path)):
            os.remove('./data/{}.txt'.format(path))
        else:
            print("Δεν υπαρχει ο παροχος");
