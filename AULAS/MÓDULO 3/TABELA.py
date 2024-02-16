# DESAFIO 73 - TABELA DO BRASILEIRÃO

nomes_times = ('PALMEIRAS', 'GRÊMIO', 'ATLÉTICO-MG', 'FLAMENGO', 'BOTAFOGO', 'BRAGANTINO', 'FLUMINENSE', 'ATHLETICO-PR', 'INTERNACIONAL', 'FORTALEZA', 'SÃO PAULO', 'CUIABÁ', 'CORINTHIANS', 'CRUZEIRO', 'VASCO DA GAMA', 'BAHIA', 'SANTOS', 'GOIÁS', 'AMÉRICA-MG')

print('-=' *76)
print(f'COLOCAÇÃO DO CAMPEONATO BRASILEIRO DE 2023: {nomes_times}', end='\n')
print('-=' *76)

print('-=' *76)
print(f'OS 5 PRIMEROS COLOCADOS SÃO: {nomes_times[0:5]}')
print('-=' *76)

print('-=' *76)
print(f'OS ÚLTIMOS 4 COLOCADOS SÃO: {nomes_times[-4:]}')
print('-=' *76)

print('-=' *76)
print(f'TABELA EM ORDEM ALFABÉTICA: {sorted(nomes_times)}')
print('-=' *76)

print('-=' *76)
print(f'O CORINTHIANS ESTÁ EM {nomes_times.index("CORINTHIANS") + 1}º COLOCADO')
print('-=' *76)