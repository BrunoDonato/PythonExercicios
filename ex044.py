print('{:=^40}'.format(' LOJAS AMARAL '))
preco = float(input('Informe o valor do produto: '))
condicao = int(input('Escolha a opção que tenha a condição de pagamento desejada \n'
                     '[ 1 ] - À VISTA: Dinheiro / Cheque (10% de desconto) \n'
                     '[ 2 ] - À VISTA: Cartão (5% de desconto)\n'
                     '[ 3 ] - Até 2x no Cartão (Preço normal)\n'
                     '[ 4 ] - 3x ou mais no Cartão (20% de juros)\n'
                     'Digite aqui a opção que deseja: '))
if condicao == 1:
    valorfinal = preco - (preco * 10 / 100)
    print('Você escolheu o pagamento À Vista com Dinheiro ou Cheque e obteve 10% de desconto.\n'
          'O valor que era de R${:.2f}, com o desconto, passou à ser R${:.2f}.'.format(preco, valorfinal))
elif condicao == 2:
    valorfinal = preco - (preco * 5 / 100)
    print('Você escolheu o pagamento À Vista com Cartão e obteve 5% de desconto.\n'
          'O valor que era de R${:.2f}, com o desconto, passou à ser R${:.2f}.'.format(preco, valorfinal))
elif condicao == 3:
    valorfinal = preco
    parcela = valorfinal / 2
    print('Você escolheu o pagamento em até 2x no Cartão. \n'
          'Sua compra será no total de R${:.2f} parcelada em 2x de R${:.2f} SEM JUROS. '.format(valorfinal, parcela))
elif condicao == 4:
    valorfinal = preco + (preco * 20 / 100)
    quantidadeparcelas = int(input('Quantas parcelas?'))
    parcela = valorfinal / quantidadeparcelas
    print('Você escolheu o pagamento em {}x no Cartão. Com isso foi acrescentado 20% de juros.'.format(quantidadeparcelas))
    print('O valor que era de R${:.2f}, com o acréscimo, passou à ser R${:.2f}.'.format(preco, valorfinal))
    print('Serão {} parcelas de R${:.2f}, totalizando os R${:.2f}'.format(quantidadeparcelas, parcela, valorfinal))
else:
    print('Opção inválida. Selecione de 1 à 4.')
