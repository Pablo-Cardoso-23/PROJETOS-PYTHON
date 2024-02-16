# DESAFIO 77 - IDENTIFICANDO VOGAIS COM TUPLAS

lista_palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')

for letras in lista_palavras:
    print(f'\nNA PALAVRA {letras} TEMOS AS VOGAIS: ', end= '')
    for vogais in letras:
        if vogais.upper() in 'AEIOU':
            print(vogais, end=' ')