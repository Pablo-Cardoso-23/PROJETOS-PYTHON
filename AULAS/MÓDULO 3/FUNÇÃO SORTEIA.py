# DESAFIO 100 - FUNÇÃO DE SORTEAR NÚMEROS

import random

def sorteia(lista_sorteados):
    print()
    print('SORTEANDO ', end='')
    for numeros in range (1, 6):
        numeros_sorteados = random.randint(0, 10)
        lista_sorteados.append(numeros_sorteados)
    print(f'{len(lista_sorteados)} VALORES DA LISTA: ', end='')
    for valores in lista_sorteados:
        print(f'{valores} ', end='')
    print('PRONTO!')


def somaPar(lista_sorteados):
    somador = 0
    print()
    for numeros in lista_sorteados:
        if numeros % 2 == 0:
            somador += numeros
    print(f'SOMANDO OS VALORES PARES DE {lista_sorteados}, TEMOS {somador}')

lista =  list()
sorteia(lista)
somaPar(lista)