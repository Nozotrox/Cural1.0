'''
Created on 03/11/2017

@author: chernomirdinmacuvele
'''      
from PyQt5.Qt import QComboBox, Qt,QSortFilterProxyModel, QCompleter, QStandardItemModel, QStandardItem,\
    QAbstractItemView, QAbstractItemModel, QApplication, QDialog, QWidget,\
    QVBoxLayout, QStyledItemDelegate, QStyleOptionViewItem, QPainter,\
    QModelIndex, QStyle
import sys

class MyComboBox(QComboBox):
    '''
    MyComboBox E um Combo Box com 
    - Completer sem permetir a insersao de dados do usuario
    -
    '''
    def __init__(self, parent=None):
        super(MyComboBox, self).__init__(parent)
          
        self.setFocusPolicy(Qt.StrongFocus)
        self.setEditable(True)
  
        #add a filter model to filter matching items
        self.pFilterModel = QSortFilterProxyModel(self)
        #To be Case sensetive
        self.pFilterModel.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.pFilterModel.setSourceModel(self.model())
          
        #add a cpmpleter, withc uses the filter model
        self.completer = QCompleter(self.pFilterModel, self)
        # always show all (filtered) completions
        self.completer.setCompletionMode(QCompleter.UnfilteredPopupCompletion)
        self.setCompleter(self.completer)
          
        #connect Signals
        self.lineEdit().textEdited[str].connect(self.pFilterModel.setFilterFixedString)
        self.completer.activated.connect(self.on_completer_activated)
          
    #on selection of an item form the completer, selct the correspondig item form combox
    def on_completer_activated(self, text):
        if text:
            index = self.findText(text)
            self.setCurrentIndex(index)
                  
    # on model change, uodate the modes of the filter and completer as well
    def setModel(self, model):
        super(MyComboBox, self).setModel(model)
        self.pFilterModel.setSourceModel(model)
        self.completer.setModel(self.pFilterModel)
              
    #on model column change, updade the mode column of hte filter and completer as well  
    def setModelColumn(self, column):
        self.completer.setCompletionColumn(column)
        self.pFilterModel.setFilterKeyColumn(column)
        super(MyComboBox, self).setModelColumn(column)
  
    def getText(self):
        return self.currentText()


class subClassStyleItem(QStyledItemDelegate):
    def __init__(self):
        super(subClassStyleItem, self).__init__()
        
        
    def paint(self, QPainter, QStyleOptionViewItem, QModelIndex):
        painter = QPainter
        option = QStyleOptionViewItem
        index = QModelIndex
        refToNonConstOpion = option
        refToNonConstOpion.showDecorationSelected =False
        #refToNonConstOpion.state = QStyle.State_HasFocus | QStyle.State_MouseOver #Only For Windows
        QStyledItemDelegate.paint(self,painter, refToNonConstOpion, index)
        
    
def modelWithCheck_search(lstResult=None):
    if lstResult is not None:
        model = QStandardItemModel()
        for idx, val in enumerate (lstResult):
            item = QStandardItem(val[0])
            item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
            item.setData(Qt.Unchecked, Qt.CheckStateRole)
            model.setItem(idx, 0, item)
        
    return model








