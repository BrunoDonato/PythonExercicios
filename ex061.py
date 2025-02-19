print('=-=-=-=- Gerador de Progressão Aritmética -=-=-=-=')
pt = int(input('Informe o Primeiro termo da PA: '))
r = int(input('Informe a Razão da PA: '))
termo = pt
c = 1
while c <= 10:
    print('{} -> '.format(termo), end='')
    termo = termo + r
    c = c+1
print('Fim')
