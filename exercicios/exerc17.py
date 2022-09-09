from math import hypot
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
hip = hypot(ca, co)
print('A hipotenusa vale = {:.2f}'.format(hip))