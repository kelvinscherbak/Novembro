import sqlite3
import sys
import login
import funcoesBanco
# Abre uma conexão como banco de dados
conexao = sqlite3.connect('database.sqlite')

login.selOpcao(conexao)

# Fecha a conexão que foi criada com banco de dados
conexao.close