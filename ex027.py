nome = str(input('Digite seu nome completo: ')).strip()
nomedividido = nome.split()
print('O primeiro nome é: {}'.format(nomedividido[0]))
print('O último nome é: {}'.format(nomedividido[-1]))


#Utilizando o len
#print('O último nome é: {}'.format(nomedividido[len(nomedividido)-1]))
