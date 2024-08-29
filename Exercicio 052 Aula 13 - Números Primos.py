#Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

numero = int(input('Digite um numero inteiro: '))
total = 0 # variavel para saber o numero dos divisivéis
for c in range (1 , numero+1):
    if numero % c == 0: # se o numero for divisivel pelo contador (c)
        print('\033[32m', end=' ')
        total += 1 # se o numero foi divisivel é mais um numero no total
    else:
        print('\033[31m', end=' ')
    print(c, end='')
print(f'\n \033[m O numero {numero} foi dividido {total} vezes')
if total == 2:   # se o total for igual a 2
    print('Ele é primo')
else:
    print('ele não é primo')

