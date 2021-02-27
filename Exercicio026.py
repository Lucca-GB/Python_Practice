frase = str(input('Digite uma frase: ')).upper().strip()
print('a letra a aparece ',frase.count('a'), ' vezes')
print('a primeira letra a aparece na posição',frase.find('a'))
print('a ultima letra a aparece {}'.format(frase.rfind('A')+1))