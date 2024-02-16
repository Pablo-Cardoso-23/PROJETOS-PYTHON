# DESAFIO 83 - VERIFICANDO EXPRESSÕES

entrada_usuario = str(input('DIGITE A EXPRESSÃO: '))
contador = 0

for parenteses in entrada_usuario:
    if parenteses == '(':
        contador += 1
    elif parenteses == ')':
        contador -= 1
    elif contador < 0:
        break

if contador == 0:
    print('EXPRESSÃO VÁLIDA!')
else:
    print('EXPRESSÃO INVÁLIDA!')