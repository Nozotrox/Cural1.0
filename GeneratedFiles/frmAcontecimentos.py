# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/chernomirdinmacuvele/Documents/workspace/Cural1.0/UserInt/frmAcontecimentos.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(290, 107)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.LECod = QtWidgets.QLineEdit(Form)
        self.LECod.setObjectName("LECod")
        self.gridLayout.addWidget(self.LECod, 0, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.LENome = QtWidgets.QLineEdit(Form)
        self.LENome.setObjectName("LENome")
        self.gridLayout.addWidget(self.LENome, 1, 1, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(72, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.PBGuardar = QtWidgets.QPushButton(Form)
        self.PBGuardar.setObjectName("PBGuardar")
        self.gridLayout.addWidget(self.PBGuardar, 2, 1, 1, 1)
        self.PBCancelar = QtWidgets.QPushButton(Form)
        self.PBCancelar.setMaximumSize(QtCore.QSize(16777208, 16777215))
        self.PBCancelar.setObjectName("PBCancelar")
        self.gridLayout.addWidget(self.PBCancelar, 2, 2, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Acontecimentos"))
        self.label.setText(_translate("Form", "Cod."))
        self.label_2.setText(_translate("Form", "Nome"))
        self.PBGuardar.setText(_translate("Form", "Guardar"))
        self.PBCancelar.setText(_translate("Form", "Cancelar"))

