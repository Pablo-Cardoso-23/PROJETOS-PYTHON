# DESAFIO 45 - JOGANDO JOKENPÔ

# IMPORTANDO BIBLIOTECAS
import random
import emoji
from time import sleep

print('\t============')
print(emoji.emojize('\t:high_voltage:P4 STORM:high_voltage:'))
print('\t============\n')

print('\t===============')
print(emoji.emojize('\t:nerd_face: INSTRUÇÕES:nerd_face:'))
print('\t===============')
print(emoji.emojize('\t1- PEDRA  :rock:'))
print(emoji.emojize('\t2- PAPEL  :page_facing_up:'))
print(emoji.emojize('\t3- TESOURA :scissors:\n'))
print(emoji.emojize(':robot: VOCÊ DIGITA UM NÚMERO CORRESPONDENTE AO ITEM ESCOLHIDO E EU INFORMO O MEU... NO FIM SÓ HÁ UM VENCEDOR!\n'))

# ESCOLHAS

ia_opcao = random.randint(1,3)
player_opcao = int(input('INSIRA O NÚMERO CORRESPONDENTE A SUA OPÇÃO: '))

# PROCESSAR

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)

# RESULTADO
print('\n\t===========================')
print(emoji.emojize('\t:crossed_swords:\tRESULTADO\t:crossed_swords:'))
print('\t===========================\n')

# PEDRA
if ia_opcao == 1 and player_opcao == 3:
    print(emoji.emojize('O COMPUTADOR ESCOLHEU :rock:  E VOCÊ ESCOLHEU :scissors:'))
    print(emoji.emojize('O COMPUTADOR GANHOU!:robot::crown:'))
    
elif player_opcao == 1 and ia_opcao == 3:
    print(emoji.emojize('VOCÊ ESCOLHEU :rock:  E O COMPUTADOR ESCOLHEU :scissors:'))
    print(emoji.emojize('VOCÊ GANHOU!:grinning_face_with_smiling_eyes::crown:'))

# PAPEL
elif ia_opcao == 2 and player_opcao == 1:
    print(emoji.emojize('O COMPUTADOR ESCOLHEU :page_facing_up:  E VOCÊ ESCOLHEU :rock:'))
    print(emoji.emojize('O COMPUTADOR GANHOU!:robot::crown:'))
    
elif player_opcao == 2 and ia_opcao == 1:
    print(emoji.emojize('VOCÊ ESCOLHEU :page_facing_up:  E O COMPUTADOR ESCOLHEU :rock:'))
    print(emoji.emojize('VOCÊ GANHOU!:grinning_face_with_smiling_eyes::crown:'))

# TESOURA
elif ia_opcao == 3 and player_opcao == 2:
    print(emoji.emojize('O COMPUTADOR ESCOLHEU :scissors:  E VOCÊ ESCOLHEU :page_facing_up:'))
    print(emoji.emojize('O COMPUTADOR GANHOU!:robot::crown:'))
    
elif player_opcao == 3 and ia_opcao == 2:
    print(emoji.emojize('VOCÊ ESCOLHEU :scissors:  E O COMPUTADOR ESCOLHEU :page_facing_up:'))
    print(emoji.emojize('VOCÊ GANHOU!:grinning_face_with_smiling_eyes::crown:'))

# EMPATE
elif ia_opcao == 1 and player_opcao == 1:
    print(emoji.emojize('O COMPUTADOR ESCOLHEU :rock:  E VOCÊ ESCOLHEU :rock:'))
    print(emoji.emojize('EMPATE:white_flag:'))

elif ia_opcao == 2 and player_opcao == 2:
    print(emoji.emojize('O COMPUTADOR ESCOLHEU :page_facing_up:  E VOCÊ ESCOLHEU :page_facing_up:'))
    print(emoji.emojize('EMPATE:white_flag:'))

elif ia_opcao == 2 and player_opcao == 2:
    print(emoji.emojize('O COMPUTADOR ESCOLHEU :scissors:  E VOCÊ ESCOLHEU :scissors:'))
    print(emoji.emojize('EMPATE:white_flag:'))