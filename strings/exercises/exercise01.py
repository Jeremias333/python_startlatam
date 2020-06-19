text1 = input("Digite um texto: ")
text2 = input("Digite outro texto: ")

print(f"A Primeira String tem: {len(text1)}")
print(f"A Segunda String tem: {len(text2)}")

if(len(text1) > len(text2)):
    print("A primeira String é maior que a segunda.")
elif(len(text2) > len(text1)):
    print("A segunda String é maior que a primeira.")    
else:
    print("A primeira String é do mesmo tamanho que a segunda.")

if(text1 == text2):
    print("O conteúdo da primeira String é igual o da segunda!")
else:
    print("O conteúdo das duas Strings são diferentes!")