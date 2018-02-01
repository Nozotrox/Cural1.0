import sys
from PyQt5.Qt import QApplication
from mainForm import frmMain
from PyQt5.QtWidgets import *

if __name__=="__main__":
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("Fusion"))
    formMain = frmMain()
    formMain.show()
    try:
        app.verbose_crash = True
#TODO: Use the line below only when not debugging
        app.exec_()
    except BaseException as e1:
        sys.exit()
    
    
    
    
