import sys

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