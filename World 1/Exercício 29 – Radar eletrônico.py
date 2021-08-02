vel = float(input('velocidade do carro: '))
if vel > 80:
    print('voce foi multado')
    multa = (vel-80) * 7
    print('o acrecimo da multa é de {} reais'.format(multa))
else:
    print('tudo ok')