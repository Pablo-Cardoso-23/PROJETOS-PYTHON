# DESAFIO 63 - SEQUÊNCIA DE FIBONACCI

print('------------------------')
print(' SEQUÊNCIA DE FIBONACCI')
print('------------------------')

termo_fibonacci = int(input('INFORME QUANTOS TERMOS VOCÊ DESEJA EXIBIR: '))

contador = 0
primeiro_termo = 1
segundo_termo = 0  


while contador < termo_fibonacci:
    calculo_termos = primeiro_termo + segundo_termo
    primeiro_termo = segundo_termo
    segundo_termo = calculo_termos
    contador += 1

    # print(sequencia_fibonacci)
    print(calculo_termos)
