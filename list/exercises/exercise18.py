kicker_votes = ["",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
kicker_percent = ["",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#variavel de controle será o jogador
total = 0

def main():
    _exit = False

    while(_exit == False):
        vote = int(input("Digite um jogador para ser votado (Ou 0 para encerrar os votos.): "))
        if(vote == 0):
            _exit = True
        elif(vote >= 1 and vote <= 23):
            print(f"Votou no jogador: {vote}")
            kicker_votes[vote] += 1
        else:
            print("Os valores precisam ser de 1 até 23, ou 0 para encerrar os votos.")
    else:
        for x in range(1, 24):#variavel que vai controlar o jogador.
            if(kicker_votes[x] > 0):#verifica se a posição x é maior que 0 para poder então ser impresso.
                print(f" O jogador {x} tem {kicker_votes[x]} votos")#imprime qual o jogador e também quantos pontos ele tem.
                
        calculate_percent()#chamando calculador de percentual

def calculate_percent():#calcular as porcentagens
    final_total = 0
    for x in range(1, 24):#variavel de controle do jogador
        if(kicker_votes[x] > 0):#verifica se a posição x é maior que 0 para poder então ser tratado
            total = kicker_votes[x]
            final_total += total
    for x in range(1, 24):#variavel que vai controlar o jogador.
        if(kicker_votes[x] > 0):#verifica se a posição x é maior que 0 para poder então ser tratado
            #calculo da porcentagem
            result = 100 * kicker_votes[x]
            kicker_percent[x] = result/final_total
    print_result(final_total)#chama resultado printado.

def print_result(final_total):
    print("\n\nNúmero do Jogador   |  Votos  |  % de votos")
    for x in range(1, 24):
        if(kicker_votes[x] > 0):
            print(f"        {x}                {kicker_votes[x]}          {kicker_percent[x]:.2f}%")
    print(f"\nTotal de votos: {final_total} - 100%")

main()#inicio do programa