n = int(input('Digite um número INTEIRO qualquer: '))
print(''' Escolha uma das opções abaixo para conversão:
[ 1 ] se deseja converter o número para Binário
[ 2 ] se deseja converter o número para Octal
[ 3 ] se deseja converter o número para Hexadecimal''')
base = int(input('Digite aqui: '))
if base == 1:
    print('O número {} convertido para Binário é igual à: {}'.format(n, bin(n)[2:]))
elif base == 2:
    print('O número {} convertido para Octal é igual à: {}'.format(n, oct(n)[2:]))
elif base == 3:
    print('O número {} convertido para Hexadecimal é igual à: {}'.format(n, hex(n)[2:]))
else:
    print('Opção INVÁLIDA! Você deve escolher as opções entre 1 e 3.')