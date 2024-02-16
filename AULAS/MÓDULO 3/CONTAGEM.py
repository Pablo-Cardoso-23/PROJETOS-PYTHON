# DESAFIO 72 - CONTAGEM POR EXTENSO(TUPLAS)

numeros_salvos = ('ZERO', 'UM', 'DOIS', 'TRÊS', 'QUATRO', 'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ', 'ONZE', 'DOZE', 'TREZE', 'QUATORZE', 'QUINZE', 'DEZESSEIS', 'DEZESSETE', 'DEZOITO', 'DEZENOVE', 'VINTE')

while True:
    entrada_usuario = int(input('DIGITE UM NÚMERO ENTRE 0 E 20: '))
    while (entrada_usuario < 0) or (entrada_usuario > 20):
        entrada_usuario = int(input('DIGITE UM NÚMERO VÁLIDO NOVAMENTE ENTRE 0 E 20: '))
    break

print(f'VOCÊ DIGITOU O NÚMERO: {numeros_salvos[entrada_usuario]}')

