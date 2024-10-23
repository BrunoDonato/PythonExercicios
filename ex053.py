frase = str(input('Informe uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
frase_reversa = ''
for c in range(len(junto) -1, -1, -1):
    frase_reversa += junto[c]
if junto == frase_reversa:
    print('É um Palíndromo!')
else:
    print('Não é um Palíndromo!')



