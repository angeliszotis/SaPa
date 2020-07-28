from PyQt5.QtWidgets import *
import sys
import gui
import guiMain

def main():
    App = QApplication(sys.argv)
    p1 = gui.Window() 
    sys.exit(App.exec_())
if __name__ == "__main__":
    main()
