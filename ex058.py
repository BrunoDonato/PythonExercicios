from random import randint
computador = randint(0, 10) #Numero pensado(sorteado) pelo computador.
print('Olá, vamos jogar! Acabei de pensar em um número entre 1 e 10, que numero é este?')
acertou = False
tentativas = 0
jogador = 0
while not acertou:
 jogador = int(input('Que numero eu pensei? '))
 tentativas += 1
 if computador == jogador:
  acertou = True
 else:
  if computador > jogador:
   print('RESPOSTA ERRADA. O numero que eu pensei é MAIOR do que o que você informou. TENTE NOVAMENTE.')
  elif computador < jogador:
   print('RESPOSTA ERRADA. O numero que eu pensei é MENOR do que o que você informou. TENTE NOVAMENTE.')
print('PARABÉNS! RESPOSTA CORRETA. Você respondeu {}, e foi exatamente no numero {} que eu pensei! \nVocê gastou {} tentativas para adivinhar!'.format(jogador, computador, tentativas))
