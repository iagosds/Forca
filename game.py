import random
from words import palavras
import string

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
            print("A palavra era: ", word)
            break 

        if len(tentativas)>0:
            print("\nVocê usou essas letras: ", " ".join(tentativas))
        print("Vidas: ", vidas)

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
            tentativas.add(chute)
        else:
            print("Caractér inválido")
        print("--------------------------")

    # VITÓRIA
    if len(letras) == 0:
        print("\nParabéns, você acertou!")
        print("A palavra era: ", word)

forca()