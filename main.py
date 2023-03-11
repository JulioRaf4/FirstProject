import games.Forca as Forca
import games.advinhação as advinhação

print("*********************************")
print("*******ESCOLHA SEU JOGO!*********")
print("*********************************")

print("[1] PARA FORCA [2] PARA ADVINHAÇÃO")
jogo = int(input())

if jogo == 1:
    print("JOGANDO FORCA")
    Forca.jogar()

elif jogo == 2:
    print("JOGANDO ADIVINHAÇÃO")
    advinhação.jogar()
