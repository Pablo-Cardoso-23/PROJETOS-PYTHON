# DESAFIO 89 - BOLETIM EM LISTAS

print('-='*36)
print('UCB - UNIVERSIDADE CATÓLICA DE BRASÍLIA'.center(70))
print('-='*36)

banco_notas = list()
dados_alunos = list()

while True:
    banco_notas.append(str(input('NOME: ').upper()))
    banco_notas.append(float(input('1ª NOTA: ')))
    banco_notas.append(float(input('2ª NOTA: ')))

    feedback_usuario = str(input('DESEJA INSERIR A NOTA DE MAIS ALGUM ALUNO [S/N]? ')).upper()

    dados_alunos.append(banco_notas[:])
    banco_notas.clear()


    while feedback_usuario != 'S' and feedback_usuario != 'N':
        print('ERRO, COMANDO NÃO CONHECIDO!')
        feedback_usuario = str(input('DESEJA INSERIR A NOTA DE MAIS ALGUM ALUNO [S/N]? ')).upper()

    if feedback_usuario == 'N':
        break

print('-='*36)
print('Nº    NOME     MÉDIA')
print('-'*36)

for indice, alunos in enumerate(dados_alunos):
    media = (alunos[1] + alunos[2]) / 2
    print(f'{indice}    {alunos[0]:^10} {media:^10}')

while True:
    exibir_notas = int(input('DESEJA EXIBIR AS NOTAS DE QUAL ALUNO? (999 ENCERRA): '))

    for indice, aluno in enumerate(dados_alunos):
        if exibir_notas == indice:
            print(f'NOTAS DE {aluno[0]} SÃO: {aluno[1:]}')

    if exibir_notas == 999:
        break