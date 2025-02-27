from datetime import date
anoatual = date.today().year
totalmaior = 0
totalmenor = 0
for c in range(1, 8):
    ano = int(input('Informe o ano de nascimento da {}ª pessoa: '.format(c)))
    idade = anoatual - ano
    if idade < 18:
        totalmenor += 1
    else:
        totalmaior += 1
print('No total, tivemos {} menores de idade, e {} pessoasdemaior maiores de idade.'.format(totalmenor, totalmaior))
