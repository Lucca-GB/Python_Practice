frase = str(input('digite um nome ou frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print('o inverso de {} é {}'.format(junto, inverso))
if(inverso == junto):
    print('é um palindromo')
else:
    print('não é um palindromo')
    