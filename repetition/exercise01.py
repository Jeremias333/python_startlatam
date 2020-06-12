question = False
notation = 0

while(question != True):
	notation = int(input("Digite um número de 0 à 10: "))
	if(notation < 0 or notation > 10):
		print("O número deve ser entre 0 e 10!")
	else:
		question = True
else:
	print(f"Saiu do loop por digitar: {notation}")