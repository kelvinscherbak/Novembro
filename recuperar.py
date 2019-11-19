import smtplib
import sqlite3
import random
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
def recuperar(conexao):
    cursor = conexao.cursor()
    email = input("Informe o Email")

    
    consulta = f"""SELECT email FROM usuario
                WHERE email = '{email}'
                
                """
    cursor.execute(consulta)
    cons = cursor.fetchall()
    email = cons[0][0]
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
        return codigo
    except Exception as Erro:
        print("\nErro ao enviar email")
        print(Erro)
def recuperacao(conexao):
    codigo = None
    cursor = conexao.cursor()
    
    code = recuperar(conexao)
    if(code == codigo):Hello wo
        nsenha = str(input("Digite a senha:\t"))
        csenha = str(input("Digite a senha novamente:\t"))
        if(nsenha == csenha):
            sql = f"""UPDATE usuario
            SET senha = '{nsenha}'
            WHERE email = '{email}'
            """
    conexao.close()
