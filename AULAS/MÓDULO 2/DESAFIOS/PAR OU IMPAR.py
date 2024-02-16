# DESSAFIO 68 - PAR OU ÍMPAR COM WHILE
import random
from time import sleep

vitorias_consecutivas = 0

while True:
    print('ESCOLHA UM NÚMERO DE 0 A 10 E DECIDA SE VOCÊ VAI ESCOLHER PAR OU IMPAR')
    resultado = ''
    numero_usuario = int(input('ESCOLHA SEU NÚMERO: '))
    escolha_usuario = str(input('ESCOLHA SUA OPÇÃO [PAR OU IMPAR]: ')) . upper()

    numero_computador = random.randint(0, 10)
    escolha_computador = ''
    
    if escolha_usuario == 'PAR':
        escolha_computador = 'IMPAR'
    else:
        escolha_computador = 'PAR'

    analise_resultados = (numero_usuario + numero_computador) % 2

    if analise_resultados == 0 and escolha_usuario == 'PAR':
        resultado = 'VITÓRIA'
        escolha_computador = 'IMPAR'
        print(f'O COMPUTADOR ESCOLHEU O NÚMERO {numero_computador} E VOCÊ ESCOLHEU O NÚMERO {numero_usuario} SOMANDO TUDO ISSO É UM NÚMERO PAR')
        sleep(1)
        print(f'O RESULTADO FOI {resultado}')
        vitorias_consecutivas += 1
        print(f'VITÓRIAS CONSECUTIVAS: {vitorias_consecutivas}')
    elif analise_resultados == 1 and escolha_usuario == 'IMPAR':
        resultado = 'VITÓRIA'
        escolha_computador = 'PAR'
        print(f'O COMPUTADOR ESCOLHEU O NÚMERO {numero_computador} E VOCÊ ESCOLHEU O NÚMERO {numero_usuario} SOMANDO TUDO ISSO É UM NÚMERO IMPAR')
        sleep(1)
        print(f'O RESULTADO FOI {resultado}')
        vitorias_consecutivas += 1
        print(f'VITÓRIAS CONSECUTIVAS: {vitorias_consecutivas}')
    else:
        resultado = 'DERROTA'
        break

print(f'O COMPUTADOR ESCOLHEU O NÚMERO {numero_computador} E VOCÊ ESCOLHEU O NÚMERO {numero_usuario} SOMANDO TUDO ISSO É UM NÚMERO {escolha_computador}')
sleep(1)
print(f'O RESULTADO FOI {resultado}')
print(f'VITÓRIAS CONSECUTIVAS: {vitorias_consecutivas}')
