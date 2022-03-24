import requestFire
from PySide2.QtWidgets import (QApplication,QTreeWidgetItem, QMainWindow,QTreeWidget)
import PySide2.QtCore
from ui_main import Ui_MainWindow
import sys
import pandas as pd

class MainWindow(QMainWindow, Ui_MainWindow):
    dataFB ={}
    dataGet ={}
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Tela de Vendas')
        # SOLICITAÇÃO DE DADOS DO FB <<<<<<<<<<<<<<<<<<<<<<
        self.dataFB = requestFire.getFB()

        self.btn_cadastrar.clicked.connect(self.getData)

        self.reset_table()

    def getData(self):
        self.idd = self.lineEdit_id.text()
        self.cliente = self.lineEdit_cliente.text()
        self.preco = self.lineEdit_preco.text()
        self.produto = self.lineEdit_produto.text()
        self.dataGet = {'ID':int(self.idd), 'cliente': self.cliente, 'preco':int(self.preco), 'produto':self.produto}
        
        print(self.dataGet)

        requestFire.cadastraDados(self.dataGet)
        

        self.lineEdit_id.setText("")
        self.lineEdit_cliente.setText("")
        self.lineEdit_preco.setText("")
        self.lineEdit_produto.setText("")
        self.dataGet ={}

        self.reset_table()
    
    def reset_table(self):
        self.tabela.clear()
        self.table_vendas()
    
    
    def table_vendas(self):
        self.tabela.setStyleSheet('background: white')
        self.dataFB = requestFire.getFB()

        for id_dados in self.dataFB:
            idfire = id_dados
            ID = self.dataFB[id_dados]['ID']
            cliente = self.dataFB[id_dados]['cliente']
            preco = self.dataFB[id_dados]['preco']
            produto = self.dataFB[id_dados]['produto']
            upDate = {ID,cliente,preco,produto,idfire}
            #IMPRESSAO NA TELA DO SISTEMA, QTreeWidgetItem só "aceitou" dado tipo string. 
            self.campo = QTreeWidgetItem(self.tabela, (str(ID),cliente,str(preco),produto,idfire))
            #self.campo.setCheckState(0, PySide2.QtCore.Qt.CheckState.Unchecked)
            self.tabela.setSortingEnabled(True)






if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()


##################################################
# DADOS PARA TESTE
# data = {'ID':4, 'cliente': 'Junior', 'preco':150, 'produto': 'Celular'}
# Ndata = {'ID':2, 'cliente': 'Maria', 'preco':2050, 'produto': 'Celular'}
##################################################

# TESTE DE SOLICITAÇÕES:

##################################################
# 01)-> CRIAR CADASTRO DE VENDA NO BANCO DE DADOS

# criar = requestFire.cadastraDados(data)
# print(criar)

##################################################
# 02)-> EDITAR CADASTRO DE VENDA NO BANCO DE DADOS

# editar = requestFire.editaVendas(data,Ndata)
# print(editar)

##################################################
# 03)-> DELETAR CADASTRO DE VENDA NO BANCO DE DADOS

# deletar = requestFire.deletarVenda(data)
# print(deletar)



