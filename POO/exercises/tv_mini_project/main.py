from tv_model import TV
import os

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    #criação do objeto tv
    list_volume = list()
    list_channel = list()

    list_volume.append(1)
    list_volume.append(10)

    list_channel.append(2)
    list_channel.append(13)

    tv = TV(list_channel, list_volume)
    
    _pass = True
    while(_pass == True):
        menu(tv)
        print("repetiu")

def menu(tv: TV):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Aviso: {tv.get_warn()}")
    if(tv.get_state() == True):
        print(f"Volume atual: {tv.get_volume()}")
        print(f"Canal atual: {tv.get_channel()}")
        option = int(input("\n 1 - Volume + \n 2 - Volume - \n 3 - Canal + \n 4 - Canal - \n 0 - Desligar \n"))
        tv.set_warn()
        if(option == 1):
            tv.volume_more()
        if(option == 2):
            tv.volume_minum()
        if(option == 3):
            tv.channel_more()
        if(option == 4):
            tv.channel.minum()
        if(option == 0):
            tv.off_tv()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Opção inválida.")
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        option = int(input("\n 1 - Ligar TV \n"))
        if(option == 1):
            tv.on_tv()
            
main()