print('=-=-=-=- SEQUÊNCIA DE FIBONACCI -=-=-=-=')
n = int(input('Quantos termos da sequencia de Fibonacci deseja mostrar? '))
primeironumero = 0
segundonumero = 1
c = 0
while c < n:
    print(primeironumero, end='')
    print(' -> ', end='')
    proximo = primeironumero + segundonumero
    primeironumero = segundonumero
    segundonumero = proximo
    c = c+1
print('Fim')