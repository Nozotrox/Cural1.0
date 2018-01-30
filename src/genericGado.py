'''
Created on 31/12/2017

@author: chernomirdinmacuvele
'''
from PyQt5.Qt import QDialog, QStandardItemModel, QStandardItem, QComboBox
import mixedModel
import QT_tblViewUtility
import FuncSQL

class scriptGado(QDialog):
    
    def setTheView(self):   
        quer = self.dictFields['quer']
        toHide = self.dictFields['fldToHide']
        toSize = self.dictFields['sizeCol']
        modelOut = mixedModel.setQueryModel(query=quer)
        
        QT_tblViewUtility.setModelInView(tblView= self.TV, ViewModel= modelOut, toHide= toHide)
        QT_tblViewUtility.setViewCustom(tblView= self.TV, lstSizeCol= toSize)
       
       
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
        
    
    def clickedField(self, mdx):
        lstOut = QT_tblViewUtility.getClickedLstVal(indexModel= mdx)
        self.clickedVal= lstOut
    