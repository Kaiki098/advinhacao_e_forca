import forca
import adivinhacao

sair = False

while(not sair):

    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("(1) Forca (2) Adivinhação (3) Sair")

    jogo = int(input("Digite sua escolha: "))

    if (jogo == 1):
        print("Jogando forca")
        forca.jogar()
    elif (jogo == 2):
        print("Jogando adivinhação")
        adivinhacao.jogar()
    elif(jogo == 3):
        sair = True

print("Você saiu do programa")

