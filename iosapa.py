# -*- coding: utf-8 -*-
# *-* coding: iso-8859-1 *-*
import Acc
import fileinput
import glob
import os

class IoSapa:
    def __init__(self):
        pass
    
    def writeF(self,filename):
        with open('./data/{}.txt'.format(filename),'w') as fo:
            account = Acc.Acc( filename,raw_input('Όνομα Λογαριασμού:'),raw_input('Κωδικός Λογαριασμού:'))

            fo.write(account.toString())

    def readF(self):
        x=0
        filename = glob.glob("data/*.txt")
        for i in filename:
            with open(str(filename[x]),"r+") as fo:
                x+=1
                #print '---------------------'
                for line in fo:
                    print(line)

    def removeF(self):

        path = raw_input("Δώσε Ονομα Παρωχου για διαγραφη:")
        print path
        if os.path.isfile('./data/{}.txt'.format(path)):
            os.remove('./data/{}.txt'.format(path))
        else:
            print("Δεν υπαρχει ο παροχος");


