import random
aluno1 = str(input('Informe o nome do primeiro aluno: '))
aluno2 = str(input('Informe o nome do segundo aluno: '))
aluno3 = str(input('Informe o nome do terceiro aluno: '))
aluno4 = str(input('Informe o nome do quarto aluno: '))

lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista) #shuffle foi utilizado para embaralhar os nomes

print('A ordem de apresentação será: {}'.format(lista))