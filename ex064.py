soma = totaldigitado = 0
while True:
    n = int(input('Digite um numeros para ser somado: (Digite 999 para encerrar) '))
    if n != 999:
        soma = soma + n
        totaldigitado += 1
    else:
        print('Voce digitou 999, e o programa foi encerrado.')
        print('No total você digitou {} números, e a soma total de todos os numeros que você digitou é: {}'''.format(totaldigitado, soma))
        break