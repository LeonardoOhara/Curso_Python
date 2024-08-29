#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
v = 0
while True:
    jogardor = int(input('Digite um numero'))
    computador = randint(0,11)
    resultado = jogardor + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou impar ? [P/I]')).strip().upper()[0]
    print(f'O jogador escolheu {jogardor} e o computador {computador} o resultado foi {resultado}') 
    print(f'Deu Par' if resultado % 2 == 0 else 'Deu Impar')
    if tipo == 'P':
        if resultado %2 == 0:
            print('você venceu')
            v += 1
        else:
            print('Você perdeu')
            break
    elif tipo == 'I':
        if resultado %2 == 1:
            print('você venceu')
            v += 1
        else:
            print('Voce perdeu') 
            break             
    print('Vamos jogar novamente?')    
print(f'Game Over Você venceu {v} vezes')