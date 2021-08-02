
import math
CO = float(input('comprimento do cateto oposto: '))
CA = float(input('comprimento do cateto adjacente: '))
hi = math.hypot(CO, CA)
print('a hipotenusa vai medir {:.2f}'.format(hi))