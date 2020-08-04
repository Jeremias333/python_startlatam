import sqlite3
from user import User

user = User()

con = sqlite3.connect("banco_dados")#cria a base/banco de dados caso não exista.
cursor = con.cursor()#abrindo conexao

def initial():#criando a tabela
	cursor.execute("""
		CREATE TABLE users(
			id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
			name TEXT NOT NULL,
			age INTEGER NOT NULL
		);
	""")
	print("Tabela criada")

	con.close()

def select_all():#pegando todos dados de uma vez
	cursor.execute("""SELECT * FROM users""")

	for linha in cursor.fetchall():
		print(linha)

def insert_one(user:User):
	cursor.execute(f"INSERT INTO users(name, age) VALUES ('{user.get_name()}','{user.get_age()}')")
	con.commit()

def delete_table():
	#Deletando tabela
	cursor.execute("""DROP TABLE users""")
	print("Tabela deletada")

def edit_one(id):
	cursor.execute(f"SELECT * FROM users WHERE id = {id}")
	lista_obj = cursor.fetchone()

	user.set_name(lista_obj[1])
	user.set_age(lista_obj[2])

	#Mostrando dados antigos e subistituindo pelos novos.
	print(f"Nome antigo: {user.get_name()}")
	user.set_name(input("Digite um novo nome: "))
	print(f"Idade antiga: {user.get_age()}")
	user.set_age(int(input("Digite um nova idade: ")))

	#fazendo update
	cursor.execute(f"UPDATE users SET name = '{user.get_name()}', age = '{user.get_age()}' WHERE id = '{id}'")

	con.commit()

def delete_one(id):
	cursor.execute("""DELETE FROM users WHERE id = ?""", (id,))
	con.commit()