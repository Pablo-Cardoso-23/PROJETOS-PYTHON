# DESAFIO 82 - SEPARANDO LISTAS EM 3 (NORMAL, ÍMPAR, PAR)

lista_normal = list()
pares_lista = list()
impar_lista = list()

while True:
    interacao_usuario = int(input('DIGITE UM NÚMERO: '))
    lista_normal.append(interacao_usuario)

    if interacao_usuario % 2 == 0:
        pares_lista.append(interacao_usuario)

    elif interacao_usuario % 2 != 0:
        impar_lista.append(interacao_usuario)

    feedback_usuario = str(input('DESEJA ADICIONAR MAIS ALGUM NÚMERO [S/N]? ')).upper()

    while feedback_usuario != 'S' and feedback_usuario != 'N':
        print('COMANDO NÃO RECONHECIDO!')
        feedback_usuario = str(input('DESEJA ADICIONAR MAIS ALGUM NÚMERO [S/N]? ')).upper()
        
    if feedback_usuario == 'N':
        break

print(f'A LISTA COMPLETA FICA COM OS SEGUINTES NÚMEROS: {lista_normal}')
print(f'A LISTA COM NÚMEROS PARES POSSUI OS SEGUINTES NÚMEROS: {pares_lista}')
print(f'A LISTA COM OS NÚMEROS ÍMPARES POSSUI OS SEGUINTES NÚMEROS: {impar_lista}')