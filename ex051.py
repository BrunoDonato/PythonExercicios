pt = int(input('Informe o Primeiro termo da Progressão Aritmética: '))
r = int(input('Informe a Razão da Progressão Aritmética: '))
decimotermo = pt + (10-1) * r
for c in range(pt, decimotermo + r, r):
    print(c)