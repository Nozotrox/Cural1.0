from GeneratedFiles import addToNovo
from PyQt5.QtWidgets import *
import con_
import srcPlus as src
import FuncSQL as sql
import sys


class toAddNovo(QDialog, addToNovo.Ui_addToNovo):
    def __init__(self, parent = None):
        super(toAddNovo, self).__init__(parent)
        self.setupUi(self)
        self.setDB()
        self.setBtnConnections()
        
        self.listOfWidgets = [
            self.categoriaComboBox,
            self.sexoComboBox,
            self.totalComboBox,
            self.dataNascimentoDateTimeEdit,
            self.dataCompraDateTimeEdit
            ]
        
    def setDB(self):
        self.dbConnection = con_.con_1()
    
    def setBtnConnections(self):
        self.adicionarPushButton.clicked.connect(self.submit)
        self.cancelarPushButton.clicked.connect(self.reject)
        self.limparPushButton.clicked.connect(self.clear)
        self.compradoCheckBox.clicked.connect(self.checkTrue)
        self.producaoInternaCheckBox.clicked.connect(self.checkTrue)
        self.limparPushButton.clicked.connect(self.clear)
        self.cancelarPushButton.clicked.connect(self.reject)
        
    def indexChanged(self):
        sender = self.sender()
        sender.setCurrentIndex(sender.currentIndex())
        sender.setCurrentText(sender.currentText())
        
    def checkTrue(self):
        sender = self.sender().objectName()
        if sender == "compradoCheckBox":
            state = self.compradoCheckBox.isChecked()
            self.dataCompraDateTimeEdit.setEnabled(state)
            
            state = not state
            self.producaoInternaCheckBox.setChecked(state)
            self.dataNascimentoDateTimeEdit.setEnabled(state)
        
        elif sender == "producaoInternaCheckBox":
            state = self.producaoInternaCheckBox.isChecked()
            self.dataNascimentoDateTimeEdit.setEnabled(state)
            
            state = not state
            self.compradoCheckBox.setChecked(state)
            self.dataCompraDateTimeEdit.setEnabled(state)
            
            
            
    
    def submit(self):
        table_name = 'tbl_gado'
        list_of_names = ['id_categoria', 'sexo',  'total', 'data_nascimento']
        list_of_values = []
        list_of_quotes = [False, False, False, True]
        
        for widgt in self.listOfWidgets:
            if not widgt.isEnabled():
                continue
            
            if isinstance(widgt, QComboBox):
                value = str(widgt.currentIndex() + 1)
            
            elif isinstance(widgt, QDateTimeEdit):
                value = self.formatDate(src.getText(widg = widgt))
                
            else:
                value = str(src.getText(widg = widgt))
            
            list_of_values.append(value)
            
        if self.producaoInternaCheckBox.isChecked():
            sql.insertVal(tblName = table_name, lstNames = list_of_names, lstVal = list_of_values, lstQuot = list_of_quotes)
            return
        
        elif self.compradoCheckBox.isChecked():
            """ Adicionar primeiro a tabela_gado"""
            list_of_names.pop()
            list_of_values.pop()
            sql.insertVal(tblName = table_name, lstNames = list_of_names, lstVal = list_of_values, lstQuot = list_of_quotes)
            
            
            table_name = 'tbl_log'
            list_of_names = ['id_acontecimento', 'id_gado', 'data_acontecimento']
            list_of_quotes = [False, False, True]
            _,last_id_gado = sql.getLast('tbl_gado')
            
            list_of_values = [
                '6',
                str(last_id_gado),
                self.formatDate(src.getText(widg=self.dataCompraDateTimeEdit))              
                ]
            
            list_of_quotes = [False, False, True]
            sql.insertVal(tblName = table_name, lstNames = list_of_names, lstVal = list_of_values, lstQuot = list_of_quotes)
        self.accept()
        
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
        
        
 
if __name__=="__main__":
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("fusion"))
    form = toAddNovo()
    form.exec_()