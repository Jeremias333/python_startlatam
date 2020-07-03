def main():
    print("Pode ser usado como a principal")

main()

#por padrão ela retorna none caso não aja valor no retorno.

def soma(*args):
    return sum(*args)


print(soma([10, 11, 20, 14, 87]))