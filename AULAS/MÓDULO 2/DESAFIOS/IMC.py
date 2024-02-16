# DESAFIO 43 - CALCULANDO O IMC

print('=========')
print('P4 STORM')
print('=========')

print('BEM-VINDO AO MEDIDOR DE IMC, INFORME SEUS DAADOS LOGO ABAIXO!')

# ENTRADA DE DADOS

pessoa_peso = float(input('INFORME SEU PESO: '))
pessoa_altura = float(input('INFORME SUA ALTURA: '))

# CÁLCULO

imc = pessoa_peso / pessoa_altura ** 2

# EXIBIÇÃO

print('\t==================')
print('\tCLASSIFICAÇÃO OMS')
print('\t==================\n')
print('|ABAIXO DE 18.5: ABAIXO DO PESO|')
print('|ENTRE 18.5 E 25: PESO IDEAL   |')
print('|25 ATÉ 30: SOBREPESO          |')
print('|30 ATÉ 40: OBESIDADE          |')
print('|ACIMA DE 40 OBESIDADE MÓRBIDA |\n')

if imc < 18.5:
    print('ATENÇÃO, SEU IMC É DE {:.2f}, LOGO VOCÊ ESTÁ ABAIXO DO PESO IDEAL!' . format(imc))
elif imc >= 18.5 and imc <= 25:
    print('ATENÇÃO, SEU IMC É DE {:.2f}, LOGO VOCÊ ESTÁ NO SEU PESO IDEAL!' . format(imc))
elif imc >= 25 and imc <= 30:
    print('ATENÇÃO, SEU IMC É DE {:.2f}, LOGO VOCÊ ESTÁ COM SOBREPESO!' . format(imc))
elif imc >= 30 and imc <= 40:
    print('ATENÇÃO, SEU IMC É DE {:.2f}, LOGO VOCÊ ESTÁ COM OBESIDADE!' . format(imc))
elif imc > 40:
    print('ATENÇÃO, SEU IMC É DE {:.2f}, LOGO VOCÊ ESTÁ COM OBESIDADE MÓRBIDA!' . format(imc))