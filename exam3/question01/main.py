"""
nos arquivos podem ser adicionados infinitas palavras com infinitos tamanhos
sendo necessário apenas respeitar o critério de formatação por quebra de linha
e sem acentuação no final.
"""
import sys
import os
script_dir = os.path.dirname(__file__)#Path absoluto

rel_path = "../utils/"#setando o relativo
abs_utils = os.path.join(script_dir, rel_path)#unindo os dois

sys.path.append(abs_utils)#unir ao path do script

from clear import clear#irá importar o clear de utils
from rand import randInt, shuffle_letters #para evitar replicar códigos chamei meu arquivos utilitários

#retorna uma palavra aleatoria do arquivo lido.
def get_words():
	list_words = []
	with open("words.txt", 'r') as words:
		list_words = words.readlines()
	
	genarete_number = randInt(1, len(list_words))#gera um numero num determinado intervalo
	
	#retorna o nome dado em x numero
	word_final = list_words[genarete_number-1]
	NOME = word_final.replace("\n", "")
	return word_final

#Retorna a palavra com suas letras embaralhadas
def shuffle_word():
	filter_word = str(get_words()).replace("\n","")#pegará uma das palavras da lista
	list_letters = list()
	
	for letter in filter_word:#irá separá as letras
		list_letters.append(letter)

	shuffle_letters(list_letters)#embaralha a referencia da variavel 
	word_final = ''.join(list_letters)#junta as letras como se nada tivesse acontecido
	
	return word_final, filter_word 

def main():
	clear()#limpa tela
	WORD = "-"
	print("Bem vindo ao 'ACERTE O MONITOR' - STARTLATAM PY04\n")

	print("Iremos lhe mostrar um monitor embaralho e você deverá acertar quem é. \n[ENTER] para continuar")
	input()#pedirá confirmação

	#inicio do jogo
	clear()#limpa a tela
	trys = 6
	print(f"Suas tentativas restantes: {trys}")
	shuf, WORD = shuffle_word()#retorna palavra embaralhada e a original
	while(True):
		if(trys < 1):
			clear()
			print(f"Desculpe suas chances se esgotaram. GAME OVER. \nA resposta era: {WORD.upper()}")
			break
		else:
			clear()
			print(f"Suas tentativas restantes: {trys}")
			print(f"Seu monitor embaralho foi: {shuf}")
			choice = input("Digite o nome que acha ser do monitor: ")

			if(choice.lower() == WORD):
				clear()
				print(f"Perfeito, o nome do monitor realmente era: {WORD.upper()}")
				break	
			else:
				trys -= 1
main()