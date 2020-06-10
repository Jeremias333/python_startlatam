name1 = input("Digite o nome do aluno: ") 
exam1 = input(f"Digite a primeira nota de {name1}: ")
exam1 = float(exam1.replace(",","."))
exam2 = input(f"Digite a segunda nota de {name1}: ")
exam2 = float(exam2.replace(",",".")) 
exam3 = input(f"Digite a terceira nota de {name1}: ")
exam3 = float(exam3.replace(",","."))

mean = ((exam1+exam2+exam3)/3)

print(f"Média: {mean}")

if mean >= 7:
    print(f"{name1} aprovado!")
else:
    print(f"{name1} reprovado!")