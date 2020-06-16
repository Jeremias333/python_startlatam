factor = 0
result = 0

print("Vamos exibir uma tabuada? \n\n\n")

factor = int(input("Quer que eu exiba a tabuada de quanto?"))

for index in range(11):
    result = factor*index
    print(factor,"X",index,"=",result) 

print("\nA ordem dos fator não altera o resultado...")