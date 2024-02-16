# DESAFIO 103 - FUNÇÃO DE EXIBIR FICHA DE UM JOGADOR

print()
print('-'*30)

def ficha(nome='<desconhecido>', gols=0):

    print(f'O JOGADOR {nome} FEZ {gols} GOL(S) NO CAMPEONATO')
    

nome_jogador = str(input('NOME DO JOGADOR: '))
numero_gols = str(input('NÚMERO DE GOLS: '))

if numero_gols.isnumeric():
    numero_gols = int(numero_gols)
else:
    numero_gols = 0

if nome_jogador.strip() == '':
    ficha(gols=numero_gols)
else:
    ficha(nome_jogador, numero_gols)
