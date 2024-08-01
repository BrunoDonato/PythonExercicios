velocidade = float(input('Informe a velocidade do carro em KM/H:  '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Você tomou uma multa por excesso de velocidade. O valor da multa é de R${:.2f}.'.format(multa))
else:
    print('Velocidade dentro do limite, sem multa.')