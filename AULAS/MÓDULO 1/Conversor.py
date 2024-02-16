#Conversor de moedas
print('Olá, bem-vindo ao nosso conversor de moedas!')
print('Consiredere que ás principais moedas estão com os resspectivos valores hoje:')
print('Valor do dólar: 5,19')
print('Valor do euro: 5,52')
print('Valor do iene japonês: 0,038')
carteira = float(input('Para começarmos, diga quanto você tem em sua carteira: R$'))
dol = carteira / 5.20
eur = carteira / 5.52
ien =  carteira / 0.38

print('Sua quantia em dólar é: USD {:.2f}'.format(dol))
print('Sua quantia em euro é: EUR {:.2f}'.format(eur))
print('sua quantia em ien é: JPY {:.2f}'.format(ien))

#Medidor de dimensões
print(input('Esse é um medidor de dimensões no caso iremos medir a largura e altura de sua parede'))
lar = float(input('Insira a largura: '))
alt = float(input('Insira a altura: '))

l = lar * alt
print('Sua parede tem dimensão de {} x {} e sua área é de {}m².'.format(lar, alt, l))
t = l / 2
print('Para pintar sua parede você vai precisar de {}L '.format(t))

#Calculadora de descontos
print('Olá, vamos calcular alguns descontos?')
valor =  float(input('Insira o valor do produto: R$ '))

n1 = valor * 0.05 
n2 = valor * 0.1 
n3 = valor * 0.15 
n4 = valor * 0.2  
n5 = valor * 0.25  
n6 = valor * 0.3 
n7 = valor * 0.35 
n8 = valor * 0.4 
n9 = valor * 0.45 
n10 = valor * 0.5 
n11 = valor * 0.55  
n12 = valor * 0.6 
n13 = valor * 0.65 
n14 = valor * 0.7 
n15 = valor * 0.75 
n16 = valor * 0.8 
n17 = valor * 0.85 
n18 = valor * 0.9 
n19 = valor * 0.95 
n20 = valor * 1 

d1 = valor - n1
d2 = valor - n2
d3 = valor - n3
d4 = valor - n4
d5 = valor - n5
d6 = valor - n6
d7 = valor - n7
d8 = valor - n8
d9 = valor - n9
d10 = valor - n10
d11 = valor - n11
d12 = valor - n12
d13 = valor - n13
d14 = valor - n14
d15 = valor - n15
d16 = valor - n16
d17 = valor - n17
d18 = valor - n18
d19 = valor - n19
d20 = valor - n20

print('O produto que custava R$ {} com o desconto de 5% fica por R$ {:.2f}'.format(valor, d1))
print('O produto que custava R$ {} com o desconto de 10% fica por R$ {:.2f}'.format(valor, d2))
print('O produto que custava R$ {} com o desconto de 15% fica por R$ {:.2f}'.format(valor, d3))
print('O produto que custava R$ {} com o desconto de 20% fica por R$ {:.2f}'.format(valor, d4))
print('O produto que custava R$ {} com o desconto de 25% fica por R$ {:.2f}'.format(valor, d5))
print('O produto que custava R$ {} com o desconto de 30% fica por R$ {:.2f}'.format(valor, d6))
print('O produto que custava R$ {} com o desconto de 35% fica por R$ {:.2f}'.format(valor, d7))
print('O produto que custava R$ {} com o desconto de 40% fica por R$ {:.2f}'.format(valor, d8))
print('O produto que custava R$ {} com o desconto de 45% fica por R$ {:.2f}'.format(valor, d9))
print('O produto que custava R$ {} com o desconto de 50% fica por R$ {:.2f}'.format(valor, d10))
print('O produto que custava R$ {} com o desconto de 55% fica por R$ {:.2f}'.format(valor, d11))
print('O produto que custava R$ {} com o desconto de 60% fica por R$ {:.2f}'.format(valor, d12))
print('O produto que custava R$ {} com o desconto de 65% fica por R$ {:.2f}'.format(valor, d13))
print('O produto que custava R$ {} com o desconto de 70% fica por R$ {:.2f}'.format(valor, d14))
print('O produto que custava R$ {} com o desconto de 75% fica por R$ {:.2f}'.format(valor, d15))
print('O produto que custava R$ {} com o desconto de 80% fica por R$ {:.2f}'.format(valor, d16)) 
print('O produto que custava R$ {} com o desconto de 80% fica por R$ {:.2f}'.format(valor, d16)) 
print('O produto que custava R$ {} com o desconto de 80% fica por R$ {:.2f}'.format(valor, d16)) 
print('O produto que custava R$ {} com o desconto de 85% fica por R$ {:.2f}'.format(valor, d17))
print('O produto que custava R$ {} com o desconto de 90% fica por R$ {:.2f}'.format(valor, d18))
print('O produto que custava R$ {} com o desconto de 95% fica por R$ {:.2f}'.format(valor, d19))
print('O produto que custava R$ {} com o desconto de 100% fica por R$ {:.2f}'.format(valor, d20))

#Reajuste salarial

print('Vamos calcular o reajuste salarial logo a seguir: ')
num1 = float(input('Insira o valor do salarial antigo: R$ '))
num2 = float(input('Insira o valor salarial atual: R$ '))

salario = num2 - num1
decimal =  salario / num1
dec = decimal * 100

print('O seu salário antigo de R${} teve o acréscimo de R${}'.format(num1, salario))
print('O funcionário passará a ganhar R$ {}'.format(num2))
print('Dito isso o seu reajuste salarial foi de {:.2f}%'.format(dec))

#feedback

import emoji

print(emoji.emojize('Obrigado por usar o nosso programa :smirking_face:'))