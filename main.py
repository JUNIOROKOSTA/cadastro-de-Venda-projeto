
from typing_extensions import Self
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
        self.btn_cadastrar.clicked.connect(self.cadastra_dados)
        self.btn_editar.clicked.connect(self.editar_valor)
        self.btn_conf_edit.clicked.connect(self.editar_cadastro)
        self.btn_excluir.clicked.connect(self.deletar_cadastro)

        self.checked_items = [""]

        self.reset_table()

    def limpar_cadastro(self):

        self.lineEdit_id.setText("")
        self.lineEdit_cliente.setText("")
        self.lineEdit_preco.setText("")
        self.lineEdit_produto.setText("")

    def charge_item(self):
        self.checked_items = []
        def recurse(parent_item):
            for i in range(parent_item.childCount()):
                child = parent_item.child(i)
                grand_children = child.childCount()
                if grand_children > 0:
                    recurse(child)
                elif child.checkState(0) == PySide2.QtCore.Qt.Checked:
                    self.checked_items = (child.text(0))
                    self.checked_items = requestFire.buscar_dados_id(self.checked_items)
        
        recurse(self.tabela.invisibleRootItem())
        return self.checked_items
    
    def editar_valor(self):
        items = self.charge_item()
        self.lineEdit_id.setText(str(items["ID"]))
        self.lineEdit_cliente.setText(str(items["cliente"]))
        self.lineEdit_preco.setText(str(items["preco"]))
        self.lineEdit_produto.setText(str(items["produto"]))
        self.reset_table()

    def cadastra_dados(self):
        data = self.getData()
        requestFire.cadastraDados(data)

        self.reset_table()
        self.limpar_cadastro()


    def getData(self):
        idd = self.lineEdit_id.text()
        cliente = self.lineEdit_cliente.text()
        preco = self.lineEdit_preco.text()
        produto = self.lineEdit_produto.text()
        return {'ID':int(idd), 'cliente': cliente, 'preco':int(preco), 'produto':produto}
    
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
    
    def editar_cadastro(self):
        novo_data = self.getData()
        requestFire.editaVendas(self.checked_items,novo_data)

        self.limpar_cadastro()
        self.reset_table()

    def deletar_cadastro(self):
        self.editar_valor()
        dataDel = self.getData()
        requestFire.deletarVenda(dataDel)

        self.limpar_cadastro()
        self.reset_table()


if __name__ == "__main__":
    app = QTW.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()