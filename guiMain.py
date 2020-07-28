from PyQt5.QtWidgets import QMainWindow , QApplication , QWidget, QLineEdit , QPushButton ,QLabel,QFrame, QPlainTextEdit 
from PyQt5 import QtCore
import sys
from SingIn import SingIn
from iosapa import IoSapa
class Window(QMainWindow):
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
      #  self.textbox = QLineEdit(self)
    #    self.textbox.move(100,100)
      #  self.textbox.resize(200,40)

        # Create a Button
      #  self.button = QPushButton('LogIn',self)
      #  self.button.move(130,150)

        # Connect button to function click
       # self.button.clicked.connect(self.singInClick)

        #Create iosapa Obj
        iosapa = IoSapa()
        #Create Plain TextEdit
        self.pt = QPlainTextEdit(self)
        i=0
        z=0
        for x in iosapa.readF():
            print(x)
            self.pt.appendPlainText(str(x))
        self.pt.move(5,5)
        self.pt.resize(450,500)
        #Create Lable
       # label = QLabel(self)
        #label.setFrameStyle(QFrame.Panel)
        #label.setText(iosapa.readF())
        #label.setGeometry(5,5,450,500)
        #label.setAlignment(QtCore.Qt.AlignLeft)

        self.show()

    def singInClick(self):
        self.trysin+=1
        if self.trysin >= 3:
            sys.exit("More than 3 Fail")
        singin= SingIn(self.textbox.text())
        self.textbox.setText("")

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())
