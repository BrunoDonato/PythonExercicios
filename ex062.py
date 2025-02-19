print('=-=-=-=- Gerador de Progressão Aritmética -=-=-=-=')
pt = int(input('Informe o Primeiro termo da PA: '))
r = int(input('Informe a Razão da PA: '))
termo = pt
c = 1
total = 0
nt = 10
while nt != 0:
    total = total + nt
    while c <= total:
        print('{} -> '.format(termo), end='')
        termo = termo + r
        c = c + 1
    print('PAUSA')
    nt = int(input('Quer mostrar mais quantos termos? '))
print('Fim')
print('No total foram mostrados {} termos.'.format(total))
