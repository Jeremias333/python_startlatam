celsius = 0
fahrenheit = 0
result = 0

def choice():
    print("Responda com 'sim' ou 'nao'\n\n\n")
    choice = input("Vamos converter °C para °F?")
    if choice == 'sim':
        c_to_f()
    elif choice == 'nao':
        choice = input("Vamos converter °F para °C?")
        if choice == 'sim':
            f_to_c()
        elif choice == 'nao':
            print("É necessário escolher uma das opções!!")
            choice()
    else:
        print("Algumas escolhas devem ser feitas!")
        choice()

def main():#método inicial.
    choice()

def c_to_f():
    celsius = input("Qual o Celsius agora? ")
    celsius = int(celsius.replace(",","."))
    
    #calculo
    result = int(((celsius/5)*9)+(32))
    print(f"{celsius}°C em Fahrenheit é: {result}°F")

def f_to_c():
    fahrenheit = input("Qual o Fahrenheit agora? ")
    fahrenheit = int(fahrenheit.replace(",","."))
    #calculo
    result = (((fahrenheit - 32)/9)*5)
    print(f"{fahrenheit}°F em Celsius é: {result:.0f}°C")

def yesornot(alt):
    if alt != 'sim' and alt != 'nao':
        print("Utilize apenas 'sim' ou 'nao' \n\nRepita o processo.\n\n")
        main()

main()