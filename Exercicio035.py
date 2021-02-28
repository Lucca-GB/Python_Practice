r1 = float(input('segmento 1:'))
r2 = float(input('segmento2: '))
r3 = float(input('segmento3: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('os segmentos podem formar um triangulo')
else:
    print('os segmentos nao podem formar um triangulo :(')