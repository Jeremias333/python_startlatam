phrase = input("Digite uma frase: ")
spaces = 0
vowels = 0

phrase = phrase.lower()

vowels += phrase.count('a')
vowels += phrase.count('e')
vowels += phrase.count('i')
vowels += phrase.count('o')
vowels += phrase.count('u')

spaces += phrase.count(' ')

print(f"Quantidades de espaços: {spaces}")
print(f"Quantidades de vogais: {vowels}")