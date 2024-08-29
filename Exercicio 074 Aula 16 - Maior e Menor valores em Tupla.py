#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.


import random
numero = [random.randrange(1,11,1) for numero in range(5)]
for n in numero:
    print(f'{n}', end=' ')
print(f'\nO maior numero é {max(numero)}')
print(f'O menor numero é {min(numero)}')






 