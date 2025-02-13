somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomehomemmaisvelho = ''
totalmulher20 = 0
for p in range(1, 5):
    print('------ {}ª PESSOA ------'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F): ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomehomemmaisvelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomehomemmaisvelho = nome
    if sexo in 'Ff' and idade < 20:
        totalmulher20 += 1

mediaidade = somaidade / 4
print('A média de idade de todas as pessoas é de {} anos.'.format(mediaidade))
print('O homem mais velho se chama {} e tem {} anos de idade.'.format(nomehomemmaisvelho, maioridadehomem))
print('No total são {} mulher(es) com menos de 20 anos de idade'.format(totalmulher20))
