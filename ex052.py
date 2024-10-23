n = int(input('Informe um numero Inteiro: '))
numdivisiveis = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end='')
        numdivisiveis += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end=' ')
print('\033[m')
print('O numero {} foi divisivel {} vezes, sendo por 1 e por ele mesmo.'.format(n, numdivisiveis))
if numdivisiveis == 2:
    print('Portanto, o numero {} É PRIMO!'.format(n), end='')
else:
    print('Portanto, o numero {} NÃO É PRIMO!'.format(n), end='')