#-*- coding: utf-8 -*-
"""Module Resource for Form Items.

This module, holds resources for many many things , that helps get information 
from lists, dictionarys, and more.
The propTypes contains most of widgets used in projects to manage data, 

Example:
    #Write Here
    #::
        $ python rscForm.py
        
Attributes:
    #Write Here the attributes
    
Todo:
    *Write here
"""
from PyQt5.Qt import QPushButton, QTabWidget,\
    QLineEdit, QPlainTextEdit, QComboBox, QCheckBox, QDoubleSpinBox, QSpinBox,\
    QDateEdit, QTimeEdit, QGroupBox, QDateTimeEdit
import QT_msg
import PyQt5
from datetime import datetime
from PyQt5.QtCore import QDateTime, QTime
from psycopg2.sql import NULL

propTypes = { "<class 'PyQt5.QtWidgets.QLineEdit'>": ("text", True),
              "<class 'PyQt5.QtWidgets.QPlainTextEdit'>": ("plainText", True),
              "<class 'PyQt5.QtWidgets.QTextEdit'>": ("plainText", True),
              "<class 'PyQt5.QtWidgets.QCheckBox'>": ("checked", False),
              "<class 'PyQt5.QtWidgets.QRadioButton'>": ("checked", False),
              "<class 'PyQt5.QtWidgets.QComboBox'>": ("currentText", False),
              "<class 'CustomWidgets.MyComboBox'>": ("currentText", False),
              "<class 'PyQt5.QtWidgets.QDateTimeEdit'>": ("text", True),
              "<class 'PyQt5.QtWidgets.QSpinBox'>": ("text", True),
              "<class 'PyQt5.QtWidgets.QDoubleSpinBox'>": ("text", True),
              "<class 'PyQt5.QtWidgets.QTimeEdit'>": ("text", True),
              "<class 'PyQt5.QtWidgets.QDateEdit'>": ("text", True),
              "<class 'PyQt5.QtWidgets.QPushButton'>": (None, False),
              "<class 'PyQt5.QtWidgets.QGroupBox'>": ("checked", False),
              "<class 'PyQt5.QtWidgets.QTabWidget'>":("objectName", False) 
            }



"""This class will help manage data from widgets, and manage the widgets"""

def setReadOnly(state = False, widg = None):
    """Sets the widget to read only by change the method readonly or Disable 
    for widgets that dont have readOnly property.
    it check the type of widget we pass than is on the Dict, it will
    see if it has the readOnly property or it will set it do Disabled.
    
    Args:
        state (boo): The state the form is (true -active, false -desactive)
        widg (QWidget): The widget we want to manipulate 
    
    Attributes:
        strType = Holds the type of widget we pass
    """
    try:
        widg.setReadOnly(state)
    except AttributeError:
        widg.setDisabled(state)
    
        
def getText(widg=None):
    """Gets the text on a given widget, it verifies the type of widget 
    the it takes the text that the widget is holding, by passing the rigth 
    property to return the information holded
    
    Args:
        widg (QWidget): The widget we want to manipulate 
    
    Attributes:
        strType = Holds the type of widget we pass
        text = the property given by the dict
        txt = the text returned or that the widget holds
    """
    txt=None
    if isinstance(widg, QDateEdit):
        txt= getData(wdgIN=widg)
    elif isinstance(widg, QDateTimeEdit):
        if widg.text() == widg.specialValueText():
            txt = NULL.string
        else:
            if isinstance(widg, QTimeEdit):
                txt = widg.dateTime().time().toPyTime().isoformat() #+ config.dictSession['tz'] 
            else:
                txt = widg.dateTime().toPyDateTime().isoformat().replace('T', ' ') #+ config.dictSession['tz']   
    elif isinstance(widg, QSpinBox) or isinstance(widg, QDoubleSpinBox):
        if widg.text() == widg.specialValueText():
            txt = NULL.string
        else:
            txtOut =removeSuffix(val=widg)
            if isinstance(widg, QSpinBox):
                txt = int(txtOut)
            else:
                txtOut = _com2dot(txtOut)
                txt= float(txtOut)
            txt = str(txt)
    else: 
        try:
            strType = str(type(widg))
            text,_ = propTypes[strType]    
            txt = str(widg.property(text))
        except KeyError:
            QT_msg.error(txt="Error Widget ainda nao Foi Definido no Dicionario", verbTxt=str(KeyError))
    return txt

def removeSuffix(val):
    ''' Metodo para remover o sufix de Spinboxes'''
    if val.suffix() != '':
        su = val.suffix()
        valSu= val.text()
        valOut = valSu.replace(su, '')
    else:
        valOut= val.text()
    return valOut
    
    

def _com2dot(inTxt):
    '''Converter Todos numereos Reais com "," para "." '''
    outTxt = inTxt.replace(',','.')
    return outTxt
       
       
def setReadOnlyAll(state = False, lstWidg = None):
    """Reimpletation of the _setReadOnly but this time for a collection of given 
    data in a list
    """
    for x in lstWidg:
        setReadOnly(state = state, widg = x) 


def getTextAll(lstWidg = None):
    """Reimpletation of the _getText but this time for a collection of given 
    data in a list
    
    but this returns a List of elements 
    """
    txtLst=[]
    for x in lstWidg:
        if x is None:
            txtLst.append(x)
        else:
            outTxt = getText(x)
            txtLst.append(outTxt)
    return txtLst


def setDataFormat(lstWidg=None):
    if isinstance(lstWidg, list):
        for x in lstWidg:
            x.setDisplayFormat("dd/MM/yyyy")
    else:
        lstWidg.setDisplayFormat("dd/MM/yyyy")
        
        
def setButtonCheckable(lstBT, state=True):
    if isinstance(lstBT, list):
        for x in lstBT:
            x.setCheckable(state)
    else:
        lstBT.setCheckable(state)
            

def getObjeName(widg=None):
    if widg is not None:
        if isinstance(widg, QTabWidget):
            objName = widg.currentWidget().objectName()
        elif isinstance(widg, QPushButton):
            objName = widg.objectName()
        else:
            print("Metodo Nao previsto")
    return objName


def setClicked2Widget(indexModel=None, lstwidgt=None):
    curWorkmodel = indexModel.model()
    clickedRow = indexModel.row()
    for idx, val in enumerate (lstwidgt):
        curClickedVal = curWorkmodel.record(clickedRow).value(idx) 
        setTxtToWidget(widget=val, val=curClickedVal)
        
        
        
def setToDefault(wdgt=None):
    if isinstance(wdgt, QDoubleSpinBox) or isinstance(wdgt, QSpinBox):
        wdgt.setValue(-1)
            
    elif isinstance(wdgt, QCheckBox) or isinstance(wdgt, QGroupBox):
        wdgt.setChecked(False)
        
    elif isinstance(wdgt, QDateTimeEdit):
        val = QDateTime.currentDateTimeUtc()
        if isinstance(wdgt, QTimeEdit):
            val = QTime.fromString('0', '0')
            wdgt.setTime(val)
        else:
            wdgt.setDateTime(val)
    
    elif isinstance(wdgt, QDateEdit):
        wdgt.setDate(PyQt5.QtCore.QDate.currentDate())
    
    elif isinstance(wdgt, QTimeEdit):
        val = QTime.fromString('0', '0')
        wdgt.setTime(val)
    
    elif isinstance(wdgt, QComboBox):
        wdgt.setCurrentIndex(0)
    else:
        wdgt.clear()
    
       
def setTxtToWidget(widget=None, val =None):
    if widget is not None:
        if isinstance(widget, QLineEdit):
            if val is 'NULL' or val == '':
                widget.setText('')
            else:
                widget.setText(str(val))
            
        elif isinstance(widget, QPlainTextEdit):
            if val is 'NULL' or val == '':
                widget.setPlainText('')
            else:
                widget.setPlainText(str(val))
                       
        elif isinstance(widget, QComboBox):
            if val is 'NULL' or val == '':
                widget.setCurrentIndex(0)
            else:
                widget.setCurrentText(str(val))
                idx = widget.findText(str(val))
                widget.setCurrentIndex(idx)
        
        elif isinstance(widget, QCheckBox):
            if val is 'NULL' or val == '':
                widget.setChecked(False)
            else:
                if isinstance(val, str)== True or val is None:
                    try:
                        if val[0] == 'T' or val[0] == 't':
                            val = True
                        else:
                            val = False
                    except (IndexError, TypeError):
                        val = False 
                widget.setChecked(val)
        
        elif isinstance(widget, QDoubleSpinBox):
            if val is 'NULL' or val == '':
                widget.setValue(-1)
            else:
                widget.setValue(float(val))
        
        elif isinstance(widget, QSpinBox):
            if val is 'NULL' or val == '':
                widget.setValue(-1)
            else:
                widget.setValue(int(val))
    
        elif isinstance(widget, QDateTimeEdit):
            if isinstance(widget, QTimeEdit):
                if val is 'NULL' or val == '':
                    val = QTime.fromString('0', '0')
                    widget.setTime(val)
                else:
                    try:
                        widget.setTime(val)
                    except TypeError:
                        dt= val
                        Newdt = dt.split(sep=':', maxsplit=2)
                        val = PyQt5.QtCore.QTime(int(Newdt[0]), int(Newdt[1]))
                        widget.setTime(val)
            else:
                if val == 'NULL' or val == '':
                    widget.setReadOnly(True)
                else:
                    try:
                        widget.setDateTime(val)
                    except TypeError:
                        try:
                            widget.setDate(val)
                        except TypeError:
                            NewData = setData(dataIN=val)
                            if NewData is not None:
                                widget.setDateTime(NewData)

        elif isinstance(widget, QGroupBox):
            if val == 'NULL':
                widget.setChecked(False)
            else:
                val = bool(val)
                widget.setChecked(val)
        
        else:
            QT_msg.error(txt='Tipo de QObject nao previsto', verbTxt=str(type(val)))
    

def GetSelectedFromView(mIdx=None, totalCol=None):
        lstOut=[]
        try:
            model = mIdx.model()
            clickedRow = mIdx.row()
            for idx in range(totalCol):
                val = model.record(clickedRow).value(idx)
                lstOut.append(val)
            return lstOut
        except AttributeError as At:
            QT_msg.error(txt='Error ', verbTxt=str(At))
            return None


def setData(dataIN=None):
    #===========================================================================
    # if len(dataIN.split(sep='/' , maxsplit=4)) < 3:
    #     newDate = dataIN.split(sep='-' , maxsplit=4)
    # else:
    #     newDate = dataIN.split(sep='/' , maxsplit=4)
    # dd=int(newDate[0])
    # mm=int(newDate[1])
    # yyyy=int(newDate[2])
    # dataOut = datetime.date(dd,mm,yyyy)
    #===========================================================================
    dataOut = None
    if len(dataIN.split(sep=' ' , maxsplit=4)) > 1: 
        datOut = dataIN.split(sep=' ' , maxsplit=4)
        newDate = datOut[0].split(sep='-')
        dataOut = buildingData(newDate = newDate)
    elif len(dataIN.split(sep='T' , maxsplit=4)) > 1 :
        datOut = dataIN.split(sep='T' , maxsplit=4)
        newDate = datOut[0].split(sep='-')
        dataOut = buildingData(newDate = newDate)
    else:
        newDate = dataIN.split(sep='-')
        dataOut = buildingData(newDate = newDate)
    return dataOut   


def buildingData(newDate):
    dd= int(newDate[2])
    mm=int(newDate[1])
    yyyy=int(newDate[0])
    dataOut = datetime(yyyy,mm,dd)  
    return dataOut   


def errorFocus(obj):
    objName = obj.objectName()
    css= "#"+str(objName)+"""{
            background-color: red;
            color:black;
            }"""
    return css


def successFocus(obj):
    objName = obj.objectName()
    css= "#"+str(objName)+"""{
            background-color: white;
            color:black;
            }"""
    return css 


def warningFocus(obj):
    objName = obj.objectName()
    css= "#"+str(objName)+"""{
            background-color: rgb(255, 255, 102);
            color:black;
            }"""
    return css 

def getData(wdgIN=None):
    oldDate = wdgIN.text()
    newDate = oldDate.split(sep='/', maxsplit=4)
    dd=int(newDate[0])
    mm=int(newDate[1])
    yyyy=int(newDate[2])
    newDate = str(datetime.date(int(yyyy),int(mm),int(dd)))
    return newDate