from PyQt5.QtWidgets import QMainWindow , QApplication , QWidget, QLineEdit , QPushButton ,QLabel,QFrame, QPlainTextEdit 
from PyQt5 import QtCore
import sys
from SingIn import SingIn
from iosapa import IoSapa
import glob
import fileinput
class Window1(QMainWindow):
    global trysin
    def __init__(self):
        super().__init__()
        
        self.title = "SaPa"
        self.top = 250
        self.left = 250
        self.width = 600
        self.height = 600

        self.InitWindow()
        
        self.trysin=0
    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)

        # Create textbox
        self.textboxA = QLineEdit(self)
        self.textboxA.move(5,320)
        self.textboxA.resize(185,40)
    # Create textbox
        self.textboxU = QLineEdit(self)
        self.textboxU.move(205,320)
        self.textboxU.resize(185,40)
    # Create textbox
        self.textboxP = QLineEdit(self)
        self.textboxP.move(405,320)
        self.textboxP.resize(185,40)

        #Create a Button
        self.buttonC = QPushButton('Εισαγωγή',self)
        self.buttonC.move(405,400)
         #Create a Button
        self.buttonD = QPushButton('Διαγραφή',self)
        self.buttonD.move(5,400)
       
       # Connect button to function click
        self.buttonC.clicked.connect(self.buttonClickC)
        self.buttonD.clicked.connect(self.buttonClickD)

        #Create iosapa Obj
        iosapa = IoSapa()
        #Create Plain TextEdit
        self.pt = QPlainTextEdit(self)
        i=0
        z=0
        x=0
        
        filename = glob.glob("data/*.txt")
        for i in filename:
            with open(str(filename[x]),"r+") as fo:
                
                for line in fo:
                    print(line)
                    self.pt.appendPlainText(line)
                self.pt.appendPlainText("----------------------------")
                x+=1

       # for x in iosapa.readF():
        #    print(x)
         #   self.pt.appendPlainText(str(x))
        self.pt.move(5,5)
        self.pt.resize(590,300)
        #Create Lable
        # label = QLabel(self)
        #label.setFrameStyle(QFrame.Panel)
        #label.setText(iosapa.readF())
        #label.setGeometry(5,5,450,500)
        #label.setAlignment(QtCore.Qt.AlignLeft)

        self.show()

    def buttonClickC(self):
        iosapa=IoSapa()
        iosapa.writeF(str(self.textboxA.text()),str(self.textboxU.text()),str(self.textboxP.text()))
        #window = Window1()
        #window.InitWindow()

    def buttonClickD(self):
        iosapa=IoSapa()
        
        iosapa.removeF(str(self.textboxA.text()))
        #window = Window1()
        #window.InitWindow()

App = QApplication(sys.argv)
#window = Window1()
sys.exit(App.exec_())
