import sqlite3 as conector

# Abertura de conexão e aquisição de cursor
conexao = conector.connect("./DB_LITE.db")
conexao.execute("PRAGMA foreign_keys = on")
cursor = conexao.cursor()

# Definição dos comandos
comando = '''DELETE FROM Pessoa WHERE cpf= 46145809;'''
cursor.execute(comando)

# Efetivação do comando
conexao.commit()

# Fechamento das conexões
cursor.close()
conexao.close()
