celsius = 0
fahrenheit = 0
result = 0

def choice():
    print("Responda com 'sim' ou 'nao'\n\n\n")
    choice = input("Vamos converter C para F?")
    if choice == 'sim':
        c_to_f()
    elif choice == 'nao':
        print("Vamos converter F para C?")
        if choice == 'sim':
            f_to_c()
        elif choice == 'nao':
            print("É necessário escolher uma das opções!!")
            choice()
    else:
        print("Algumas escolhas devem ser feitas!")
        choice()

def main():
    choice()

def c_to_f():
    fahrenheit = input("Qual o Fahrenheit agora? ")
    fahrenheit = float(fahrenheit.replace(",","."))
    #calculo
    result = (fahrenheit-32)/9 
def f_to_c():
    celsius = input("Qual o Celsius agora? ")
    celsius = float(celsius.replace(",","."))
    #calculo

def yesornot(alt):
    if alt != 'sim' and alt != 'nao':
        print("Utilize apenas 'sim' ou 'nao' \n\nRepita o processo.\n\n")
        main()

main()