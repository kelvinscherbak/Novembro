import sqlite3
import sys
conexao = sqlite3.connect('database.sqlite')
# sqlite3.connect('database.sqlite')

cursor = conexao.cursor()
login = " "
def criar_tabela_usuario(conexao):
    # conexao = sqlite3.connect("database.sqlite")
    cursor = conexao.cursor()
    sql = """
        CREATE TABLE IF NOT EXISTS usuario (
            userid INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL UNIQUE,
            login TEXT NOT NULL UNIQUE,
            senha  TEXT NOT NULL,
            primeiroacesso BOOLEAN DEFAULT 1
        )
    """
    cursor.execute(sql)

def criar_tabela_card(conexao):
    cursor = conexao.cursor()
    sql = """
        CREATE TABLE IF NOT EXISTS card(
            cardid INTEGER PRIMARY KEY AUTOINCREMENT,
            n_card TEXT NOT NULL,
            n_seg TEXT NOT NULL,
            cpf TEXT NOT NULL,
            validade TEXT NOT NULL

        )
    
    
    """
    cursor.execute(sql)  
def criar_tabela_saldo(conexao):
    cursor = conexao.cursor()
    sql = """
        CREATE TABLE IF NOT EXISTS saldo(
            saldoid INTEGER PRIMARY KEY AUTOINCREMENT,
            saldo_impressoes INTEGER NOT NULL

        )
    
    
    """
    cursor.execute(sql)

def criar_tabela_info(conexao):
    cursor = conexao.cursor()
    sql = """
        CREATE TABLE IF NOT EXISTS info(
            infoid INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            telefone TEXT NOT NULL,
            apelido TEXT,
            endereco TEXT NOT NULL,
            n_endereco TEXT NOT NULL,
            complemento TEXT,
            userid INTEGER,
            cardid INTEGER,
            saldoid INTEGER,
            FOREIGN KEY (userid) REFERENCES usuario(userid),
            FOREIGN KEY (cardid) REFERENCES card(cardid),
            FOREIGN KEY (saldoid) REFERENCES saldo(saldoid)
        )
    
    
    """
    cursor.execute(sql)

def registrar(conexao):
    cursor = conexao.cursor()
    email = input("Informe o Email para cadastrar:\t")
    while("@" not in email):
        print("Email invalido, email inserido: ",email,"Ex: exemplo@email.com\n")
        email = input("informe o Email correto: ")
    login = input("Informe login:\t")
    login = str.upper(login)
    senha = input("Informe senha:\t ")
    while(senha != input("Confirme sua senha: ")):
        print("As senhas não conferem! Tente novamente")

    consulta = f"""SELECT login FROM usuario
                Where login = '{login}'
                """
    cursor.execute(consulta)
    cons = cursor.fetchall()
    sql = f"""
        INSERT INTO usuario ('email','login',senha) VALUES(
        '{email}',
        '{login}',
        '{senha}'
        )  """
    if (cons == []):
        cursor.execute(sql)
        conexao.commit()
        print("Cadastrado com sucesso!")
    else:
        print("Este login já existe")


def recuperar():
    import smtplib
    import sqlite3
    import random
    import sys
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders

    global codigo

    conexao = sqlite3.connect("database.sqlite")
    sqlite3.connect("database.sqlite")
    cursor = conexao.cursor()
    consulta = f"""SELECT email FROM usuario
                Where email = '{input("Informe o Email")}'
                
                """
    cursor.execute(consulta)
    cons = cursor.fetchall()
    email = cons[0][0]
    nome = cons[0][1]
    try:
        fromaddr = "kecosta1@hotmail.com"
        toaddr = email
        msg = MIMEMultipart()

        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "Recuperação de senha do sistema Kevinho"
        codigo = random.randint(1000, 9999)
        body = f"\nOlá Tudo bem?! \n\n\n\t O codigo de recuperação da sua conta é: {codigo}"

        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('smtp.outlook.com', 587)
        server.starttls()
        server.login(fromaddr, "kelvin12345")
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()
        print('\nEmail enviado com sucesso!')
    except Exception as Erro:
        print("\nErro ao enviar email")
        print(Erro)
    if(code == codigo):
        nsenha = str(input("Digite a senha:\t"))
        csenha = str(input("Digite a senha novamente:\t"))
        if(nsenha == csenha):
            sql = f"""UPDATE usuario
            SET senha = '{nsenha}'
            WHERE email = '{email}'
            """

# sql = """ SELECT * FROM usuario """
# cursor.execute(sql)
# lista = cursor.fetchall()
# print("\tid\t\t\t Nome\t\t\t Login\t\t\tSenha")
# for u in (lista):
#         print("\t{}\t\t\t {}\t\t\t {}\t\t\t".format(u[0], u[1], u[2], u[3]))
def logar(conexao):
    global login
    c=0
    while(True):
        tentativas = 0
        for i in range (3):
            try:
                cursor = conexao.cursor()
                login = input("Informe o usuario:\t")
                login = str.upper(login)
                senha = input("Informe a senha:\t")
                consultar = f"""SELECT login, senha FROM usuario
                            Where login = '{login}' AND senha = '{senha}'
                            """
                cursor.execute(consultar)
                query = cursor.fetchall()
                l = query[0][0]
                s = query[0][1]
                if (l == login and s == senha):
                    i == 3
                    print("Ok")
                    sql = f"""SELECT userid FROM usuario
                            WHERE login = '{login}'
                    
                    """
                    cursor.execute(sql)
                    idusuario = cursor.fetchall()
                    return idusuario[0][0]
                else:
                    return False
            except:
                print(f"Tente novamente!")
                c = c + 1
                if(c == 3):
                    print("Limite de tentativas excedidas... Saindo")
                    sys.exit()
                    break
    return logado

def pa(conexao):
    cursor = conexao.cursor()
    global login
    sql = f"""SELECT primeiroacesso,login FROM usuario
            WHERE login = '{login}'
       """
    cursor.execute(sql)
    valor = cursor.fetchall()
    aux = valor[0][0]
    print(aux)
    return aux


##Finalizar o cadastro
def finalizarCadastro(conexao):
    cursor = conexao.cursor()
    nome = input("Informe seu nome completo ")
    tel = input("Informe seu numero de celular ")
    apelido = input("Informe seu apelido ")
    endereco = input("Informe seu Logradouro ")
    num = input("Informe numero da sua casa")
    comp = input("Qual seria o complemento")

    sql = f"""INSERT INTO info(nome,telefone,apelido,endereco,n_endereco,complemento) 
    VALUES("{nome}","{tel}",{apelido},"{endereco}","{num}",{comp})
    """
    cursor.execute(sql)
    conexao.commit()


# criar_tabela_usuario(conexao)
# criar_tabela_saldo(conexao)
# criar_tabela_card(conexao)
# criar_tabela_info(conexao)

conexao.close()

