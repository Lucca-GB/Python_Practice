from datetime import date
atual = date.today().year

anoNasc = int(input("\nEm que ano o nadador(a) nasceu? \n"))

idade = atual - anoNasc

if(idade <= 9):
    print('\nMIRIM\n')
elif(idade <= 14):
    print('\nINFANTIL\n')
elif(idade <= 19):
    print('\nJUNIOR\n')
elif(idade <= 25):
    print('\nSENIOR\n')
else:
    print('\nMASTER\n')