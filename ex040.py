n1 = float(input('Informe a primeira nota entre 0 e 10: '))
n2 = float(input('Informe a segunda nota entre 0 e 10: '))
media = ((n1 + n2) / 2)
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}.'.format(n1, n2, media))
if media < 5:
    print('O aluno está REPROVADO!'.format(media))
elif media >= 5 and media < 7:
    print('O aluno está em RECUPERAÇÃO.'.format(media))
elif media > 7:
    print('O aluno está APROVADO.'.format(media))
