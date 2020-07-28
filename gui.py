from PyQt5.QtWidgets import QMainWindow , QApplication , QWidget, QLineEdit , QPushButton ,QLabel,QFrame 
from PyQt5 import QtCore
from guiMain import *
import sys
from SingIn import SingIn
class Window(QMainWindow):
    global trysin
    def __init__(self):
        super().__init__()
        
        self.title = "SaPa"
        self.top = 250
        self.left = 250
        self.width = 400
        self.height = 400

        self.InitWindow()
        
        self.trysin=0
    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)

        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(100,100)
        self.textbox.resize(200,40)

        # Create a Button
        self.button = QPushButton('LogIn',self)
        self.button.move(130,150)

        # Connect button to function click
        self.button.clicked.connect(self.singInClick)

        #Create Lable
        label = QLabel(self)
        label.setFrameStyle(QFrame.Panel)
        label.setText("SaPa\nΜε 3ης προσπαθειες κληνει")
        label.setGeometry(100,5,200,90)
        label.setAlignment(QtCore.Qt.AlignCenter)

        self.show()

    def singInClick(self):
        self.trysin+=1
        p1=SingIn(self.textbox.text())
        p2=Window1()
        if self.trysin >= 3:
            print("exit")
            sys.exit("More than 3 Fail")
        elif p1 :
            print('hi')
            p2.InitWindow()
            #self.close()
            self.textbox.setText("")


