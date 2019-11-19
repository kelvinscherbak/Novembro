import sqlite3
import menus
import funcoesBanco
from sys import exit
# Abre uma conexão como banco de dados
conexao = sqlite3.connect('database.sqlite')
def inicio(conexao):
    funcoesBanco.criarTabelas(conexao)
    while(True):
        login = menus.selOpcao(conexao)
        if(login == False):
            sys.exit()
        menus.menuLogado(conexao,login)
inicio(conexao)

# Fecha a conexão que foi criada com banco de dados
conexao.close