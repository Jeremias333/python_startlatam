class Car:
	def __init__(self, consume:int):
		self.consume = consume#quanto gasta por 1km andado
		self.gas = 0#gas é nivel

	def move(self, km):
		init_final = km
		if(self.gas < 1):
			return "Não pode viajar pois está sem combustível."
		elif(self.gas > 0):
			while(self.gas > 0):
				self.gas -= 1
				km -= self.consume
				print(km)
				if(self.gas == 0):
					return f"Ops a gasolina acabou... Conseguimos andar: {init_final-km}km"
				elif(km <= 0):
					print("entrou")
					return f"Andou os {init_final}km"
			return f"Não temos combustivel suficiente para continuar a viagem, andamos {init_final-km}"
		else:
			return "O tanque está vazio não podemos andar"

	def get_gas(self):
		return self.gas

	def more_gas(self, gas):
		self.gas += gas