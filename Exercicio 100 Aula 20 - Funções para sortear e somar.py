# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint
from time import sleep
lista = list()
def sorteio(lista):
    for c in range (0, 5):
        n = randint(0, 10)
        lista.append(randint(1, 10))
        print (f'{n}', end=' ', flush=True )
        sleep(0.3)
    print('Pronto!')

def somaPar(lista): 
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(f'\nSomando os valores pares de {lista}, temos {soma}', end='')      


sorteio(lista)
somaPar(lista)