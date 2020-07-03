from datetime import datetime

class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), "%Y"))
    
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
    
    def falar(self, assunto):
        if(self.comendo):
            print(f"{self.nome} não pode comer falando.")
            return
        else:
            if(not self.falando):
                self.falando = True
                print(f"{self.nome} está falando sobre: {assunto}")
            else:
                print(f"{self.nome} está falando agora sobre: {assunto}")

    def parar_falar(self):
        if(not self.falando):
            print(f"{self.nome} não estava falando")
            return
        
        print(f"{self.nome} parou de falar.")
        self.falando = False

    def comer(self, alimento):
        if(self.comendo):
            print("Já está comendo")
            return

        print(f"{self.nome} está comendo {alimento}.")
        self.comendo = True

    def parar_comer(self):
        if(self.comendo):
            self.comendo = False
            print(f"{self.nome} parou de comer")
        else:
            print(f"{self.nome} não está comendo nada")
    
    def get_ano_nasc(self):
        return (self.ano_atual - self.idade)