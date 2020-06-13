#nome maior que 3 caracteres.
#idade 0-150
#salario > 0
#sexo f ou m
#estado_civil s c v d

name = ""
idade = 0
sales = 0.0
gender = ""
marital_status = ""
_pass = False

print("Para se cadastrar é necessário preencher umas informações!\n\n")
while(not _pass): 
    if(len(name) < 3):
        name = input("Digite o nome [Dica: precisa ser 3 ou mais letras]: ")
    else:
        if(idade > 0 and idade <= 150):
            idade = input("Digite a idade [Dica: precisa ser entre 1 e 150]: ")
        else:
            if(sales <= 1.0):
                sales = float(input("Digite o salário [Dica: precisa ser maior que 1.0 o valor]: "))
            else:
                if (gender != "m" and gender != "f"):
                    gender = (input("Digite o sexo [Dica: precisa ser 'm' ou 'f']: ")).lower()
                    gender = gender[:1]
                else:
                    if(marital_status != 's' and marital_status != 'c' and marital_status != 'v' and marital_status != 'd'):
                        marital_status = (input("Digite o salário [Dica: precisa ser 's', 'c', 'v' ou 'd']: ")).lower()
                        marital_status = marital_status[:1]
                    else:
                        print("Tudo preechido corretamente!")
                        _pass = True
else:
    print("Cadastrado com sucesso.")