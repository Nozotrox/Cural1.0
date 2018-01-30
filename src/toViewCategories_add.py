from GeneratedFiles import ViewCategories_add
from PyQt5.QtWidgets import *
import simpelModel
import srcPlus as src
import con_
import FuncSQL as sql
import sys

class toViewCategories_add(QDialog, ViewCategories_add.Ui_addGeralDialog):
    
    def __init__(self, parent = None):
        super(toViewCategories_add, self).__init__(parent)
        
        self.setupUi(self)
        self.list_of_widgets = [self.idLineEdit, self.idCategoriaLineEdit, self.sexoComboBox, self.totalLineEdit, self.dataNascimentoDateTime]
        self.setDB()
        self.setButtonConnection()
        
        
    def setDB(self):
        self.dbConnection = con_.con_1()
        
    def setButtonConnection(self):
        self.submeterPushButton.clicked.connect(self.submit)
        self.limparPushButton.clicked.connect(self.clearData)
        self.cancelarPushButton.clicked.connect(self.reject)
        
    def submit(self):
        table_name = 'tbl_gado'
        lstNames = ['id', 'id_categoria', 'sexo', 'total', 'data_nascimento']      
        lstVal = []
        
        for widg in self.list_of_widgets:
            lstVal.append(src.getText(widg = widg))
        
        lstVal[4] = "'" + self.formatDate(lstVal[4]) + "'"
        lstQuote = [False,False, True, False, False]
        sql.insertVal(tblName = table_name, lstNames = lstNames, lstVal = lstVal, lstQuot = lstQuote)
        
    def clearData(self):
        for widgt in self.list_of_widgets:
            src.setTxtToWidget(widget = widgt, val = '')

    
    def formatDate(self, data):
        portions = data.split(" ")
        date = portions[0].split("-")
        
        ''' Getting separate values '''
        day = date[2]
        month = date[1]
        year = date[0]
        sqlFormat = month + '-' + day + '-' + year
        
        portions[0] = sqlFormat
        return " ".join(portions)
    
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("Fusion"))
    form = toViewCategories_add()
    form.exec_()
