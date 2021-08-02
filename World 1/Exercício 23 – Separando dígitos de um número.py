#digito = input('Digite um numero: ')
#dividido = digito.split()
#print('unidade: ',digito[3])
#print('dezena: ', digito[2])
#print('centena: ', digito[1])
#print('milhar: ',digito[0])

#método matematico:

num = int(input('digite um numero: '))
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10
print('numero: {}'.format(num))
print('Unidade: {}'.format(unidade))
print('dezena: {}'.format(dezena))
print('centeza: {}'.format(centena))
print('milhar: {}'.format(milhar))