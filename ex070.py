valortotal = produtosacimamil = menorpreco = cont = 0
maisbarato = ''
print('------------ CAIXA ------------ ')
while True:
        nomeproduto = str(input('Nome do produto: '))
        preco = float(input('Preço do produto: R$ '))
        cont += 1
        valortotal += preco
        if preco > 1000:
                produtosacimamil += 1
        if cont == 1 or preco < menorpreco:
                menorpreco = preco
                maisbarato = nomeproduto
        resposta = ''
        while resposta not in ('S', 'N'):
                resposta = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
        if resposta in 'Nn':
                break
        print('--------------------------------')
print(f'Valor total da compra: R${valortotal:.2f}')
print(f'{produtosacimamil} produto(s) custam mais de R$1000.00')
print(f'O produto mais barato foi o(a){maisbarato} que custa: {menorpreco}')