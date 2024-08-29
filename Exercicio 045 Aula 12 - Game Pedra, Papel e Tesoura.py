# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep
print('Jogo do Jo Ken Po')
print('''[0] Pedra 
[1] Papel
[2] Tesoura''')
player = int(input('Escolha entre Pedra , Papel ou Tesoura: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!!')
lista = ('pedra', 'papel','tesoura')
pc = randint (0, 2)

if player == pc:
    print('empate')
elif player == 0 and pc == 1:
    print('você perdeu')
elif player == 0 and pc ==2:
    print('você ganhou')
elif player == 1 and pc == 2:
    print('você perdeu')
elif player == 1 and pc == 0:
    print('você ganhou')
elif player == 2 and pc == 0:
    print('você perdeu')
elif player == 2 and pc == 1:
    print('você ganhou')
else:
    print('Error!')

print('=' * 50)
print(f'Jogador jogou {lista[player]} o computador jogou {lista[pc]}')
print('=' * 50)

# Outro modo de estrutura

from time import sleep
from random import randint
itens = ('pedra', 'papel', 'tesoura')
computador = randint (0, 2)
print(''' Suas Opções: 
[0] Pedra 
[1] Papel 
[2] Tesoura''')
jogador = int(input('Escolha do Jogador:'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!!')
print('=' * 10)
print(f'jogador jogou {lista[jogador]}')
print(f'Computador jogou {lista[computador]}')
print('=' * 10)
if computador == 0: # computador jogou pedra
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('computador vence!')
    elif jogador == 2:
        print('jogador vence')
    else:
        print(' jogada invalida')

elif computador == 1: # computador jogou papel
    if jogador == 0:
        print('computador vence')
    elif jogador == 1:
        print('empate!')
    elif jogador == 2:
        print('jogador vence')
    else:

        print(' jogada invalida')

elif computador == 2: # computador jogou tesoura
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('computador vence!')
    elif jogador == 2:
        print('jogador venceu')
    else:
        print('jogada invalida')
