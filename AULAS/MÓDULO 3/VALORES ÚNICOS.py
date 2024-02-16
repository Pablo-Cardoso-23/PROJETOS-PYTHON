# DESAFIO 79 - LISTA COM APENAS VALORES ÚNICOS

lista_unica = []

while True:
    entrada_usuario = int(input('DIGITE UM VALOR: '))

    if entrada_usuario not in lista_unica:
        lista_unica.append(entrada_usuario)
        print('VALOR ADICIONADO COM SUCESSO!')
        
    else:
        lista_unica.append(entrada_usuario)
        deletar_numero = lista_unica.pop()
        print('VALOR DUPLICADO, NÃO SERÁ ADICIONADO!')

    feedback_user = str(input('DESEJA CONTINUAR [S/N]? ')).upper()

    while (feedback_user != 'S') and (feedback_user != 'N'):
        print('COMANDO NÃO RECONHECIDO!')
        feedback_user = str(input('DESEJA CONTINUAR [S/N]? ')).upper()

    if feedback_user == 'N':
        break

print(f'VOCÊ DIGITOU OS VALORES: {sorted(lista_unica)}')