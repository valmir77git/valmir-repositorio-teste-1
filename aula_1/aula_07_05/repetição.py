import time
import random

print ("### jogo da adivinhação ###")
print ()
print ("Estou pensando em um número...")

time.sleep(1.5)

numero = random.randint(0,10)

print ("pensei!")
print ("você poderá tentar adivinhar ele")
print ()
# * para i tem um intervalo de 1 até 4
#for i in range(1,4):
#    print (f"Essa é a sua {i} tentativa")
#    tentativa = int (input("Digite um valor entre o e 10: "))
#
#    if tentativa == numero:
#        print ("Parabéns você acertou!")
#    else:
#        print("Você errou")

acertou = False 
num_tentativa = 0
# enquanto acertou for false...
while acertou == False:
    num_tentativa += 1 # mesma coisa que num_tentativa = num_tentativa +1
    print (f"Essa é a {num_tentativa}ª tentativa")
    tentativa = int (input("Digite um valor entre o e 10: "))

    if tentativa == numero:
       print ("Parabéns você acertou!")
       acertou = True
    else:
        print("Você errou")
        if num_tentativa == 10:
            print("Você passou de 10 tentativas, BURRO PRA KCT! ")
