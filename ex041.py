from datetime import date
anoatual = date.today().year
anonascimento = int(input('Informe o Ano de Nascimento do atleta: '))
idade = anoatual - anonascimento
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Categoria: MIRIM.')
elif idade > 9 and idade <= 14:
    print('Categoria: INFANTIL.')
elif idade > 14 and idade <= 19:
    print('Categoria: JÚNIOR')
elif idade > 19 and idade <= 20:
    print('Categoria: SÊNIOR')
else:
    print('Categoria: MASTER')