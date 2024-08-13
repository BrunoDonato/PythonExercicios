valorcasa = float(input('Informe o valor da casa: R$'))
salario = float(input('Informe o salário do comprador: R$'))
anos = int(input('Em quantos anos o comprador vai pagar a casa? '))
quantidadeparcelas = anos * 12
valormensal = valorcasa / quantidadeparcelas
if valormensal <= (salario * 30/100):
    print('Parabéns! Seu empréstimo foi aprovado para comprar a casa no valor de R${:.2f}. \n'
          'Você irá pagar {} parcelas no valor de R${:.2f} por mês!'.format(valorcasa, quantidadeparcelas, valormensal))
else:
    print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}'.format(valorcasa, anos, valormensal))
    print('Infelizmente não podemos aprovar o seu empréstimo.')