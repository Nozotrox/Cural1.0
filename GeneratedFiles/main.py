# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/chernomirdinmacuvele/Documents/workspace/Cural1.0/UserInt/main.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuCural = QtWidgets.QMenu(self.menubar)
        self.menuCural.setObjectName("menuCural")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionIntroducao_Geral = QtWidgets.QAction(MainWindow)
        self.actionIntroducao_Geral.setObjectName("actionIntroducao_Geral")
        self.actionINtroducao_de_Novos = QtWidgets.QAction(MainWindow)
        self.actionINtroducao_de_Novos.setObjectName("actionINtroducao_de_Novos")
        self.actionIntroducao_de_Mortos = QtWidgets.QAction(MainWindow)
        self.actionIntroducao_de_Mortos.setObjectName("actionIntroducao_de_Mortos")
        self.actionVizualizar = QtWidgets.QAction(MainWindow)
        self.actionVizualizar.setObjectName("actionVizualizar")
        self.actionIntroducao_Geral_2 = QtWidgets.QAction(MainWindow)
        self.actionIntroducao_Geral_2.setObjectName("actionIntroducao_Geral_2")
        self.actionIntroducao_de_Novos = QtWidgets.QAction(MainWindow)
        self.actionIntroducao_de_Novos.setObjectName("actionIntroducao_de_Novos")
        self.actionIntroducao_de_Mortos_2 = QtWidgets.QAction(MainWindow)
        self.actionIntroducao_de_Mortos_2.setObjectName("actionIntroducao_de_Mortos_2")
        self.actionVizualizacao = QtWidgets.QAction(MainWindow)
        self.actionVizualizacao.setObjectName("actionVizualizacao")
        self.actionCural_Mag_1 = QtWidgets.QAction(MainWindow)
        self.actionCural_Mag_1.setObjectName("actionCural_Mag_1")
        self.actionCural_Mag2 = QtWidgets.QAction(MainWindow)
        self.actionCural_Mag2.setObjectName("actionCural_Mag2")
        self.menuCural.addAction(self.actionCural_Mag_1)
        self.menuCural.addAction(self.actionCural_Mag2)
        self.menubar.addAction(self.menuCural.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Menu Cural"))
        self.menuCural.setTitle(_translate("MainWindow", "Cural"))
        self.actionIntroducao_Geral.setText(_translate("MainWindow", "Introducao Geral"))
        self.actionINtroducao_de_Novos.setText(_translate("MainWindow", "Introducao de Novos"))
        self.actionIntroducao_de_Mortos.setText(_translate("MainWindow", "Introducao de Mortos"))
        self.actionVizualizar.setText(_translate("MainWindow", "Vizualizacao"))
        self.actionIntroducao_Geral_2.setText(_translate("MainWindow", "Introducao Geral"))
        self.actionIntroducao_de_Novos.setText(_translate("MainWindow", "Introducao de Novos"))
        self.actionIntroducao_de_Mortos_2.setText(_translate("MainWindow", "Introducao de Mortos"))
        self.actionVizualizacao.setText(_translate("MainWindow", "Vizualizacao"))
        self.actionCural_Mag_1.setText(_translate("MainWindow", "Cural Mag 1"))
        self.actionCural_Mag2.setText(_translate("MainWindow", "Cural Mag2"))

