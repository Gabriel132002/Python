from math import sin, cos, tan, radians
ang = float(input('Digite o os graus do ângulo: '))
sen = sin(radians(ang))
coss = cos(radians(ang))
tange = tan(radians(ang))

print('Seno = {:.2f}'.format(sen))
print('Cosseno = {:.2f}'.format(coss))
print('Tangente = {:.2f}'.format(tange))
