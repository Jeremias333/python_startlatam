import sys
from dao.dao_funcionario import DaoFuncionario
from models.funcionario import Funcionario

funcionario = Funcionario("Jeremias", "Entregado", 1999.00)
funcionario_edit = Funcionario("Jeremias", "Gerente Vendas", 3999.43)#objeto para usar em update

dao_funcionario = DaoFuncionario()

#dao_funcionario.add(funcionario)
# dao_funcionario.select_all()
# print(dao_funcionario.select_id(6))
#dao_funcionario.pass_sql("alter table funcionarios auto_increment = 1")
#print(dao_funcionario.select_name_id(4))
#dao_funcionario.delete_by_id(4)
#print(dao_funcionario.update_obj(funcionario_edit, 5))

def list_employee():
	for x in dao_funcionario.select_all():
		print(str(x).strip("()"))

	input("\nAperte Enter para voltar ao menu")
	main_menu()

def add_employee():
	funcionario = Funcionario()
	print("[NOVO USUÁRIO]")
	while(True):	
		funcionario.set_name(input("Digite o nome do funcionário: "))
		funcionario.set_function(input("Digite a função do funcionário: "))
		funcionario.set_salary(input("Digite o salário do funcionário: "))

		if(dao_funcionario.add(funcionario)):
			print("Adicionado com sucesso!")
			break
		else:
			print("Acorreu um erro por favor repita o processo...")

def main_menu():
	_pass = True
	while(_pass):
		choice = int(input("1 - Lista de funcionários \n2 - Adicionar funcionário"
		 "\n3 - Atualizar um funcionário \n4 -  Deletar um funcionário \nEscolha um: "))

		if(choice == 1):
			list_employee()
		if(choice == 2):
			add_employee()
		if(choice == 3):
			update_employee()
		if(choice == 4):
			delete_employee()
		if(choice == 0):
			print("Obrigado por utilizar nosso sistema!")
			sys.exit()


main_menu()
