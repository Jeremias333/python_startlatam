import os#importando o pacote necessário para executar a limpeza.

print("Vai ser limpo")
os.system('cls' if os.name == 'nt' else 'clear')#irá utilizar cls para windows ou clear para distro linux.

print("Não vai ser limpo daqui para baixo.")