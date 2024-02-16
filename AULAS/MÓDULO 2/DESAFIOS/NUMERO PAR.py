# DESAFIO 50 - SOMA DE NÚMEROS INTEIROS PARES

print('=========')
print('P4 STORM')
print('=========')

soma = 0

for p in range(1, 7):
    numeros = int(input('INSIRA UM NÚMERO: '))
    par = numeros % 2
    if par == 0:
        print('\033[0;30;42m True \033[m  {} É UM NÚMERO PAR!' . format(numeros))
        if par == 0:
            soma += numeros
    else:
        print('\033[0;30;41m False \033[m  {} NÃO É UM NÚMERO PAR(DESCONSIDERADO)' . format(numeros))

print('SOMA DOS NÚMEROS PARES: {}' . format(soma))