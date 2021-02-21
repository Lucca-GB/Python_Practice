from random import choice
nome1 = str(input('nome um: '))
nome2 = str(input('nome dois: '))
nome3 = str(input('nome tres: '))
nome4 = str(input('nome quatro: '))
lista = [nome1, nome2, nome3, nome4]
escolhido = choice(lista)
print('aluno escolhido: {}'.format(escolhido))