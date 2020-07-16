from carro import Car

car = Car(10)
car.more_gas(0)
print("Combustivel ",car.get_gas())
print(car.move(1000))
print("Combustivel ",car.get_gas())