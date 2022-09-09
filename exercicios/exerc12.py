prec = float(input('Preço do produto em R$: '))
novo = prec - (prec * 5 / 100)
print('O produto tem um desconto de 5% com um valor de R${:.1f}'.format(novo))