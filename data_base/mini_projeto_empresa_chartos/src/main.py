from dao.dao_funcionario import DaoFuncionario
from models.funcionario import Funcionario

funcionario = Funcionario("Jeremias", "Entregador", 1999.00)
dao_funcionario = DaoFuncionario()

dao_funcionario.add(funcionario)