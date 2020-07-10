import mysql.connector
from os import path
import sys
sys.path.append(path.join(path.dirname(__file__), '..'))#diretório relativo acessando pastas top-level

from dao.connect_factory import ConnectFactory
from models.funcionario import Funcionario

connect_factory = ConnectFactory()#instanciando.

cursor = connect_factory.get_cursor()#conexão pertence agora a esta variável.
con = connect_factory.get_connection()#para fazer commits finais no banco.

class DaoFuncionario:
	def __init__(self):
		self.sql = ""

	def add(self, funcionario:Funcionario):
		self.sql = "insert into funcionarios (nome, funcao, salario) values (%s, %s, %s)"
		val = (funcionario.name, funcionario.function, funcionario.salary)
		cursor.execute(self.sql, val)
		con.commit()
		return cursor.rowcount
		
	def delete_by_id(self, id):
		self.sql = "delete from funcionarios where id = %s"
		val = (id, )
		cursor.execute(self.sql, val)
		con.commit()
		return cursor.rowcount

	def update(self, funcionario:Funcionario, id):
		self.sql = "update funcionarios set nome = %s, funcao = %s, salario = %s  where id = %s"
		val = (funcionario.name, funcionario.function, funcionario.salary, id)
		cursor.execute(self.sql, val)
		con.commit()
		return cursor.rowcount

	def select_all(self):
		self.sql = "select * from funcionarios"
		cursor.execute(self.sql)
		result = cursor.fetchall()#passará todas linhas retornadas para result
		return result

	def select_id(self, id):
		self.sql = "select * from funcionarios where id = %s"
		val = (id, )
		cursor.execute(self.sql, val)
		result = cursor.fetchone()
		return result

	def select_name_id_one(self, id):
		self.sql = "select id, nome from funcionarios where id = %s"
		val = (id, )
		cursor.execute(self.sql, val)
		result = cursor.fetchone()
		return result

	def select_name_id_all(self):
		self.sql = "select id, nome from funcionarios"
		cursor.execute(self.sql, )
		result = cursor.fetchall()
		return result

	def select_id_exist(self, id):
		self.sql = "select id from funcionarios where id = %s"
		val = (id, )
		cursor.execute(self.sql, val)
		result = cursor.fetchone()
		return cursor.rowcount

	def pass_sql(self, sql):
		cursor.execute(sql, )
		con.commit()