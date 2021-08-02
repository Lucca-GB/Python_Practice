maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('peso da {}º pessoa: '.format(c)))
    if(c == 1):
        maior = peso
        menor = peso
    else:
        if(peso > maior):
            maior = peso
        if(peso < menor):
            menor = peso
print('o maior peso lido foi de {}kg'.format(maior))
print('o menor peso lido foi de {}kg'.format(menor))
