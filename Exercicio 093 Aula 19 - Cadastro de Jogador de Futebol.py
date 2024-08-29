#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
from operator import itemgetter
jogadores = dict()
gol = list()
soma = 0
jogadores['nome'] = str(input('Nome do Jogador: ')).strip()
jogadores['partida'] = int(input(f'Quantas partidas {jogadores["nome"]} jogou?'))
for jogador in range(0, jogadores["partida"]):
    gol.append(int(input(f'Quantos gols na partida {jogador} ? ')))
    jogadores['gols'] = gol.copy() # copy the partida data to the output 
print ('=-'*30)
print (jogadores)
print ('=-'*30)
for i, k in enumerate(jogadores):
    print(f'O campo {k} tem valor {jogadores[k]}')
print ('=-'*30)
print (f'O jogador {jogadores["nome"]} jogou {jogadores['partida']} partidas')
for i, k in enumerate(gol): 
    soma += k
    print(f'Na Partida {i}, fez {k} gols.')
print(f'Foi um total de {soma} gols')

# modo guanabara

jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do Jogador :'))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))
for c in range (0, tot):
    partidas.append(int(input(f'Quantas gols na partida {c}')))
jogador ['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('=-'*30)
print(jogador)
print('=-'*30)
for k , v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('=-'*30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i , v in enumerate(jogador["gols"]):
    print(f'     -> Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')