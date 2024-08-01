from random import randint
from time import sleep
num = randint(0, 5) #Número sorteado pelo computador
print('-=-' * 26)
print('SEJA BEM VINDO! VOU PENSAR EM UM NÚMERO E TE DESAFIO À ADIVINHAR QUAL É ELE!')
print('-=-' * 26)
resposta = int(input('Eu pensei em um número entre 0 e 5. Qual é ele: '))
print('CONFERINDO SUA RESPOSTA...')
sleep(2)
if resposta == num:
    print('Parabéns! Você digitou o número {} e acertou na mosca, foi exatamente o que pensei!'.format(resposta))
else:
    print('EU VENCI, HAHA! Você digitou o número {}, e eu pensei no número {}!'.format(resposta, num))
