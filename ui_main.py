# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_design.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1011, 650)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(800, 600))
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_dados = QFrame(self.centralwidget)
        self.frame_dados.setObjectName(u"frame_dados")
        self.frame_dados.setMinimumSize(QSize(500, 220))
        self.frame_dados.setMaximumSize(QSize(16777215, 250))
        self.frame_dados.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.frame_dados.setFrameShape(QFrame.StyledPanel)
        self.frame_dados.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_dados)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_d_cadastro = QFrame(self.frame_dados)
        self.frame_d_cadastro.setObjectName(u"frame_d_cadastro")
        self.frame_d_cadastro.setStyleSheet(u"background-color: rgb(240, 240, 240);")
        self.frame_d_cadastro.setFrameShape(QFrame.StyledPanel)
        self.frame_d_cadastro.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_d_cadastro)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_id = QLabel(self.frame_d_cadastro)
        self.label_id.setObjectName(u"label_id")
        self.label_id.setMinimumSize(QSize(60, 0))
        font = QFont()
        font.setFamily(u"Segoe UI Symbol")
        font.setPointSize(10)
        self.label_id.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_id)

        self.lineEdit_id = QLineEdit(self.frame_d_cadastro)
        self.lineEdit_id.setObjectName(u"lineEdit_id")
        self.lineEdit_id.setMinimumSize(QSize(0, 15))
        self.lineEdit_id.setMaximumSize(QSize(16777215, 20))
        self.lineEdit_id.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.lineEdit_id)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_cliente = QLabel(self.frame_d_cadastro)
        self.label_cliente.setObjectName(u"label_cliente")
        self.label_cliente.setMinimumSize(QSize(60, 0))
        self.label_cliente.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_cliente)

        self.lineEdit_cliente = QLineEdit(self.frame_d_cadastro)
        self.lineEdit_cliente.setObjectName(u"lineEdit_cliente")
        self.lineEdit_cliente.setMinimumSize(QSize(0, 15))
        self.lineEdit_cliente.setMaximumSize(QSize(16777215, 20))
        self.lineEdit_cliente.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.lineEdit_cliente)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_preco = QLabel(self.frame_d_cadastro)
        self.label_preco.setObjectName(u"label_preco")
        self.label_preco.setMinimumSize(QSize(60, 0))
        self.label_preco.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_preco)

        self.lineEdit_preco = QLineEdit(self.frame_d_cadastro)
        self.lineEdit_preco.setObjectName(u"lineEdit_preco")
        self.lineEdit_preco.setMinimumSize(QSize(0, 15))
        self.lineEdit_preco.setMaximumSize(QSize(16777215, 20))
        self.lineEdit_preco.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_4.addWidget(self.lineEdit_preco)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_produto = QLabel(self.frame_d_cadastro)
        self.label_produto.setObjectName(u"label_produto")
        self.label_produto.setMinimumSize(QSize(60, 0))
        self.label_produto.setFont(font)

        self.horizontalLayout_5.addWidget(self.label_produto)

        self.lineEdit_produto = QLineEdit(self.frame_d_cadastro)
        self.lineEdit_produto.setObjectName(u"lineEdit_produto")
        self.lineEdit_produto.setMinimumSize(QSize(0, 15))
        self.lineEdit_produto.setMaximumSize(QSize(16777215, 20))
        self.lineEdit_produto.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_5.addWidget(self.lineEdit_produto)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)


        self.horizontalLayout.addWidget(self.frame_d_cadastro)

        self.frame_d_btn = QFrame(self.frame_dados)
        self.frame_d_btn.setObjectName(u"frame_d_btn")
        self.frame_d_btn.setMinimumSize(QSize(120, 0))
        self.frame_d_btn.setMaximumSize(QSize(200, 16777215))
        self.frame_d_btn.setStyleSheet(u"background-color: rgb(240, 240, 240);")
        self.frame_d_btn.setFrameShape(QFrame.StyledPanel)
        self.frame_d_btn.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_d_btn)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btn_cadastrar = QPushButton(self.frame_d_btn)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setMaximumSize(QSize(16777215, 50))
        self.btn_cadastrar.setStyleSheet(u"QPushButton{\n"
"	border-radius: 7px;\n"
"	border: 1px solid rgb(30, 30, 30);\n"
"	background-color: rgb(234, 234, 234);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 7px;\n"
"	border: 1px solid rgb(60, 60, 60);\n"
"	background-color: rgb(244, 244, 255);\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.btn_cadastrar)

        self.btn_conf_edit = QPushButton(self.frame_d_btn)
        self.btn_conf_edit.setObjectName(u"btn_conf_edit")
        self.btn_conf_edit.setMaximumSize(QSize(16777215, 50))
        self.btn_conf_edit.setStyleSheet(u"QPushButton{\n"
"	border-radius: 7px;\n"
"	border: 1px solid rgb(30, 30, 30);\n"
"	background-color: rgb(234, 234, 234);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 7px;\n"
"	border: 1px solid rgb(60, 60, 60);\n"
"	background-color: rgb(244, 255, 244);\n"
"}")

        self.verticalLayout_2.addWidget(self.btn_conf_edit)


        self.horizontalLayout.addWidget(self.frame_d_btn)


        self.verticalLayout.addWidget(self.frame_dados)

        self.frame_D_tabela = QFrame(self.centralwidget)
        self.frame_D_tabela.setObjectName(u"frame_D_tabela")
        self.frame_D_tabela.setStyleSheet(u"background-color: rgb(65, 65, 65);")
        self.frame_D_tabela.setFrameShape(QFrame.StyledPanel)
        self.frame_D_tabela.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_D_tabela)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.tabela = QTreeWidget(self.frame_D_tabela)
        self.tabela.setObjectName(u"tabela")

        self.horizontalLayout_6.addWidget(self.tabela)

        self.frame = QFrame(self.frame_D_tabela)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(120, 0))
        self.frame.setStyleSheet(u"background-color: rgb(240, 240, 240);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 50))
        self.label.setLayoutDirection(Qt.RightToLeft)
        self.label.setScaledContents(False)
        self.label.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.label)

        self.btn_editar = QPushButton(self.frame)
        self.btn_editar.setObjectName(u"btn_editar")
        self.btn_editar.setMinimumSize(QSize(100, 50))
        self.btn_editar.setMaximumSize(QSize(100, 50))
        self.btn_editar.setStyleSheet(u"QPushButton{\n"
"	border-radius: 7px;\n"
"	border: 1px solid rgb(30, 30, 30);\n"
"	background-color: rgb(234, 234, 234);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 7px;\n"
"	border: 1px solid rgb(60, 60, 60);\n"
"	background-color: rgb(255, 244, 244);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_editar)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.frame_2)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 50))
        self.label_2.setLayoutDirection(Qt.RightToLeft)
        self.label_2.setScaledContents(False)
        self.label_2.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.label_2)

        self.btn_excluir = QPushButton(self.frame)
        self.btn_excluir.setObjectName(u"btn_excluir")
        self.btn_excluir.setMaximumSize(QSize(16777215, 50))
        self.btn_excluir.setStyleSheet(u"QPushButton{\n"
"	border-radius: 7px;\n"
"	border: 1px solid rgb(30, 30, 30);\n"
"	background-color: rgb(234, 234, 234);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 7px;\n"
"	border: 1px solid rgb(60, 60, 60);\n"
"	background-color: rgb(255, 244, 244);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_excluir)


        self.horizontalLayout_6.addWidget(self.frame)


        self.verticalLayout.addWidget(self.frame_D_tabela)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_id.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_cliente.setText(QCoreApplication.translate("MainWindow", u"CLIENTE", None))
        self.label_preco.setText(QCoreApplication.translate("MainWindow", u"PRECO", None))
        self.label_produto.setText(QCoreApplication.translate("MainWindow", u"PRODUTO", None))
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"CADASTRA", None))
        self.btn_conf_edit.setText(QCoreApplication.translate("MainWindow", u"CONFIRMA\n"
"EDI\u00c7\u00c3O", None))
        ___qtreewidgetitem = self.tabela.headerItem()
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"ID_FB", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"Produto", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"Preco", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Cliente", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"ID", None));
        self.label.setText(QCoreApplication.translate("MainWindow", u"Marque um item para Editar", None))
        self.btn_editar.setText(QCoreApplication.translate("MainWindow", u"EDITAR", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Excluir cadastro selecionado", None))
        self.btn_excluir.setText(QCoreApplication.translate("MainWindow", u"EXCLUIR", None))
    # retranslateUi

