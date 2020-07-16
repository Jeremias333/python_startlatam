import random

def printRand(init, final):
	print(random.randint(init, final))

def randInt(init, final):
	return random.randint(init, final)

def shuffle_letters(word):
	random.shuffle(word)

#printRand(int(input("inicio: ")), int(input("final: ")))