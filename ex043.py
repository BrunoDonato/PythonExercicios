peso = float(input('Informe o seu peso (kg): '))
altura = float(input('Informe a altura (m): '))
imc = peso / (altura ** 2)
print('Seu IMC é de {:.1f} e você está '.format(imc), end='')
if imc < 18.5:
    print('ABAIXO DO PESO ideal.')
elif 18.5 <= imc < 25:
    print('no PESO IDEAL')
elif 25 <= imc <= 30:
    print('em SOBREPESO')
elif 30 <= imc < 40:
    print('em OBESIDADE, cuidado')
else:
    print('em OBESIDADE MÓRBIDA, cuidado imediato!')
