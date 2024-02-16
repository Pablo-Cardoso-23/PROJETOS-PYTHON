#teste1
nome = str(input('Olá, qual o seu nome? '))
if nome == 'Pablo':
    print('Que nome lindo!')
print('Bom dia, {}'.format(nome))

#teste2

n1 = float(input('Insira a primeira nota: '))
n2 = float(input('Insira a segunda nota: '))
m = (n1 + n2)/2

print('Sua média é: {}'.format(m))

if m >=6:
    print('Parabéns, você está no caminho certo!')
else:
    print('Que pena, tente se esforçar mais!')

#Jogo de adivinhação

print('Vamos jogar um jogo de adivinhação, onde você deve tentar adivinhar de 0 a 5 o número que escolhi.')
import random
ia = random.randint(0,5)
num = int(input('Insira o número: '))

if num == ia:
    print('parabéns! o número escolhido pelo computador foi {} mesmo'.format(ia))
else:
    print('Ah, que pena! o computador escolheu o número {}'.format(ia))

#Radar eletônico

km = float(input('Insira a velocidade atual do seu carro: '))
vel = (km - 80) * 7

if km <=80:
    print('Tenha um bom dia!')
else:
    print('Motorista multado, o valor da sua multa é de: R${}'.format(vel))
    print('Dirija com mais atenção para que não aconteça na próxima vez.')

#Par ou Ímpar

ins = int(input('Insira um número: '))
div = ins %2

if div == 0:
    print('O número é par')
else:
    print('O número é ímpar')


#Calculando o preço de uma viagem

vi = int(input('insira a distância da viagem: '))
if vi <=200:

    preço = vi * 0.50

else:
    preço = vi * 0.45

print('A distância que será percorrida será {} km e custará R$ {:.2f}'.format(vi, preço))

#Ano Bissexto
from datetime import date

ano = int(input('Insira o ano que deseja analisar, se for o ano atual apenas digite 0: '))
if ano == 0:
    ano = date.today().year
    
if ano %4 == 0 and ano %100 != 0 or ano %400 == 0:

    print('O ano {} é  bissexto.'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))


#Menor e maior valor

a = int(input('Insira o primero número: '))
b = int(input('Insira o segundo número: '))
c = int(input('Insira o terceiro número: '))

menor = a

if b<a and b<c:
    menor = b

if c<a and c<b:
    menor = c

maior = a

if b>a and b>c:
    maior = b

if c>a and c>b:
    maior = c

print('O menor número é: {}'.format(menor))
print('O maior númmero é: {}'.format(maior))

#Aumentos múltiplos

inf = int(input('Qual o salário do funcionário? '))

if inf >= 1250:
    aumento = inf * 0.1
    aumento = inf + aumento

else:
    aumento = inf * 0.15 
    aumento = inf + aumento

print('O salário do funcionário vai passar a ser: R$ {}'.format(aumento))

#Analisando triângulo

print('Hora de analisar se alguns segmentos podem formar um triângulo:')

s1 = int(input('Insira o primeiro segmento: '))
s2 = int(input('Insira o segundo segmento: '))
s3 = int(input('Insira o terceiro segmento: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos a seguir podem formar um triângulo.')

else:
    print('Os segmentos a seguir a seguir não podem formar um triângulo.')

#Como adicionar cores no terminal

print('\033[1;35;42m Concluímos todos os testes! \033[m')