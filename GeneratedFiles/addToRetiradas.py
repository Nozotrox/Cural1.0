# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addToRetiradas.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_addToRetiradas(object):
    def setupUi(self, addToRetiradas):
        addToRetiradas.setObjectName("addToRetiradas")
        addToRetiradas.resize(297, 363)
        self.layoutWidget = QtWidgets.QWidget(addToRetiradas)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 30, 258, 311))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(self.layoutWidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.idMortosLabel = QtWidgets.QLabel(self.splitter)
        self.idMortosLabel.setObjectName("idMortosLabel")
        self.idRetiradosComboBox = QtWidgets.QComboBox(self.splitter)
        self.idRetiradosComboBox.setObjectName("idRetiradosComboBox")
        self.verticalLayout.addWidget(self.splitter)
        spacerItem = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.splitter_4 = QtWidgets.QSplitter(self.layoutWidget)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.dataRetiradaLabel = QtWidgets.QLabel(self.splitter_4)
        self.dataRetiradaLabel.setObjectName("dataRetiradaLabel")
        self.dataRetiradaDateTimeEdit = QtWidgets.QDateTimeEdit(self.splitter_4)
        self.dataRetiradaDateTimeEdit.setEnabled(True)
        self.dataRetiradaDateTimeEdit.setObjectName("dataRetiradaDateTimeEdit")
        self.verticalLayout.addWidget(self.splitter_4)
        spacerItem1 = QtWidgets.QSpacerItem(17, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.splitter_7 = QtWidgets.QSplitter(self.layoutWidget)
        self.splitter_7.setOrientation(QtCore.Qt.Vertical)
        self.splitter_7.setObjectName("splitter_7")
        self.descricaoLabel = QtWidgets.QLabel(self.splitter_7)
        self.descricaoLabel.setObjectName("descricaoLabel")
        self.descricaoPlainTextEdit = QtWidgets.QPlainTextEdit(self.splitter_7)
        self.descricaoPlainTextEdit.setObjectName("descricaoPlainTextEdit")
        self.verticalLayout.addWidget(self.splitter_7)
        self.splitter_5 = QtWidgets.QSplitter(self.layoutWidget)
        self.splitter_5.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_5.setObjectName("splitter_5")
        self.adicionarPushButton = QtWidgets.QPushButton(self.splitter_5)
        self.adicionarPushButton.setObjectName("adicionarPushButton")
        self.limparPushButton = QtWidgets.QPushButton(self.splitter_5)
        self.limparPushButton.setObjectName("limparPushButton")
        self.cancelarPushButton = QtWidgets.QPushButton(self.splitter_5)
        self.cancelarPushButton.setObjectName("cancelarPushButton")
        self.verticalLayout.addWidget(self.splitter_5)

        self.retranslateUi(addToRetiradas)
        QtCore.QMetaObject.connectSlotsByName(addToRetiradas)

    def retranslateUi(self, addToRetiradas):
        _translate = QtCore.QCoreApplication.translate
        addToRetiradas.setWindowTitle(_translate("addToRetiradas", "Dialog"))
        self.idMortosLabel.setText(_translate("addToRetiradas", "Id do gado:"))
        self.dataRetiradaLabel.setText(_translate("addToRetiradas", "Data da Retirada:"))
        self.descricaoLabel.setText(_translate("addToRetiradas", "Descircao: "))
        self.adicionarPushButton.setText(_translate("addToRetiradas", "Adicionar"))
        self.limparPushButton.setText(_translate("addToRetiradas", "Limpar"))
        self.cancelarPushButton.setText(_translate("addToRetiradas", "Cancelar"))

