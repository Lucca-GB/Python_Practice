from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0

for pessoas in range(1, 8):
    nasc = int(input('ano de nascimento da {} pessoa: '.format(pessoas)))
    idade = atual - nasc
    print('essa pessoa tem {} anos'.format(idade))
    if(idade >= 18):
        print('essa pessoa é maior \n', end='')
        totmaior += 1
    else:
        print('\n essa pessoa é menor \n', end='')
        totmenor += 1
print('tem {} maiores de idade'.format(totmaior))
print('e {} menores de idade'.format(totmenor))
