import psycopg2
conn = psycopg2.connect(database="postgres", user="postgres",
                        password="admin", host="127.0.0.1", port="5432")
print("Conexão com o Banco de Dados aberta com sucesso!")
cur = conn.cursor()
cur.execute("""select * from public."agenda" where "id" = 1""")
registro = cur.fetchall()
print(registro)
conn.commit()
print("Seleção realizada com sucesso!")
conn.close()
