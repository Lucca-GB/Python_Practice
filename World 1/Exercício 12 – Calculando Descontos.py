preco_produto = int(input('O produto custa: R$'))
preco_desconto = (5 * preco_produto)
preco_desconto2 = preco_desconto/100
print('agora com o desconto de 5%, o produto vale: {}'.format( preco_produto - preco_desconto2))
