# DESAFIO 52 - DESVENDANDO UM NÚMERO PRIMO

print('=========')
print('P4 STORM')
print('=========\n')

numero_verificar = int(input('INFORME O NÚMERO: '))

if numero_verificar % 2 != 0 or numero_verificar == 2:
    print('O NÚMERO {} É PRIMO.' . format(numero_verificar))
else: 
    print('O NÚMERO {} NÃO É PRIMO.' . format(numero_verificar))


# UTILIZANDO FOR
    
numero_entrada = int(input('INFORME O NÚMERO: '))
total = 0

for n in range(1, numero_entrada + 1):
    
    if numero_entrada % n == 0:
        print('\033[34m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print('{} ' . format(n), end='')

print('\nO NÚMERO ({}) FOI DIVISÍVEL ({}) VEZES.' . format(numero_entrada, total))
if total == 2:
    print('O NÚMERO {} É PRIMO!' . format(numero_entrada))
else:
    print('O NÚMERO {} NÃO É PRIMO' . format(numero_entrada))