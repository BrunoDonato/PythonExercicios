dias = int(input('Por quantos dias o carro foi alugado? '))
kmrodadados = float(input('Qual a quantidade de Km percorridos pelo carro? '))

preco = (dias * 60) + (kmrodadados * 0.15)

print('O valor cobrado será: R${:.2f}'.format(preco))