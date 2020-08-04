class User:
	def __init__(self):#construtor
		self.id = 0,
		self.name = "",
		self.age = 0

	def set_id(self, id):
		self.id = id

	def set_name(self, name):
		self.name = name

	def set_age(self, age):
		self.age = age

	def get_id(self):
		return self.id

	def get_name(self):
		return self.name

	def get_age(self):
		return self.age