salario = float(input('Informe o salário: R$'))
if salario > 1250:
    novo = salario + (salario * 0.1)
else:
    novo = salario + (salario * 0.15)
print('Quem recebia {} vai passar à receber: R${:.2f}'.format(salario, novo))
