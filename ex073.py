tabela = ('São Paulo', 'Fluminense', 'Flamengo', 'Cruzeiro', 'Vasco',
          'Atlético-MG', 'Tupi', 'Palmeiras', 'Corinthians', 'Santos',
          'Grêmio', 'Internacional', 'Bahia', 'Vitória', 'Ceará',
          'Botafogo', 'Criciúma', 'Chapecoense', 'Londrina', 'Fortaleza')
print(f'__' * 50)
print(f'TABELA BRASILEIRÃO: {tabela}')
print(f'__' * 50)
print(f'Os 5 primeiros colocados da tabela são: {tabela[0:5]}')
print(f'__' * 50)
print(f'Os últimos 4 colocados da tabela são: {tabela[17:]}')
print(f'__' * 50)
print(f'A lista dos times em ordem alfabética é:{sorted(tabela)}')
print(f'__' * 50)
print(f'A Chapecoense está na {tabela.index('Chapecoense')+1} posição')
print(f'__' * 50)
