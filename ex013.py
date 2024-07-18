salario = float(input('Digite o salário: R$'))
novosalario = salario + (salario * 15/100)
print('O novo salário com aumento de 15% é igual a: R${:.2f}'.format(novosalario))