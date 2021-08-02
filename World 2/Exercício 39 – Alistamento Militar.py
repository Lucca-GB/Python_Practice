from datetime import date
anoAtual = date.today().year

anoNasc = int(input("\nem que ano vc nasceu? "))

qntAnos = anoAtual - anoNasc

print('\nquem nasceu em {} tem {} anos em {}'.format(anoNasc, qntAnos, anoAtual))

if(qntAnos < 18):
    saldo = 18 - qntAnos
    print("\nvocê ainda vai se alistar no exército. Faltam {} anos".format(saldo))
    ano = anoAtual + saldo
    print('\nseu alistamento será em {}'.format(ano))
elif(qntAnos == 18):
    print("\njá é hora de voce se alistar no exército.")
elif(qntAnos > 18):
    saldo = qntAnos - 18
    print("\nvc ja deveria ter se alistado ha {} anos".format(saldo))
    ano = anoAtual - saldo
    print('\nseu alistamento foi em {}'.format(ano))
