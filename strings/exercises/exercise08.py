phrase = input("Digite uma frase para sabermos se é palíndromo: ")
inverted_phrase = phrase[::-1]

if(phrase == inverted_phrase):
    print(f"É Palíndromo: {phrase} é igual a {inverted_phrase}")
else:
    print(f"Não é Palindromo: {phrase} é diferente de {inverted_phrase}")