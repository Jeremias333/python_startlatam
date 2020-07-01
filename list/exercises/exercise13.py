annual_temperature = ["", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
annual_month = ["", "Janeiro", "Fervereiro", "Março", "Abril", "Maio", "Junho", 
                "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
med = 0

def main():
    _pass = False
    print("Vamos calcular a média anual das temperaturas")
    
    cont = 1
    while(_pass == False):
        if(cont == 13):
            _pass = True
        else:
            temperature = float(input(f"Digite a temperatura para {annual_month[cont]}: "))
            annual_temperature[cont] = temperature
            cont+=1
    print(" ")
    printer(calc_temperature())#chama o printer que recebe como parametro a média que é retornada pelo calculo da temperatura


def calc_temperature():#utiliza o list gloal anteriormente criado
    values = 0
    for x in range(1, 13):
        if(x > 0):
            values += annual_temperature[x]
    med = (values/12)
    return med

def printer(med):
    print(f"A média de temperatura é: {med}")
    for x in range(1, 13):
        print(f"{annual_month[x]} esse ano fez {annual_temperature[x]}º")
        
main()