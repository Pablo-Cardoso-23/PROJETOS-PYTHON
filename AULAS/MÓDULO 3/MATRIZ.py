# DESAFIO 86 - CRIANDO UMA MATRIZ

principal = list()
coluna_zero = list()
coluna_um = list()
coluna_dois = list()
posicao = 0

for contador in range(0,3):
    coluna_zero.append(int(input(f'DIGITE UM VALOR PARA A POSIÇÃO [0,{posicao}]: ')))
    posicao += 1
    contador += 1

principal.append(coluna_zero[:])
coluna_um.clear()

posicao = 0
for contador in range(0,3):
    coluna_um.append(int(input(f'DIGITE UM VALOR PARA A POSIÇÃO [1,{posicao}]: ')))
    posicao += 1
    contador += 1

principal.append(coluna_um[:])
coluna_um.clear()

posicao = 0
for contador in range(0,3):
    coluna_dois.append(int(input(f'DIGITE UM VALOR PARA A POSIÇÃO [2,{posicao}]: ')))
    posicao += 1
    contador += 1

principal.append(coluna_dois[:])
coluna_dois.clear()

print('-='*45)

print(f'[{principal[0][0]:^5}] [{principal[0][1]:^5}] [{principal[0][2]:^5}]')
print(f'[{principal[1][0]:^5}] [{principal[1][1]:^5}] [{principal[1][2]:^5}]')
print(f'[{principal[2][0]:^5}] [{principal[2][1]:^5}] [{principal[2][2]:^5}]')