import os
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in

rel_utils = "utils/"
abs_utils = os.path.join(script_dir, rel_utils)

import sys
sys.path.append(abs_utils)

from people import People
from clear import clear

rel_path = "data/peoples.txt"
abs_file_path = os.path.join(script_dir, rel_path)



def main():
    main_menu()

def main_menu():
    clear()
    _pass = True

    while(_pass):
        print("\n[MENU PRINCIPAL]\n0 - Sair\n1 - Criar nova pessoa\n2 - Lista de Pessoas")
        var = int(input("\nDigite uma opção: "))
        clear()
        if(var == 1):
            create_menu()
        if(var == 2):
            list_menu()
        if(var == 0):
            sys.exit()#fecha o programa caso digitado 0

def create_menu():
    _pass = True
    cont = 0
    name = ""
    age = 0
    weight = 0.0
    height = 0.0

    while(_pass):
        print("[CRIANDO NOVA PESSOA]")
        cont += 1
        if(cont == 1):
           name = input("Digite o nome da nova pessoa: ")           
        if(cont == 2):
            age = int(input("Digite a idade da nova pessoa: "))
        if(cont == 3):
            weight = float(input("Digite o peso da nova pessoa: "))
        if(cont == 4):
            height = float(input("Digite a altura da nova pessoa: "))
        clear()
        if(cont == 5):
            write_arch(name, age, weight, height)#chama método de escrita
            break
        
def list_menu():
    _pass = True
    all_people = ""

    archive = open(abs_file_path, 'r')
    while(_pass):
        print("[LISTA DAS PESSOAS]")
        print("0 - Voltar para Menu Inicial")
        for line in archive:
            str_temp = line[0:line.find("#")]#busca o texto do primeiro elemento percorrendo do inicio até o primeiro #
            all_people += str_temp+"\n"
        print(all_people)
        choice = input("Escolha um para ver detalhes: ")
        if(choice == "0"):
            clear()
            break
        else:
            people_menu(choice)
    archive.close()

def people_menu(choice):
    clear()
    print("[PESSOA DETALHADA]")
    val = list()
    archive = open(abs_file_path, 'r')#abre a lista para poder achar um único
    for line in archive:#percorre a lista e retorna um único
        str_temp = line[0]
        if(str_temp == choice):
            final_string = line.replace("#", "\n")#troco # por \n
            val = (final_string.split("\n"))#split por \n lançando o array na list val.
            #sequencias de prints formatados
            print(f"ID: {val[0][0]}")
            print(f"Nome: {val[0][3:len(val[0])]}")#pega o elemento do 3 até o fim do primeiro elemento.
            print(f"Idade: {val[1]}")
            print(f"Peso: {val[2]}kg")
            print(f"Tamanho: {val[3]}cm\n")
            input("Digite Enter para voltar para a lista de pessoas")
            clear()
    archive.close()
    
"""
Na hora de escrever, por toda pessoa em uma linha só e demarcar com - para split
"""
def write_arch(name, age, weight, height):
    last = 0
    people = People(name, int(age), float(weight), float(height))
    print(last_id())
    last += int(last_id())
    final_str = get_all()
    final_str += f"{(last)+1} - {people.get_name()}#{people.get_age()}#{people.get_weight():.2f}#{people.get_height():.2f}\n"
    with open(abs_file_path, 'w') as archive:
        archive.write(final_str)

    clear()
    print("Pessoa adicionada com sucesso")

def last_id():
    if(os.stat(abs_file_path).st_size == 0):
        return 0
    else:  
        with open(abs_file_path, 'r') as archive:
            last_id = archive.readlines()[-1]
            return last_id[0]

def get_all():
    olds = ""
    with open(abs_file_path, 'r') as archive:
        for line in archive:
            olds += line
    return olds       
main()