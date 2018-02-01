import editToMortos
from PyQt5.QtWidgets import *
import mixedModel as mx
import srcPlus as src
import con_
import FuncSQL as sql
import sys

class toEditMortos(QDialog, editToMortos.Ui_Editar_Mortos):
    
    def __init__(self, parent = None):
        super(toEditMortos, self).__init__(parent)
        
        self.setupUi(self)
        self.setDB()
        self.selectionFunctionality()
        self.setButtonConnection()
        
        
    def setDB(self):
        self.dbConnection = con_.con_1()
        query = '''select id_gado, data_acontecimento, descricao
                    from tbl_log
                    where
                    id_acontecimento = 1; 
        '''
        list_of_newNames = ['ID Gado', 'Data da Morte', 'Descricao']
        
        self.model = mx.setQueryModel(query = query, lstNewNames = list_of_newNames )
        self.tableView.setModel(self.model)
        self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        
        mx.setModel4CombBox(tblName = 'tbl_log', lstNames = 'id_gado', widg = self.idComboBox, namePos=0)
        
    def setButtonConnection(self):
        """::>> Setting up button connections """
        self.submeterPushButton.clicked.connect(self.submit)
        self.cancelarPushButton.clicked.connect(self.reject)
    
    def selectionFunctionality(self):
        self.tableView.clicked.connect(self.showData)
        
        """::>> Setting up the mapping """
        """::>> These are the first widgets to map """
        self.sync_with_widgets = mx.withWidgets()
        self.list_of_widgets = [None, self.dataAcontecimentoDateTime , self.descricaoPlainTextEdit]
        self.sync_with_widgets.setMapper(self.model, self.list_of_widgets)
        
    def showData(self):
        self.sync_with_widgets.sychClickWithMap(self.tableView.currentIndex())
        row = self.tableView.currentIndex().row()
        
        """ Updating ID comboBox """
        value = self.model.record(row).value(0)
        index = self.idComboBox.findText(str(value))
        self.idComboBox.setCurrentIndex(index)
        
        """ Current Item ID """
        self.currentItemId = self.model.record(row).value(0)
        
    def submit(self):
        """::>> Submit for fields of tbl_gado"""
        table_name = 'tbl_log'
        lstNames = ['id_gado', 'data_acontecimento','descricao']
        lstVal = [self.idComboBox.currentText(),
                  src.getText(self.dataAcontecimentoDateTime),
                  src.getText(self.descricaoPlainTextEdit)]
        lstQuote = [False,True, True]
        cond = 'id_gado'
          
        condVal = self.idComboBox.currentText()
        sql.updateVal(tblName = table_name, lstNames = lstNames, lstVals = lstVal, lstQuot = lstQuote, cond = cond, conVal = condVal)
        
        
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
    
# if __name__ == "__main__":
#      
#     app = QApplication(sys.argv)
#     app.setStyle(QStyleFactory.create("Fusion"))
#     form = toEditMortos()
#     form.exec_()
