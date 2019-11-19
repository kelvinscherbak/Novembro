import tempfile
import win32api
import win32print
import os
import sys
from PyPDF2 import PdfFileReader
def numpage(arquivo):
    for path in arquivo:
        pdf_reader = PdfFileReader(path)
    return pdf_reader.getNumPages()

def impress():
    global nome
    lista = os.listdir()
    # print(lista)
    for i in range(len(lista)):
        # numero = i + 1
        print(i,lista[i])
    selec = input("Qual numero do arquivo desejado:  ")
    if(selec == ""):
        sys.exit()
    selec = int(selec)
    nome = lista[selec]
    arquivo = [nome]
    numero = numpage(arquivo)
    r = input(f"Deseja imprimir um total de {numero} páginas?")
    r = str.upper(r)
    if(r == "S"):
        try:
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
        return numero

