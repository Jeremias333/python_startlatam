word = "OMA ET AILUJ"

print(word[-1])#para pegar o ultimo caracter.
print(word[0:2])#[inicio:final]
print(word[:12])#[:final] pega todos caracteres do inicio até o numero desejado
print(word[1:])#[1:] pega todos caracteres do inicio até o numero desejado
print(word[::-1])#pegando todos caracteres de trás para frente.


print(word.split())#o metodo split() por padrão transforma a str em um array separado pelo parametro passado
#caso não tenha nada, ele separa por espaço.

print(word.split("OMA ET "))#todos que eu quero retirar passo por parametro

#para unir palavras
text1 = ' '.join(['hello', 'world'])  # -> 'hello world' - ficará entre o espaço em branco.
text2 = ',,'.join(['first line', 'second line'])  # -> 'first line,second line' - ficará entre os valores que já existe.

print(text1, "\n",text2)

print(f"O tamanho da {word} é: {len(word)}")

print(word == text1)#ver se os conteúdos das strings são iguais.