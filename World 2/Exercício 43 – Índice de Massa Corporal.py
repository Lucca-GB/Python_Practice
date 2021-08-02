Peso = float(input("Insira o seu peso: (kg)"))
Altura = float(input("Insira a sua altura: (m)"))

IMC = Peso / (Altura ** 2)
print("\nseu IMC é de: {:.1f}".format(IMC))

if(18.5 <= IMC < 25):
    print("\nPESO IDEAL\n")
elif(25 <= IMC < 30):
    print("\nSOBREPESO\n")
elif(30 <= IMC < 40):
    print("\nOBESIDADE\n")
elif(IMC >= 40):
    print('\nOBESIDADE MÓRBIDA\n')