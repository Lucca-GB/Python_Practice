n = int(input('digite um numero: '))
tot = 0
for c in range(1, n + 1):
    if(n % c == 0):
        tot += 1
        print('{}'.format(c), end=', ')
print('\no numero {} foi dividido {} vezes'.format(n, tot))
if(tot == 2):
    print('PRIMO')
else:
    print('NÃO É PRIMO')
