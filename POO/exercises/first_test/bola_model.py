"""
    Classe modelo para bola
    atributos: color: str, circumference: float, material = ""
"""
class Bola:
    color = ""
    circumference = 0.0
    material = ""

    def __init__(self, color: str, circumference: float, material: str):
        self.color = color
        self.circumference = circumference
        self.material

    def change_color(self, color: str):
        self.color = color

    def saw_color(self):
        return self.color
    


