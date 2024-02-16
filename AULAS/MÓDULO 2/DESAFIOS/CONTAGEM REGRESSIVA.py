# DESAFIO - 46 - CONTAGEM REGRESSIVA

import emoji
from time import sleep

print('\t==========')
print(emoji.emojize(':high_voltage:\t P4 STORM \t:high_voltage:'))
print('\t==========')

# CONTAGEM

print('INICIANDO CONTAGEM EM INSTANTES...')
sleep(1)

for c in range(10, 0, -1):
    print(emoji.emojize(':grimacing_face:'),c)
    sleep(1)
print(emoji.emojize(':fireworks: :confetti_ball: CONTAGEM CONCLUÍDA :confetti_ball: :fireworks:'))