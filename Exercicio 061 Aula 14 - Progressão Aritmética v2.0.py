#Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('=' * 36)
print('10 TERMOS DA PROGRESSÃO ARITIMETICA')
print('=' * 36)
primeiro = int(input(f'Primeiro Termo '))
razao = int(input(f'Razão '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo} - ', end='')
    termo += razao
    cont += 1
print('FIM')
