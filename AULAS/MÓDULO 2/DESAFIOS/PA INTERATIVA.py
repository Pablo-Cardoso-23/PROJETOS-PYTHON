# DESAFIO 62 - PA COM ESCOLHA

primeiro_termo = int(input('INFORME O PRIMEIRO TERMO: '))
razao = int(input('INFORME A RAZÃO: '))
termo = primeiro_termo
contador = 1
feedback_user = 0
mais_termos = 10
while mais_termos != 0:
    feedback_user += mais_termos
    while(contador <= feedback_user):
        print(' ===> {} ' . format(termo), end='')
        termo += razao
        contador += 1
        termos_exibidos = termo
    print('PAUSA')
    mais_termos = int(input('QUANTOS TERMOS VOCÊ DESEJA EXIBIR A MAIS? '))

print('PROGRESSÃO FINALIZADA COM {} TERMOS EXIBIDOS.' . format(feedback_user))