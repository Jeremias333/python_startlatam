import sys
sys.path.append("C:/utils/")

import rand

def start():
	dice1 = 0
	dice2 = 0

	_playing = True
	plays = 0
	point = 1

	play(plays, point, dice1, dice2, _playing)


def play(plays, point, dice1, dice2, _playing):
	while(_playing):
		if(plays == 0):
			plays = 1

		input("Pressione enter para jogar os dados... ")

		dice1 = rand.randInt(1,6)
		dice2 = rand.randInt(1,6)

		print(f"Resultado do 1º dado: {dice1}")
		print(f"Resultado do 2º dado: {dice2}")

		sum_dice = dice2+dice1
		print(f"\nSoma dos dados: {sum_dice}")

		if(plays == 1):
			#caso tenha tirado 2, 3 ou 12 na primeira vez irá tratar essa condição
			if(sum_dice == 2 or sum_dice == 3 or sum_dice == 12):
				print("\nCRAPS!!! Você perdeu!!! ")
				sys.exit()
			
			#ponto
			if(sum_dice == 4 or sum_dice == 5 or sum_dice == 6 or 
								sum_dice == 8 or sum_dice == 9 or
								sum_dice == 10):
				print("\nParabéns!! Fez um ponto. Continue jogando, caso venha tirar um 7 depois irá perder!")
				point = 1
				plays = 2

			
			#ganhou
			if(sum_dice == 7 or sum_dice == 11):
				print("\nNatural, você venceu")
				sys.exit()

		elif(plays == 2):
			#ponto
			if(sum_dice == 4 or sum_dice == 5 or sum_dice == 6 or 
								sum_dice == 8 or sum_dice == 9 or 
								sum_dice == 10 or sum_dice == 11):
				print("\nParabéns!! Você venceu o jogo.")
				sys.exit()
			if(sum_dice == 7):
				print("\nInfelizmente o número deu 7 depois de ter 1 ponto. FIM DE JOGO")
				sys.exit()
start()