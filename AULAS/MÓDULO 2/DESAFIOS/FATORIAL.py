# DESAFIO 60 - FATORIAL DE UM NÚMERO

from time import sleep

user_numero = int(input('INFORME O NÚMERO: '))
reducao = user_numero 
fatorial = 1

while reducao > 1:

    fatorial *= reducao
    reducao -= 1
    print('===>',fatorial)
    sleep(1)
    
    if(reducao <= 1):
        print('\nO FATORIAL DE ({}) É IGUAL A: ({})' . format(user_numero, fatorial))
        break