pessoasdemaior = homens = mulheresmenosvinte =0
while True:
        print('-------- CADASTRE UMA PESSOA --------')
        idade = int(input('Informe a idade: '))
        sexo = ''
        while sexo not in ('M', 'F'):
                sexo = str(input('Informe o sexo [M/F]: ')).strip().upper()[0]
        resposta = ''
        while resposta not in ('S', 'N'):
                resposta = str(input('Quer continuar?[S/N]:  ')).strip().upper()[0]
        print('-------------------------------------')
        if idade >= 18:
                pessoasdemaior += 1
        if sexo in 'Mm':
                homens += 1
        if idade < 20 and sexo in 'Ff':
                mulheresmenosvinte += 1
        if resposta in 'N':
                break
print('-------- RESULTADOS --------')
print(f'Pessoas com mais de 18 anos: {pessoasdemaior}')
print(f'No total foi(ram) cadastrado(s) {homens} homens.')
print(f'No total foi(ram) cadastrada(s) {mulheresmenosvinte} mulhere(s) com menos de 20 anos.')