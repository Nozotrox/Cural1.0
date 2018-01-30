'''
Created on 12/09/2017
Modulo de Funcoes para interacao com o TableView
@author: chernomirdinmacuvele
'''
import QT_msg as msg
from PyQt5.Qt import QAbstractItemView, QModelIndex, QWidget


def setModelInView(tblView=None, ViewModel=None, toHide=None):
        ''' Associa um modelo a um table view, opcionalmente esconde colunas no table view
    
        Args:
            tblView = A table view que sera usada
            model= o Modelo que sera usado (modelo da classe ou da tabela)
            toHide = lista de boleanos (com o mesmo numero de elementos que o numero de colunas no model) indicando para cada coluna se deve ser escondida (True)
            '''
        if ViewModel is None:
            msg.error(txt="Erro Nao doi atribuido um modelo a Tabela")
        else:
            tblView.setModel(ViewModel)
            if toHide is not None:
                for idx, val in enumerate (toHide):
                    tblView.setColumnHidden(idx, val)
            
        
def getClicked(indexModel = None, colIdent = 0):#
        ''' Leva o Model index da linha selecionada
            depois, seleciona o model,
            depois a linha selcionada e depois o valor 
            encontrado nessa linha 
            Args:
                indexModel: o indexModel que forncido pelo click
                colIdent = Identificacao da coluna -o nome ou numero da coluna do valor desejado (str ou int)
        
        '''
        curWorkmodel = indexModel.model()
        clickedRow = indexModel.row()
        clickedRowVal = curWorkmodel.record(clickedRow).value(colIdent)
        return (clickedRowVal, clickedRow)


def getClickedLstVal(indexModel = None):#
        ''' Leva o Model index da linha selecionada
            depois, seleciona o model,
            depois a linha selcionada e depois o valor 
            encontrado nessa linha 
            Args:
                indexModel: o indexModel que forncido pelo click
                colIdent = Identificacao da coluna -o nome ou numero da coluna do valor desejado (str ou int)
        
        '''
        lstVal = []
        curWorkmodel = indexModel.model()
        clickedRow = indexModel.row()
        col = curWorkmodel.columnCount()
        for idx in range(col):
            lstVal.append(curWorkmodel.record(clickedRow).value(idx))
        return (lstVal)


def getFristLine(model=None):
    lstOut=[]
    bOK = model.record(0).isEmpty()
    col = model.columnCount()
    if bOK:
        for idx in range(col):
            lstOut.append(model.record(0).value(idx))
    return bOK, lstOut


def setSharedTbl(tblView=None, Viewmodel=None, idxRow=None):
        '''Metodo configura a tabela que sera compartilhada,
        recebendo:
        viewModel = a classe do model
        idxRow = Nº da linha selcionada
        tblView = a tabela compartilhada '''
        if Viewmodel is not None and idxRow  is not  None and tblView  is not  None:
            setModelInView(tblView=tblView, ViewModel=Viewmodel)
            tblView.selectRow(idxRow)
        else:
            msg.error(txt='Error Parametros incompletos')
    

def setViewCustom(tblView = None, lstSizeCol=None):
        '''
        Costumize the form
        *Este modo customiza o view mudando a forma como sao selacionados os elementos e
        O seu comportamento.
        - No editing possible.
        - Selecting only rows.
        - When the user selects an item, any already-selected item becomes unselected. It is possible for the user to deselect the selected item.
        '''
        tblView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        tblView.setSelectionBehavior(QAbstractItemView.SelectRows)
        tblView.setSelectionMode(QAbstractItemView.SingleSelection)
        if lstSizeCol is None:
            tblView.resizeColumnsToContents()
        else:
            for idx, val in enumerate (lstSizeCol):
                tblView.setColumnWidth(idx, int(val))
        tblView.horizontalHeader().setStretchLastSection(True)


def resizeForm(formToResize = None, Wx=None,Hx=None):
    formToResize.setFixedSize(Wx,Hx)
    

