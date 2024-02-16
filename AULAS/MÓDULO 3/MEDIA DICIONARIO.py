# DESAFIO 90 - SITUAÇÃO DE UM ALUNO USANDO DICIONÁRIO

informacoes_aluno = dict()

informacoes_aluno['nome'] = str(input('NOME: ')).upper()
informacoes_aluno['media'] = float(input(f'MÉDIA DE {informacoes_aluno["nome"]}: '))

if informacoes_aluno['media'] < 7 and informacoes_aluno['media'] >= 5:
    print(f'NOME É  IGUAL A {informacoes_aluno["nome"]}')
    print(f'MÉDIA É  IGUAL A {informacoes_aluno["media"]}')
    print('SITUAÇÃO É IGUAL A: RECUPERAÇÃO')
elif informacoes_aluno['media'] <= 4.9 and informacoes_aluno['media'] >= 0:
    print(f'NOME É  IGUAL A {informacoes_aluno["nome"]}')
    print(f'MÉDIA É  IGUAL A {informacoes_aluno["media"]}')
    print('SITUAÇÃO É IGUAL A: REPROVADO')
else:
    print(f'NOME É  IGUAL A {informacoes_aluno["nome"]}')
    print(f'MÉDIA É  IGUAL A {informacoes_aluno["media"]}')
    print('SITUAÇÃO É IGUAL A: APROVADO')