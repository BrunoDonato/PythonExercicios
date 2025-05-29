from random import randint
numeros = (randint(1, 10), randint(1, 10),randint(1, 10),randint(1, 10),randint(1, 10))
print(f'Números gerados: ', end='')
for n in numeros:
        print(f'{n} ', end='')
print(f'\nO menor número sorteado foi: {min(numeros)}')
print(f'O maior numero sorteado foi: {max(numeros)}')
