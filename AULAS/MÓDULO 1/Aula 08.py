#Quebrando um número
import math
num = float(input('Insira um número: '))
real = math.trunc(num)
print('Você inseriu o número {} e sua porção inteira é {}'.format(num, real))

#Calcular a hipotenusa
import math
op = float(input('Insira o cateto  oposto: '))
ad = float(input('Insira o caateto adjacente: '))
hip = math.hypot(op, ad)
print('A hipotenusa é {:.2f}'.format(hip))

#Seno, Cosseno e Tangente
import math
sct = float(input('Insira o ângulo que deseja: '))
s = math.sin(math.radians(sct))
c = math.cos(math.radians(sct))
t = math.tan(math.radians(sct))
print('O Seno de {} é {:.2f}'.format(sct, s))
print('O Cosseno de {} é {:.2f}'.format(sct, c))
print('A Tangente de {} é {:.2f}'.format(sct, t))

#Sorteando um número
print('Certo, vamos sortear alguns números.')
import random
nome1 = str (input('Insira o primeiro número: '))
nome2 = str (input('Insira o segundo número: '))
nome3 = str (input('Insira o terceiro número: '))
nome4 = str (input('Insira o quarto número: '))
lista = [nome1, nome2, nome3, nome4]
escolhido = random.choice(lista)
print('O nome sorteado foi: {}'.format(escolhido))

#Sorteando uma ordem na lista
print('Para fecharvamos sortear alguns nomes.')
import random
nm1 = str(input('Insira o primeiro nome: '))
nm2 = str(input('Insira o segundo nome: '))
nm3 = str(input('Insira o terceiro nome: '))
nm4 = str(input('Insira o quarto nome: '))
ordem = [nm1, nm2, nm3, nm4]
random.shuffle(ordem)
print('A sequência de apresentação será: ')
print(ordem)

#Tocando um MP3
print('Tocando: Movimento - Kawe ft. Teto')
import pygame
pygame.init()
pygame.mixer_music.load('music.mp3')
pygame.mixer_music.play()
input()
pygame.event.wait()

import emoji

print(emoji.emojize(':winking_face_with_tongue:'))