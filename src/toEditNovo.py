import editToNovos
from PyQt5.QtWidgets import *
import mixedModel as mx
import srcPlus as src
import con_
import FuncSQL as sql
import sys

class toEditNovo(QDialog, editToNovos.Ui_Editar_Novos):
    
    def __init__(self, parent = None):
        super(toEditNovo, self).__init__(parent)
        
        self.setupUi(self)
        self.setDB()
        self.selectionFunctionality()
        self.setButtonConnection()
        
        
    def setDB(self):
        self.dbConnection = con_.con_1()
        table_name = 'tbl_gado'
        list_of_values_tRelate = [None, ['id', 'nome']]
        list_of_tableNames = [None, 'tbl_categorias']
        list_of_new_names = ['id', 'Categoria', 'sexo', 'Data de Nascimento' ,'Total']
        
        _,self.model = mx.setViewModel(tblName = table_name, lstVal2Rel = list_of_values_tRelate, lstRelTblName = list_of_tableNames, lstNewNames= list_of_new_names)
        self.tableView.setModel(self.model)
        self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        
    def setButtonConnection(self):
        """::>> Setting up button connections """
        self.submeterPushButton.clicked.connect(self.submit)
        self.cancelarPushButton.clicked.connect(self.reject)
    
    def selectionFunctionality(self):
        self.tableView.clicked.connect(self.showData)
        
        """::>> Setting up the mapping """
        """::>> These are the first widgets to map """
        self.sync_with_widgets = mx.withWidgets()
        self.list_of_widgets = [None, None,None, self.dataNascimentoDateTimeEdit, self.totalLineEdit]
        self.sync_with_widgets.setMapper(self.model, self.list_of_widgets)
        
    def showData(self):
        self.sync_with_widgets.sychClickWithMap(self.tableView.currentIndex())
        row = self.tableView.currentIndex().row()
        
        """ Update the sexo comboBox """
        value = self.model.record(row).value(2)
        self.sexoComboBox.setCurrentText(value)
        
        """ Updating the categoria comboBox """
        value = self.model.record(row).value(1)
        self.categoriaComboBox.setCurrentText(value)
        
        """ Current Item ID """
        self.currentItemId = self.model.record(row).value(0)
        
    def submit(self):
        """::>> Submit for fields of tbl_gado"""
        table_name = 'tbl_gado'
        lstNames = ['id_categoria', 'sexo', 'data_nascimento','total']
        lstVal = [self.categoriaComboBox.currentIndex() + 1,
                  self.sexoComboBox.currentText(),
                  src.getText(self.dataNascimentoDateTimeEdit),
                  src.getText(self.totalLineEdit)]
        lstQuote = [False,True, True, False]
        cond = 'id'
          
        condVal = self.currentItemId
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
#     form = toEditNovo()
#     form.exec_()
