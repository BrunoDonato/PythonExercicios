resposta = 'S'
somavalores = totalvalores = media = maior = menor = 0
while resposta in 'Ss' :
    num = int(input('Digite um numero: '))
    somavalores += num
    totalvalores += 1
    if totalvalores == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resposta = str(input('Quer continuar? S/N ')).upper().strip()
media = somavalores / totalvalores
print('Você digitou {} numeros e, somando todos, a media deles foi de: {}'.format(totalvalores, media))
print('O MAIOR valor digitado foi {}, e o MENOR valor digitado foi {}.'.format(maior, menor))
































'''print('O maior numero que voce digitou foi: {}'.format(novomaior))
print('O menor numero que voce digitou foi: {}'.format(novomenor))
print('Somando todos os numeros digitados, a media é de: {}'.format(media))'''