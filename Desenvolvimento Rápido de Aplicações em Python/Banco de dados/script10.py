import sqlite3 as conector
from modelo import Pessoa

# Abertura de conexão e aquisição de cursor
conexao = conector.connect("./DB_LITE.db")
cursor = conexao.cursor()

# Criação de um objeto do tipo Pessoa
pessoa = Pessoa(46145809, 'FELIPE', '1990-01-31', False,)

# Definição de um comando com query parameter
comando = '''INSERT INTO Pessoa (cpf, nome, nascimento, oculos) VALUES (?, ?, ?, ?);'''
cursor.execute(comando, (pessoa.cpf, pessoa.nome, pessoa.data_nascimento, pessoa.usa_oculos))

# Efetivação do comando
conexao.commit()

# Fechamento das conexões
cursor.close()
conexao.close()
