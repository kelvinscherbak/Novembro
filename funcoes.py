# import sqlite3
# import sys
# import  simple_mail
# conexao = sqlite3.connect("banco.sqlite")

# sqlite3.connect("banco.sqlite")

# ### CRIA A TABELA USUARIO
# def criar_tabela_usuario(conexao):


#     cursor = conexao.cursor()

#     sql = """
#         CREATE TABLE IF NOT EXISTS user (
#             email TEXT NOT NULL,
#             nome TEXT NOT NULL,
#             login TEXT NOT NULL UNIQUE,
#             senha TEXT NOT NULL
            
#         );
#         """
#     cursor.execute(sql)




# ### Função de mostrar menu e opções ( Logar / Registrar / recuperar senha )
# def menu():
# #  Define que o usuario não esta logado para poder entrar no while do menu
#     logado = False
#     while(logado == False):
#         # print("\nSelecione a opção via teclado:\n1 - logar\n2 - Registrar\n3 - Recuperar senha\n\n0 Sair")
#         opcao = int(input(
#             """\nSelecione a opção via teclado:
#                 \n1 - logar
#                 \n2 - Registrar
#                 \n3 - Recuperar senha
#                 \n4 - Ver lista dos usuarios
#                 \n\n0 - Sair
#                 \n\n\n\t\t\tOpção:"""))
#         print(" ")
#         if(opcao == 0):
#             print("Você escolheu sair! Até mais :D")
#             break
#         elif(opcao == 1):
#             logar(conexao)
#         elif(opcao == 2):
#             inserir_user(conexao)
#         elif(opcao == 3):
#             simple_mail.recovery()
#         elif(opcao == 4):
#             imprimirBanco(conexao)





# ### Inserir registro na tabela (Nome / login / senha)
# def inserir_user(conexao):
#     cursor = conexao.cursor()
#     email = input("Informe o Email para cadastrar")
#     nome = input("Informe nome:\t")
#     login = input("Informe login:\t")
#     login = str.upper(login)
#     senha = input("Informe senha:\t ")


#     consulta = f"""SELECT login FROM user
#                 Where login = '{login}'
#                 """
#     cursor.execute(consulta)
#     cons = cursor.fetchall()
#     sql = f"""
#         INSERT INTO user VALUES(
#         '{email}',
#         '{nome}',
#         '{login}',
#         '{senha}'
#         )  """
#     if (cons == []):
#         cursor.execute(sql)
#         conexao.commit()
#     else: print("Este login já existe")





# ### Imprime a lista de Usuarios cadastrados
# def imprimirBanco(conexao):

#     cursor = conexao.cursor()
#     select = 'SELECT * FROM user'
#     cursor.execute(select)
#     lista = cursor.fetchall()
#     print("\tNome\t\t\t Login\t\t\t Senha\t\t\t")
#     for u in (lista):
#         print("\t{}\t\t\t {}\t\t\t {}\t\t\t".format(u[0],u[1],u[2]))




# ### Deleta a tabela
# def delTable():
#     cursor = conexao.cursor()
#     tabela = input("Informe o nome da tabela")
#     deletar = f"DROP TABLE '{tabela}'"
#     cursor.execute(deletar)
#     conexao.commit()



# ### Função de realizar o login

# def logar(conexao):
#         global logado
#         tentativas = 0
#         for i in range (3):
#             c=3
#             try:
#                 cursor = conexao.cursor()
#                 login = input("Informe o usuario:\t")
#                 login = str.upper(login)
#                 senha = input("Informe a senha:\t")
#                 consultar = f"""SELECT login, senha FROM usuario
#                             Where login = '{login}' AND senha = '{senha}'
#                             """
#                 cursor.execute(consultar)
#                 query = cursor.fetchall()
#                 l = query[0][0]
#                 s = query[0][1]
#                 if (l == login and s == senha):
#                     i == 3
#                     logado = True
#                     log = True
#                     break
#             except:
#                 print(f"Tente novamente! Voltando ao menu")
#                 break



# # def recovery():
# #     login = input(" Informe o nome de usuario")
# #     login = str.upper(login)
# #     cursor = conexao.cursor()



# def menulogado():
#     while(logado == True):
#         opcao = int(input("""
#         Selecione a opção desejada:
        
#         1 - Contatos 
#         2 - Produtos
#         3 - Configurações da Conta
        
        
#         0 - Deslogar 
        
        
#                         Opção: """))
#         if(opcao == 0):
#             logado = False
#         elif(opcao == 1):
#             print("Contatos")
#         elif(opcao == 2):
#             print("produtos")
#         elif(opcao == 3):
#             config()

   