# DESAFIO 88 - SORTEANDO NÚEMEROS MEGA SENA

import random
from time import sleep

lista_numeros_aleatorios = list()
jogo_gerado = list()

print('-='*36)
print('MEGA SENA'.center(60))
print('-='*36)

usuario_numeros = int(input('DIGITE O NÚMERO DE JOGOS QUE SERÃO SORTEADOS: '))
jogos_contador = 1

while jogos_contador <= usuario_numeros:
    contador = 0
    while True:
        numeros_aleatorios = random.randint(1,60)

        if numeros_aleatorios not in lista_numeros_aleatorios:
            lista_numeros_aleatorios.append(numeros_aleatorios)
            contador += 1
        if contador >= 6:
            break
    
    jogos_contador += 1
    lista_numeros_aleatorios.sort()
    jogo_gerado.append(lista_numeros_aleatorios[:])
    lista_numeros_aleatorios.clear()

print('\n')

print('-='*36)
print('NÚMEROS ESCOLHIDOS'.center(60))
print('-='*36)

for indice, lista in enumerate(jogo_gerado):
    print(f'JOGO {indice + 1}: {lista}')
    sleep(1)

print('-='*36)