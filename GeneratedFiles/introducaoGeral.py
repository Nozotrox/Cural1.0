# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/chernomirdinmacuvele/Documents/workspace/Cural1.0/UserInt/introducaoGeral.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(265, 285)
        self.gridLayout_3 = QtWidgets.QGridLayout(Form)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.PBSalvar = QtWidgets.QPushButton(Form)
        self.PBSalvar.setObjectName("PBSalvar")
        self.gridLayout_2.addWidget(self.PBSalvar, 0, 1, 1, 1)
        self.PBCancelar = QtWidgets.QPushButton(Form)
        self.PBCancelar.setObjectName("PBCancelar")
        self.gridLayout_2.addWidget(self.PBCancelar, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 2)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.SBTotal = QtWidgets.QSpinBox(Form)
        self.SBTotal.setObjectName("SBTotal")
        self.gridLayout.addWidget(self.SBTotal, 6, 2, 1, 2)
        self.SBTotalVivos = QtWidgets.QSpinBox(Form)
        self.SBTotalVivos.setObjectName("SBTotalVivos")
        self.gridLayout.addWidget(self.SBTotalVivos, 4, 2, 1, 2)
        self.CBCategoria = QtWidgets.QComboBox(Form)
        self.CBCategoria.setObjectName("CBCategoria")
        self.gridLayout.addWidget(self.CBCategoria, 1, 1, 1, 3)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 2)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 2)
        self.SBTotalMortos = QtWidgets.QSpinBox(Form)
        self.SBTotalMortos.setObjectName("SBTotalMortos")
        self.gridLayout.addWidget(self.SBTotalMortos, 5, 2, 1, 2)
        self.CBSexo = QtWidgets.QComboBox(Form)
        self.CBSexo.setObjectName("CBSexo")
        self.gridLayout.addWidget(self.CBSexo, 2, 1, 1, 3)
        self.DTEData = QtWidgets.QDateTimeEdit(Form)
        self.DTEData.setObjectName("DTEData")
        self.gridLayout.addWidget(self.DTEData, 3, 2, 1, 2)
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)
        self.LECod = QtWidgets.QLineEdit(Form)
        self.LECod.setObjectName("LECod")
        self.gridLayout.addWidget(self.LECod, 0, 1, 1, 3)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Introducao Geral de Gados"))
        self.PBSalvar.setText(_translate("Form", "Salvar"))
        self.PBCancelar.setText(_translate("Form", "Cancelar"))
        self.label_5.setText(_translate("Form", "Total Mortos:"))
        self.label_4.setText(_translate("Form", "Total Vivos:"))
        self.label_2.setText(_translate("Form", "Sexo:"))
        self.label.setText(_translate("Form", "Categoria:"))
        self.label_6.setText(_translate("Form", "Total:"))
        self.label_3.setText(_translate("Form", "Data de Nascimento:"))
        self.DTEData.setDisplayFormat(_translate("Form", "dd/MM/yyyy"))
        self.label_7.setText(_translate("Form", "Cod:"))

