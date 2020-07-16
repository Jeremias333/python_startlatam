def call_reverse(num):
	str_num = str(num)
	return str_num[::-1]


def main():
	num = int(input("Digite um número para ver ele reversamente: "))
	print(f"Seu número original: num \nSeu número reverso: {call_reverse(num)}")

main()