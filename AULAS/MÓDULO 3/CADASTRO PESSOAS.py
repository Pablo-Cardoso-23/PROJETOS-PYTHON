# DESAFIO 94 - CADASTRANDO PESSOAS 

dados_clientes = dict()
listagem_dados = list()
idade = 0

while True:

    dados_clientes['nome'] = str(input('INFORME O NOME: ')).upper()
    dados_clientes['sexo'] = str(input('INFORME O SEXO [M/F]: ')).upper()

    while dados_clientes['sexo'] != 'M' and dados_clientes['sexo'] != 'F':
        print('DÍGITO INVÁLIDO, INFORME UM DADO VÁLIDO!')
        dados_clientes['sexo'] = str(input('INFORME O SEXO [M/F]: ')).upper()
    
    dados_clientes['idade'] = int(input('INFORME A IDADE: '))
    idade += dados_clientes['idade']

    listagem_dados.append(dados_clientes.copy())
    feedback_usuario = str(input('DESEJA CADASTRAR MAIS ALGUÉM?[S/N]: ')).upper()

    while feedback_usuario != 'S' and feedback_usuario != 'N':
        print('DÍGITO INVÁLIDO, INFORME UM COMANDO VÁLIDO!')
        feedback_usuario = str(input('DESEJA CADASTRAR MAIS ALGUÉM?[S/N]: ')).upper()

    if feedback_usuario == 'N':
        break

media_idade = idade / len(listagem_dados)

print()
print('-='*36)

print(f'=> O GRUPO TEM {len(listagem_dados)} PESSOAS.')
print(f'=> A MÉDIA DE IDADE É DE: {media_idade :.2f} ANOS.')
print('=> AS MULHERES CADASTRADAS FORAM: ', end='')

for dados_clientes in listagem_dados:
    if dados_clientes['sexo'] == 'F':
        print(f'{dados_clientes["nome"]}... ', end='')

if 'F' not in dados_clientes['sexo']:
    print('NÃO HÁ DADOS DE MULHERES CADASTRADOS.')

print()

print('=> LISTA DAS PESSOAS QUE ESTÃO ACIMA DA MÉDIA DE IDADE:')
print()
for dados_clientes in listagem_dados:
    if dados_clientes['idade'] > media_idade:
        print(f'NOME = {dados_clientes["nome"]}; SEXO = {dados_clientes["sexo"]}; IDADE = {dados_clientes["idade"]}')

print('-='*36)
print()
print('<<PROGRAMA ENCERRADO>>')