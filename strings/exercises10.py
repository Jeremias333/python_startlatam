zero = "Zero"
one = "Um"
two = "Dois"
three = "Três"
four = "Quatro"
five = "Cinco"
six = "Seis"
seven = "Sete"
eight = "Oito"
nine = "Nove"
ten = "Dez"
eleven = "Onze"
twelves = "Doze"
threelves = "Treze"
fourteen = "Quatorze"
fiftheen = "Quinze"
sixteen = "Desesseis"
seventeen = "Desessete"
eighteen = "Desoito"
nineteen = "Desenove"

twenty = "Vinte"
threrty = "Trinta"
fourty = "Quarenta"
fifth = "Cinquenta"
sixty = "Sessenta"
seventy = "Setenta"
eighty = "Oitenta"
ninety = "Noventa"

_pass = False

def algarism_func(num):#Retorna o nome.
    if(num == 1):
        return(one)
    elif(num == 2):
        return(two)
    elif(num == 3):
        return(three)
    elif(num == 4):
        return(four)
    elif(num == 5):
        return(five)
    elif(num == 6):
        return(six)
    elif(num == 7):
        return(seven)
    elif(num == 8):
        return(eight)
    elif(num == 9):
        return(nine)


while(not _pass):#iniciará aqui.
    num = int(input("Digite um número de 0 até 99: "))

    if(num >= 0):
        _pass = True
    else:
        print("Digite mais uma vez, atente a condição... \n")

if(num == 0):
    print(zero)
elif(num == 1):
    print(one)
elif(num == 2):
    print(two)
elif(num == 3):
    print(three)
elif(num == 4):
    print(four)
elif(num == 5):
    print(five)
elif(num == 6):
    print(six)
elif(num == 7):
    print (seven)
elif(num == 8):
    print(eight)
elif(num == 9):
    print(nine)
elif(num == 10):
    print(ten)
elif(num == 11):
    print(eleven)
elif(num == 12):
    print(twelves)
elif(num == 13):
    print(three)
elif(num == 14):
    print(fourteen)
elif(num == 15):
    print(fiftheen)
elif(num == 16):
    print(sixteen)
elif(num == 17):
    print(seventeen)
elif(num == 18):
    print(eighteen)
elif(num == 19):
    print(nineteen)

if(num >= 20 and num <= 99):
    algarism = []
    num_text = str(num)
    algarism = [int(num_text[0]), int(num_text[1])]
    print(algarism)

    #deve haver um tratamento para dividir nossas variáveis.
   
    if(algarism[0] == 2 and algarism[1] <= 9):
        if(algarism[1] == 0):
            print(twenty)
        else:
            print(twenty," e ", algarism_func(algarism[1])
    elif(algarism[0] == 3 and algarism[1] <= 9):
        if(algarism[1] == 0):
            print(threrty)
        else:
            print(threrty," e ", algarism_func(algarism[1])

    elif(algarism[0] == 4 and algarism[1] <= 9):
        if(algarism[1] == 0):
            print(fourty)
        else:
            print(fourty," e ", algarism_func(algarism[1])

    elif(algarism[0] == 5 and algarism[1] <= 9):
        if(algarism[1] == 0):
            print(fifth)
        else:
            print(fifth," e ", algarism_func(algarism[1])
    elif(algarism[0] == 6 and algarism[1] <= 9):
        if(algarism[1] == 0):
            print(sixty)
        else:
            print(sixty," e ", algarism_func(algarism[1])
    elif(algarism[0] == 7 and algarism[1] <= 9):
        if(algarism[1] == 0):
            print(seventy)
        else:
            print(seventy," e ", algarism_func(algarism[1])
    elif(algarism[0] == 8 and algarism[1] <= 9):
        if(algarism[1] == 0):
            print(eighty)
        else:
            print(eighty," e ", algarism_func(algarism[1])
    elif(algarism[0] == 9 and algarism[1] <= 9):
        if(algarism[1] == 0):
            print(ninety)
        else:
            print(ninety," e ", algarism_func(algarism[1])
else:
    print("fim")