# DESAFIO 44 - CALCULANDO O PREÇO DE UM PRODUTO

print('=========')
print('P4 STORM')
print('=========')

# ENTRADA DE DADOS

nome_produto = str(input('INSIRA O NOME DO PRODUTO: '))
valor_produto = float(input('INSIRA O VALOR DO PRODUTO: R$'))

# ESCOLHA

print('\t===================')
print('\tFORMA DE PAGAMENTO')
print('\t===================\n')
print('|1 - À VISTA DINEHIRO/CHEQUE|')
print('|2 - À VISTA NO CARTÃO      |')
print('|3 - EM ATÉ 2X NO CARTÃO    |')
print('|4 - 3X OU MAIS NO CARTÃO   |\n')

forma_pagamento = int(input('INFORME O NÚMERO CORRESPONDENTE A FORMA DE PAGAMENTO: '))

# RESULTADO

if forma_pagamento == 1:
    calculo_desconto = (valor_produto * 0.1)
    desconto = valor_produto - calculo_desconto
    print('CLIENTE GANHOU 10% DE DESCONTO!')
    print('VALOR TOTAL: R${:.2f}' . format(desconto))

elif forma_pagamento == 2:
    calculo_desconto = (valor_produto * 0.05)
    desconto = valor_produto - calculo_desconto
    print('CLIENTE GANHOU 5% DE DESCONTO!')
    print('VALOR TOTAL: R${:.2f}' . format(desconto))

elif forma_pagamento == 3:
    numero_parcelas = valor_produto / 2
    print('COMPRA PARCELADA EM 2X DE R${:.2f}' . format(numero_parcelas))
    print('VALOR TOTAL: R${:.2f}' . format(valor_produto))

elif forma_pagamento == 4:
    tempo_juros = int(input('INSIRA QUANTAS VEZES NO CARTÃO: '))
    calculo_juros = (0.2 * valor_produto) + valor_produto
    total_juros = calculo_juros / tempo_juros
    print('COMPRA PARCELADA EM {}X DE R${:.2f} COM JUROS' . format(tempo_juros, total_juros))
    print('COMPRA DE R${:.2f} TEM CUSTO FINAL DE R${:.2f}' . format(valor_produto, calculo_juros))