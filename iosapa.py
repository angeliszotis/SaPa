# -*- coding: utf-8 -*-
# *-* coding: iso-8859-1 *-*
import Acc
import fileinput

class IoSapa:
    global filename
    filename = 'test'

    def __init__(self,filename):
        self.filename = filename

    def writeF(self):
        fo = open('{}.txt'.format(filename),"ab")
        
       # whereuse =
       #username =
        #password = 
        account = Acc.Acc( raw_input('Πάροχος Λογισμού:'),raw_input('Όνομα Λογαριασμού:'),raw_input('Κωδικός Λογαριασμού:'))

        fo.write(account.toString())
        fo.close()

    def readF(self):
        fo = open('{}.txt'.format(filename),"r+")
        for i in fo:
            print(i)
        fo.close()

    def positionF(self):
        fo = open('{}.txt'.format(filename),"r+")
        x = raw_input("Dose onoma")
        for i in fo:

            print(i)

        position = fo.tell()
        print "perioxi:",position
        #reposition 
        position = fo.seek(0.0)
        fo.close()

    def changeF(self):
        #read input file
        fin = open( '{}.txt'.format(filename),"rt")
        #read file contents to string
        data = fin.read()
        #replace all occurrences of the required string
        data = data.replace(raw_input('leksi find:'), raw_input('leksi replace:'))
        #close the input file
        fin.close()
        #open the input file in write mode
        fin = open('{}.txt'.format(filename), "wt")
        #overrite the input file with the resulting data
        fin.write(data)
        #close the file
        fin.close()

p1 = IoSapa("takis")
x = raw_input("dose ti thes")
if x == 'w' :
    p1.writeF()
else :
    p1.changeF()
