import sqlite3
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