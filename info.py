import sqlite3
def criar_tabela_info(conexao):
    cursor = conexao.cursor()
    sql = """
        CREATE TABLE IF NOT EXISTS info(
            infoid INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            sobrenome TEXT NOT NULL,
            cpf TEXT NOT NULL,
            telefone TEXT NOT NULL,
            apelido TEXT,
            userid INTEGER,
            cardid INTEGER,
            saldoid INTEGER,
            FOREIGN KEY (userid) REFERENCES usuario(userid),
            FOREIGN KEY (cardid) REFERENCES card(cardid),
            FOREIGN KEY (saldoid) REFERENCES saldo(saldoid)
        )
    
    
    """
    cursor.execute(sql)
