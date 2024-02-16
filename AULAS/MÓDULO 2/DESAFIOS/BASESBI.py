# DESAFIO 37 - CONVERTENDO BASES NUMÉRICAS

print('=========')
print('P4 STORM')
print('=========')

# ENTRADA DE DADOS
numero_converter = int(input('INSIRA O NÚEMRO QUE DESEJA CONVERTER: '))

print('ESCOLHA PARA QUAL BASE VOCÊ DESEJA CONVERTER: ')
print('1- BASE BINÁRIA')
print('2- BASE OCTAL')
print('3- BASE HEXADECIMAL')

escolha = int(input('DIGITE O NÚMERO DA BASE ESCOLHIDA: '))

if escolha == 1:
   converter = bin(numero_converter)[2:]
   print('O NÚMERO NA BASE DECIMAL ({}) CONVERTIDO PARA A BASE BINÁRIA É IGUAL A ({})' . format(numero_converter,converter))
elif escolha == 2:
   converter = oct(numero_converter)[2:]
   print('O NÚMERO NA BASE DECIMAL ({}) CONVERTIDO PARA A BASE OCTAL É IGUAL A ({})' . format(numero_converter,converter))
elif escolha == 3:
   converter = hex(numero_converter)[2:]
   print('O NÚMERO NA BASE DECIMAL ({}) CONVERTIDO PARA A BASE HEXADECIMAL É IGUAL A ({})' . format(numero_converter, converter))
else:
   print('DÍGITO INVÁLIDO!')