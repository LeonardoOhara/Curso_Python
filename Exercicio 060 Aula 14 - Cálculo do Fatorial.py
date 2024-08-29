#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
#5! = 5 x 4 x 3 x 2 x 1 = 120

from math import factorial
numero = int(input('Digite o numero'))
result = factorial(numero)
print(f'{result}')

# outro modo

numero = int(input('Digite o numero aqui:'))
contador = numero
factory = 1
while contador > 0:
    print(f'{contador}', end='')
    print('x' if contador>1 else '=', end= '')
    factory *= contador
    contador -= 1
print(f'{factory}')



