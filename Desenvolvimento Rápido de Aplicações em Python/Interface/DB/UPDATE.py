import psycopg2
conn = psycopg2.connect(database="postgres", user="postgres",
                        password="admin", host="127.0.0.1", port="5432")
print("Conexão com o Banco de Dados aberta com sucesso!")
cur = conn.cursor()
print("Consulta antes da atualização")
cur.execute("""select * from public."agenda" where "id" = 1""")
registro = cur.fetchone()
print(registro)
# Atualização de um único registro
cur.execute(
    """Update public."agenda" set "telefone" = '02188888888' where "id" = 1""")
conn.commit()
print("Registro Atualizado com sucesso! ")
cur = conn.cursor()
print("Consulta depois da atualização")
cur.execute("""select * from public."agenda" where "id" = 1""")
registro = cur.fetchone()
print(registro)
conn.commit()
print("Seleção realizada com sucesso!")
conn.close()
