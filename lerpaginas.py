
from PyPDF2 import PdfFileReader
def numpage(arquivo):
    for path in arquivo:
        pdf_reader = PdfFileReader(path)
    return pdf_reader.getNumPages()
    

arquivo = ["Seminário Materiais.pdf"]
numero = numpage(arquivo)
print(numero)
# if __name__ == '__main__':
#     paths = ['Seminário Materiais.pdf', 'merged.pdf']
#     merge_pdfs(paths, output='merged2.pdf')
