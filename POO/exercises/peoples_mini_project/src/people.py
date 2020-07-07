class People:
    
    def __init__(self, name: str, age: int, weight: float, height: float):
        self.name = name
        self.age = age 
        self.weight = weight
        self.height = height

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_weight(self):
        return self.weight
    
    def get_height(self):
        return self.height

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_weight(self, weight):
        self.weight = weight

    def set_height(self, height):
        self.height = height