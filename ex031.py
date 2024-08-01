distancia = float(input('Informe a distância da viagem em KM: '))
print('A sua viagem vai começar...')
if distancia <= 200:
    valorpassagem = distancia * 0.50
else:
    valorpassagem = distancia * 0.45
print('E o valor da passagem é de R${:.2f}'. format(valorpassagem))