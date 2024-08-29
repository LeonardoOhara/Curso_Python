#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior_peso = float('-inf')
menor_peso = float('inf')
for i in range (5):
    peso = float(input(f'Digite o peso da pessoa {i+1} (em KG)'))
    if peso > maior_peso:
        maior_peso = peso
    if peso < menor_peso:
        menor_peso = peso
print(f'O maior peso é {maior_peso} KG')
print(f'O menor peso é {menor_peso} KG')

# Outro exemplo

maior = 0
menor = 0
for p in range (1,6):
    peso = float(input(f'Peso da {p} pessoa:'))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso é {maior}')
print(f'O menor peso é {menor}')


