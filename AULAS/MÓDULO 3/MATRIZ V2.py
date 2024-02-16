# DESAFIO 87 - MATRIZ V2

matriz = list()
coluna_zero = list()
coluna_um = list()
coluna_dois = list()
linha_contador = 0
total = 0

for contador in range(0, 3):
    coluna_zero.append(int(input(f'DIGITE UM NÚMERO PARA A POSIÇÃO [0, {linha_contador}]: ')))
    linha_contador += 1
    contador += 1

matriz.append(coluna_zero[:])
coluna_zero.clear()

linha_contador = 0
soma_valores_pares = 0
for contador in range(0,3):
    coluna_um.append(int(input(f'DIGITE UM NÚMERO PARA A POSIÇÃO [1, {linha_contador}]: ')))
    linha_contador += 1
    contador += 1

matriz.append(coluna_um[:])
coluna_um.clear()

linha_contador = 0
for contador in range(0,3):
    coluna_dois.append(int(input(f'DIGITE UM NÚMERO PARA A POSIÇÃO [2, {linha_contador}]: ')))
    linha_contador += 1
    contador += 1

matriz.append(coluna_dois[:])
coluna_dois.clear()

total_terceira_coluna = matriz[0][2] + matriz[1][2] + matriz[2][2]

for elementos in matriz[0]:
    if elementos % 2 == 0:
       total += (elementos)
for elementos in matriz[1]:
    if elementos % 2 == 0:
       total += (elementos)
for elementos in matriz[2]:
    if elementos % 2 == 0:
       total += (elementos)

print('-='*36)

print(f'[{matriz[0][0]:^5}] [{matriz[0][1]:^5}] [{matriz[0][2]:^5}]')
print(f'[{matriz[1][0]:^5}] [{matriz[1][1]:^5}] [{matriz[1][2]:^5}]')
print(f'[{matriz[2][0]:^5}] [{matriz[2][1]:^5}] [{matriz[2][2]:^5}]')

print('-='*36)

print(f'A SOMA DE TODOS OS VALORES PARES DIGITADOS É IGUAL A: {total}.')
print(f'A SOMA DOS VALORES DA TERCEIRA COLUNA É IGUAL A: {total_terceira_coluna}.')
print(f'O MAIOR NÚMERO NA SEGUNDA LINHA FOI {max(matriz[1])}.')

print('-='*36)