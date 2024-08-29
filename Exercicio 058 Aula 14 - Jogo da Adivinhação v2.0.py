#Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
computador = randint(0, 10)
print('Bem vindo ao jogo da adivinhação! Acabei de pensar um numero qual seria ele .....?')
acertou = False # condição para ativar a variavel 'acertou'
palpites = 0
while not acertou:                          # enquanto ele não acertou
    jogador = int(input('Digite seu palpite: '))
    palpites += 1
    if jogador == computador: # se jogador for igual a jogador
        acertou = True # recebe true e printa embaixo fora do aninhamento
    else:
        if jogador < computador:
            print('Mais....tente novamente')
        elif jogador > computador:
            print('Menos....tente novamente')


print(f'Acertou com {palpites} tentativas.')

