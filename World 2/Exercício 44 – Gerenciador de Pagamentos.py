print('{:=^40}'.format(' lojinha '))

preco = float(input('preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO
[1] a vista dinheiro/cheque
[2] a vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')

opcao = int(input('qual é a opção? '))
if(opcao == 1):
    total = preco - (preco * 10 / 100)
elif(opcao == 2):
    total = preco - (preco * 5 / 100)
elif(opcao ==3):
    total = preco
    parcela = total / 2
    print('sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif(opcao == 4):
    total = preco + (preco * 20 / 100)
    totalParcela = int(input('quantas parcelas? '))
    parcela = total/ totalParcela
    print('sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totalParcela, parcela))
else:
    total = preco
    print('OPÇÃO INVÁLIDADE DE PAGAMENTO. TENTE NOVAMENTE!')
print('sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco, total))
