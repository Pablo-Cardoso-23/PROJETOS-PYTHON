# DESAFIO 67 - TABUADA COM WHILE
print('TABUADA')

contador = 0
numero_usuario = int(input('DIGITE O NÚMERO: '))

while True:
        
        if numero_usuario > 0:
            print('ESCOLHA A OPERAÇÃO QUE DESEJA REALIZAR:')
            print('[1] - SOMA')
            print('[2] - SUBTRAÇÃO')
            print('[3] - MULTIPLICAÇÃO')
            print('[4] - DIVISÃO')

            escolha_da_operacao = int(input('DIGITE O NÚEMRO DO SERVIÇO: '))

            if escolha_da_operacao == 1:
                while contador < 10:
                    contador += 1
                    soma_numeros = numero_usuario + contador
                    print(f'{numero_usuario} + {contador} = {soma_numeros}')
                contador = 0
            elif escolha_da_operacao == 2:
                while contador < 10:
                    contador += 1
                    subtrair_numeros = contador - numero_usuario
                    print(f'{contador} - {numero_usuario} = {subtrair_numeros}')
                contador = 0
            elif escolha_da_operacao == 3:
                while contador < 10:
                    contador += 1
                    multiplicar_numeros = numero_usuario * contador
                    print(f'{numero_usuario} x {contador} = {multiplicar_numeros}')
                contador = 0
            elif escolha_da_operacao == 4:
                while contador < 10:
                    contador += 1
                    dividir_numeros = contador / numero_usuario
                    print(f'{contador} / {numero_usuario} = {dividir_numeros}')
                contador = 0
            
            numero_usuario = int(input('INFORME UM NÚMERO: '))
        
        elif numero_usuario < 0:
            break
                    