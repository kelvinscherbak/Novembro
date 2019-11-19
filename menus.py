import sqlite3
import sys
import logar
import imprimir
import funcoesBanco
import registrar
import recuperar
conexao = sqlite3.connect('database.sqlite')
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
    \n\n
    Selecione a opção desejada:
    \t1 - Imprimir novo arquivo\n
    \t2 - Consultar saldo \n
    \t3 - Realizar Recarga\n
    \t4 - Configurações\n\n
    \t0 - Deslogar \n
    """)



# Abre uma conexão como banco de dados

cursor = conexao.cursor()
def selOpcao(conexao):
    conexao = sqlite3.connect('database.sqlite')
    cursor = conexao.cursor()
    while(True):
        mainMenu()
        op = int(input("Informe a opção desejada: "))
        if(op == 0):
            print("Você escolheu sair! :( ")
            sys.exit()
        elif(op == 1):
            iduser = logar.logar(conexao)
            iduser = int(iduser)
            funcoesBanco.pa(conexao,iduser)
            if(iduser!= False):
                return iduser
                break
            elif(iduser == False):
                print("Erro ao logar")
        elif(op == 2):
           registrar.registrar(conexao)
        elif(op == 3):
            recuperar.recuperacao(conexao)
    conexao.close()


def inserirSaldo(conexao, idusuario):
    print("inserirsaldo")
    cursor = conexao.cursor()
    creditos = int(input("Quantos creditos deseja inserir? "))
    idusuario = int(input("Quantos creditos deseja inserir? "))

    sql = f"""INSERT INTO saldo(saldo_impressoes,userid) VALUES ({creditos},{idusuario})
    """
    cursor.execute(sql)
    conexao.commit
def consultarSaldo(conexao,idusuario):
    sql = f"""SELECT saldo_impressoes FROM saldo
            INNER JOIN usuario
            ON saldo.userid = usuario.userid
            WHERE usuario.userid = {idusuario} """
    cursor.execute(sql)
    saldo = cursor.fetchall()
    return saldo
def impressao(conexao,idusuario):
    saldo = consultarSaldo(conexao,idusuario)
    print(saldo[0][0])
    if(saldo[0][0] == "" or saldo[0][0] == 0):
        inserirSaldo(conexao, idusuario)
    elif(saldo[0][0] > 0):
        imprimir.impress()

def menuLogado(conexao, idusuario):
    conexao = sqlite3.connect('database.sqlite')
    cursor = conexao.cursor()
    menuLogin()
    while(True):
        op = int(input("Opção: "))
        if(op == 1):
           impressao(conexao,idusuario)
           menuLogin()
               
        if(op == 0):
            break
            sys.exit()
# Fecha a conexão que foi criada com banco de dados
    conexao.close()

