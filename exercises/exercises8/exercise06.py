days_study = 0
cash_day = 0.0

print("Para receber seu auxilio precisamos de algumas informações: ")

days_study = input("Quantos dias você estudou? ")
cash_day = input("Quanto você ganha por dia? ")

days_study = int(days_study.replace(",","."))
cash_day = float(cash_day.replace(",","."))

total_cash = (days_study*cash_day)

print(f"Total a ser pago é: {total_cash:.2f}")