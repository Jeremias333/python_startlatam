#Lista guarda mais de um dado em uma variavel que pode ser navegada por index.

list_1 = list()
print(type(list_1))
list_2 = []
print(type(list_2))

list_1 = ["Nick"]#não pode se atribuir str a uma list! apenas uma list para list
print(list_1)
list_1.append("Carla")#adicionar ao fim da lista
print(list_1)

print(list_2)#print de lista vazia

list_2 = ["Cajá", "Caju", "Melancia", "Manga"]#atribuindo lista populada
print(list_2)

#toda lista começa em zero no seu index
list_2.insert(3, "Cana")#adicionando num indice especifico
print(list_2)

del list_2[3]#deletando item em um index especifico
print(list_2)

print("Ultimo elemento tirado da lista: ",list_2.pop())#tira o ultimo elemento da lista e retorna seu valor
print(list_2)

print(list_1.pop(0))#retirando da lista com index
print(list_1)

list_2[0] = "Cajazinho"#alterar elemento em um index especifico.

print(list_2)
list_1.append("Nick")
list_2.extend(list_1)#unindo listas e iteráveis.
print(list_2)

list_2.remove("Carla")#remove valor especifico da lista
print(list_2)

print(len(list_2))#tamanho da lista

for x in list_2:#navegando pela lista usando loop
    print(x)

#list_2.append("Carla")

if("Carla" in list_2):#verificar a lista
    print("Carla está na lista")
else:
    print("Carla não está na lista")

list_3 = [1, 2, 3, 4, 5, 6]
print(list_3)
list_3.reverse()
print(list_3)

list_3.sort(reverse=False)
print(list_3)

#existe uma forma de fazer referencias a uma lista meio que unir as duas.
list_first = [1,3,5,7,9]
list_second = list_first
print(list_second)
list_first.append("Adicionado no list_first")
print(list_second)

#para adicionar sem referencia utiliza-se[:]
list_third = list_first[:]
list_first.append("novo")
print(list_first)
print(list_third)


A = [[1,4,0], [-2, 0, 1]]

print(A[0][0])#matriz