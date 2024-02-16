# DESAFIO 74 - UTILIZANDO TUPLAS COM NÚMEROS ALEATÓRIOS

import random

primeiro_numero = random.randint(0,10)
primeiro_numero_tupla = (primeiro_numero,)

segundo_numero = random.randint(0,10)
segundo_numero_tupla = (segundo_numero,)

terceiro_numero = random.randint(0,10)
terceiro_numero_tupla = (terceiro_numero,)

quarto_numero = random.randint(0,10)
quarto_numero_tupla = (quarto_numero,)

quinto_numero = random.randint(0,10)
quinto_numero_tupla = (quinto_numero, )

numeros_sorteados = primeiro_numero_tupla + segundo_numero_tupla + terceiro_numero_tupla + quarto_numero_tupla +  quinto_numero_tupla

maior_numero = sorted(numeros_sorteados)
menor_numero = sorted(numeros_sorteados)

print(f'OS VALORES SORTEADOS FORAM: {numeros_sorteados}')

print(f'O MAIOR NÚMERO FOI: {maior_numero[4]}')
print(f'O MENOR NÚMERO FOI: {menor_numero[0]}')
