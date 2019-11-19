import sqlite3
import sys
import usuario
import cartao
import info
import saldo

conexao = sqlite3.connect('database.sqlite')
# sqlite3.connect('database.sqlite')
def pa(conexao,idusuario):
    cursor = conexao.cursor()
    sql = f"""SELECT primeiroacesso FROM usuario
            WHERE userid = '{idusuario}'
       """
    cursor.execute(sql)
    valor = cursor.fetchall()
    if(valor[0][0] == 1):
        finalizarCadastro(conexao,idusuario)


##Finalizar o cadastro
def finalizarCadastro(conexao,id):
    cursor = conexao.cursor()
    nome = input("Informe seu nome: ")
    sobrenome = input("Informe seu sobrenome: ")
    apelido = input("Há algum apelido ao qual deseja infomar? ")
    tel = input("Informe seu numero de celular: ")
    cpf = input("Informe seu cpf: ")

    sql = f"""INSERT INTO info(nome,sobrenome,cpf,telefone,apelido,userid) 
    VALUES("{nome}","{sobrenome}","{tel}","{cpf}","{apelido}",{id})
    """
    cursor.execute(sql)
    conexao.commit()
    sql = f"""UPDATE usuario 
    SET primeiroacesso = 0
    WHERE userid = {id}
    """
    cursor.execute(sql)
    conexao.commit()
    creditos = 9
    sql = f"INSERT INTO saldo(saldo_impressoes,userid) VALUES ({creditos},{id})"
    cursor.execute(sql)
    conexao.commit()
def criarTabelas(conexao):
    usuario.criar_tabela_usuario(conexao)
    saldo.criar_tabela_saldo(conexao)
    cartao.criar_tabela_card(conexao)
    info.criar_tabela_info(conexao)


conexao.close()
