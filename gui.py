from PyQt5.QtWidgets import QMainWindow , QApplication , QWidget, QLineEdit , QPushButton
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.title = "SaPa"
        self.top = 100
        self.left = 100
        self.width = 400
        self.height = 400

        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)

        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20,20)
        self.textbox.resize(200,40)

        # Create a Button
        self.button = QPushButton('LogIn',self)
        self.button.move(20,80)

        # Connect button to function click
        #self.button.clicked.connect(self.onclick)

        self.show()

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())
