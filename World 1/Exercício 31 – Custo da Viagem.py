
distancia = float(input('distancia da viajem em km: '))
if distancia < 200:
    preco45 = distancia * 0.45
    print('esta viagem custará {} reais'.format(preco45))
elif distancia > 200:
    preco50 = distancia * 0.50
    print('a viajem custará {} reais'.format(preco50))