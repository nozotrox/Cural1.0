# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ViewCategories_add.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_addGeralDialog(object):
    def setupUi(self, addGeralDialog):
        addGeralDialog.setObjectName("addGeralDialog")
        addGeralDialog.resize(287, 218)
        self.widget = QtWidgets.QWidget(addGeralDialog)
        self.widget.setGeometry(QtCore.QRect(10, 30, 261, 179))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(self.widget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.idCategoriaLabel = QtWidgets.QLabel(self.splitter)
        self.idCategoriaLabel.setObjectName("idCategoriaLabel")
        self.idLineEdit = QtWidgets.QLineEdit(self.splitter)
        self.idLineEdit.setObjectName("idLineEdit")
        self.idLabel = QtWidgets.QLabel(self.splitter)
        self.idLabel.setObjectName("idLabel")
        self.idCategoriaLineEdit = QtWidgets.QLineEdit(self.splitter)
        self.idCategoriaLineEdit.setObjectName("idCategoriaLineEdit")
        self.verticalLayout.addWidget(self.splitter)
        spacerItem = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.splitter_4 = QtWidgets.QSplitter(self.widget)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.splitter_3 = QtWidgets.QSplitter(self.splitter_4)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.sexoLabel = QtWidgets.QLabel(self.splitter_3)
        self.sexoLabel.setObjectName("sexoLabel")
        self.sexoComboBox = QtWidgets.QComboBox(self.splitter_3)
        self.sexoComboBox.setObjectName("sexoComboBox")
        self.sexoComboBox.addItem("")
        self.sexoComboBox.addItem("")
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_4)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.totalLabel = QtWidgets.QLabel(self.splitter_2)
        self.totalLabel.setObjectName("totalLabel")
        self.totalLineEdit = QtWidgets.QLineEdit(self.splitter_2)
        self.totalLineEdit.setObjectName("totalLineEdit")
        self.verticalLayout.addWidget(self.splitter_4)
        spacerItem1 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.splitter_5 = QtWidgets.QSplitter(self.widget)
        self.splitter_5.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_5.setObjectName("splitter_5")
        self.DataDeNascimentoLabel = QtWidgets.QLabel(self.splitter_5)
        self.DataDeNascimentoLabel.setObjectName("DataDeNascimentoLabel")
        self.dataNascimentoDateTime = QtWidgets.QDateTimeEdit(self.splitter_5)
        self.dataNascimentoDateTime.setDisplayFormat("M/d/yyyy hh:mm")
        self.dataNascimentoDateTime.setObjectName("dataNascimentoDateTime")
        self.verticalLayout.addWidget(self.splitter_5)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.submeterPushButton = QtWidgets.QPushButton(self.widget)
        self.submeterPushButton.setObjectName("submeterPushButton")
        self.horizontalLayout.addWidget(self.submeterPushButton)
        spacerItem3 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.limparPushButton = QtWidgets.QPushButton(self.widget)
        self.limparPushButton.setObjectName("limparPushButton")
        self.horizontalLayout.addWidget(self.limparPushButton)
        spacerItem4 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.cancelarPushButton = QtWidgets.QPushButton(self.widget)
        self.cancelarPushButton.setObjectName("cancelarPushButton")
        self.horizontalLayout.addWidget(self.cancelarPushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(addGeralDialog)
        QtCore.QMetaObject.connectSlotsByName(addGeralDialog)

    def retranslateUi(self, addGeralDialog):
        _translate = QtCore.QCoreApplication.translate
        addGeralDialog.setWindowTitle(_translate("addGeralDialog", "Dialog"))
        self.idCategoriaLabel.setText(_translate("addGeralDialog", "Id_Categoria: "))
        self.idLabel.setText(_translate("addGeralDialog", "Id: "))
        self.sexoLabel.setText(_translate("addGeralDialog", "Sexo:"))
        self.sexoComboBox.setItemText(0, _translate("addGeralDialog", "m"))
        self.sexoComboBox.setItemText(1, _translate("addGeralDialog", "f"))
        self.totalLabel.setText(_translate("addGeralDialog", "Total:"))
        self.DataDeNascimentoLabel.setText(_translate("addGeralDialog", "Data de Nascimento:"))
        self.submeterPushButton.setText(_translate("addGeralDialog", "Submeter"))
        self.limparPushButton.setText(_translate("addGeralDialog", "Limpar"))
        self.cancelarPushButton.setText(_translate("addGeralDialog", "Cancelar"))
