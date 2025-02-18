n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opcao = 0
while opcao != 5:
    print('------ MENU ------')
    print('''    [ 1 ] - SOMAR
    [ 2 ] - MULTIPLICAR
    [ 3 ] - SABER O MAIOR NUMERO
    [ 4 ] - DIGITAR NOVOS NUMEROS
    [ 5 ] - SAIR DO PROGRAMA''')
    opcao = int(input('Informe o número da OPERAÇÃO que deseja realizar: '))
    if opcao > 5 or opcao < 1:
        print('Opção INVÁLIDA. Tente novamente.')
    elif opcao == 1:
        soma = n1 + n2
        print('A soma dos dois valores digitados é: {} '.format(soma))
    elif opcao == 2:
        multiplicacao = n1 * n2
        print('{} multiplicado por {} é igual à: {}'.format(n1, n2, multiplicacao))
    elif opcao == 3:
        if n1 > n2:
            print('Analisando os numeros {} e {}, o maior valor é: {}'.format(n1, n2, n1))
        elif n1 == n2:
            print('Os dois numeros informados são iguais.')
        else:
            print('Analisando os numeros {} e {}, o maior valor é: {}'.format(n1, n2, n2))
    elif opcao == 4:
        print('Informe os dois novos numeros que deseja: ')
        n1 = int(input('Primeiro numero: '))
        n2 = int(input('Segundo numero: '))
print('Obrigado por utilizar nossos serviços, volte sempre!')