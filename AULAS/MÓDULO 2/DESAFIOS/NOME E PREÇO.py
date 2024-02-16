# DESAFIO 70 - SALVANDO PREÇO E NOME

from time import sleep

print('--------------')
print('LOJA P4 STORM')
print('--------------')

contador = 0
total_compras = 0
produtos_mais_mil = 0
produto_mais_barato = ''
valor_produto_barato = 0

while True:
    nome_produto = str(input('INSIRA O NOME DO PRODUTO: '))
    valor_produto = float(input('INFORME O VALOR DO PRODUTO: R$'))
    contador += 1
    
    total_compras += valor_produto

    if valor_produto > 1000:
        produtos_mais_mil += 1

    if contador == 1:
        produto_mais_barato = nome_produto
        valor_produto_barato = valor_produto

    elif valor_produto < valor_produto_barato:
        produto_mais_barato = nome_produto
        valor_produto_barato = valor_produto

    feedback_usuario = str(input('DESEJA ADICIONAR MAIS ALGUM PRODUTO [S/N]? ')) . upper()

    while(feedback_usuario != 'S') and (feedback_usuario != 'N'):
        feedback_usuario = str(input('DESEJA ADICIONAR MAIS ALGUM PRODUTO [S/N]? ')) . upper()

    if feedback_usuario == 'N':
        break
print('\n-------------------')
print(' COMPRA FINALIZADA')
print('-------------------\n')
sleep(1)
print('\t---------------')
print('\t LOJA P4 STORM')
print('\t---------------\n')
print(f'VALOR TOTAL DA COMPRA: R${total_compras :.2f}')
print(f'QUANTIDADE DE PRODUTOS QUE CUSTAM MAIS DE MIL REAIS: {produtos_mais_mil}')
print(f'NOME DO PRODUTO MAIS BARATO: {produto_mais_barato} QUE CUSTA R${valor_produto_barato :.2f}')
