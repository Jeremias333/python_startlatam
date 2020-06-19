name = input("Digite seu nome: ")

for x in range(len(name)+1):
    print(f"{name[:x].upper()}")
    