nome = str(input('digite o seu nome completo: ')).strip()
dividido = nome.split()
print('primeiro nome: ',dividido[0])
print('ultimo nome: ', dividido[len(dividido)-1])