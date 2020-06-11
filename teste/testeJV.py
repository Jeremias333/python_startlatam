idade=input("qual a sua idade?")
if idade < 12:
    print("criança")
elif idade < 18:
    print("adolescente")
elif idade < 60:
    print("adulto")
else:
    print("idoso")
print(f" você já pode ir a tal canto pois já tem {idade}")