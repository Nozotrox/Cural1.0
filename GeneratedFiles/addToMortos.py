# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addToMortos.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_addToMortos(object):
    def setupUi(self, addToMortos):
        addToMortos.setObjectName("addToMortos")
        addToMortos.resize(297, 348)
        self.widget = QtWidgets.QWidget(addToMortos)
        self.widget.setGeometry(QtCore.QRect(20, 20, 258, 311))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(self.widget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.idMortosLabel = QtWidgets.QLabel(self.splitter)
        self.idMortosLabel.setObjectName("idMortosLabel")
        self.idMortosComboBox = QtWidgets.QComboBox(self.splitter)
        self.idMortosComboBox.setObjectName("idMortosComboBox")
        self.verticalLayout.addWidget(self.splitter)
        spacerItem = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.splitter_4 = QtWidgets.QSplitter(self.widget)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.dataMorteLabel = QtWidgets.QLabel(self.splitter_4)
        self.dataMorteLabel.setObjectName("dataMorteLabel")
        self.dataMorteDateTimeEdit = QtWidgets.QDateTimeEdit(self.splitter_4)
        self.dataMorteDateTimeEdit.setEnabled(True)
        self.dataMorteDateTimeEdit.setObjectName("dataMorteDateTimeEdit")
        self.verticalLayout.addWidget(self.splitter_4)
        spacerItem1 = QtWidgets.QSpacerItem(17, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.splitter_7 = QtWidgets.QSplitter(self.widget)
        self.splitter_7.setOrientation(QtCore.Qt.Vertical)
        self.splitter_7.setObjectName("splitter_7")
        self.descricaoLabel = QtWidgets.QLabel(self.splitter_7)
        self.descricaoLabel.setObjectName("descricaoLabel")
        self.descricaoPlainTextEdit = QtWidgets.QPlainTextEdit(self.splitter_7)
        self.descricaoPlainTextEdit.setObjectName("descricaoPlainTextEdit")
        self.verticalLayout.addWidget(self.splitter_7)
        self.splitter_5 = QtWidgets.QSplitter(self.widget)
        self.splitter_5.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_5.setObjectName("splitter_5")
        self.adicionarPushButton = QtWidgets.QPushButton(self.splitter_5)
        self.adicionarPushButton.setObjectName("adicionarPushButton")
        self.limparPushButton = QtWidgets.QPushButton(self.splitter_5)
        self.limparPushButton.setObjectName("limparPushButton")
        self.cancelarPushButton = QtWidgets.QPushButton(self.splitter_5)
        self.cancelarPushButton.setObjectName("cancelarPushButton")
        self.verticalLayout.addWidget(self.splitter_5)

        self.retranslateUi(addToMortos)
        QtCore.QMetaObject.connectSlotsByName(addToMortos)

    def retranslateUi(self, addToMortos):
        _translate = QtCore.QCoreApplication.translate
        addToMortos.setWindowTitle(_translate("addToMortos", "Dialog"))
        self.idMortosLabel.setText(_translate("addToMortos", "Id do gado:"))
        self.dataMorteLabel.setText(_translate("addToMortos", "Data de morte:"))
        self.descricaoLabel.setText(_translate("addToMortos", "Descircao: "))
        self.adicionarPushButton.setText(_translate("addToMortos", "Adicionar"))
        self.limparPushButton.setText(_translate("addToMortos", "Limpar"))
        self.cancelarPushButton.setText(_translate("addToMortos", "Cancelar"))

