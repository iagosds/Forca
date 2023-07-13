import random
from words import palavras
import string
def imprime_mensagem_perdedor(word):
    print("A palavra era {}".format(word))
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

    if(erros == 6):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 0):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def choice():

    # DEFINIÇÃO DA PALAVRA A SER ADIVINHADA
    word = random.choice(palavras)
    while '-' in word or ' ' in word:
        word = random.choice(palavras)
    
    return word.upper()

def forca():
    word = choice()
    letras = set(word) # PALAVRA SENDO SEPARADA
    alfabeto = set(string.ascii_uppercase) # DEFINIÇÃO DE QUAIS CARACTÉRES PODERÃO SER UTILIZADOS
    tentativas = set() # REGISTRO DAS TENTATIVAS DO USUÁRIO
    vidas = 7

    while len(letras)>0:

        #derrota
        if vidas == 0:
            print("\nSuas vidas se esgotaram! Tente novamente!")
            imprime_mensagem_perdedor(word)
            break 

        if len(tentativas)>0:
            print("\nVocê usou essas letras: ", " ".join(tentativas))
        print("Vidas: ", vidas-1)

        # PALAVRA REVELANDO APENAS AS LETRAS QUE JA FORAM ADIVINHADAS
        visto = [letter if letter in tentativas else '-' for letter in word] 
        print("Palavra: ", " ".join(visto))
        chute = input("Digite uma letra: ").upper() # TENTATIVA DO USUÁRIO
        print()

        if chute in alfabeto:
            if chute in letras:
                letras.remove(chute)
            elif chute in tentativas:
                print("\nVocê ja tentou essa letra!\n")
            else:
                vidas-=1
                desenha_forca(vidas)
            tentativas.add(chute)
        else:
            print("Caractér inválido")
        print("--------------------------")

    # VITÓRIA
    if len(letras) == 0:
        imprime_mensagem_vencedor()

forca()
