import sys
from dao.dao_funcionario import DaoFuncionario
from models.funcionario import Funcionario
from utils.clear import clear

# funcionario = Funcionario("Jeremias", "Entregado", 1999.00)
# funcionario_edit = Funcionario("Jeremias", "Gerente Vendas", 3999.43)#objeto para usar em update

dao_funcionario = DaoFuncionario()

#dao_funcionario.add(funcionario)
# dao_funcionario.select_all()
# print(dao_funcionario.select_id(6))
#dao_funcionario.pass_sql("alter table funcionarios auto_increment = 1")
#print(dao_funcionario.select_name_id(4))
#dao_funcionario.delete_by_id(4)
#print(dao_funcionario.update_obj(funcionario_edit, 5))

def list_employee():
    clear()
    print("ID |      NOME      |      FUNÇÃO     |  SALÁRIO  ")
    for x in dao_funcionario.select_all():
        print(str(x).strip("()").replace(","," - "))

    input("\nAperte [ENTER] para voltar ao menu: ")
    clear()
    main_menu()

def add_employee():
	funcionario = Funcionario()
	clear()
	print("[NOVO FUNCIONÁRIO]")
	while(True):	
	    funcionario.set_name(input("Digite o nome do funcionário: "))
	    funcionario.set_function(input("Digite a função do funcionário: "))
	    funcionario.set_salary(input("Digite o salário do funcionário: "))
	    clear()
	    if(dao_funcionario.add(funcionario)==1):
	        return True
	    else:
	        return False

def delete_employee():
    funcionario = Funcionario()
    clear()
    print("[DELETAR FUNCIONÁRIO]")
    while(True):
        for x in dao_funcionario.select_name_id_all():
            print(str(x).strip('()').replace(",","-"))

        choice = int(input("Escolha um para ser excluído: "))
        if(dao_funcionario.delete_by_id(choice) == 1):
            clear()
            print("{Excluido com sucesso...}\n")
            break
        else:
            clear()
            print("{Opção inválida! Digite novamente...}\n")
            print("[DELETAR FUNCIONÁRIO]")
            
def update_employee():
    funcionario = Funcionario()
    clear()
    print("[ATUALIZAR FUNCIONÁRIO]")
    while(True):
        for x in dao_funcionario.select_name_id_all():
            print(str(x).strip('()').replace(",","-"))

        choice = int(input("Escolha um para ser atualizado: "))
        
        if(dao_funcionario.select_id_exist(choice) == 1):
            clear()
            print(f"[ATUALIZANDO: {dao_funcionario.select_id(choice)}]")

            funcionario.set_name(input("Digite o nome do funcionário: "))
            funcionario.set_function(input("Digite a função do funcionário: "))
            funcionario.set_salary(input("Digite o salário do funcionário: "))
            
            if(dao_funcionario.update(funcionario, choice) ==  1):
                clear()
                print("{Atualizdo com sucesso...}\n")
                break
        else:
            clear()
            print("{Opção inválida! Digite novamente...}\n")
            print("[ATUALIZAR FUNCIONÁRIO]")

def main_menu():
    clear()
    _pass = True
    while(_pass):
        print("     [EMPRESA CHARTOS]")
        choice = int(input("1 - Lista de funcionários \n2 - Adicionar funcionário"
        "\n3 - Atualizar um funcionário \n4 - Deletar um funcionário \n0 - Sair \n\nEscolha uma opção: "))

        if(choice == 1):
            list_employee()
        if(choice == 2):
            print("{Adicionado com sucesso...}\n") if add_employee() == True else print("Acorreu um erro por favor repita o processo...")
        if(choice == 3):
            update_employee()
        if(choice == 4):
            delete_employee()
        if(choice == 0):
            clear()
            print("Obrigado por utilizar nosso sistema!")
            sys.exit()
        clear()
main_menu()
