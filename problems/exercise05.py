number = "10.25"
decimal = number.replace(number[:2]," ")#trocando os dois primeiro valores por space, se colocar apartir de 100 quebra o programa.

print(f"A parte decimal do {number} é: {decimal}")#se eu não estivesse tão preguiçoso daria pra fazer algo percorrer a string e dar replace em todos numero até o ponto.