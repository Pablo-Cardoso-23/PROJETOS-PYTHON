# DESAFIO 38 - MAIOR VALOR

print('=========')
print('P4 STORM')
print('=========')

# ENTRADA DE DADOS

primeiro_numero = int(input('INSIRA O PRIMEIRO NÚMERO: '))
segundo_numero = int(input('INSIRA O SEGUNDO NÚMERO: '))

# ANÁLISE 

if primeiro_numero > segundo_numero:
    print('O PRIMEIRO NÚMERO ({}) É MAIOR DO QUE O SEGUNDO NÚMERO ({}).' . format(primeiro_numero, segundo_numero))
elif segundo_numero > primeiro_numero:
    print('O SEGUNDO NÚMERO ({}) É MAIOR DO QUE O PRIMEIRO NÚMERO ({}).' . format(segundo_numero, primeiro_numero))
elif primeiro_numero == segundo_numero:
    print('NÃO EXISTE UM NÚMERO MAIOR, JÁ QUE O PRIMEIRO NÚMERO ({}) É IGUAL AO SEGUNDO NÚMERO ({}).' . format(primeiro_numero, segundo_numero))