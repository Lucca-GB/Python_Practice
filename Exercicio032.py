from datetime import date #biblioteca que trabalha com datas
ano = int(input('que ano quer analisar? coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year #pega a data atual independente de tudo
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('o ano {} é BISSEXTO'.format(ano))
else:
    print('o ano {} NÃO é BISSEXTO'.format(ano))