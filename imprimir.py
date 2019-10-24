import tempfile
import win32api
import win32print
import os

def impress():
    global nome
    lista = os.listdir()
    # print(lista)
    for i in range(len(lista)):
        # numero = i + 1
        print(i,lista[i])
    selec = int(input("Qual numero do arquivo desejado:  "))

    nome = lista[selec]
    try:
        # nome = input("Nome do arquivo") 
        # ext = input("informe o tipo do arquivo pdf ou txt")
        # ext = "." + ext 
        # nome = nome + ext
        arq = open(nome)
        win32api.ShellExecute (
        0,
        "print",
        nome,
        
        '/d:"%s"' % win32print.GetDefaultPrinter (),
        ".",
        0
        )
    
    except:
        print("Erro na impressão, tente novamente")
