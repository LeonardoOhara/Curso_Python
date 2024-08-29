#Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
total = 0
total2 =0
for c in range (1 , 8):
    ano = int(input(f'O ano da {c}º de nascimento: '))
    atual = date.today().year
    idade = atual - ano
    if idade >= 18:
        total += 1
    elif idade < 18:
        total2 += 1
print(f'o total de pessoas mais velhas é de : {total} \n'
      f'e de pessoas menor de 18 anos é de : {total2}')

