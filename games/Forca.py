import random
def jogar():
      
    mensagem_bem_vindo()
   
    palavra_secreta = escolhe_palavra_secreta()
          
    letras_acertadas = imprime_letras_acertadas(palavra_secreta)
    erros = 0
    
    print(letras_acertadas)
    
    acertou = enforcou = False
    while not enforcou and not acertou:
        chute = pedechute()

        if chute in palavra_secreta:                     
            marca_chute_acertado(chute, letras_acertadas, palavra_secreta)
            
        else:
            print("Ops... você errou uma")
            erros += 1
            print("{} Erro até agr!".format(erros))
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)
        
    if acertou:
        mensagem_vencedora()
    
    else:
        mensagem_perdedora(palavra_secreta)
        
    print("Fim de jogo")

def mensagem_bem_vindo():
    print("*********************************")
    print("Bem vindo ao jogo da Forca!")
    print("*********************************")

def escolhe_palavra_secreta():
    palavras = []
    arquivo = open("nomes.txt", "r")
    for linha in arquivo:
        linha = linha.strip().upper()
        palavras.append(linha)
    arquivo.close()
    palavra_secreta = random.choice(palavras)
    return palavra_secreta
        
def imprime_letras_acertadas(palavra):
   return ["_"]*len(palavra)

def pedechute():
    chute = str(input("Chute uma letra: "))
    chute = chute.strip().upper()
    return chute

def marca_chute_acertado(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:             
        if chute == letra:
            print("Encontrei a letra [{}] na posição [{}]".format(letra, index))
            letras_acertadas[index] = letra
        
        index = (index + 1) 

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

def mensagem_vencedora():
    print("Parabéns, você foi o ganhador!")
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
    
def mensagem_perdedora(palavra_secreta):
    print("Você perdeu!")
    print("A Palavra secreta era:",palavra_secreta)
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
    
if (__name__ == "__main__"):
    jogar()
    