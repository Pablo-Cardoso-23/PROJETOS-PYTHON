# DESAFIO 57 - ANALISANDO O SEXO DE UMA PESSOA

print('---------')
print('P4 STORM')
print('---------')

pessoa_sexo = str(input('INFORME SEU SEXO [M/F]: ')) . upper()

if(pessoa_sexo == 'M' or pessoa_sexo == 'F'):
    print('CADASTRADO')

else:
    while(pessoa_sexo != 'M' or pessoa_sexo != 'F'):
        print('ERRO, SEXO NÃO IDENTIFICADO!')
        pessoa_sexo = str(input('INFORME SEU SEXO NOVAMENTE [M/F]: ')) . upper()
        if(pessoa_sexo == 'M' or pessoa_sexo == 'F'):
            print('CADASTRADO')
            break