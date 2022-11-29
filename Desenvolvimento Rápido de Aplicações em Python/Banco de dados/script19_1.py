import sqlite3 as conector
from modelo import Veiculo

# Abertura de conexão e aquisição de cursor
conexao = conector.connect("./DB_LITE.db")
cursor = conexao.cursor()

# Definição dos comandos
comando = '''SELECT * FROM Veiculo;'''
cursor.execute(comando)

# Recuperação dos registros
reg_veiculos = cursor.fetchall()
for reg_veiculo in reg_veiculos:
    veiculo = Veiculo(*reg_veiculo)
    print("Placa:", veiculo.placa, ", Marca:", veiculo.marca)

# Fechamento das conexões
cursor.close()
conexao.close()
