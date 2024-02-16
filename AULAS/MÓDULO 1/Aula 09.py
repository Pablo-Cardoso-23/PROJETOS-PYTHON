#Manipulando texto (fatiamento)

frase = 'Curso em vídeo'
print(frase[1:12:2])

#Desafio 22

nome = input('Insira seu nome: ')
nome = nome.upper()
print(nome)

nome = nome.lower()
print(nome)

'-'.join(nome)
nm = len(nome)
print (nm)

divide = nome.upper().strip().split()
print(divide [0])
final = len(divide [0])
print(final)

#Desafio 23

num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('A unidade é: {}'.format(u))
print('A dezena é: {}'.format(d))
print('A centena é: {}'.format(c))
print('O milhar é: {}'.format(m))

#Desafio 24

city = input('Digite o nome da cidade: ')
city = city.title()
result = 'Santo' in city
print('Essa cidade possui o nome santo, a afirmação é:  {}'.format(result))

#Desafio 25

name = input('Insira seu nome: ')
name = name.title()
nome = 'Silva' in name
print('Essa pessoa tem Silva no nome, essa afirmação é: {}'.format(nome))

#Desafio 26

let = str (input('Insira algo com a letra "A": '))
let = let.upper().strip()
print('A letra "A" aparece {} vezes'.format(let.count('A')))
print('A letra "A" aparece pela primeira vez na posição: {}'.format(let.find('A')+1))
print('A letra "A" aparece pela última vez na posição: {}'.format(let.rfind('A')+1))

#Desafio 27

nm = input('Insira seu nome: ').strip()
nm = nm.split()
print('Olá, é um prazer te conhecer!')
print('Seu primeiro nome é {}'.format(nm [0]))
print('O seu último nome é: {0}'.format(nm[len(nm)-1]))