v='''
Created on 30/12/2017

@author: chernomirdinmacuvele
'''

"""
    ::>> Este modulo serve para abrir connecoes a bases de dados, nomeadamente
        -DBCural
        -DBCural_2
    
    ::>> Esta connecao e feita usando-se o QSqldDatabase e o driver QPSQL para que
    melhor funcione ao usar base de dados do PostgresSQL.

"""
from PyQt5.QtSql import QSqlDatabase

""" 
:: temp >> I don't see the necessity on the following two lines. Need explanation.

"""
_db_1 = QSqlDatabase.addDatabase("QPSQL")
_db_2 = QSqlDatabase.addDatabase("QPSQL")


"""
::>> Funcao que estabelece connecao com a base de dados DBCural
"""
def con_1():
    _db_1 = QSqlDatabase.addDatabase("QPSQL")
    _db_1.setDatabaseName("Cural1.0")
    _db_1.setUserName("postgres")
    _db_1.setPassword("postgres")
    _db_1.setPort(5432)
    _db_1.setHostName("localhost")
    _db_1.open()
    if _db_1.open():
        return _db_1     
    else:
        return False

"""
::>> Funcao que fecha a conecao com a base de dados DBCural de modo a liertar qualquer tipo de recursos adquiridos.
"""
def close_con():
    if _db_1.open():
        """" ::>> Acho que e suposto terminar a conexao com a base de dados neste bloco """
        _db_1.close()
        return print("Closed")     
    else:
        return False
    
"""
::>> Funcao que estabelece connecao com a base de dados DBCural_2
"""   
def con_2():
    _db_2 = QSqlDatabase.addDatabase("QPSQL")
    _db_2.setDatabaseName("Cural2.0")
    _db_2.setUserName("postgres")
    _db_2.setPassword("postgres")
    _db_2.setPort(5432)
    _db_2.setHostName("localhost")
    if _db_2.open():
        return _db_2     
    else:
        return False
    
def con_3():
    _db_2 = QSqlDatabase.addDatabase("QPSQL")
    _db_2.setDatabaseName("Cural3.0")
    _db_2.setUserName("postgres")
    _db_2.setPassword("postgres")
    _db_2.setPort(5432)
    _db_2.setHostName("localhost")
    if _db_2.open():
        return _db_2     
    else:
        return False


"""
::>> Funcao que fecha a conecao com a base de dados DBCural_2 de modo a liertar qualquer tipo de recursos adquiridos.
"""
def close_con_2():
    if _db_2.open():
        """" ::>> Acho que e suposto terminar a conexao com a base de dados neste bloco"""
        _db_2.close()
        return print("Closed")     
    else:
        return False
    