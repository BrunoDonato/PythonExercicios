from math import hypot
catoposto = float(input('Informe o cateto oposto do triângulo retângulo: '))
catadj = float(input('Informe o cateto adjacente do triângulo retângulo: '))
hip = hypot(catoposto, catadj)
print('A hipotenusa do triângulo retângulo informado é: {:.2f}'.format(hip))