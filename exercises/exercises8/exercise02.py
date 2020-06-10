imc = 0
weight = 0
height = 0

print("Vamos calcular seu IMC(índice de massa corporal)")
height = input("\nInforme sua altura: ")
height = float(height.replace(",","."))

weight = input("\nInforme seu peso: ")
weight = float(weight.replace(",","."))

imc = ((weight)/(height**2))
imc = round(imc)
print("...")

print(f"O seu índice de massa corporal é: {imc:.2f}")
print(f"\n\nFormula: {imc} = {weight} / ({height} * {height})")