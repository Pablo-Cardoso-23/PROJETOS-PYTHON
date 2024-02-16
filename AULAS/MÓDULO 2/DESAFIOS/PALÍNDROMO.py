# DESAFIO 53 - PALÍNDROMO

import emoji
from time import sleep

print('----------')
print('|P4 STORM|')
print('----------')

entrada_texto = str(input('INFORME A FRASE/PALAVRA: ')) . strip() . upper()
separa_string = entrada_texto.split()
junta_string = ''.join(separa_string)
palindromo = ''

for palavra in range(len(junta_string) -1, -1, -1):
    palindromo += junta_string[palavra]

if (palindromo ==  junta_string):
    print('\nORIGINAL: {}' . format(entrada_texto))
    print(emoji.emojize('\n:counterclockwise_arrows_button: INVERTENDO :counterclockwise_arrows_button:\n'))
    sleep(1)
    print('INVERTIDO: {}' . format(palindromo))
    print(emoji.emojize('\n:check_mark_button: É UM PALÍNDROMO :check_mark_button:'))
else:
    print('\nORIGINAL: {}' . format(entrada_texto))
    print(emoji.emojize('\n:counterclockwise_arrows_button: INVERTENDO :counterclockwise_arrows_button:'))
    sleep(1)
    print('\nINVERTIDO: {}' . format(palindromo))
    print(emoji.emojize('\n:cross_mark: NÃO É UM PALÍNDROMO :cross_mark:'))