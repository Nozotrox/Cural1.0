# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/chernomirdinmacuvele/Documents/workspace/Cural1.0/UserInt/mortos.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(263, 187)
        self.gridLayout_3 = QtWidgets.QGridLayout(Form)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.SBTotalMortos = QtWidgets.QSpinBox(Form)
        self.SBTotalMortos.setObjectName("SBTotalMortos")
        self.gridLayout.addWidget(self.SBTotalMortos, 3, 2, 1, 2)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 2)
        self.CBCategoria = QtWidgets.QComboBox(Form)
        self.CBCategoria.setObjectName("CBCategoria")
        self.gridLayout.addWidget(self.CBCategoria, 0, 1, 1, 3)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 2)
        self.DTEData = QtWidgets.QDateTimeEdit(Form)
        self.DTEData.setObjectName("DTEData")
        self.gridLayout.addWidget(self.DTEData, 2, 2, 1, 2)
        self.CBSexo = QtWidgets.QComboBox(Form)
        self.CBSexo.setObjectName("CBSexo")
        self.gridLayout.addWidget(self.CBSexo, 1, 1, 1, 3)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.PBSalvar = QtWidgets.QPushButton(Form)
        self.PBSalvar.setObjectName("PBSalvar")
        self.gridLayout_2.addWidget(self.PBSalvar, 0, 1, 1, 1)
        self.PBCancelar = QtWidgets.QPushButton(Form)
        self.PBCancelar.setObjectName("PBCancelar")
        self.gridLayout_2.addWidget(self.PBCancelar, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Mortos"))
        self.label_2.setText(_translate("Form", "Sexo:"))
        self.label_3.setText(_translate("Form", "Data de Nascimento:"))
        self.label_5.setText(_translate("Form", "Total Mortos:"))
        self.DTEData.setDisplayFormat(_translate("Form", "dd/MM/yyyy"))
        self.label.setText(_translate("Form", "Categoria:"))
        self.PBSalvar.setText(_translate("Form", "Salvar"))
        self.PBCancelar.setText(_translate("Form", "Cancelar"))

