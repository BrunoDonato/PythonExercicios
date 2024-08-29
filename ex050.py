soma = 0
contador = 0
for c in range(1, 7):
    n = int(input('Digite o {} número: '.format(c)))
    if n % 2 == 0:
        soma += n
        contador += 1
print('A soma do(s) {} número(s) PAR(ES) que foram digitados é: {}'.format(contador, soma))