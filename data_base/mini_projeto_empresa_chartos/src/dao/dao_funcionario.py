from os import path
import sys
sys.path.append(path.join(path.dirname(__file__), '..'))#diretório relativo acessando pastas top-level

from dao.connect_factory import ConnectFactory
from models.funcionario import Funcionario

connect = ConnectFactory()
con = connect.get_connection()#conexão pertence agora a esta variável.

class DaoFuncionario:
    def __init__(self):
        pass
    
    def add(self, funcionario:Funcionario):
        con.execute(f"insert into funcionarios (nome, funcao, salario) values ({funcionario.name}, {funcionario.function}, {funcionario.salary})")
        #continue