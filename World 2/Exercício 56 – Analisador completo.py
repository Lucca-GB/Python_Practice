somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

for p in range(1, 5):
    print('----- {}º PESSOA -----'.format(p))
    nome = str(input('NOME DA PESSOA: ')).strip()
    idade = int(input('IDADE DA PESSOA: '))
    sexo = str(input('SEXO DA PESSOA [M/F]: ')).strip()
    somaidade += idade

    if(p == 1 and sexo in 'Mm'):
        maioridadehomem = idade
        nomevelho = nome
    if(sexo in 'Mm' and idade > maioridadehomem):
        maioridadehomem = idade
        nomevelho = nome
    if(sexo in 'Ff' and idade < 20):
        totmulher20 += 1
mediaidade = somaidade / 4
print('a media das idades é de {} anos'.format(mediaidade))
print('o homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))
