# DESAFIO 102 - FUNÇÃO FATORIAL

def fatorial(numero = 1, show = False):
    """
        -> CALCULA O FATORIAL DE UM NÚMERO.
        :param numero: O NÚMERO A SER CALCULADO.
        :param  show: (OPCIONAL) MOSTRAR OU NÃO A CONTA PASSO A PASSO.
        :return: O VALOR DO FATORIAL DE UM NÚMERO.
    """
    padrao_fatorial = 1

    if show == True:
        print('-'*30)
        for etapas in range (numero, 0, -1):
            padrao_fatorial *= etapas
            print(f'{etapas}' , end='')
            if etapas > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        
    elif show == False:
        print('-'*30)
        for etapas in range (numero, 0, -1):
            padrao_fatorial *= etapas
    
    return padrao_fatorial


print(fatorial(5, show=True))
# help(fatorial)
# print(fatorial(5, show=False))