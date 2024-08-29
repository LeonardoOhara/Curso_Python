#O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. 
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

a = input('Digite seu nome: ')
b = input('Digite seu nome: ')
c = input('Digite seu nome: ')
d = input('Digite seu nome: ')
lista = [a, b, c, d]

resultado = random.shuffle(lista)

print(f'os alunos em ordem aleatoria são ')
print(lista)

# ou

from random import shuffle

a = input('Digite seu nome: ')
b = input('Digite seu nome: ')
c = input('Digite seu nome: ')
d = input('Digite seu nome: ')
lista = [a, b, c, d]

resultado = shuffle(lista)

print(f'os alunos em ordem aleatoria são ')
print(lista)
