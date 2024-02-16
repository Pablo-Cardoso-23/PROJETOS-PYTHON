# DESAFIO 75 - INSERINDO NÚMEROS EM TUPLAS

entrada_numeros = (int(input('DIGITE UM NÚMERO: ')),
int(input('DIGITE OUTRO NÚMERO: ')), 
int(input('DIGITE MAIS UM NÚMERO: ')),
int(input('DIGITE O ÚLTIMO NÚMERO: ')))

print(f'VOCÊ DIGITOU OS NÚMEROS {entrada_numeros}')
print(f'O NÚMERO 9 APARECEU {entrada_numeros.count(9)} VEZES')
print(f'O NÚMERO 3 APARECEU NA POSIÇÃO: {entrada_numeros.index(3)+1}')
print('OS NÚMEROS PARES DIGITADOS FORAM: ', end='')

for dividir_numeros in entrada_numeros:
    if dividir_numeros % 2 == 0:
        print(dividir_numeros, end= ' ')