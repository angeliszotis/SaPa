from tkinter import *
import tkinter as tk
import sys
import fileinput
import glob

root = Tk()
root.title('SaPa')
root.geometry("400x400")
class Log:

    def __init__(self,master):
        frameA = Frame(master)
        frameA.pack()

        self.e = Entry(master,bg="white")
        self.e.pack()

        self.btn = Button(master,text="logIn",command=self.loginclick)
        self.btn.pack(pady=20)


    def loginclick(self):
        Frase="123"
        if self.e.get() == Frase :
            print("yes")
            self.newWindow()
            self.e.delete(0,END)
            self.btn['state']= 'disable'
        else:
            sys.exit()

    def newWindow(self):
        nw =Toplevel()
        nw.title("SaPa Control Accounts")
        nw.geometry("600x600")

        #Three Entrys
        self.acLabel=Label(nw,text="Παροχως Λογαριασμου").grid(row=0,column=3)
        self.eAcc = Entry(nw).grid(row=1,column=3)

        self.usLabel=Label(nw,text="Ονομα Λογαριασμου").grid(row=2,column=3)
        self.eUs = Entry(nw).grid(row=3,column=3)


        self.paLabel=Label(nw,text="Κωδικος Λογαριασμου").grid(row=4,column=3)
        self.ePa = Entry(nw).grid(row=5,column=3)


        self.btnInsert=Button(nw,text="Επιβεβεωση",bg="green",command=self.insertF).grid(row=6,column=3)

        self.btnRemove=Button(nw,text="Αφαιρεση",bg="red",command=self.removeF).grid(row=8,column=0)

        #Text
        self.text = Text(nw,width=45,height=25,padx=10)
        self.text.grid(row=0,column=0,columnspan=3,rowspan=6)
        x=0
        self.filename = glob.glob("./data/*.txt")
        #print(filename)
        for i in self.filename:
            with open(str(self.filename[x]),"r+") as fo:
           #fo = open(str(filename[x]),"r+")
                for line in fo:
                    self.text.insert(END,line)
                    
                self.text.insert(END,"\n--------------------------------------------\n")
                x+=1
        self.text.config(state=DISABLED)

    def insertF(self):
        pass
    def removeF(self):
        pass


def main():
    o1=Log(root)  
    root.mainloop()

if __name__ == "__main__":
    main()
