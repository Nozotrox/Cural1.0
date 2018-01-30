'''
Created on 05/01/2018

@author: chernomirdinmacuvele
'''
from PyQt5.Qt import QDialog, QStandardItemModel, QStandardItem, QComboBox,\
    QLineEdit, QPlainTextEdit
import mixedModel
import QT_tblViewUtility
import FuncSQL
import rscForm

class GenericIntroducao(QDialog):
    
    def notNull(self, wdgt=None):
        bOK=True
        if isinstance(wdgt, QLineEdit):
            if wdgt.text() is '':
                bOK= False
        elif isinstance(wdgt, QPlainTextEdit):
            if wdgt.toPlainText() is '':
                bOK= False
        elif isinstance(wdgt, QComboBox):
            if wdgt.currentText() is '' or wdgt.currentText() is None:
                bOK= False
        return bOK
    

    def toFill(self):
        if self.lstToEdit is not None:
            lstWdt = self.dictFields['lstWidget']
            lstVals = self.lstToEdit
            if len(lstWdt) == len(lstVals):
                for idx, val in enumerate(lstVals):
                    rscForm.setTxtToWidget(widget= lstWdt[idx], val= val)
            
    
    def setCombBox(self):
        lstQuer = self.dictCB['quer']
        lstWdg = self.dictCB['widgets']
        for idx, quer in enumerate(lstQuer):
            model = mixedModel.setQueryModel(query=quer)
            lstWdg[idx].setModel(model)
            lstWdg[idx].setModelColumn(1)
            self.CBTextHint(Combox= lstWdg[idx])
               
               
    def CBTextHint(self, Combox=None):
        mdel = QStandardItemModel(Combox.model())
        firstIndex = mdel.index(0, Combox.modelColumn(), Combox.rootModelIndex())
        firstItem = QStandardItem(mdel.itemFromIndex(firstIndex))
        firstItem.setSelectable(False)