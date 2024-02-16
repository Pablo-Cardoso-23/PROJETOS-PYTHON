# DESAFIO 58 - ADIVINHANDO O NÚMERO QUE O COMPUTADOR PENSOU

import random
import emoji

print('---------')
print('P4 STORM')
print('---------')

print('\t\t----------INSTRUÇÕES----------')
print(emoji.emojize(':face_with_monocle: O COMPUTADOR PENSA EM UM NÚMERO ENTRE 0 E 10, SUA MISSÃO VAI SER A DE TENTAR ADIVINHAR'))

ia_opcao = random.randint(0,10)
user_opcao = int(input('INFORME SEU NÚMERO: '))
user_tentativas = 1

if(user_opcao == ia_opcao):
        user_tentativas += 1
        print(emoji.emojize(':robot: O COMPUTADOR ESCOLHEU O NÚMERO ({}) E VOCÊ ESCLOHEU O NÚMERO ({})' . format(ia_opcao, user_opcao)))
        print(emoji.emojize(':crown: PARABÉNS, VOCÊ GANHOU!'))
        print(emoji.emojize(':page_with_curl: TOTAL TENTATIVAS: {}' . format(user_tentativas)))

while (user_opcao != ia_opcao):
    user_tentativas += 1
    print('RESULTADO: VOCÊ ERROU!')
    if(ia_opcao > user_opcao):
         print('TENTE CHUTAR UMM POUCO MAIS ALTO!')
    else:
         print('TENTE CHUTAR UM POUCO MAIS BAIXO!')
    
    user_opcao = int(input('INFORME SEU NÚMERO NOVAMENTE: '))
    

    if(user_opcao == ia_opcao):
        print(emoji.emojize(':robot: O COMPUTADOR ESCOLHEU O NÚMERO ({}) :beaming_face_with_smiling_eyes: E VOCÊ ESCLOHEU O NÚMERO ({})' . format(ia_opcao, user_opcao)))
        print(emoji.emojize('PARABÉNS, VOCÊ GANHOU! :crown:'))
        print(emoji.emojize(':page_with_curl: TOTAL TENTATIVAS: {}' . format(user_tentativas)))
        break