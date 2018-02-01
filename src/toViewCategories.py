import ViewCategories
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *
from PyQt5.Qt import Qt
import con_
import simpelModel
import mixedModel
from QT_tblViewUtility import getClickedLstVal
#::> Testing import
import sys
from mixedModel import withWidgets
import FuncSQL as sql
import srcPlus as src
from simpelModel import SimpleModel



class toViewCategories(QDialog,ViewCategories.Ui_EditGeralDialog):
    
    def __init__(self, parent = None):
        super(toViewCategories, self).__init__(parent)
        self.setupUi(self)
        self.setDB()
        self.selectionFunctionality()
        self.setModelToComboBoxes()
#         self.nomeLineEdit.setDisabled(True)

        self.list_of_widgtes_to_toggle = [self.acontecimentoComboBox, self.acontecimentoDateTime, self.descricaoPlainTextEdit]
        
    
    def setDB(self):
        self.database_connection = con_.con_1()    
        table_name = "tbl_gado"
        filtro = None
        lstVal2Real = [None,['id ', 'nome']]
        lstRelTblName = [None,'tbl_categorias']
        
        
        """ Setting up Models """
        """ This is the model for the table that will be displayed:: tbl_gado """
        _, self.model = mixedModel.setViewModel(tblName= table_name, filtro=None, lstVal2Rel = lstVal2Real, lstRelTblName=lstRelTblName)
        self.tableView.setModel(self.model)
        self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        
        """THis is the model for the table that won't be displayed but it will be necessary for mapping the widgets """
        self.second_model = SimpleModel(self.database_connection, tblName='tbl_log')
        self.second_model.setModel()
        self.second_model.model.sort(2, Qt.AscendingOrder)
        '''Need to sort the tableView according to the id_gado so the values from the first model can correspond to the values of the second model'''
        
        self.index_gado_in_log = []
        for x in range(int(self.second_model.model.rowCount())):
            self.index_gado_in_log.append(self.second_model.model.record(x).value(2))
        self.index_gado_in_log.sort()
        
        
    def selectionFunctionality(self):
        self.tableView.clicked.connect(self.showData)
        
        """::>> Setting up the mapping """
        """::>> These are the first widgets to map """
        self.sync_with_widgets = mixedModel.withWidgets()
        self.list_of_widgets = [None, None, None, self.dataDateTimeEdit, self.totalLineEdit]
        self.sync_with_widgets.setMapper(self.model, self.list_of_widgets)
        
        """::>> Setting up button connections """
        self.submeterPushButton.clicked.connect(self.submit)
        self.cancelarPushButton.clicked.connect(self.reject)
    
    def setModelToComboBoxes(self):
        list_of_comboBoxes = [self.categoriaComboBox, self.acontecimentoComboBox]
        table_names = ['tbl_categorias', 'tbl_acontecimento']
        list_of_names = ['nome', 'nome']
        
        for index in range(len(list_of_comboBoxes)):
            mixedModel.setModel4CombBox(tblName = table_names[index], lstNames = list_of_names[index], widg = list_of_comboBoxes[index], namePos = 0)
        
        
    def showData(self):
        self.sync_with_widgets.sychClickWithMap(self.tableView.currentIndex())
        row = self.tableView.currentIndex().row()
        index = 2
        self.sexoComboBox.setCurrentText(self.tableView.currentIndex().model().record(row).value(index))
        self.currentItemId = self.tableView.currentIndex().model().record(row).value(0)
        
        if self.currentItemId in self.index_gado_in_log:
            correspondingRow = self.index_gado_in_log.index(self.currentItemId)
            value = self.second_model.model.record(correspondingRow).value(1)
            
            """ Update the comboBox """
            self.acontecimentoComboBox.setCurrentIndex(value - 1)
            
            value = self.second_model.model.record(correspondingRow).value(4)
            """ Update the descricao PlainTextEdit """
            self.descricaoPlainTextEdit.setPlainText(value)
            
            value = self.second_model.model.record(correspondingRow).value(3)
            """ Update the data_acontecimento DateTimeEdit"""
            src.setTxtToWidget(widget = self.acontecimentoDateTime, val = value)
        
        if self.currentItemId in self.index_gado_in_log:
            for widget in self.list_of_widgtes_to_toggle:
                widget.setEnabled(True)
        
        else:
            for widget in self.list_of_widgtes_to_toggle:
                widget.setEnabled(False)


    def submit(self):
        """::>> Submit for fields of tbl_gado"""
        table_name = 'tbl_gado'
        lstNames = ['id_categoria', 'sexo', 'data_nascimento','total']
        lstVal = [self.categoriaComboBox.currentIndex() + 1,
                  self.sexoComboBox.currentText(),
                  src.getText(self.dataDateTimeEdit),
                  src.getText(self.totalLineEdit)]
        lstQuote = [False,True, True, False]
        cond = 'id'
          
        condVal = self.currentItemId
        sql.updateVal(tblName = table_name, lstNames = lstNames, lstVals = lstVal, lstQuot = lstQuote, cond = cond, conVal = condVal)
        
        
        """::>> Submit for fields of tbl_log"""
        if self.currentItemId in self.index_gado_in_log:
            table_name = 'tbl_log'
            lstNames = ['id_acontecimento','id_gado','data_acontecimento','descricao']
            lstVal = [self.acontecimentoComboBox.currentIndex() + 1,
                      self.currentItemId,
                      src.getText(self.dataDateTimeEdit),
                      src.getText(self.descricaoPlainTextEdit)]
            
            lstQuote = [False, False, True, True]
            cond = 'id_gado'
            condVal = self.currentItemId
            
            sql.updateVal(tblName = table_name, lstNames = lstNames, lstVals = lstVal, lstQuot = lstVal, cond = cond, conVal = condVal)

            
        
# if __name__ == "__main__":     
#     app = QApplication(sys.argv)
#     formMain = toViewCategories()
#     app.setStyle(QStyleFactory.create("Fusion"))
#     formMain.exec_()