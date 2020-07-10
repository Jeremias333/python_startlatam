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
		#continue