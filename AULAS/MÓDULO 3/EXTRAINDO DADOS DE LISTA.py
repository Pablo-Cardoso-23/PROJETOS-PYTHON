# DESAFIO 81 - EXTRAINDO DADOS DE UMA LISTA

lista_criada = list()
contador_numeros = 0

while True:
    contador_numeros += 1
    numeros_usuario = int(input('DIGITE UM NÚMERO: '))
    lista_criada.append(numeros_usuario)

    feedback_user = str(input('DESEJA ADICIONAR MAIS ALGUM NÚMERO [S/N]? ')).upper()

    while feedback_user != 'S' and feedback_user != 'N':
        feedback_user = str(input('DESEJA ADICIONAR MAIS ALGUM NÚMERO [S/N]? ')).upper()

    if feedback_user == 'N':
        break

lista_criada.sort(reverse=True)

print(f'AO TOTAL FORAM DIGITADOS {contador_numeros} NÚMEROS')
print(f'A LISTA EM ORDEM DECRESCENTE FICA NA SEGUINTE MANEIRA: {lista_criada}')

if 5 not in lista_criada:
    print('O NÚMERO 5 NÃO ESTÁ NA LISTA.')
else:
    print('O NÚMERO 5 FOI DIGITADO.')
