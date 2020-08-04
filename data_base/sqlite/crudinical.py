import sqlite3

con = sqlite3.connect("banco_dados")#cria a base/banco de dados caso não exista.
cursor = con.cursor()

def initial():
	cursor.execute("""
		CREATE TABLE users(
			id INTEGER(10) NOT NULL PRIMARY KEY,
			name TEXT NOT NULL,
			age INTEGER NOT NULL
		);
	""")
	print("Tabela criada")

	con.close()

def select_all():
	cursor.execute("""select * from users""")

	for linha in cursor.fetchall():
		print(linha)

	con.close()