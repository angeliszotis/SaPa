import sys
from PyQt4 import QtGui , QPlainTextEdit

class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50,50,600,400)
        self.setWindowTitle("SaPa")
        self.setWindowIcon(QtGui.QIcon('')) #edo vale icon
        self.b = QPlainTextEdit(self)
        self.show()

    def popmessage(self):
        choise = QtGui.QMessageBox.question(self,)#dose minima edo

    def run():
        app = QtGui.QApplication(sys.argv)
        GUI = Window()
        sys.exit(app.exec_())

run()
