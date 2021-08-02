from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('''
[1]PEDRA
[2]PAPEL
[3]TESOURA''')

player = int(input('qual é a sua jogada? \n'))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)

print('-' * 20)
print('pc: {}'.format(itens[computador]))
print('player: {}'.format(itens[player]))
print('-' * 20)

if(computador == 0):
    if(player == 0):
        print('EMPATE')
    elif(player == 1):
        print('JOGADOR VENCEU')
    elif(player == 2):
        print('COMPUTADOR VENCEU')
    else:
        print('Ocorreu um erro.')
elif(computador == 1):
    if(player == 0):
        print('COMPUTADOR VENCEU')
    elif(player == 1):
        print('EMPATE')
    elif(player == 2):
        print('JOGADOR VENCEU')
    else:
        print('Ocorreu um erro.')
elif(computador == 2):
    if(player == 0):
        print('JOGADOR VENCEU')
    elif(player == 1):
        print('COMPUTADOR VENCEU')
    elif(player == 2):
        print('EMPATE')
    else:
        print('Ocorreu um erro.')
