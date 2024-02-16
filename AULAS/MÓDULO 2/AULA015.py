numero = 0
soma = 0
while True:
    numero = int(input('DIGITE UM NÚMERO: '))
    if numero == 999:
        break
    soma += numero

print(f'A SOMA VALE {soma}')