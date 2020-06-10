def yesornot(alt):
    if alt != 'sim' and alt != 'nao':
        print("Utilize apenas 'sim' ou 'nao' \n\nRepita o processo.\n\n")
        main()

def main():
    print("Responda sempre com 'sim' ou 'nao'")
    print("-------------------------------------------------------------------------------------------")
    
    wake_up = input("Olá vamos acordar?")
    yesornot(wake_up)#se for algo diferente de sim e nao ele repete o main.
    
    if wake_up == "sim":

        see_cell = input("Olhar o celular?")
        yesornot(see_cell)

        if see_cell == "sim":     
            print("Procrastinamos e perdemos o dia...")#fim de execução.
        elif see_cell == "nao":
            
            trainning = input("Vamos treinar?")
            yesornot(trainning)

            if trainning == "sim":
                
                print("Uffaaa, treinamos bem, estamos cansados... Nosso dia vai ser uma maravilha...")

            elif see_cell == "nao":
                
                print("Pensamos de mais e perdemos nosso dia inteiro.... Boa.")#fim da execução
    
    elif wake_up == "nao":
        
        print("Ok vamos dormir mais né? ZzzzZzzzz...")#fim da execução.

main()