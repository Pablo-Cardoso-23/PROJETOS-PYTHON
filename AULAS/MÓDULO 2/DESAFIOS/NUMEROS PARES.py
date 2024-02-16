# DESAFIO 47 - NÚMEROS PARES DE 1 A 50

import emoji
from time import sleep

print('\t==========')
print(emoji.emojize(':high_voltage:\t P4 STORM \t:high_voltage:'))
print('\t==========')

# CÁLCULO

print('========================')
print(' LISTA DE NÚMEROS PARES')
print('========================')
sleep(1)

for c in range(2, 51, 2):
    resto_divisao = c % 2

    if resto_divisao == 0:
        print('O NÚMERO {} É PAR!' . format(c))
        sleep(0.5)
print(emoji.emojize('\n:check_mark_button: FIM DA VERIFICAÇÃO :check_mark_button:'))