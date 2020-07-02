'''
Onde o método se inicia.
'''
def main():
    cont = 1
    while(cont == 1):
        type_num(int(input("Digite um número: ")))

'''
Irá retornar P para números positivos passados no parametro e N caso seja
zero ou negativo.
'''
def type_num(num):
    if(num < 1):
        print("N")
    else:
        print("P")

main()#inicio do programa.