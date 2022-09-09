dias = int(input('Dias alugados: '))
km = float(input('Quantos Km rodados: '))
pgd = dias * 60
pgkm = km * 0.15
total= pgd + pgkm
print('Preço dos dias alugados é de: R${:.2f}'.format(pgd))
print('Preço por km rodade é de: R${:.2f}'.format(pgkm))
print('O total é de: R${:.2f}'.format(total))