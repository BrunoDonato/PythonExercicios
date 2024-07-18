reais = float(input('Digite quantos reais você tem: R$'))
dolar = 5.44
quantidade = reais/dolar
print('Com R${:.2f}, você consegue comprar U${:.2f}'.format(reais, quantidade))