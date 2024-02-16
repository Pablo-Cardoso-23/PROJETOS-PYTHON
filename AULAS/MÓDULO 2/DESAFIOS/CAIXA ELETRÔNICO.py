# DESAFIO 71 - CAIXA ELETRÔNICO
print('\t----------------')
print('\t BANCO P4 STORM')
print('\t----------------\n')

import math

operacao_finalizada = True

while operacao_finalizada == True:
    print('CÉDULAS DISPONÍVEIS: R$50, R$20, R$10 E R$1')
    retirar_quantia = int(input('INFORME O VALOR DE RETIRADA: R$'))

    resto_divisao = retirar_quantia

    total_cedulas_50 = resto_divisao / 50
    resto_divisao %= 50
    total_cedulas_20 = resto_divisao / 20
    resto_divisao %= 20
    total_cedulas_10 = resto_divisao / 10
    resto_divisao %= 10
    total_cedulas_1 = resto_divisao / 1
    resto_divisao %= 1

    total_cedulas_50 = math.trunc(total_cedulas_50)
    total_cedulas_20 = math.trunc(total_cedulas_20)
    total_cedulas_10 = math.trunc(total_cedulas_10)
    total_cedulas_1 = math.trunc(total_cedulas_1)

    operacao_finalizada = False

    print('\n\t----------------')
    print('\t BANCO P4 STORM')
    print('\t-----------------\n')
    print('SERÁ SOLICITADO AS SEGUINTES CÉDULAS:\n')
    if total_cedulas_50 > 0:
        print(f'{total_cedulas_50} NOTAS DE R$50')
    if total_cedulas_20 > 0:
        print(f'{total_cedulas_20} NOTAS DE R$20')
    if total_cedulas_10 > 0:
        print(f'{total_cedulas_10} NOTAS DE R$10')
    if total_cedulas_1 > 0:
        print(f'{total_cedulas_1} NOTAS DE R$1')
    