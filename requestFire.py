from joblib import PrintTime
import verificaDados
import requests as rest
import json
linkBD = "https://meuprojeto01-66f74-default-rtdb.firebaseio.com/"

##################################################
# CONSUTAR DE EXISTE ID DE CADASTRO DE VENDA NO BANCO DE DADOS
def getFB():
    result = rest.get(f'{linkBD}/VENDAS/.json')
    result= result.json()
    return result

##################################################
# CONSUTAR DE EXISTE ID DE CADASTRO DE VENDA NO BANCO DE DADOS
def consultCadastro(data):

    confirm = verificaDados.verifica(data['cliente'],linkBD,data['ID'])
    id = data['ID']
    if confirm :
        print(f'O ID: {id} Existe no banco de dados')
        return "OK"
    else:
        return True
##################################################
# 03)-> DELETAR CADASTRO DE VENDA NO BANCO DE DADOS
def deletarVenda(data1):
    if consultCadastro(data1) == "OK":
        idDel= verificaDados.verifica(data1['cliente'],linkBD,data1['ID'])
        rest.delete(f'{linkBD}/VENDAS/{idDel}/.json')
        print('Cadastro Excluido com Sucesso!!!')
    else:
        print('Cadastro não existe no Banco de dado. Operação Falhou!!!')

##################################################
# 02)-> EDITAR CADASTRO DE VENDA NO BANCO DE DADOS
def editaVendas(data1,Ndata):
    if consultCadastro(data1) == "OK":
        if data1['ID'] == Ndata['ID']:
            idEdit = verificaDados.verifica(data1['cliente'],linkBD,data1['ID'])
            rest.patch(f'{linkBD}/VENDAS/{idEdit}/.json', data=json.dumps(Ndata))
            print('Operação de Edição realizada com secesso!!!')
        else: print('IDs de registro diferentes!!!')

##################################################
# 01)-> CRIAR CADASTRO DE VENDA NO BANCO DE DADOS
def cadastraDados(data):
    if consultCadastro(data) == True:
        rest.post(f'{linkBD}/VENDAS/.json', data=json.dumps(data))
        print('Operação realizada com secesso!!!')
