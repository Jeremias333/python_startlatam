#criação de classes.
class MyFirstClass:
	def __init__:
		year_act = 2020

    #pass
    @classmethod
    def born_year(cls, name, ano_nasc):
    	year = (cls.year_act - ano_nasc)
    	return cls(name, year)
    	
a = MyFirstClass()

print(a)

#class com atributo.
class Point:
    def __init__(self, x, y):#constructor
        pass
    def reset(self):#metodo para resetar
        self.x = 0
        self.y = 0

p1 = Point(1,2)
p2 = Point(3,4)

p1.x = 5
p1.y = 4

p2.x = 3
p2.y = 6

print(p1.x)

p1.reset()
print(p1.x)


