born_date = input("Digite sua data de nascimento: ")

born_date = born_date.split("/")

#print(born_date)

born_date_month = born_date[1]
born_date_day = born_date[0]
bron_date_year = born_date[2]

#print(born_date_month)

if(born_date_month == "01"):
    print(f"Você nasceu em {born_date_day} de Janeiro de {bron_date_year}")

elif(born_date_month == "02"):
    print(f"Você nasceu em {born_date_day} de Fervereiro de {bron_date_year}")

elif(born_date_month == "03"):
    print(f"Você nasceu em {born_date_day} de Março de {bron_date_year}")

elif(born_date_month == "04"):
    print(f"Você nasceu em {born_date_day} de Abril de {bron_date_year}")

elif(born_date_month == "05"):
    print(f"Você nasceu em {born_date_day} de Maio de {bron_date_year}")

elif(born_date_month == "06"):
    print(f"Você nasceu em {born_date_day} de Junho de {bron_date_year}")

elif(born_date_month == "07"):
    print(f"Você nasceu em {born_date_day} de Julho de {bron_date_year}")

elif(born_date_month == "08"):
    print(f"Você nasceu em {born_date_day} de Agosto de {bron_date_year}")

elif(born_date_month == "09"):
    print(f"Você nasceu em {born_date_day} de Setembro de {bron_date_year}")

elif(born_date_month == "10"):
    print(f"Você nasceu em {born_date_day} de Outubro de {bron_date_year}")

elif(born_date_month == "11"):
    print(f"Você nasceu em {born_date_day} de Novembro de {bron_date_year}")

elif(born_date_month == "12"):
    print(f"Você nasceu em {born_date_day} de Dezembro de {bron_date_year}")

else:
    print("Erro com o formato da data")