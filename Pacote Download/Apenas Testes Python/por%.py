salário = float(input('Qual é o salário do funcionário ? R$'))
novo = salário + (salário * 13 / 100)
print('O funcionário que ganhava R$:{:.2f}, passará a receber R$:{:.2f}'.format(salário, novo))
