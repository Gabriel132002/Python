larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
ar = larg * alt
print('Dimensão da parede é de {}x{}, área de {}m²'. format(larg, alt, ar))
tinta = ar/2
print('Será necessário {}L de tinta'.format(tinta))