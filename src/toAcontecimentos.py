'''
Created on 18/01/2018

@author: chernomirdinmacuvele
'''
import frmAcontecimentos
from PyQt5.Qt import QDialog, QLineEdit
import mixedModel as mMixed
import FuncSQL as fSql
import srcPlus
from GenericIntroducoes import GenericIntroducao
import QT_msg

class toAcontecimentos(frmAcontecimentos.Ui_Form, GenericIntroducao):
    
    def __init__(self, parent = None):
        super(toAcontecimentos, self).__init__(parent)
        self.setupUi(self)
        
        self.setDict()
        self.configPB()
        
    def addAcontencimentos(self):
        tblName = self.dictField['tbl']
        lstNames = self.dictField['fld']
        
        lstWidget = self.dictField['wdgName']
        lstVal = srcPlus.getTextAll(lstWidg = lstWidget)
        lstQuot = self.dictField['toQuote']
        
        bOK = self.verfEmpty(lstWidget= lstWidget)
        if bOK:      
            _bok, _msg = fSql.insertVal(tblName= tblName, lstNames= lstNames, lstVal= lstVal, lstQuot= lstQuot)
            QT_msg.Sucessos(txt= _msg)
        
        
    def verfEmpty(self, lstWidget):
        bOK = False
        for val in lstWidget:
            bok = self.notNull(wdgt= val)
            if not bok:
                val.setStyleSheet(srcPlus.warningFocus(obj= val))
                QT_msg.aviso(txt= "Porfavor prencha todos Campos!")
                bOK = False
                break
            else:
                val.setStyleSheet(srcPlus.successFocus(obj= val))
                bOK = True
        return bOK
                
        
        
        
    def configPB(self):
        self.PBCancelar.clicked.connect(self.close)
        self.PBGuardar.clicked.connect(self.addAcontencimentos)
        

    def setDict(self):
        self.dictField = {'fld':['id', 'nome'],
                          'toQuote':[True, True],
                          'wdgName':[self.LECod, self.LENome],
                          'tbl':'tbl_acontecimento',
                          }