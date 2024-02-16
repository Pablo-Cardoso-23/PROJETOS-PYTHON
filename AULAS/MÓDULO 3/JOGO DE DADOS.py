# DESAFIO 91 - JOGANDO DADOS

import random
from time import sleep
from operator import itemgetter

numeros_jogadores = {'jogador1': random.randint(1,6),
                     'jogador2': random.randint(1,6),
                     'jogador3': random.randint(1,6),
                     'jogador4': random.randint(1,6)}
print()
print('VALORES SORTEADOS:')

for jogadores, numeros in numeros_jogadores.items():
    print(f'   O {jogadores.upper()} TIROU {numeros}')
    sleep(1)

print()
ranking = dict()
ranking = sorted(numeros_jogadores.items(), key=itemgetter(1), reverse= True)
print('RANKING DOS JOGADORES:')
posicao = 1
for jogadores, numeros in ranking:
    print(f'   {posicao}º LUGAR: {jogadores.upper()} COM {numeros}')
    sleep(1)
    posicao += 1