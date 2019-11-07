import sqlite3
import sys
import funcoesBanco
import imprimir
# Abre uma conexão como banco de dados
conexao = sqlite3.connect('database.sqlite')
cursor = conexao.cursor()
def selOpcao(conexao):
    while(True):
        mainMenu()
        op = int(input("Informe a opção desejada: "))
        if(op == 0):
            print("Você escolheu sair! :( ")
            sys.exit()
        elif(op == 1):
            iduser = funcoesBanco.logar(conexao)
            iduser = int(iduser)
            x = funcoesBanco.pa(conexao)
            if(x == 1):
                funcoesBanco.finalizarCadastro(conexao)
            if(iduser!= False):
                menuLogado(iduser)
        elif(op == 2):
           funcoesBanco.registrar(conexao)
        elif(op == 3):
            funcoesBanco.recuperar()


def mainMenu():
    print("""
    Bem-vindo selecione a opção desejada: 
    \t1 - Logar\n
    \t2 - Registrar\n
    \t3 - Recuperar senha\n
    \t0 - Sair do sistema \n
    """)


def menuLogin():
    print("""
    Olá bem vind@,\n\n
    Selecione a opção desejada:
    \t1 - Imprimir novo arquivo\n
    \t2 - Consultar saldo \n
    \t3 - Realizar Recarga\n
    \t4 - Configurações\n\n
    \t0 - Deslogar \n
    """)

def menuLogado(idusuario):

    menuLogin()
    while(True):
        op = int(input("Opção: "))
        if(op == 1):
            print("Entrou")
            sql = f"""SELECT saldo_impressoes FROM saldo
            INNER JOIN info
            ON saldo.saldoid = info.saldoid
            WHERE info.userid = {idusuario} """

            cursor.execute(sql)
            saldo = cursor.fetchall()
            if(saldo[0][0] > 0):
                imprimir.impress()
        if(op == 0):
            break
            sys.exit()
# Fecha a conexão que foi criada com banco de dados
conexao.close
