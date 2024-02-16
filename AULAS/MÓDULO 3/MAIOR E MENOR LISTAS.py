# DESAFIO 78 - MAIOR E MENOR UTILIZANDO LISTAS

numeros_lista = []

maior_valor = 0
menor_valor = 0

for valores in range(0,5):
    numeros_lista.append(int(input(f'DIGITE UM NÚMERO PARA A POSIÇÃO {valores}: ')))
    if valores == 0:
        maior_valor = numeros_lista[valores]
        menor_valor = numeros_lista[valores]
    else:
        if numeros_lista[valores] > maior_valor:
            maior_valor = numeros_lista[valores]
        if numeros_lista[valores] < menor_valor:
            menor_valor = numeros_lista[valores]


print('-=' *31)
print(f'VOCÊ DIGITOU OS VALORES: {numeros_lista}')

print(f'O MAIOR VALOR DIGITADO FOI: {maior_valor} NAS POSIÇÕES: ', end='')
for posicao, valores in enumerate(numeros_lista):
    if valores == maior_valor:
        print(f'{posicao}...', end='')
print()

print(f'O MENOR VALOR DIGITADO FOI: {menor_valor} NAS POSIÇÕES: ', end='')
for posicao, valores in enumerate(numeros_lista):
    if valores == menor_valor:
        print(f'{posicao}...', end='')
print()