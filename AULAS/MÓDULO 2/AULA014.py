'''r = 'S' 

while r == 'S':
    c = int(input('INFORME UM VALOR: '))
    r = str(input('DESEJA CONTINUAR? [S/N]')) . upper()

print('FIM')'''

n = 1
par = impar = 0
while n != 0:
    n = int(input('INFORME UM VALOR: ')) 
    if n != 0:

        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('VOCÊ INSERIU {} NUMEROS PARES E {} NÚMEROS ÍMPARES.' . format(par, impar))