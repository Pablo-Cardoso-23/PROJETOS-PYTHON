# DESAFIO 64 - TRATANDO VALORES INTEIROS

user_number = int(input('INFORME UM NÚMERO INTEIRO [999 PARA O PROGRAMA]: '))
contador = 0
soma_numeros = 0

while user_number != 999:
    if(user_number != 999):
        soma_numeros += user_number
        contador += 1
        user_number = int(input('INFORME UM NÚMERO INTEIRO [999 PARA O PROGRAMA]: '))
    else:
        break

print('VOCÊ DIGITOU {} NÚMEROS E A SOMA ENTRE ELES É IGUAL A: {}' . format(contador, soma_numeros))