#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
import time
from operator import itemgetter
jogadores = dict()
for i in range(0,4):
    jogadores[f'jogador {i+1}'] = randint(1,6)
    time.sleep(0.3)   
    print(f'O jogador {i+1} tirou {jogadores[f"jogador {i+1}"]} no dado')
ranking = dict()
print(' == RANKING DOS JOGADORES == ')
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True) # itemgetter serve para acessar um item da lista 
for i, v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0]} com {v[1]}')
print()