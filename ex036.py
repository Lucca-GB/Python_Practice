casaValor = float(input('\nValor da casa? R$ '))

salario = float(input('Salario? R$ '))

anos = int(input('quantos anos de financiamento? '))

prestacao =  casaValor / (anos * 12)

minimo = salario * 30 / 100

print('\npara pagar uma casa de R${:.2f} em {} anos'.format(casaValor, anos), end='')
print(' a prestacao será de R${:.2f}'.format(prestacao))
if(prestacao <= minimo):
    print('\nEmpréstimo pode ser CONCEDIDO\n')
else:
    print('\nEmpréstimo NEGADO\n')