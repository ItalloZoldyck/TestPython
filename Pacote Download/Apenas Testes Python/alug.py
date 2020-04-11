dias = int(input('Quantos dias alugado? '))
km = int(input('Quatos Km foram rodados? '))
pago = (dias * 60) + (km * 0.15)
print('O total a ser pago é de R${:.2f}'.format(pago))

