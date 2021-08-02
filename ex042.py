seg1 = float(input('primeiro segmento: '))
seg2 = float(input('segundo segmento: '))
seg3 = float(input('terceiro segmento: '))

if(seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2):
    print('\npode formar um triangulo ', end='')
    if(seg1 == seg2 == seg3):
        print('EQUILATERO')
    elif(seg1 != seg2 != seg3 != seg1):
        print('ESCALENO')
    else:
        print('ISÓCELES')
else:
    print('\nnao pode formar um triangulo')
