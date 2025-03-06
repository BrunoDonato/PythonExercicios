from random import randint
numerojogador = 0
verificasoma = ''
vitorias = 0
print('---------- VAMOS JOGAR PAR OU IMPAR! ----------')
while True:
    numerocomputador = randint(0, 10)
    numerojogador = int(input('Escolha o valor que deseja jogar[0 à 10]: '))
    escolhajogador = str(input('Escolha PAR ou IMPAR [P/I]: ')).upper().strip()[0]
    soma = numerocomputador + numerojogador
    if soma % 2 == 0:
        verificasoma = 'PAR'
    else:
        verificasoma = 'IMPAR'
    if escolhajogador in 'P':
        if soma % 2 == 0:
            print('-' * 60)
            print('Você VENCEU!')
            print(f'VOCÊ jogou {numerojogador}, e o COMPUTADOR jogou {numerocomputador}. Total de {soma} deu {verificasoma}.')
            print('-' * 60)
            vitorias += 1
        else:
            print('Você PERDEU!')
            break
    elif escolhajogador in 'I':
        if soma % 2 == 1:
            print('-' * 60)
            print('Você VENCEU!')
            print(f'VOCÊ jogou {numerojogador}, e o COMPUTADOR jogou {numerocomputador}. Total de {soma} deu {verificasoma}.')
            print('-' * 60)
            vitorias += 1
        else:
            print('Você PERDEU!')
            break
    print('VAMOS JOGAR NOVAMENTE...')
print(f'VOCÊ jogou {numerojogador}, e o COMPUTADOR jogou {numerocomputador}. Total de {soma} deu {verificasoma}\nVocê venceu {vitorias} vez(es). GAME OVER!')
