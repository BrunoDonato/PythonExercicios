n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n1 > n2:
    print('O Primeiro número({}) é maior que o Segundo número({}).'.format(n1, n2))
elif n2 > n1:
    print('O Segundo número({}) é maior que o Primeiro número({}).'.format(n2, n1))
else:
    print('Não existe valor maior, os dois números são iguais.')