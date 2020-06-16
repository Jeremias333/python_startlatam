side1 = 0
side2 = 0
side3 = 0

side1 = float(input("Para sabermos qual o tipo de Triangulo precisamos saber seu primeiro lado em cm: "))
side2 = float(input("Certo, agora o segundo lado: "))
side3 = float(input("Precisamos também do terceiro número: "))

print("l1:",side1,"cm")
print("l2:",side2,"cm")
print("l3:",side3,"cm")

'''
testando se forma um triangulo:
|l1-l2| < l3 < l1+l2

'''

cond1 = (side1-side2)*-1
cond2 = side3
cond3 = side1+side2

if(cond1 < cond2 and cond2 < cond3):
    print("Isso é um triângulo! Parabéns passou os dados certinhos.")
    
    if(side1 == side2 and side3 == side1):
        print("O triangulo criado por você é EQUILATERO")
    elif(side1 == side3 and side2 != side1):
        print("O triangulo criado por você é ISOCELES")
    else:
        print("O triagulo criado por você é ESCALENO")
else:
    print("Os valores passados não formam um triângulo...")