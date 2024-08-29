#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
#O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

import random
import time
print('=-'*20)
print('Palpite da Mega Sena')
print('=-'*20)
lista = [0,0,0,0,0,0]
palpite = int(input('Quantos Palpites você quer ? '))
for c in range (0 , palpite):
    lista[0] = random.randint(1,61)
    lista[1] = random.randint(1,61)
    lista[2] = random.randint(1,61)
    lista[3] = random.randint(1,61)
    lista[4] = random.randint(1,61)
    lista[5] = random.randint(1,61)
    time.sleep(0.5)
    print(f'Jogo {c}: {lista}')
print('Boa Sorte!')

# Modo Guanabara 

from random import randint
from time import sleep
lista = list()
jogos = list()
print('-'*30)
print('    Jogos da Mega Sena    ')
print('-'*30)
quant = int(input('Quantos jogos você quer que eu sorteie?')) 
tot = 1 
while tot <= quant:
    cont = 0
    while True:
      num = randint(1,60)
      if num not in lista:
        lista.append(num)
        cont += 1
      if cont >= 6:
        break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-='* 3, f'Sortenado {quant} Jogos', '-='*3)
for i, l in enumerate(jogos):
    print(f'jogo {i+1}: {l}')
    sleep(1)
print('Boa sorte!')