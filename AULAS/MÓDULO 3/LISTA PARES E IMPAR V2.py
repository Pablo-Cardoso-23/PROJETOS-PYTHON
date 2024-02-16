# DESAFIO 85 - CRIANDO LISTAS COM NÚMEROS PARES E ÍMPARES V2

juncao_numeros = list()
pares = list()
impares = list()
contador = 0

while contador < 7:
    digitos_usuario = (int(input(f'DIGITE O {contador + 1}º VALOR: ')))

    if digitos_usuario % 2 == 0:
        pares.append(digitos_usuario)
    elif digitos_usuario % 2 != 0:
        impares.append(digitos_usuario)

    contador += 1

juncao_numeros.append(impares[:])
juncao_numeros.append(pares[:])
    
print(f'LISTA COM NÚMEROS PARES DIGITADOS {sorted(juncao_numeros[1])}')
print(f'LISTA COM NÚMEROS ÍMPARES DIGITADOS {sorted(juncao_numeros[0])}')
