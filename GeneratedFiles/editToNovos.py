# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editToNovos.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Editar_Novos(object):
    def setupUi(self, Editar_Novos):
        Editar_Novos.setObjectName("Editar_Novos")
        Editar_Novos.resize(441, 446)
        self.layoutWidget = QtWidgets.QWidget(Editar_Novos)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 280, 381, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.splitter = QtWidgets.QSplitter(self.layoutWidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.splitter_2 = QtWidgets.QSplitter(self.splitter)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.sexoLabel = QtWidgets.QLabel(self.splitter_2)
        self.sexoLabel.setObjectName("sexoLabel")
        self.sexoComboBox = QtWidgets.QComboBox(self.splitter_2)
        self.sexoComboBox.setObjectName("sexoComboBox")
        self.sexoComboBox.addItem("")
        self.sexoComboBox.addItem("")
        self.horizontalLayout.addWidget(self.splitter)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.splitter_7 = QtWidgets.QSplitter(self.layoutWidget)
        self.splitter_7.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_7.setObjectName("splitter_7")
        self.categoriaLabel = QtWidgets.QLabel(self.splitter_7)
        self.categoriaLabel.setObjectName("categoriaLabel")
        self.categoriaComboBox = QtWidgets.QComboBox(self.splitter_7)
        self.categoriaComboBox.setObjectName("categoriaComboBox")
        self.categoriaComboBox.addItem("")
        self.categoriaComboBox.addItem("")
        self.categoriaComboBox.addItem("")
        self.categoriaComboBox.addItem("")
        self.horizontalLayout.addWidget(self.splitter_7)
        self.layoutWidget_2 = QtWidgets.QWidget(Editar_Novos)
        self.layoutWidget_2.setGeometry(QtCore.QRect(30, 310, 236, 71))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.splitter_3 = QtWidgets.QSplitter(self.layoutWidget_2)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.dataNascimentoLabel = QtWidgets.QLabel(self.splitter_3)
        self.dataNascimentoLabel.setObjectName("dataNascimentoLabel")
        self.dataNascimentoDateTimeEdit = QtWidgets.QDateTimeEdit(self.splitter_3)
        self.dataNascimentoDateTimeEdit.setObjectName("dataNascimentoDateTimeEdit")
        self.verticalLayout.addWidget(self.splitter_3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.splitter_5 = QtWidgets.QSplitter(self.layoutWidget_2)
        self.splitter_5.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_5.setObjectName("splitter_5")
        self.totalLabel = QtWidgets.QLabel(self.splitter_5)
        self.totalLabel.setObjectName("totalLabel")
        self.totalLineEdit = QtWidgets.QLineEdit(self.splitter_5)
        self.totalLineEdit.setObjectName("totalLineEdit")
        self.verticalLayout.addWidget(self.splitter_5)
        self.tableView = QtWidgets.QTableView(Editar_Novos)
        self.tableView.setGeometry(QtCore.QRect(10, 20, 421, 231))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        self.tableView.setObjectName("tableView")
        self.layoutWidget_3 = QtWidgets.QWidget(Editar_Novos)
        self.layoutWidget_3.setGeometry(QtCore.QRect(30, 410, 182, 25))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.submeterPushButton = QtWidgets.QPushButton(self.layoutWidget_3)
        self.submeterPushButton.setObjectName("submeterPushButton")
        self.horizontalLayout_2.addWidget(self.submeterPushButton)
        spacerItem3 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.cancelarPushButton = QtWidgets.QPushButton(self.layoutWidget_3)
        self.cancelarPushButton.setObjectName("cancelarPushButton")
        self.horizontalLayout_2.addWidget(self.cancelarPushButton)

        self.retranslateUi(Editar_Novos)
        QtCore.QMetaObject.connectSlotsByName(Editar_Novos)

    def retranslateUi(self, Editar_Novos):
        _translate = QtCore.QCoreApplication.translate
        Editar_Novos.setWindowTitle(_translate("Editar_Novos", "Dialog"))
        self.sexoLabel.setText(_translate("Editar_Novos", "Sexo:"))
        self.sexoComboBox.setItemText(0, _translate("Editar_Novos", "M"))
        self.sexoComboBox.setItemText(1, _translate("Editar_Novos", "F"))
        self.categoriaLabel.setText(_translate("Editar_Novos", "Categoria"))
        self.categoriaComboBox.setItemText(0, _translate("Editar_Novos", "Boi"))
        self.categoriaComboBox.setItemText(1, _translate("Editar_Novos", "Vaca"))
        self.categoriaComboBox.setItemText(2, _translate("Editar_Novos", "Touro"))
        self.categoriaComboBox.setItemText(3, _translate("Editar_Novos", "Vitelo"))
        self.dataNascimentoLabel.setText(_translate("Editar_Novos", "Data de Nascimento:"))
        self.totalLabel.setText(_translate("Editar_Novos", "Total:"))
        self.submeterPushButton.setText(_translate("Editar_Novos", "Submeter"))
        self.cancelarPushButton.setText(_translate("Editar_Novos", "Cancelar"))

