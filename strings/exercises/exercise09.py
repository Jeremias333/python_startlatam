cpf_typed = input("Digite seu CPF sem acentuações: ")

#base - xxx.xxx.xxx-xx
cpf_formatted = ["x","x","x",".","x","x","x",".","x","x","x","-","x","x",]#list para formatação

tree = 0#variavel de controle para marcar o 3 dígitos e depois o "."
jump = 0#variavel de controle do cpf não formatado, ele precisa ficar atras do array do loop que inclui "." e "-"
for x in range(0, 14):
    if(x == 12 or x == 14):#para tratar os dois ultimos dígitos
        jump -= 1

    tree += 1#vai receber toda vez que o loop fizer reinicio
    
    cpf_formatted[x] = cpf_typed[x-jump]#a list do cpf formatado recebe o valor numerico inserido pelo usuário
    
    if(tree==4):#a cada 3 digitos é adicionado o . na 4 casa do array
        jump += 1
        cpf_formatted[x] = "."
        tree = 0
    
    if(x == 11):#depois de bater 12 será posto um "-" para separar os dois ultimos dígitos
        jump += 1
        tree = 0
        cpf_formatted[x] = "-"
    
print(cpf_formatted)#print da list completa
print("".join(cpf_formatted))#cpf formatado e em string