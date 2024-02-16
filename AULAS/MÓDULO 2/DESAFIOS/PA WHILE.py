# DESAFIO 61 - PA COM WHILE

primeiro_termo = int(input('INFORME O PRIMEIRO TERMO: '))
razao = int(input('INFORME A RAZÃO: '))
termo = primeiro_termo
contador = 0

while contador < 10:
    print('===> {}' . format(termo))

    termo += razao
    contador += 1

print('FINALIZADO')