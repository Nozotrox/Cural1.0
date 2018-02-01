import addToMortos
from PyQt5.QtWidgets import *
import con_
import srcPlus as src
import FuncSQL as sql
import sys
import mixedModel


class toAddMortos(QDialog, addToMortos.Ui_addToMortos):
    def __init__(self, parent = None):
        super(toAddMortos, self).__init__(parent)
        self.setupUi(self)
        self.setDB()
        self.setBtnConnections()
        self.setModelToWidget()
        self.listOfWidgets = [
            self.idMortosComboBox,
            self.dataMorteDateTimeEdit,
            self.descricaoPlainTextEdit
            ]
        
    def setDB(self):
        self.dbConnection = con_.con_1()
        
    def setModelToWidget(self):
        """ Setting a model to the id_gado widget """
        mixedModel.setModel4CombBox(tblName = 'tbl_gado', lstNames = 'id', widg = self.idMortosComboBox, namePos=0)
        
    def setBtnConnections(self):
        self.adicionarPushButton.clicked.connect(self.submit)
        self.cancelarPushButton.clicked.connect(self.reject)
        self.limparPushButton.clicked.connect(self.clear)
        self.cancelarPushButton.clicked.connect(self.reject)
            
            
    def submit(self):
        table_name = 'tbl_log'
        list_of_names = ['id_acontecimento', 'id_gado',  'data_acontecimento', 'descricao']
        list_of_values = [
            '1',
            str(self.idMortosComboBox.currentText()),
            self.formatDate(src.getText(self.dataMorteDateTimeEdit)),
            src.getText(self.descricaoPlainTextEdit)
            ]
        list_of_quotes = [False, False, True, True]
        sql.insertVal(tblName = table_name, lstNames = list_of_names, lstVal = list_of_values, lstQuot = list_of_quotes)
            
        
    def clear(self):
        for widgt in self.listOfWidgets:
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
        
        
# 
# if __name__=="__main__":
#     app = QApplication(sys.argv)
#     app.setStyle(QStyleFactory.create("fusion"))
#     form = toAddMortos()
#     form.exec_()