t = int(input('tabuada do: '))
n = 1
for c in range(1, 10+1):
    print(t * n)
    n += 1
print('FIM')

#seria possivel fazer em 3 linhas apenas também:
#num = int(input('tabuada do: ))
#for c in range(1, 11):
#   print('{} x {:2} = {}'.format(num, c, num*c))
