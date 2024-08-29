# Um professor quer sortear um dos seus quatro alunos para apagar
# o quadro. Faça um programa que ajude ele, lemdo o nome deles e escrevendo
# o nome do escolhido.

import random
a = str(input('Digite seu nome :'))
b = str(input('Digite seu nome: '))
c = str(input('Digite seu nome: '))
d = str(input('Digite seu nome: '))
lista = [a, b, c, d]
Resultado = random.choice(lista)

print(f'o aluno escolhido foi {Resultado}')

from random import choice
a = str(input('Digite seu nome :'))
b = str(input('Digite seu nome: '))
c = str(input('Digite seu nome: '))
d = str(input('Digite seu nome: '))
lista = [a, b, c, d]
Resultado = choice(lista)

print(f'o aluno escolhido foi {Resultado}')
