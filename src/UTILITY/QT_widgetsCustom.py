'''
Created on 27/10/2017

@author: chernomirdinmacuvele
'''
from PyQt5 import QtCore
from PyQt5.Qt import QTimer, QLabel

objSpecial =None
msgSpecial =None

def eventFilterForRulesOnFucos(widget, event):
        '''
        Metodo para apanhar o evento de focusOut, nos wdgts
        -LineEdit
        -SpinBox
        -PlainText
        o Metodo apanha o evento depois, executa a regra e se a For true 
        Deixa o widget Vermelho caso contrario ficar branco
        '''
        if event.type() == QtCore.QEvent.FocusOut:
            nome = widget.objectName()
            bOK =True #exeRule(wdgName=nome)#
            if bOK:
                style = errorFocus(obj=widget)
                widget.setFocus()
                widget.setStyleSheet(style)
            else:
                style = successFocus(obj=widget)
                widget.setStyleSheet(style)
            return False
        else:
            return False 
    

def errorFocus(obj= None):
    if obj is not None:
        objName = obj.objectName()
        css= "#"+str(objName)+"""{
                color:red;
                }"""
        obj.setStyleSheet(css)



    
    
        
def successFocus(obj= objSpecial):
    if obj is not None:
        objName = obj.objectName()
        css= "#"+str(objName)+"""{
                color:black;
                }"""
        obj.setStyleSheet(css)
        

def successDatabase(obj= None):
    if obj is not None:
        objName = obj.objectName()
        css= "#"+str(objName)+"""{
                color:green;
                }"""
        obj.setStyleSheet(css)


def warningFocus(obj= None):
    if obj is not None:
        objName = obj.objectName()
        css= "#"+str(objName)+"""{
                color:orange;
                }"""
        obj.setStyleSheet(css)


    
