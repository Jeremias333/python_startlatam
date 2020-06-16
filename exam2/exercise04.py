_pass = 0

def question(yesorno):
    if(yesorno == 'sim'):
        return 1
    elif(yesorno == 'nao'):
        return 0
    else:
        print("Apenas será aceito 'sim' ou 'nao' como resposta.\n\n")
        main()

def verdict(response):#metodo de veredito
    if(response == 2):
        print("Você é um suspeito, continuaremos essa conversa em outro momento")
    elif(response >= 3 and response < 5):
        print("Você foi autuado! É um cumplice")
    elif(response == 5):
        print("Você é um assassino! Está autuado!")
    else:
        print("É inocente, está dispensado.")

def main(): 
    _pass = 0

    while(_pass == 0):
        response = 0
        first = ""

        print("FBI: Precisamos fazer algumas perguntas \nrespeito do assassinato que aconteceu pelos arredores. \nSem justificativas",
        " responda apenas com 'sim' ou 'nao'")

        first = input("\nEstá disposto a colaborar com a investigação?")

        if(first == 'sim'):
        #iniciar interrogatório
           response += question(input("Telefonou para a vítima?"))
           response += question(input("Esteve no local do crime?"))
           response += question(input("Mora perto da vítima?"))
           response += question(input("Devia para a vítima?"))
           response += question(input("Já trabalhou com a vítima?"))

           verdict(response)
           _pass = 1
        elif(first == 'nao'):
            print("Certo vamos começar denovo!\n\n\n")
        else:
            print("Responda apenas com 'sim' ou 'nao'. Vamos começar denovo\n\n\n")
    else:
        print("Saiu do loop")

main()