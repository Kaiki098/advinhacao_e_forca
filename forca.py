import random

def jogar():

    imprime_mensagem_abertura()

    tema = escolhe_tema()

    palavra_secreta = carrega_palavra_secreta(tema)

    letras_acertadas = ["_" for letras in palavra_secreta]

    acertou = False
    enforcou = False

    erros = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = solicita_chute()

        if(chute in palavra_secreta):
            substitui_letra_acertada(palavra_secreta, chute, letras_acertadas)      
        else:
            erros += 1
            desenha_forca(erros)

        acertou = "_" not in letras_acertadas
        enforcou = erros == 7

        print(letras_acertadas) 

    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

    print("Fim do jogo")


def imprime_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def escolhe_tema():
    tema = input("Escolha um tema de jogo\nFrutas || Objetos || Games || Todos\n").lower() 
    if(tema != "frutas" and tema != "objetos" and tema != "games"):
        tema = "todos"
    return tema

def carrega_palavra_secreta(nome = "todos"):
    palavras = []
    
    nome_arquivo = "/Users/kaiki/OneDrive/Documentos/Python/Alura/Formacao_Python_Orientado_a_Objetos/Início_em_Python/arquivos/" + nome + ".txt"

    with open(nome_arquivo, "r") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta

def solicita_chute():
    chute = input("Digite a letra: ")
    chute = chute.strip().upper()
    return chute


def substitui_letra_acertada(palavra_secreta, chute, letras_acertadas):
    index = 0
    for letra in palavra_secreta: 
        if(chute == letra):
            letras_acertadas[index] = chute
        
        index += 1

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__ == "__main__"):
    jogar()