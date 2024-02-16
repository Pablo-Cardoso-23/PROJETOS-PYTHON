# DESAFIO 98 - CONTAGEM COM FUNÇÕES

from time import sleep
import emoji

def contador(inicial, final, passo):

    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1  

    print()
    print('-='*20)
    print(f'CONTAGEM DE {inicial} ATÉ {final} EM {passo} EM {passo}')
    print('-='*20)

    if inicial < final:
        contador_inicial = inicial
        while contador_inicial <= final:
            print(f'{contador_inicial} ',end='', flush= True)
            sleep(0.5)
            contador_inicial += passo
        print('FIM!')
    else:
        contador_inicial = inicial
        while contador_inicial >=  final:
            print(f'{contador_inicial} ', end='', flush= True )
            sleep(0.5)
            contador_inicial -= passo
        print('FIM!')
    
    
contador(1, 10, 1)
contador(10, 0, 2)

print()
print(emoji.emojize(':nerd_face: AGORA É SUA VEZ DE PERSONALIZAR A CONTAGEM!'))
inicial = (int(input('INFORME O INÍCIO: ')))
final = (int(input('INFORME O FIM: ')))
passo = (int(input('INFORME O PASSO: ')))
contador(inicial, final, passo)
