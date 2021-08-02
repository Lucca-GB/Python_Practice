from math import radians, sin, cos, tan
angulo = float(input('angulo: '))
seno = sin(radians(angulo))
print('angulo: {}    SENO de {:.2f}'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('angulo: {}    CONSSENO de {:.2f}'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('angulo: {}    TANGENTE de {:.2f}'.format(angulo, tangente))