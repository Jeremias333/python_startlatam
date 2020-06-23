num = int(input("Digite um número menor 1000: "))

hundred = num//100%10
dicker = num//10%10
unities = num//1%10

print(f"Existem {hundred} centenas, {dicker} dezenas e {unities} unidades")