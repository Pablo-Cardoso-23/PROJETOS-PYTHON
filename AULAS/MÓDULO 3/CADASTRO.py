# DESAFIO 92 - CADASTRANDO E VERIFICANDO CARTEIRA DE TRABALHO

from datetime import date

ano_atual = date.today().year

dados_cadastrado = dict()

dados_cadastrado['nome'] = str(input('INFORME O NOME: '))
dados_cadastrado['idade'] = int(input('INFORME O ANO DE NASCIMENTO: '))
dados_cadastrado['ctps'] = int(input('INFORME O NÚMERO DA CARTEIRA DE TRABALHO(0 NÃO TEM): '))

idade_cadastrado = ano_atual - dados_cadastrado['idade']
dados_cadastrado['idade'] = idade_cadastrado

if dados_cadastrado['ctps'] == 0:
    print()
    print('-='*36)
elif dados_cadastrado['ctps'] != 0:
    print()
    print('-='*36)
    dados_cadastrado['anoContratado'] = int(input('INFORME O ANO DE CONTRATAÇÃO: '))
    dados_cadastrado['salario'] = float(input('INFORME O SALÁRIO: R$ ')) 
    dados_cadastrado['aposentadoria'] = dados_cadastrado['idade'] + (dados_cadastrado['anoContratado'] + 35) - ano_atual

idade_cadastrado = ano_atual - dados_cadastrado['idade']

for titulos, dados in dados_cadastrado.items():
    print()
    print(f'{titulos} TEM O VALOR DE {dados}'.upper())