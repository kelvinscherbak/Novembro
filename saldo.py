def criar_tabela_saldo(conexao):
    cursor = conexao.cursor()
    sql = """
        CREATE TABLE IF NOT EXISTS saldo(
            saldoid INTEGER PRIMARY KEY AUTOINCREMENT,
            saldo_impressoes INTEGER DEFAULT 0,
            userid INTEGER NOT NULL,
            FOREIGN KEY (userid) REFERENCES usuario(userid)
        )
    
    
    """
    cursor.execute(sql)


