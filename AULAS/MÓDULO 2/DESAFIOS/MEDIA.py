# DESAFIO 40 - CALCULANDO MÉDIA

print('==========')
print('P4 STORM')
print('==========')

# ENTRADA DE DADOS

primeira_nota = float(input('INSIRA A PRIMEIRA NOTA: '))
segunda_nota = float(input('INSIRA A SEGUNDA NOTA: '))

# CÁLCULO

media_aluno = (primeira_nota + segunda_nota) / 2

# RESULTADO

if media_aluno < 5:
    print('NOTA FINAL DO ALUNO: {:.1f}' . format(media_aluno))
    print('O ALUNO ESTÁ REPROVADO!')
elif media_aluno >= 5 and media_aluno <= 6.9:
    print('NOTA FINAL DO ALUNO: {:.1f}' . format(media_aluno))
    print('O ALUNO ESTÁ DE RECUPERAÇÃO!')
elif media_aluno >= 7.0 and media_aluno < 10:
    print('NOTA FINAL DO ALUNO: {:.1f}' . format(media_aluno))
    print('O ALUNO ESTÁ APROVADO!') 
elif media_aluno > 10:
    print('NOTA FINAL DO ALUNO: {:.1f}' . format(media_aluno))
    print('EXCESSO DE NOTA!')