# DESAFIO 93 - ANÁLISE DE JOGADOR

dados_jogador = dict()
gols = list()

dados_jogador['nome'] = str(input('NOME DO JOGADOR: '))
total_partidas = int(input('INFORME QUANTAS PARTIDAS TEM O JOGADOR: '))

for partidas in  range (0, total_partidas):
    gols.append(int(input(f'INFORME QUANTOS GOLS O JOGADOR FEZ NA PARTIDA {partidas + 1}: ')))

dados_jogador['gols'] = gols[:]
dados_jogador['total'] = sum(gols)

print(dados_jogador)

print('-=' *36)

for titulo, dados in dados_jogador.items():
    print(f'O CAMPO {titulo} TEM O VALOR {dados}.'.upper())

print('-=' *36)

print(f'O JOGADOR {dados_jogador["nome"]} JOGOU {total_partidas} PARTIDAS'.upper())

partida = 1

for  gols in dados_jogador['gols']:
    print(f'   => NA PARTIDA {partida}, FEZ {gols}'.upper())
    partida += 1

print(f'FOI UM TOTAL DE {dados_jogador["total"]} GOLS.')