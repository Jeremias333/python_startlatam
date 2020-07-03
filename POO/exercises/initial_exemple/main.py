from pessoa import Pessoa
import os
os.system('cls' if os.name == 'nt' else 'clear')

pessoa1 = Pessoa("Jeremias", 20)

print(f"Nome da pessoa1: {pessoa1.nome}")
print(f"Idade da pessoa1: {pessoa1.idade}")

#área de testes
pessoa1.comer("Jaca")
pessoa1.comer("Jaca")
pessoa1.parar_comer()
pessoa1.comer("Arroz")
pessoa1.parar_comer()
pessoa1.falar("Java")
pessoa1.falar("Java")
pessoa1.parar_falar()
print(f"Estamos em: {Pessoa.ano_atual}")

print(f"{pessoa1.nome} nasceu em {pessoa1.get_ano_nasc()}")