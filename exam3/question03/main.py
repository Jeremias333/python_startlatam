def print_retangle(lines=1, columns=1):
	if(columns > 20):
		columns = 20
		print("O valor máximo das colunas devem ser 20 por isso trocamos")
	if(lines > 20):
		lines = 20
		print("O valor máximo das linhas devem ser 20 por isso trocamos")
	if(columns < 1):
		columns = 1
		print("O valor minimo das colunas é 1 por isso trocamos")
	if(lines < 1):
		lines = 1
		print("O valor minimo das linhas é 1 por isso trocamos")

	retangle = ""
	columns_int = int(columns)
	lines_int = int(lines)

	if(lines == 1 and columns == 1):
		print("++")

	if(lines == 2 and columns == 2):
		print("++\n++")

	if(lines >= 3 and columns >= 3):
		for x in range(1, lines_int):
			if(x == 1):
				retangle += "+"+("-"*(columns_int-2))+"+\n"
			
			if(x > 1 and lines_int > 2):
				retangle += "|"+(" "*(columns_int-2))+"|\n"

			if(x == lines_int-1):
				retangle += "+"+("-"*(columns_int-2))+"+"
		print(retangle)

def main():
	lines = int(input("Digite a quantidade de linhas para desenhar o triangulo: "))
	columns = int(input("Digite a quantidade de colunas para desenhar o triangulo: "))
	print_retangle(lines, columns)

main()