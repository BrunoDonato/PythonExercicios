import random
aluno1 = str(input('Informe o nome do primeiro aluno: '))
aluno2 = str(input('Informe o nome do segundo aluno: '))
aluno3 = str(input('Informe o nome do terceiro aluno: '))
aluno4 = str(input('Informe o nome do quarto aluno: '))
alunos = [aluno1, aluno2, aluno3, aluno4]
sorteio = random.choice(alunos) #choice vai escolher apenas 1 dos alunos da lista
print('O aluno sorteado foi: {}'.format(sorteio))

