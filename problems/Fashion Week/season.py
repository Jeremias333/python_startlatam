def calc_season(day, month):
    if((month == 3 and day >=20) or (month >= 4 and day <= 31) or (month == 6 and day <= 20)):
        print(f"Estamos no {OUT}")
    if((month == 6 and day >= 21) or (month >= 7 and day <= 31) or (month == 9 and day <= 22)):
        print(f"Estamos no {INV}")
    if(month >= 9 and day >= 23 and month <= 12 and day <= 24):
        print(f"Estamos na {PRI}")
    if((month == 12 and day >= 25) or (month == 1 and day >= 1) or (month == 3 and day <= 19) or (month == 2 and day <= 29)):
        print(f"Estamos no {VER}")
    _pass = 1

day = 0
month = 0

OUT = "Outono"
INV = "Interno"
PRI = "Primavera"
VER = "Verão"

_pass = 0

print("Vamos ver qual a estação estamos...\n\n")

while(_pass == 0):
    day = int(input("Digite o dia: "))
    month = int(input("Digite o mês: "))

    if(day >= 1 and month <= 31): #conferida base
        if(month >= 1 and month <= 12): #conferida base
            if(month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12): #meses com 31 dias
                calc_season(day, month)
                break
            if(day <= 30 and month == 4 or month == 6 or month == 9 or month == 11):#meses com 31 dias
                if(month == 2 and day <= 29 or day >= 1):#fervereiro
                    calc_season(day, month)
                    break #para evitar o programa repetir ou cair na resolução dos meses com 30
                else:  
                    calc_season(day, month)
                    break
            else:
                print(f"O mês escolhido não possui {day}")
        else:
            print("Mês está fora do alcance, repita o processo...")
    else:
        print("Dia está fora do alcance, repita o processo...")
else:
    print("fim do loop")