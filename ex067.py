cont = 0
print('---------- GERADOR DE TABUADA ----------')
while True:
    numero = int(input('Digite o número que deseja ver a TABUADA [Digite um número NEGATIVO para ENCERRAR]: '))
    print('_' * 80)
    if numero < 0:
        break
    for cont in range(1,11):
        print(f'{numero} x {cont} = {cont*numero}')
    print('_' * 80)
print('PROGRAMA ENCERRADO!')