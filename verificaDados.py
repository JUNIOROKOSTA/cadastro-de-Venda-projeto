from pandas import notnull
import requests as rest

##################################################
# VERIFICAR CADASTROS DO BANCO DE DADOS

def verifica(data = '',linkBD = '',n = ''):
    n= int(n)
    requisicaoGet = rest.get(f'{linkBD}/VENDAS/.json')
    getJsonRest = requisicaoGet.json()
    for id_dados in getJsonRest:
        idfire = id_dados
        ID = getJsonRest[id_dados]['ID']
        cliente = getJsonRest[id_dados]['cliente']
        preco = getJsonRest[id_dados]['preco']
        produto = getJsonRest[id_dados]['produto']
        #print(f'ID: {type(ID)},// clienet: {cliente},// preço: {preco},// produto: {produto},// IDFire: {idfire}')
        if cliente == data and ID == n:
            return idfire
        elif ID == n:
            return {"ID":ID,"cliente": cliente, "preco":preco,"produto":produto}
