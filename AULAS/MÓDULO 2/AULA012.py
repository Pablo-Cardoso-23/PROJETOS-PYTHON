nome = str(input('QUAL O SEU NOME? '))

if nome == 'Pablo':
    print('QUE NOME BONITO!')
elif nome == 'Vitor':
    print('FLICKS!')
elif nome == 'Vitória' or nome == 'Nadielly' or nome == 'Helaine':
    print('UP!')
elif nome in 'Joaquina':
    print('EAI, PAI. TU TÁ AONDE?')
else: 
    print('SEU NOME É BEM COMUM!')

print('TENHA UM BOM DIA, {}!' . format(nome))