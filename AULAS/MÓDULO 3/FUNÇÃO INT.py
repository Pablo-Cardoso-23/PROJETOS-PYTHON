# DESAFIO 104 - FUNÇÃO INPUT LEIAINT

def leiaInt(numero):
    status_validade = False
    number = 0
    
    while True:
        usuario_numero = str(input(numero))
        if usuario_numero.isnumeric():
            number = int(usuario_numero)
            status_validade = True
        else:
            print('\033[4;31mERRO! DIGITE UM NÚMERO INTEIRO VÁLIDO.\033[m')
            status_validade = False
        if status_validade:
            break
    return number


usuario_numero = leiaInt('DIGITE UM NÚMERO: ')
print(f'VOCÊ ACABOU DE DIGITAR O NÚMERO {usuario_numero}')
