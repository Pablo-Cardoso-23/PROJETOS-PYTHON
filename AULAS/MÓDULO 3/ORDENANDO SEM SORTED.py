# DESAFIO 80 - ORDENANDO NÚEMROS SEM USAR O COMANDO SORTED

lista_numeros = list()
contador = 0


while contador <= 4:
    valores_usuario = int(input('DIGITE UM NÚMERO: '))
    if contador == 0 or valores_usuario > lista_numeros[-1]:
        lista_numeros.append(valores_usuario)
    else:
        posicao = 0
        while posicao < len(lista_numeros):
            if valores_usuario <= lista_numeros[posicao]:
                lista_numeros.insert(posicao, valores_usuario)
                break
            posicao += 1

    contador += 1

print(f'LISTA EM ORDDEM CRESCENTE: {lista_numeros}')
    