preco = float(input('Digite o preço do produto: R$'))
precodesconto = preco - (preco * 5/100)
print('O produto que custava R${}, com um desconto de 5% vai custar R${}'.format(preco, precodesconto))