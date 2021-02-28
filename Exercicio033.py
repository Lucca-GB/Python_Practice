valor1 = int(input('primeiro valor: '))
valor2 = int(input('segundo valor: '))
valor3 = int(input('terceiro valor: '))
#verificando quem é menor
menor = valor1
if valor2 < valor1 and valor2 < valor3:
    menor = valor2
if valor3 < valor1 and valor3 < valor2:
    menor = valor3
#verificando quem é o maior
maior = valor1
if valor2 > valor1 and valor2 > valor3:
    maior = valor2
if valor3 > valor1 and valor3 > valor2:
    maior = valor3

print('o menor valor digitado foi {}'.format(menor))
print('o maior valor digitado foi {}'.format(maior))