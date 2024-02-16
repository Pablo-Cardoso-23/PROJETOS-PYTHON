# DESAFIO 69 - IDADE E SEXO DE UMA PESSOA
feedback_usuario = ''
mais_dezoito_anos = 0
homens_cadastrados = 0
mulheres_menosVinte_anos = 0

while True:
        
        idade_usuario = int(input('INFORME SUA IDADE: '))
        sexo_usuario = str(input('INFORME SEU SEXO [M/F]: ')) . upper()
        while (sexo_usuario != 'M') and (sexo_usuario != 'F'):
             sexo_usuario = str(input('INFORME SEU SEXO [M/F]: ')) . upper()
        
        if idade_usuario > 18:
            mais_dezoito_anos += 1
        if sexo_usuario == 'M':
            homens_cadastrados += 1
        if idade_usuario < 20 and  sexo_usuario == 'F':
            mulheres_menosVinte_anos += 1

        feedback_usuario = str(input('DESEJA CADASTRAR MAIS ALGUÉM [S/N]? ')) . upper()

        while (feedback_usuario != 'S') and (feedback_usuario != 'N'):
            feedback_usuario = str(input('DESEJA CADASTRAR MAIS ALGUÉM [S/N]? ')) . upper()
    

        if feedback_usuario == 'N':
            feedback_usuario == False
            # print('\t|ANALISANDO OS DADOS|\n')
            # print(f'PESSOAS COM MAIS DE 18 ANOS: {mais_dezoito_anos}')
            # print(f'HOMENS CADASTRADOS: {homens_cadastrados}')
            # print(f'MULHERES COM MENOS DE 20 ANOS: {mulheres_menosVinte_anos}')
            break

print('\t|ANALISANDO OS DADOS|\n')
print(f'PESSOAS COM MAIS DE 18 ANOS: {mais_dezoito_anos}')
print(f'HOMENS CADASTRADOS: {homens_cadastrados}')
print(f'MULHERES COM MENOS DE 20 ANOS: {mulheres_menosVinte_anos}')