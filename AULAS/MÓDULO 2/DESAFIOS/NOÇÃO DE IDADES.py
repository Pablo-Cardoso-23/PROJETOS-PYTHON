# DESAFIO 56 - IDENTIFICANDO A MÉDIA DE IDADE, HOMEM MAIS VELHO E QAUNTAS MULHERES TEM MENOS DE 20 ANOS

print('----------')
print('|P4 STORM|')
print('----------')

soma = 0
homem_mais_velho = 0
nome_homem = ''
idade_homem_velho = 0
mulheres_novas =  0
soma_idade = 0
media_idade = 0

for c in range(1,5):
    print('-' *30)
    print('{}ª PESSOA' . format(c))
    nome = str(input('INFORME SEU NOME: '))
    idade = int(input('INFORME SUA IDADE: '))
    sexo = str(input('INFORME SEU SEXO [M/F]: ')).upper()[0]

    print('-' *30)

    soma_idade += idade

    if(sexo == 'M' and idade > idade_homem_velho):
        idade_homem_velho = idade
        nome_homem = nome
    elif(sexo == 'F' and idade < 20):
        mulheres_novas += 1

media_idade = soma_idade / c

print('MÉDIA DE IDADE: {}' . format(media_idade))
print('NOME DO HOMEM MAIS VELHO: {}' . format(nome_homem))

if mulheres_novas == 0:
    print('NÃO HÁ PRESENÇA DE MULHERES NO GRUPO!')
else:
    print('QUANTIDADE DE MULHERES COM MENOS DE 20 ANOS: {}' . format(mulheres_novas))