import math

delta = 0
_pass = 0
val_a = 0
val_b = 0
val_c = 0
delta = 0
root1 = 0
root2 = 0

while(_pass == 0):
    print("Vamos calcular Delta. Delta = b²-4.a.c\n")
    val_a = int(input("Digite o valor para A"))

    if(val_a == 0):
        print("A deve ser diferente de 0")
    else:
        val_b = int(input("Digite o valor B"))
        val_c = int(input("Digite o valor C"))
        delta = (((val_b)**2) -4 * (val_a) * (val_c)) 
        if(delta < 0):
            print(f"O Delta foi negativo: {delta}, gerou nenhuma raiz")
            _pass = 1
        elif(delta == 0):
            print(f"Delta foi igual {delta} a raiz é: ")
            root1 = (-1)*(val_b)/(2*val_a)
            print("Raíz unica de: ",root1)
            _pass = 1
        else:
            print(f"Delta foi positivo: {delta} e gerou duas raizes: ")
            root1 = (((-1)*val_b) + math.sqrt(delta))/2*val_a
            root2 = (((-1)*val_b) - math.sqrt(delta))/2*val_a

            print("Raíz I de: ",root1)
            print("Raíz II de: ",root2)
            _pass = 1
print("Fim do programa")
