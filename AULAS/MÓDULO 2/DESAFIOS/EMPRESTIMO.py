# DESAFIO 36 - APROVANDO EMPRÉSTIMO

print ('==============')
print('BANCO P4 STORM')
print ('==============')

# ENTRADA DE DADOS
valor_imovel = float(input('INSIRA O VALOR DO IMÓVEL: R$'))
salario = float(input('INSIRA SEU SALÁRIO: R$'))
ano_pagamento = int(input('INFORME EM QUANTOS ANOS DESEJA PAGAR: '))

# CÁLCULO
numero_prestacoes = ano_pagamento * 12
valor_limite_prestacoes = salario * 0.3
valor_prestacoes = valor_imovel / numero_prestacoes

# VERIFICAÇÃO DE APROVAÇÃO
if valor_prestacoes > valor_limite_prestacoes:
    print('PEDIDO DE EMPRÉSTIMO NEGADO, POIS O VALOR DAS PRESTAÇÕES EXCEDE O VALOR MÁXIMO DE 30% DO SALÁRIO DO QUE O CLIENTE PODE PAGAR!')
else:
    print('PEDIDO DE EMPRÉSTIMO APROVADO, O CLIENTE PODE PROSSEGUIR COM SEU PEDIDO!')
    print('O VALOR DAS PRESTAÇÕES POSSUEM O VALOR DE: R${:.2f}' . format(valor_prestacoes))