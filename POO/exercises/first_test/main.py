from bola_model import Bola
import os
os.system('cls' if os.name == 'nt' else 'clear')

bola1 = Bola("Azul", 15.0, "Plástico")

print(bola1.saw_color())
bola1.change_color("Vermelha")
print(bola1.saw_color())