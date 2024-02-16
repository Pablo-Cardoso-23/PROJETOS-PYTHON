# DESAFIO 65 - DESCOBRINDO A MÉDIA, MAIOR E MENOR

soma_numeros = 0
contador = 0
maior_valor = 0
menor_valor = 0
feedback_user = 'S'

while feedback_user == 'S': 
        user_number = int(input('INFORME UM NÚMERO INTEIRO: '))
        soma_numeros += user_number
       
        feedback_user = str(input('DESEJA INSERIR OUTRO NÚMERO? [S/N] ==> ')) . upper()
        contador += 1
        if contador == 1:
            maior_valor = user_number
            menor_valor = user_number
        else:
            if user_number > maior_valor:
                maior_valor = user_number
            elif user_number < menor_valor:
                menor_valor = user_number
                 
        if feedback_user == 'N':
             media_numeros = soma_numeros/contador
             print('A MÉDIA ENTRE OS ({}) VALORES DIGITADOS É IGUAL A: ({:.1f})' . format(contador, media_numeros))
             print('O MAIOR VALOR DIGITADO PELO USUÁRIO FOI: ({})' . format(maior_valor))
             print('O MENOR VALOR DIGITADO PELO USUÁRIO FOI: ({})' . format(menor_valor))
             break