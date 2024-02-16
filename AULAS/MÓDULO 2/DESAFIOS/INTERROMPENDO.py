# DESAFIO 66 - INTERROMPENDO COM 999
contador_number = 0
soma_number = 0
number_user = int(input('DIGITE UM NÚMERO: '))

while True:
    if number_user != 999:
        soma_number += number_user
        contador_number += 1
        number_user = int(input('DIGITE UM NÚMERO: '))
    else :
        break

print(f'AO TODO FORAM DIGITADOS {contador_number} TOTALIZANDO A SOMA DE TODOS OS VALORES DIGITADOS, O RESULTADO É IGUAL A: {soma_number}')