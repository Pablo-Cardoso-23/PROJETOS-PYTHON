# DESAFIO 96 - CALCULANDO A ÁREA DE UM TERRENO

def Area(largura, comprimento):
    print()
    print('-'*20)
    print('CONTROLE DE TERRENO')
    print('-'*20)
    total = largura * comprimento
    print(f'A ÁREA DE UM TERRENO {largura} X {comprimento} É DE {total:.1f} m².')


print()
largura = float(input('INFORME A LARGURA(m): '))
comprimento = float(input('INFORME O COMPRIMENTO(m): '))
Area(largura, comprimento)