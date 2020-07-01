import sys
sys.path.append("C:/utils/")

from util import yesorno
import rand

list_quest = ['','','','','']
cont = 0

quest = input("Telefonou para a vítima ?")
list_quest[0] = yesorno(quest)

quest = input("Esteve no local do crime ?")
list_quest[1] = yesorno(quest)

quest = input("Mora perto da vítima ?")
list_quest[2] = yesorno(quest)

quest = input("Devia para a vítima ?")
list_quest[3] = yesorno(quest)

quest = input("Já trabalhou com a vítima ?")
list_quest[4] = yesorno(quest)

print(list_quest)

for x in list_quest:
	if(x == 1):
		cont+=1
if(cont == 2):
	print("suspeito")
elif(cont == 3 or cont == 4):
	print("cumplice")
elif(cont == 5):
	print("assassino")
else:
	print("inocente")