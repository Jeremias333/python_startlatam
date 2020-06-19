name = input("Digite seu nome: ")

for x in range(len(name)):
    print(f"{name[:-x].upper()}")