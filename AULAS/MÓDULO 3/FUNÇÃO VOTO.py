# DESAFIO 101 - FUNÇÃO DE VOTAÇÃO DE ELEIÇÃO

from datetime import date
ano_atual = date.today().year

def Voto(idade = 0):

    idade = ano_atual - usuario_idade
    opcional = 'VOTO OPCIONAL'
    negado = 'VOTO NEGADO'
    obrigatorio = 'VOTO OBRIGATÓRIO'

    if idade < 18 and idade >= 16 or idade >= 70:
        return opcional
    elif idade < 16:
        return negado
    elif idade >= 18 and idade <= 69:
        return obrigatorio


usuario_idade = int(input('INFORME EM QUE ANO VOCÊ NASCEU: '))
age = ano_atual - usuario_idade
if Voto(usuario_idade):
    print(f'COM {age} ANOS: {Voto()}')