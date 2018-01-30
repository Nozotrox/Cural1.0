from main import Ui_MainWindow
from PyQt5.Qt import QMainWindow
import con_
from toViewData import toViewData

class frmMain(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None, dbCon=None, user_info = None):
        super(frmMain,self).__init__(parent=parent)
        self.setupUi(self)
        
        self.configDict()
        
        self.actionCural_Mag_1.triggered.connect(self.tableViewToOpen)
        self.actionCural_Mag2.triggered.connect(self.configDict)
        
    def tableViewToOpen(self):
        objName = self.sender().objectName()
        con = self.dictDB.get(objName)
        
        self.toOpen = toViewData(dbCon=con())
        self.toOpen.show()
        
        
    def configDict(self):
        self.dictDB={'actionCural_Mag_1': con_.con_1,
                         'actionCural_Mag2': con_.con_2}
    
