# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editToMortos.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Editar_Mortos(object):
    def setupUi(self, Editar_Mortos):
        Editar_Mortos.setObjectName("Editar_Mortos")
        Editar_Mortos.resize(341, 438)
        self.splitter_9 = QtWidgets.QSplitter(Editar_Mortos)
        self.splitter_9.setGeometry(QtCore.QRect(11, 241, 235, 20))
        self.splitter_9.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_9.setObjectName("splitter_9")
        self.dataAcontecimentoLabel = QtWidgets.QLabel(self.splitter_9)
        self.dataAcontecimentoLabel.setObjectName("dataAcontecimentoLabel")
        self.dataAcontecimentoDateTime = QtWidgets.QDateTimeEdit(self.splitter_9)
        self.dataAcontecimentoDateTime.setObjectName("dataAcontecimentoDateTime")
        self.splitter_4 = QtWidgets.QSplitter(Editar_Mortos)
        self.splitter_4.setGeometry(QtCore.QRect(11, 407, 150, 23))
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.submeterPushButton = QtWidgets.QPushButton(self.splitter_4)
        self.submeterPushButton.setObjectName("submeterPushButton")
        self.cancelarPushButton = QtWidgets.QPushButton(self.splitter_4)
        self.cancelarPushButton.setObjectName("cancelarPushButton")
        self.splitter_10 = QtWidgets.QSplitter(Editar_Mortos)
        self.splitter_10.setGeometry(QtCore.QRect(11, 273, 289, 122))
        self.splitter_10.setOrientation(QtCore.Qt.Vertical)
        self.splitter_10.setObjectName("splitter_10")
        self.descricaoLabel = QtWidgets.QLabel(self.splitter_10)
        self.descricaoLabel.setObjectName("descricaoLabel")
        self.descricaoPlainTextEdit = QtWidgets.QPlainTextEdit(self.splitter_10)
        self.descricaoPlainTextEdit.setObjectName("descricaoPlainTextEdit")
        self.tableView = QtWidgets.QTableView(Editar_Mortos)
        self.tableView.setGeometry(QtCore.QRect(10, 10, 321, 171))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        self.tableView.setObjectName("tableView")
        self.splitter = QtWidgets.QSplitter(Editar_Mortos)
        self.splitter.setGeometry(QtCore.QRect(10, 200, 151, 20))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.idLabel = QtWidgets.QLabel(self.splitter)
        self.idLabel.setObjectName("idLabel")
        self.idComboBox = QtWidgets.QComboBox(self.splitter)
        self.idComboBox.setObjectName("idComboBox")

        self.retranslateUi(Editar_Mortos)
        QtCore.QMetaObject.connectSlotsByName(Editar_Mortos)

    def retranslateUi(self, Editar_Mortos):
        _translate = QtCore.QCoreApplication.translate
        Editar_Mortos.setWindowTitle(_translate("Editar_Mortos", "Dialog"))
        self.dataAcontecimentoLabel.setText(_translate("Editar_Mortos", "Data da Morte"))
        self.submeterPushButton.setText(_translate("Editar_Mortos", "Submeter"))
        self.cancelarPushButton.setText(_translate("Editar_Mortos", "Cancelar"))
        self.descricaoLabel.setText(_translate("Editar_Mortos", "Descricao:"))
        self.idLabel.setText(_translate("Editar_Mortos", "Id do Gado:"))

