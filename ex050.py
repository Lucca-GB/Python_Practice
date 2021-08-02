soma = 0

for c in range(1, 6+1):
    ni = int(input('digite o {}º numero: '.format(c)))
    if(ni % 2 == 0):
        soma = soma + ni
print('a soma dos NI será {}'.format(soma))
