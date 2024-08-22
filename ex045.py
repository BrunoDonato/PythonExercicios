from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('''Escolha o que você quer ser...
[ 0 ] - Pedra 
[ 1 ] - Papel 
[ 2 ] - Tesoura ''')
jogador = int(input('Digite o número correspondente à opção que deseja escolher: '))
print('-+' * 15)
print('O Computador jogou: {}'.format(itens[computador]))
print('O Jogador jogou: {}'.format(itens[jogador]))
print('-+' * 15)
print('JO')
sleep(0.8)
print('KEN')
sleep(0.8)
print('PO!')
print('-+' * 15)
if computador == 0:  #Computador jogou Pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCEU')
    elif jogador == 2:
        print('COMPUTADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1:  #Computador jogou Papel
    if jogador == 0:
        print('COMPUTADOR VENCEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2:  #Computador jogou Tesoura
    if jogador == 0:
        print('JOGADOR VENCEU')
    elif jogador == 1:
        print('COMPUTADOR VENCEU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')
