def main():
    cont = int(input("Digite um valor e vamos contar ele vezes ele mesmo"))
    count(cont)

def count(cont):
    list_number = list()
    for x in range(1, cont+1):
        list_number.append(cont)

    print(list_number)


main()