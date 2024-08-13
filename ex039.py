from datetime import date
anoatual = date.today().year
anonascimento = int(input('Informe o Ano de Nascimento: '))
idade = anoatual - anonascimento
if idade < 18:
    saldo = 18 - idade
    print('Você nasceu em {} e está com {} anos de idade em {}. Falta(m) {} ano(s) para poder se alistar.'.format(anonascimento, idade, anoatual, saldo))
    ano = anoatual + saldo
    print('Seu alistamento será em {}. '.format(ano))
elif idade == 18:
    print('Você nasceu em {}, está com {} anos de idade em {}, e deve se alistar IMEDIATAMENTE.'.format(anonascimento, idade, anoatual))
else:
    saldo = idade - 18
    print('Este jovem nasceu em {}, já está com {} anos de idade em {}, e ja deveria ter se alistado há {} ano(s).'.format(anonascimento, idade, anoatual, saldo))
    ano = anoatual - saldo
    print('Seu alistamento foi em {}.'.format(ano))