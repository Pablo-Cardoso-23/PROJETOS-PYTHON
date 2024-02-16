# DESAFIO 54 - VERIFICANDO QUEM É O MAIOR DE IDADE DE UM GRUPO

from datetime import date

print('=========')
print('P4 STORM')
print('=========')

ano_atual = date.today().year
maiores_idade = 0
menores_idade = 0

for n in range(1,8):
    verificar_idade = int(input('INFORME SEU ANO DE NASCIMENTO: '))
    calculo_idade = ano_atual - verificar_idade

    if calculo_idade >= 21:
        maiores_idade += 1
    elif calculo_idade < 21:
        menores_idade += 1

print('---------------------------')
print('|PESSOAS MAIORES DE IDADE |')
print('|NÚMERO: {}                |' . format(maiores_idade))
print('---------------------------\n')

print('---------------------------')
print('|PESSOAS MENORES DE IDADE |')
print('|NÚMERO: {}                |' . format(menores_idade))
print('---------------------------\n')
