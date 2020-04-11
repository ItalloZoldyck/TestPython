print('Digite o seu valor para converte-lo (cotação da moeda de acordo com o dia 27/03/20. ')
real = float(input('Qaunto você possui R$?: '))
dolar = real / 5.11
euro = real / 5.56
iene = real / 0.047
peso = real / 0.22
rublo = real / 0.064
bitcoin = real / 33737.48
boliviano = real / 0.74
print('Com R$:{:.2f}, você poderá comprar US$:{:.2f}'.format(real, dolar))
print('Com R$:{:.2f}, você poderá comprar EU$:{:.2f}'.format(real, euro))
print('Com R$:{:.2f}, você poderá comprar IJP$:{:.2f}'.format(real, iene))
print('Com R$:{:.2f}, você poderá comprar MX$:{:.2f}'.format(real, peso))
print('Com R$:{:.2f}, você poderá comprar URS:{:.2f}'.format(real, rublo))
print('Com R$:{:.2f}, você poderá comprar BT:{:.2f}'.format(real, bitcoin))
print('Com R$:{:.2f}, você poderá comprar PBV:{:.2f}'.format(real, boliviano))
