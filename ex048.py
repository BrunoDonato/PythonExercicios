print('Este programa calcula a SOMA entre todos os números ÍMPARES e MÚLTIPLOS DE 3 entre 1 e 500')
soma = 0
contador = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        contador += 1
        soma += c
print('A soma dos {} números é: {}'.format(contador, soma))