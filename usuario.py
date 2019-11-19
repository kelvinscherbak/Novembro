import sqlite3

def criar_tabela_usuario(conexao):
    conexao = sqlite3.connect('database.sqlite')
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
    conexao.close()