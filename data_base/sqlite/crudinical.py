import sqlite3
from user import User

con = sqlite3.connect("banco_dados")#cria a base/banco de dados caso não exista.
cursor = con.cursor()

def initial():
	cursor.execute("""
		CREATE TABLE users(
			id INTEGER(10) PRIMARY KEY,
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

def insert_one(user:User):
	cursor.execute(f"insert into users(name, age) values ('{user.get_name()}','{user.get_age()}')")

def delete_table():
	cursor.execute("""drop table users""")
	print("Tabela deletada")