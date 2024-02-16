# DESAFIO 51 - PA 10 PRIMEIROS TERMOS

print('=========')
print('P4 STORM')
print('=========')

primeiro_termo = int(input('INSIRA O PRIMEIRO TERMO: '))
razao = int(input('INSIRA A RAZÃO: '))
posicao_termo = primeiro_termo + (10 - 1) * razao

for n in range(primeiro_termo, posicao_termo + razao, razao):
    pa = primeiro_termo + razao
    print('---> ',n)
    print('ACABOU')