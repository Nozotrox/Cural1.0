import addToGeral
from PyQt5.QtWidgets import *
import con_
import srcPlus as src
import FuncSQL as sql
import sys
from GenericIntroducoes import GenericIntroducao
from toEditNovo import toEditNovo


class toIntroducaoGeral(addToGeral.Ui_addGeral, GenericIntroducao):
    def __init__(self, parent = None):
        super(toIntroducaoGeral, self).__init__(parent)
        
        self.setupUi(self)
        self.listOfWidgetsAcontecimento = [self.dataAcontecimentoDateTime, self.acontecimentoComboBox, self.descricaoTextEdit]
        self.listOfWidgetsGado = [self.categoriaComboBox, self.sexoComboBox, self.dataNascimentoDateTime, self.totalSpinBox]
        self.setDB()
        self.setBtnConnections()
        
        
    def setDB(self):
        self.dbConnection = con_.con_1()
    
    def setBtnConnections(self):
        self.nascidoCheckBox.clicked.connect(self.checkTrue)
        self.acontecimentoCheckBox.clicked.connect(self.checkTrue)
        self.adicionarPushButton.clicked.connect(self.submit)
        self.categoriaComboBox.currentIndexChanged.connect(self.indexChanged)
        self.sexoComboBox.currentIndexChanged.connect(self.indexChanged)
        self.limparPushButton.clicked.connect(self.clear)
        self.cancelarPushButton.clicked.connect(self.reject)
        
    def clear(self):
        for widgt in self.listOfWidgetsAcontecimento:
            src.setTxtToWidget(widget = widgt, val = '')
        
        for widg in self.listOfWidgetsGado:
            src.setTxtToWidget(widget = widg, val = '')
        
    def indexChanged(self):
        sender = self.sender()
        sender.setCurrentIndex(sender.currentIndex())
        sender.setCurrentText(sender.currentText())
        
    def checkTrue(self):
        sender = self.sender().objectName()
        if sender == "nascidoCheckBox":
            state = self.nascidoCheckBox.isChecked()
            self.dataNascimentoDateTime.setEnabled(state)
        
        elif sender == "acontecimentoCheckBox":
            state = self.acontecimentoCheckBox.isChecked()
            self.acontecimentoGroupBox.setEnabled(state)
    
    def submit(self):
        
        self.listOfWidgetsAcontecimento = [self.dataAcontecimentoDateTime, self.acontecimentoComboBox, self.descricaoTextEdit]
        self.listOfWidgetsGado = [self.categoriaComboBox, self.sexoComboBox, self.dataNascimentoDateTime, self.totalSpinBox]
        
        table_name = 'tbl_gado'
        list_of_names = ['id_categoria', 'sexo', 'data_nascimento', 'total']
        list_of_values = []
        list_of_quotes = [False, True, True, False]
        
        
        for widget in self.listOfWidgetsGado:
            if not widget.isEnabled():
                list_of_values.append('Null')
                list_of_quotes[2] = False
                continue
    
            if isinstance(widget, QComboBox):
                
                if widget.objectName() == 'sexoComboBox':
                    value = widget.currentText()
                else:
                    value = str(widget.currentIndex() + 1)
            else:
                
                if widget.objectName() == "dataNascimentoDateTime":
                    value = self.formatDate(src.getText(widget))
                else:
                    value = src.getText(widget)
            list_of_values.append(value)
        
        sql.insertVal(tblName = table_name,lstNames = list_of_names, lstVal = list_of_values, lstQuot = list_of_quotes)
        
        if self.acontecimentoCheckBox.isEnabled():
            _,last_id_gado = sql.getLast(tblName='tbl_gado')
            
            table_name = 'tbl_log'
            list_of_names = ['id_acontecimento', 'id_gado', 'data_acontecimento', 'descricao']
            list_of_values = [
                str(self.acontecimentoComboBox.currentIndex() + 1),
                str(last_id_gado),
                self.formatDate(src.getText(widg = self.dataAcontecimentoDateTime)),
                src.getText(widg  = self.descricaoTextEdit)
                            ]
            list_of_quotes = [False, False, True, True]
            sql.insertVal(tblName = table_name,lstNames = list_of_names, lstVal = list_of_values, lstQuot = list_of_quotes)
        self.accept()
                
    
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
    
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     form = toEditNovo()
#     form.exec_()
#         