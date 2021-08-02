from random import randint #importa uma modulo que permite o computador sortear um numero aleatorio
from time import sleep #modulo que permite o computador espere algum tempo usando a função sleep()
computador = randint(0, 5) #Faz o computador "pensar" em um numero // referente ao modulo random
print('-' * 20)
print('vou pensar em um numero entre 0 e 5. Tente adivnhar  ')
print('-' * 20)
jogador = int(input('em que numero eu pensei? ')) #jogador tenta adivnhar
print('processando...')
sleep(3) #função referente ao modulo time
if jogador == computador:
    print('voce acertou')
else:
    print('você errou, o numero certa é {}'.format(computador))