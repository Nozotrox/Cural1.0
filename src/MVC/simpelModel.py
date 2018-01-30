'''
Created on 18/09/2017

@author: chernomirdinmacuvele
'''
from PyQt5.Qt import QSqlTableModel, QDataWidgetMapper,\
    QSqlRecord, QSqlField, Qt
import QT_msg as msg 
class SimpleModel():
    def __init__(self, dbcon=None, tblName=None, dictField=None):
        super(SimpleModel, self).__init__()
        self.tblName = tblName
        self.dicFields = dictField
    
    def setModel(self):
        '''
        Metodo para Configurar o SQLTABLEMODEL, para uma determina tabela na base de dados
        caso se a configuracao seja bem feita e devolvido um true e caso contrario e devolvido um 
        False e a mensagem de erro.
        '''
        bOK = False
        self.model = QSqlTableModel()
        self.model.setTable(self.tblName)
        self.model.sort(0, Qt.AscendingOrder)
        bOK = self.model.select()
        if bOK:
            return bOK
        else:
            msg.error(txt= 'Error Nao Foi possivel Configurar o model', verbTxt=self.model.lastError().text())
            return bOK
    
    
    def setModelInView(self, tblView=None):
        '''
        Metodo para atribuir um Modelo a table View
        '''
        tblView.setModel(self.model)
       
        
    def setMapper(self):
        '''
        Metodo para configuara o mappper, onde iremos atribuir ao mapper um model e widgets para 
        podermos mapper a informacao no modelo,  mudaremos o tipo de submitPocalicy para manual para
        que so se atualize os campos com clickar do um botao atualizar
        '''
        self.mapper = QDataWidgetMapper()
        self.mapper.setModel(self.model)
        for idx, val in enumerate(self.dicFields['fldWidget']):
            self.mapper.addMapping(val, self.model.fieldIndex(self.dicFields['fldName'][idx]))
        self.mapper.setSubmitPolicy(self.mapper.ManualSubmit)
        self.mapper.toFirst()
        
        
    def setTblMapper(self, indexModel=None):
        '''
        Metodo para scronizar o click do TableView com os dados do mapper isto e
        para quando se selecionar um elemento na tabela, ser esse que ira aparecer no 
        widgets mapeados.
        '''
        currentModel = indexModel.model()
        clickedRow = indexModel.row()
        self.mapper.setCurrentModelIndex(indexModel)
        for i in range(len(self.dicFields['fldName'])):
            currentModel.index(clickedRow,i)
    
    
    def addData(self):
        '''
        Metodo para prepara a modelo e mapper para inserir um novo 
        elemento.
        '''
        row = self.model.rowCount()
        bOK = self.model.insertRow(row)
        self.mapper.setCurrentIndex(row)
        if bOK:
            return bOK
        else:
            msg.error(txt= 'Error Nao Foi possivel Configurar o model para a insercao de um novo elemento.', verbTxt=self.model.lastError().text())
            return bOK
    
    
    def insertData(self, lstVal):
        '''
        Metodo para inserir novos dados na base de dados, 
        primeiro configura os tipos de compos depois leva os valores 
        da lista de valores e por fim executa e se a insercao for bem succedida 
        e envida retorna verdade caso contrario retorn falso e menssagem com erro
        '''
        insertRecord = QSqlRecord()
        for idx, val in enumerate(self.dicFields['fldName']):
            insertRecord.append(QSqlField(val,self.dicFields['fldType'][idx]))
        for indx, val in enumerate(lstVal):
            insertRecord.setValue(indx, val)
        bOK= self.model.insertRowIntoTable(insertRecord)   
        if bOK:
            msg.inserted()
            self.model.select()
            return bOK
        else:
            msg.error(txt= 'Error Nao Foi possivel Inserir o novo elemento.', verbTxt=self.model.lastError().text())
            return bOK
    
    
    def saveChange(self):
        '''
        Metodo para Atulizar os dados editados, caso or bem succedida 
        e envida retorna verdade caso contrario retorn falso e menssagem com erro
        '''
        bOK = self.mapper.submit()
        if bOK:
            msg.updated(txt='Dados Atulizados Com sucessos')
            self.model.select()
            return bOK
        else:
            msg.error(txt= 'Error Nao Foi possivel Atualizar o elemento .', verbTxt=self.model.lastError().text())
            return bOK