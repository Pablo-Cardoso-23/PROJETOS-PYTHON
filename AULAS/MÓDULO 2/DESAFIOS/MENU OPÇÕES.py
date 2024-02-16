# DESAFIO 59 - CRIANDO UM MENU DE OPÇÕES

from time import sleep

print('---------')
print('P4 STORM') 
print('---------')

novo_valor1 = 0
novo_valor2 = 0
opcao = 0

primeiro_valor = int(input('INFORME UM NÚMERO: '))
segundo_valor = int(input('INFORME OUTRO NÚMERO: '))

while opcao != 5:

    print('-'*25)
    print('\tMENU')
    print('-'*25)

    print('|[1] - SOMAR           |')
    print('|[2] - MULTIPLICAR     |')
    print('|[3] - MAIOR           |')
    print('|[4] - NOVOS NÚMEROS   |')
    print('|[5] - SAIR DO PROGRAMA|\n')

    opcao = int(input('ESCOLHA UMA DAS OPÇÕES: '))

    if(opcao == 1):
        somar_valores = primeiro_valor + segundo_valor
        print('\nA SOMA ENTRE ({}) E ({}) É IGUAL A: ({})' . format(primeiro_valor, segundo_valor, somar_valores))
        print('='*40)
        sleep(2)
    elif(opcao == 2):
        multiplicar_valores = primeiro_valor * segundo_valor
        print('\nA MULTIPLICAÇÃO ENTRE ({}) E ({}) É IGUAL A: ({})' . format(primeiro_valor, segundo_valor, multiplicar_valores))
        print('='*40)
        sleep(2)
    elif(opcao == 3):
        if(primeiro_valor > segundo_valor):
            print('\nCOMPARANDO O NÚMERO ({}) COM O NÚMERO ({}) O MAIOR NÚMERO É: ({}).' . format(primeiro_valor, segundo_valor, primeiro_valor))
            print('='*40)
            sleep(2)
        elif(primeiro_valor < segundo_valor):
            print('\nCOMPARANDO O NÚMERO ({}) COM O NÚMERO ({}) O MAIOR NÚMERO É: ({}).' . format(primeiro_valor, segundo_valor, segundo_valor))
            print('='*40)
            sleep(2)
        elif(primeiro_valor ==  segundo_valor):
            print('\nCOMPARANDO O NÚMERO ({}) COM O NÚMERO ({}) TEMOS A CONCLUSÃO QUE SÃO NÚMEROS IGUAIS.' . format(primeiro_valor, segundo_valor))
            print('='*40)
            sleep(2)
    elif(opcao == 4):
        novo_valor1 = int(input('INFORME UM NÚMERO: '))
        primeiro_valor = novo_valor1
        novo_valor2 = int(input('INFORME OUTRO NÚMERO: '))
        segundo_valor = novo_valor2
        print('='*40)
        sleep(1)

    elif(opcao == 5):
        print('PROGRAMA FINALIZADO!')
        break
