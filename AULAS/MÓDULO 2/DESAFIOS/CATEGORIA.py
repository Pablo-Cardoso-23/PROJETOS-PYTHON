# DESAFIO 41 - CATEGORIA DE NATAÇÃO

from datetime import date

print('==================================')
print('CONFEDEREAÇÃO NACIONAL DE NATAÇÃO')
print('==================================')

#ENTRADA DE DADOS 

print('\t====================')
print('\tTABELA DE CATEGORIA')
print('\t====================\n')
print('|ATÉ 9 ANOS - MIRIM       |')
print('|ATÉ 14 ANOS - INFANTIL   |')
print('|ATÉ 19 ANOS - JUNIOR     |')
print('|ATÉ 20 ANOS - SÊNIOR     |')
print('|ACIMA DE 20 ANOS - MASTER|\n')

ano_nascimento = int(input('INFORME SEU ANO DE NASCIMENTO: '))

#CÁLCULO 

ano_atual = date.today().year
categoria = ano_atual - ano_nascimento

# RESULTADO

if categoria <= 9:
    print('VOCÊ TEM {} ANOS' . format(categoria))
    print('SUA CATEGORA É MIRIM!')
elif categoria > 9 and categoria <= 14:
    print('VOCÊ TEM {} ANOS' . format(categoria))
    print('SUA CATEGORIA É INFATIL!')
elif categoria > 14 and categoria <= 19:
    print('VOCÊ TEM {} ANOS' . format(categoria))
    print('SUA CATEGORIA É JUNIOR!')
elif categoria > 19 and categoria <= 20:
    print('VOCÊ TEM {} ANOS' . format(categoria))
    print('SUA CATEGORIA SÊNIOR!')
elif categoria > 20:
    print('VOCÊ TEM {} ANOS' . format(categoria))
    print('SUA CATEGORIA É MASTER!')