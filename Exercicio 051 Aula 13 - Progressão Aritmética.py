#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

print('=' * 36)
print('10 TERMOS DA PROGRESSÃO ARITIMETICA')
print('=' * 36)


t = int(input(f'Primeiro Termo '))
r = int(input(f'Razão '))
d = t + (10 - 1) * r         # calculo para o décimo termo
for c in range (t, d + r , r): # aqui no 10 termo temos q adicionar décimo + razão.
    print(f'{c}', end= '-->')
print('FIM')
