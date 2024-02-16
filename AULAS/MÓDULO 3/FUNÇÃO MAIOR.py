# DESAFIO 99 - FUNÇÃO DE ANALISAR O MAIOR 

def maior(*numeros):
    contador = 0
    maior = 0
        
    print()
    print('-='*30)
    print('ANALISANDO OS VALORES PASSADOS...')
    for numbers in numeros:
        print(f'{numbers} ', end='')
        if contador == 0:
            maior = numbers
        elif numbers > maior:
            maior = numbers
        contador += 1
    print(f'FORAM INFORMADOS {len(numeros)} VALORES AO TODO')
    print(f'O MAIOR VALOR INFORMADO FOI {maior}')
    print('-='*30)


maior(4, 7, 0)
maior(2, 9, 4, 5, 7, 1)
maior(1, 2)
maior(6)
maior()