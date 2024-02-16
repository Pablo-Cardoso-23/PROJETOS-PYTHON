# DESAFIO 84 - CRIANDO LISTAS E VERIFICANDO O PESO

lista_pessoas = list()
dados_gerais = list()
maiores_pesos = 0
menores_pesos = 0

while True:
    lista_pessoas.append(str(input('INFORME SEU NOME: ')))
    lista_pessoas.append(float(input('INFORME SEU PESO: ')))

    if len(dados_gerais) == 0:
        maiores_pesos = lista_pessoas[1]
        menores_pesos = lista_pessoas[1]
    else:
        if lista_pessoas[1] > maiores_pesos:
            maiores_pesos = lista_pessoas[1]
        elif lista_pessoas[1] < menores_pesos:
            menores_pesos = lista_pessoas[1]

    dados_gerais.append(lista_pessoas[:])
    lista_pessoas.clear()

    feedback_usuario = str(input('DESEJA CADASTRAR MAIS ALGUÉM [S/N]? ')).upper()

    while feedback_usuario != 'S' and feedback_usuario != 'N':
        feedback_usuario = str(input('DESEJA CADASTRAR MAIS ALGUÉM [S/N]? ')).upper()

    if feedback_usuario == 'N':
        break   

print(f'AO TODO FORAM CADASTRADAS {len(dados_gerais)} PESSOAS.')
print(f'O MAIOR PESO CADASTRADOS {maiores_pesos}Kg. PESOS DE: ', end='')
for pessoas_cadastradas in dados_gerais:
    if pessoas_cadastradas[1] == maiores_pesos:
        print(f'{pessoas_cadastradas[0]}...', end='')
print()
print(f'O MENOR PESO FOI DE {menores_pesos}Kg. Pesos de: ', end='')
for pessoas_cadastradas in dados_gerais:
    if pessoas_cadastradas[1] == menores_pesos:
        print(f'{pessoas_cadastradas[0]}...', end= '')
print()