# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ViewCategories.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EditGeralDialog(object):
    def setupUi(self, EditGeralDialog):
        EditGeralDialog.setObjectName("EditGeralDialog")
        EditGeralDialog.resize(548, 571)
        self.tableView = QtWidgets.QTableView(EditGeralDialog)
        self.tableView.setGeometry(QtCore.QRect(20, 10, 491, 231))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        self.tableView.setObjectName("tableView")
        self.splitter_4 = QtWidgets.QSplitter(EditGeralDialog)
        self.splitter_4.setGeometry(QtCore.QRect(100, 540, 150, 23))
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.submeterPushButton = QtWidgets.QPushButton(self.splitter_4)
        self.submeterPushButton.setObjectName("submeterPushButton")
        self.cancelarPushButton = QtWidgets.QPushButton(self.splitter_4)
        self.cancelarPushButton.setObjectName("cancelarPushButton")
        self.splitter = QtWidgets.QSplitter(EditGeralDialog)
        self.splitter.setGeometry(QtCore.QRect(100, 260, 164, 20))
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
        self.splitter_3 = QtWidgets.QSplitter(EditGeralDialog)
        self.splitter_3.setGeometry(QtCore.QRect(100, 330, 229, 20))
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.label_2 = QtWidgets.QLabel(self.splitter_3)
        self.label_2.setObjectName("label_2")
        self.dataDateTimeEdit = QtWidgets.QDateTimeEdit(self.splitter_3)
        self.dataDateTimeEdit.setObjectName("dataDateTimeEdit")
        self.line = QtWidgets.QFrame(EditGeralDialog)
        self.line.setGeometry(QtCore.QRect(100, 360, 341, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.splitter_5 = QtWidgets.QSplitter(EditGeralDialog)
        self.splitter_5.setGeometry(QtCore.QRect(300, 260, 151, 20))
        self.splitter_5.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_5.setObjectName("splitter_5")
        self.totalLabel = QtWidgets.QLabel(self.splitter_5)
        self.totalLabel.setObjectName("totalLabel")
        self.totalLineEdit = QtWidgets.QLineEdit(self.splitter_5)
        self.totalLineEdit.setObjectName("totalLineEdit")
        self.splitter_7 = QtWidgets.QSplitter(EditGeralDialog)
        self.splitter_7.setGeometry(QtCore.QRect(100, 290, 161, 20))
        self.splitter_7.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_7.setObjectName("splitter_7")
        self.categoriaLabel = QtWidgets.QLabel(self.splitter_7)
        self.categoriaLabel.setObjectName("categoriaLabel")
        self.categoriaComboBox = QtWidgets.QComboBox(self.splitter_7)
        self.categoriaComboBox.setObjectName("categoriaComboBox")
        self.splitter_8 = QtWidgets.QSplitter(EditGeralDialog)
        self.splitter_8.setGeometry(QtCore.QRect(100, 380, 171, 20))
        self.splitter_8.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_8.setObjectName("splitter_8")
        self.acontecimentoLabel = QtWidgets.QLabel(self.splitter_8)
        self.acontecimentoLabel.setObjectName("acontecimentoLabel")
        self.acontecimentoComboBox = QtWidgets.QComboBox(self.splitter_8)
        self.acontecimentoComboBox.setObjectName("acontecimentoComboBox")
        self.splitter_9 = QtWidgets.QSplitter(EditGeralDialog)
        self.splitter_9.setGeometry(QtCore.QRect(100, 410, 261, 20))
        self.splitter_9.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_9.setObjectName("splitter_9")
        self.categoriaLabel_2 = QtWidgets.QLabel(self.splitter_9)
        self.categoriaLabel_2.setObjectName("categoriaLabel_2")
        self.acontecimentoDateTime = QtWidgets.QDateTimeEdit(self.splitter_9)
        self.acontecimentoDateTime.setObjectName("acontecimentoDateTime")
        self.splitter_10 = QtWidgets.QSplitter(EditGeralDialog)
        self.splitter_10.setGeometry(QtCore.QRect(100, 450, 331, 71))
        self.splitter_10.setOrientation(QtCore.Qt.Vertical)
        self.splitter_10.setObjectName("splitter_10")
        self.descricaoLabel = QtWidgets.QLabel(self.splitter_10)
        self.descricaoLabel.setObjectName("descricaoLabel")
        self.descricaoPlainTextEdit = QtWidgets.QPlainTextEdit(self.splitter_10)
        self.descricaoPlainTextEdit.setObjectName("descricaoPlainTextEdit")

        self.retranslateUi(EditGeralDialog)
        QtCore.QMetaObject.connectSlotsByName(EditGeralDialog)

    def retranslateUi(self, EditGeralDialog):
        _translate = QtCore.QCoreApplication.translate
        EditGeralDialog.setWindowTitle(_translate("EditGeralDialog", "Dialog"))
        self.submeterPushButton.setText(_translate("EditGeralDialog", "Submeter"))
        self.cancelarPushButton.setText(_translate("EditGeralDialog", "Cancelar"))
        self.sexoLabel.setText(_translate("EditGeralDialog", "Sexo:"))
        self.sexoComboBox.setItemText(0, _translate("EditGeralDialog", "M"))
        self.sexoComboBox.setItemText(1, _translate("EditGeralDialog", "F"))
        self.label_2.setText(_translate("EditGeralDialog", "Data de Nascimento:"))
        self.totalLabel.setText(_translate("EditGeralDialog", "Total:"))
        self.categoriaLabel.setText(_translate("EditGeralDialog", "Categoria"))
        self.acontecimentoLabel.setText(_translate("EditGeralDialog", "Acontecimeto"))
        self.categoriaLabel_2.setText(_translate("EditGeralDialog", "Data do Acontecimeto"))
        self.descricaoLabel.setText(_translate("EditGeralDialog", "Descricao:"))
