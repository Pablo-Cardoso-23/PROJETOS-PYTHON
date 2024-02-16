#Calculadora
print('Olá, seja bem-vindo!')
print('Preparado para os testes?')
num1 = int(input('Insira um número: '))
num2 = int(input('Insira outro número: '))
s = (num1 + num2)
sub = (num1 - num2)
mult = (num1 * num2)
div = (num1 / num2)
pot = (num1 ** num2)
r4n1 =  (num1  **(1/2))
r4n2 = (num2 **(1/2))

print('A soma entre {} e {} é igual a: {}'.format(num1, num2, s))
print('A subtração entre {} e {} é igual a: {}'.format(num1, num2, sub))
print('A multiplcação entre {} e {} é igual a: {}'.format(num1, num2, mult))
print('A divisão entre {} e {} é igual a: {}'.format(num1, num2, div))
print('A poetência de {} elevado a {} é igual a: {}'.format(num1, num2, pot))
print('A raiz quadrada de {} é igual a: {}'.format(num1, r4n1))
print('A raiz quadrada de {} é igual a: {}'.format(num1, r4n2))

#Conversões de medidas
print(input('Certo, vamos realizar algumas conversões?'))
print(input('Logo em seguida insira um valor, em seguida veremos esse valor em metros, quilômetros e assim por diante'))
num3 = int(input('Insira o número para realizar ás conversões: '))
m = num3 
km = num3 * 10
hm = 10 * km
dam = 10 * hm
dm = num3 /10
cm = dm /10
mm = cm /10

print('{} em metros é igual a: {} '.format(num3, m))
print('{} em quilômetros é igual a: {} '.format(num3, km))
print('{} em hectômetro é igual a: {}'.format(num3, hm))
print('{} em decâmetro é igual a: {}'.format(num3, dam))
print('{} em decímetro é igual a: {}'.format(num3, dm))
print('{} em centímetro é igual a: {}'.format(num3, cm))
print('{} em milímetro é igual a: {}'.format(num3, mm))

#Calcular média anual
print(input('Uau, chegamos muito longe!'))
print(input('É, hora de calcular algumas médias de notas :)'))
nota1 = float(input('Insira a primeira nota: '))
nota2 = float(input('Insira a segunda nota: '))
nota3 = float(input('Insira a terceira nota: '))
nota4 = float(input('Insira a quarta nota: '))
média = (nota1 + nota2 + nota3 + nota4) / 4
print('Sua média anual é {}'.format(média))

#Antecessor e sucessor
print(input('Ok, agora vamos testar o comando de sucessor e antecessor'))
print(input('Logo abaixo insira um determinado número inteiro, pode ser qualquer um!'))
num4 = int(input('Insira seu número: '))
ant = num4 - 1
suc = num4 + 1
print('De acordo com o número inserido o antecessor de {} é {} e o seu sucessor é {}'.format(num4, ant, suc))