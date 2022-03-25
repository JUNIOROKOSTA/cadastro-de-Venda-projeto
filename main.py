
from PySide2 import QtWidgets as QTW
from ui_main import Ui_MainWindow
import PySide2.QtCore
import sys
import requestFire

class MainWindow(QTW.QMainWindow, Ui_MainWindow):
    
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Tela de Vendas')
        # SOLICITAÇÃO DE DADOS DO FB <<<<<<<<<<<<<<<<<<<<<<
        self.data_get ={}
        self.data_fb = requestFire.getFB()
        self.checked_items =[]
        self.lineEdit_id.setText("")
        self.lineEdit_cliente.setText("")
        self.lineEdit_preco.setText("")
        self.lineEdit_produto.setText("")
        
        self.btn_cadastrar.clicked.connect(self.getData)
        self.btn_editar.clicked.connect(self.charge_item)

        self.reset_table()

    def charge_item(self):

        def recurse(parent_item):
            for i in range(parent_item.childCount()):
                child = parent_item.child(i)
                grand_children = child.childCount()
                if grand_children > 0:
                    recurse(child)
                    print("1: ",child)
                elif child.checkState(0) == PySide2.QtCore.Qt.Checked:
                    self.checked_items = (child.text(0))
                    self.checked_items = requestFire.buscar_dados_id(self.checked_items)
                    

        recurse(self.tabela.invisibleRootItem())
        print(self.checked_items)
        self.lineEdit_id.setText(str(self.checked_items["ID"]))
        self.lineEdit_cliente.setText(str(self.checked_items["cliente"]))
        self.lineEdit_preco.setText(str(self.checked_items["preco"]))
        self.lineEdit_produto.setText(str(self.checked_items["produto"]))
        self.checked_items = []
        self.reset_table()



    def getData(self):
        idd = self.lineEdit_id.text()
        cliente = self.lineEdit_cliente.text()
        preco = self.lineEdit_preco.text()
        produto = self.lineEdit_produto.text()
        self.data_get = {'ID':int(idd), 'cliente': cliente, 'preco':int(preco), 'produto':produto}
        
        print(self.data_get)

        requestFire.cadastraDados(self.data_get)
        

        self.lineEdit_id.setText("")
        self.lineEdit_cliente.setText("")
        self.lineEdit_preco.setText("")
        self.lineEdit_produto.setText("")
        self.data_get ={}

        self.reset_table()
    
    def reset_table(self):
        self.tabela.clear()
        self.table_vendas()
    
    
    def table_vendas(self):
        self.tabela.setStyleSheet('background: white')
        self.data_fb = requestFire.getFB()

        for id_dados in self.data_fb:
            idfire = id_dados
            idd = self.data_fb[id_dados]['ID']
            cliente = self.data_fb[id_dados]['cliente']
            preco = self.data_fb[id_dados]['preco']
            produto = self.data_fb[id_dados]['produto']
            #IMPRESSAO NA TELA DO SISTEMA, QTreeWidgetItem só "aceitou" dado tipo string. 
            campo = QTW.QTreeWidgetItem(self.tabela, (str(idd),cliente,str(preco),produto,idfire))
            campo.setCheckState(0, PySide2.QtCore.Qt.CheckState.Unchecked)
            self.tabela.setSortingEnabled(True)
   







if __name__ == "__main__":
    app = QTW.QApplication(sys.argv)
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