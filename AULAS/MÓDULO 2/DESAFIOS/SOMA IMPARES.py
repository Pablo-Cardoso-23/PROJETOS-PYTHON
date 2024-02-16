# DESAFIO 48 - SOMA DE NÚMEROS ÍMPARES MÚLTIPLOS DE 3

import emoji 

print('\t==========')
print(emoji.emojize(':high_voltage:\t P4 STORM \t:high_voltage:'))
print('\t==========')


soma = 0
cont = 0

for i in range(1, 501, 2):
    impar = i % 2
    if impar == 1:
         print('NÚMEROS ÍMPARES: {}' . format(i))
         if i % 3 == 0:
            cont += 1
            soma = soma + i

print('SOMA DE TODOS OS NÚMEROS MÚLTIPLOS  DE TRÊS ({}): {}' . format(cont,soma))