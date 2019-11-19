import funcoesBanco
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
    finalizar = input("Deseja completar seu cadastro agora? Sim ou Não")
    finalizar = str.upper(finalizar)
    if(finalizar == "S" or finalizar == "SIM"):
        sql = f"""SELECT userid FROM usuario
                            WHERE login = '{login}'
                    
                    """
        cursor.execute(sql)
        idusuario = cursor.fetchall()
        aux = idusuario[0][0]
        funcoesBanco.finalizarCadastro(conexao,aux)
        
