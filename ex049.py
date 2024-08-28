numero = int(input('Informe o número que deseja saber a tabuada: ')) #numero informado pelo usuario
for c in range(1, 11): #contador
    print('{} x {} = {}'.format(numero, c, numero*c))