# DESAFIO 49 - TABUADA UTILIZANDO O LAÇO FOR

import emoji 
from time import sleep

print('\t==========')
print(emoji.emojize(':high_voltage:\t P4 STORM \t:high_voltage:'))
print('\t==========')

numero = int(input('INSIRA O NÚMERO: '))

print('===================================')
print(' VERIFIQUE A TABUADA DO NÚMERO {} ' . format(numero))
print('===================================\n')

print('|1 - ADIÇÃO       |')
print('|2- SUBTRAÇÃO     |')
print('|3 - MULTIPLICAÇÃO|')
print('|4 - DIVISÃO      |\n')

escolha_operacao = int(input('INSIRA O NÚMERO  DA OPERAÇÃO DESEJADA: '))

print(emoji.emojize('\n:clockwise_vertical_arrows: PROCESSANDO :clockwise_vertical_arrows:'))

if escolha_operacao == 1:
    for n in range(1, 11):
        resultado = numero + n
        print('{} + {} = {}' . format(numero, n, resultado))
elif escolha_operacao == 2:
    for n in range(1, 11):
        resultado = numero - n
        print('{} - {} = {}' . format(numero, n, resultado))
elif escolha_operacao == 3:
    for n in range(1,11):
        resultado = numero * n
        print('{} X {} = {}' . format(numero, n, resultado))
elif escolha_operacao == 4:
    for n in range(1, 11):
        resultado = numero / n
        print('{} / {} = {}' . format(numero, n, resultado))