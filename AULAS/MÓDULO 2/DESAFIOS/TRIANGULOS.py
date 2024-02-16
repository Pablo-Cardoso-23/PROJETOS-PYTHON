# DESAFIO 42 - TRIÂNGULOS

print('=========')
print('P4 STORM')
print('=========')

print('VERIFICANDO UM TRIÂNGULO')

s1 = int(input('INSIRA O PRIMEIRO SEGMENTO: '))
s2 = int(input('INSIRA O SEGUNDO SEGMENTO: '))
s3 = int(input('INSIRA O TERCEIRO SEGMENTO: '))

# if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    # print('OS SEGMENTOS A SEGUIR: ({}), ({}), ({}) PODEM FORMAR UM TRIÂNGULO.')
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2 and s1 == s2 and s1 == s3 and s2 == s3:
    print('TRATA-SE DE UM TRIÂNGULO EQUILÁTERO')

elif s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2 and s1 == s2 or s1 == s3 or s2 == s3:
    print('TRATA-SE DE UM TRIÂNGULO ISÓSCELES!')

elif  s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2 and s1 != s2 and s1 != s3 and s2 != s3:
    print('TRATA-SE DE UM TRIÂNGULO ESCALENO!')

# else:
    # print('Os segmentos a seguir a seguir não podem formar um triângulo.')