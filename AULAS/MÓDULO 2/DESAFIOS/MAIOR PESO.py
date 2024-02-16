# DESAFIO 55 - VERIFICANDO A PESSOA COMM O MAIOR PESO

import emoji
from time import sleep

print('=========')
print('P4 STORM')
print('=========')

maior_peso = 0
menor_peso = 0

for p in range(1,6):
    informar_peso = float(input('INFORME O PESO DA {}ª PESSOA: ' . format(p)))

    if p == 1:
        maior_peso = informar_peso
        menor_peso = informar_peso
    else:
        if informar_peso > maior_peso:
            maior_peso = informar_peso

        elif informar_peso < menor_peso:
            menor_peso = informar_peso

print(emoji.emojize('\n:clockwise_vertical_arrows: ANALISANDO PESOS :clockwise_vertical_arrows:'))
sleep(1)

print(emoji.emojize(':face_with_open_mouth: MAIOR PESO: {:.1f}Kg' . format(maior_peso)))
print(emoji.emojize(':neutral_face: MENOR PESO: {:.1f}Kg' . format(menor_peso)))