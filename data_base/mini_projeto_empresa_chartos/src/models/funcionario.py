class Funcionario:
    def __init__(self, name:str="", function:str="", salary:float=0.0):
        self.id = 0
        self.name = name
        self.function = function
        self.salary = salary

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_function(self):
        return self.function

    def get_salary(self):
        return self.salary

    def set_id(self, id:int):
        self.id = id

    def set_name(self, name:str):
        self.name = name

    def set_function(self, function:str):
        self.function = function

    def set_salary(self, salary:float):
        self.salary = salary