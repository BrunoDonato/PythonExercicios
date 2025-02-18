sexo = str(input('Informe o seu Sexo M/F: ')).upper().strip()[0]
while sexo not in 'MmFf':
        sexo = str(input('Sua resposta não é válida, informe o Sexo novamente (M/F): ')).upper().strip()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))