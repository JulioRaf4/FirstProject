import  random
def jogar():

    
    escolha = -1
    tentativa = 0
    sorte = random.randint(0,100)
    invalido = False

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    while invalido == False :
        print("INSIRA UMA DIFICULDADE")
        print("(1)Facil - (2) Médio - (3) Difícil")
        dificuldade = int(input())
        if dificuldade > 0 and dificuldade < 4:
            invalido = True

    if dificuldade == 1:
        jogadas = 20 
        print("[MODO FACÍL ESCOLHIDO]")
    elif dificuldade == 2:
        jogadas = 10
        print("[MODO MÉDIO ESCOLHIDO]")

    elif dificuldade == 3:
        jogadas = 5
        print("[MODO HARD ESCOLHIDO]")   
        
    while jogadas > tentativa :
        print("Faça sua escolha:", end=" ")
        escolha = int(input())
        tentativa += 1
        print("{}º Tentativa".format(tentativa))
        if sorte > escolha and escolha >= 0:
            print("Mais... Tente outra vez")

        elif sorte < escolha and escolha <= 100:
            print("Menos... Tente outra vez")
    
        elif sorte == escolha:
            print("Parabéns!")
            print("Você ganhou!, o número sorteado foi:",sorte )
            print("Quantidade de tentavivas:",tentativa)  

        else:
            print("Insira um valor entre 0 e 100")
            
    if sorte != escolha:
        print("Você perdeu!")
        print("Quantidade de tentavivas:",tentativa) 
        print("Número sorteado foi:", sorte)

if __name__ == "__main__":
    jogar()
