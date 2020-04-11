print('Lista de exercícios: testes aritméticos')

nome = input('Nome do usúario: ')
print('Ótimo! vamos começar {}?'.format(nome))
#
print('1° teste, encotre o sucessor e o antecessor de um número.')

n = int(input('Digite um número: '))
a = n - 1
s = n + 1
print('Analisando o valor {}, seu antecessor é {} e o seu sucessor é {}'.format(n, a, s))
#
print('2° teste, calcular o dobro, o triplo e a raiz quadrada.')

n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro de {}, vale {}.'.format(n, d))
print('O triplo de {}, vale {}.\nA raiz quadrada de {} é igual a {:.3f}.'.format(n, d, t, r))
#
print('3° teste, programa para ler, calcular e mostrar a média de um aluno.')

n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
média = (n1 + n2) / 2
print('A média entre {:.1f} e {:.1f} é igual a {:.1f}'.format(n1, n2, média))
#
print('4° teste, programa que identifica um valor em metros e o exibe convertido em centímetros e milímetros.')

medida = float(input('Uma distância em metros: '))
cm = medida * 100
mm = medida * 1000
print('A medida de {:.0f}m corresponde a {:.0f}mm'.format(medida, cm, mm,))
#
print('5° teste, programa para ler um número inteiro e mostra a sua tabuada.')

num = int(input('Digite um número para ver a tabuada de: '))
print('=' * 12)
print('{} x {:2} = {}'.format(num, 1, num*1))
print('{} x {:2} = {}'.format(num, 2, num*2))
print('{} x {:2} = {}'.format(num, 3, num*3))
print('{} x {:2} = {}'.format(num, 4, num*4))
print('{} x {:2} = {}'.format(num, 5, num*5))
print('{} x {:2} = {}'.format(num, 6, num*6))
print('{} x {:2} = {}'.format(num, 7, num*7))
print('{} x {:2} = {}'.format(num, 8, num*9))
print('{} x {:2} = {}'.format(num, 0, num*10))
print('=' * 12)
#
print('6° teste, conversor de moeda.')

real = float(input('Quanto você tem em sua carteira? R$'))
dolar = real / 4.79
euro = real / 5.53
iene = real / 0.046
bitcoin = real / 33.340
print('Com R${:.2f}, você pode comprar US${:.2f}'.format(real, dolar))
print('Com R${:.2f}, você pode comprar EU${:.2f}'.format(real, euro))
print('Com R${:.2f}, você pode comprar IE${:.2f}'.format(real, iene))
print('Com R${:.2f}, você pode pode comprar BT${:.2f}'.format(real, bitcoin))
##
print('7° teste, ferramenta para auxíliar em pintura, medidas de superficies.')

larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
área = larg * alt
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(larg, alt, área))
tinta = área / 2
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))
#
print('8° teste, valor em porcentagem')

preço = float(input('Qual é o preço do produto? R$'))
novo = preço - (preço * 15 / 100)
print('O produto custava R${:.2f}, com o desconto de 15%, custará R${:.2f}'.format(preço, novo))

