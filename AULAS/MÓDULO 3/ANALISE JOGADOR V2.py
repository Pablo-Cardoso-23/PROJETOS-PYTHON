# DESAFIO 93 - ANÁLISE DE JOGADORES

dados_jogadores = dict()
quantidade_gols = list()
listagem_dados = list()

while True:
    print('-'*50)
    dados_jogadores.clear()
    dados_jogadores['nome'] = str(input('NOME DO JOGADOR: ')).upper()
    quantidade_partidas = int(input('INFORME QUANTAS PARTIDAS TEM O JOGADOR: '))
    quantidade_gols.clear()
    
    for partidas in range(0, quantidade_partidas):
        quantidade_gols.append(int(input(f'INFORME QUANTOS GOLS O JOGACDOR FEZ NA PARTIDA {partidas + 1}: ')))

    dados_jogadores['gols'] = quantidade_gols[:]
    dados_jogadores['total'] = sum(quantidade_gols)
    listagem_dados.append(dados_jogadores.copy())

    print('-'*50)
    feedback_usuario = str(input('DESEJA CADASTRAR MAIS ALGUM JOGARDOR? [S/N]: ')).upper()

    while feedback_usuario != 'S' and feedback_usuario != 'N':
        print('ERRO, ESSE COMANDO NÃO É VÁLIDO!')
        feedback_usuario = str(input('DESEJA CADASTRAR MAIS ALGUM JOGARDOR? [S/N]: ')).upper()
    
    if feedback_usuario == 'N':
        break

print('-='*50)
print('COD', end='')
for itens in dados_jogadores.keys():
    print(f'{itens:^12}'.upper(), end='')

print()

for indice, dados_jogador in enumerate(listagem_dados):
    print(f'{indice}     {dados_jogador["nome"]}     {dados_jogador["gols"]}        {dados_jogador["total"]}')

while True:
    busca = int(input('DESEJA EXIBIR OS DADOS DE QUAL JOGADOR? '))

    if busca == 999:
        break
    if busca >= len(dados_jogadores):
        print(f'ERRO, NÃO EXISTE JOGADOR COM O CÓDIGO {busca}!')
    else:
        print(f'--LEVANTAMENTO DE ESTATÍSTICAS DE {listagem_dados[busca]["nome"]}')
        for indice, gols in enumerate(listagem_dados[busca]['gols']):
            print(f'   NO JOGO {indice + 1} O JOGADOR FEZ {gols}') 
    print('-'*50)
print('ENCERRADO')