user = ""
password = ""
_pass = False


while(_pass == False):

	user = input("Digite o nome de usuário: ")
	password = input("Digite o sua senha: ")

	if(user == password):
		print("O usuário não pode ser igual a senha, repita o processo")		
	else:
		_pass = True
else:	
	print("Logado com sucesso")