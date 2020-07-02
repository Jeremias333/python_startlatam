#tuplas são lista mais rápidas e estáticas. basicamente uma lista constante.

#um grande diferencial seria a poderosa atribuição
x, y = 13, 45

print(x, y)

print(x)

print(type(x))

t = tuple()

print(type(t))

t = tuple([1,2,'yo'])
print(t)

t = ('1', '2', '3')
print(t.__getitem__(0))
#as tuplas são feitas com ().