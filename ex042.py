print('-=-' * 18)
print('Analisando se 3 retas formam um triângulo ou não! ')
print('-=-' * 18)
r1 = float(input('Informe o comprimento da primeira reta: '))
r2 = float(input('Informe o comprimento da segunda reta: '))
r3 = float(input('Informe o comprimento da terceira reta: '))
if (r1+r2) > r3 and (r1+r3) > r2 and (r2 + r3) > r1:
    print('As 3 retas FORMAM um triângulo ', end='')
    if r1 == r2 == r3:
        print('Equilátero.')
    elif r1 != r2 != r3 != r1:
        print('Escaleno.')
    else:
        print('Isósceles.')
else:
    print('As 3 retas NÃO FORMAM um triângulo!')
