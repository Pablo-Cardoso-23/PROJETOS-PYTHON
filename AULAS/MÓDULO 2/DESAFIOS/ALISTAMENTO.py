# DESAFIO 39 - ALISTAMENTO MILITAR

from datetime import date

print('==================================')
print('SERVIÇO DE ALISTAMENTO BRASILEIRO')
print('==================================')

# ENTRADA DE DADOS 

nome_candidato = str(input('INFORME SEU NOME COMPLETO: '))
local_candidato = str(input('INFORME SEU ESTADO: '))
nascimento_candidato = int(input('INFORME O ANO DE NASCIMENTO: '))

# CÁLCULO

ano_atual = date.today().year
ano_alistamento = ano_atual - nascimento_candidato
futuro_alistado = 18 - ano_alistamento
alistamento_futuro =  nascimento_candidato + ano_alistamento + 18 - ano_alistamento
passado_alistado = ano_alistamento - 18

# ANÁLISE DO CANDIDATO

if ano_alistamento == 18:
    print('ATENÇÃO CANDIDATO, {}. ESSE É O SEU ANO DE REALIZAR O ALISTAMENTO MILITAR!' . format(nome_candidato))
elif ano_alistamento < 18:
    print('ATENÇÃO, CANDIDATO {}. AINDA NÃO CHEGOU A SUA HORA DE REALIZAR O ALISTAMENTO MILITAR!' . format(nome_candidato))
    print('AINDA FALTAM {} ANOS PARA VOCÊ REALIZAR SEU ALISTAMENTO MILITAR, SENDO POSSÍVEL SOMENTE NO ANO DE {}!' . format(futuro_alistado, alistamento_futuro))
elif ano_alistamento > 18:
    print('ATENÇÃO CANDIDATO, {}. SEU PRAZO PARA REALIZAR O ALISTAMENTO MILITAR ULTRAPASSOU, CASO AINDA NÃO TENHA REALIZADO O ALISTAMENTO MILITAR PROCURE A JUNTA MAIS PRÓXIMA PARA OBTER MAIS INFORMAÇÕES!' . format(nome_candidato))
    print('TEMPO ULTRAPASSADO: {} ANOS.' . format(passado_alistado))