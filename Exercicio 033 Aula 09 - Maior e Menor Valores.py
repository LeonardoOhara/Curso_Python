#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

numero1 = int(input('Digite o primeiro numero'))
numero2 = int(input('Digite o segundo numero'))
numero3 = int(input('Digite o terceiro numero'))

# identificando numero menor
menor = numero1
if numero2<numero1 and numero2<numero3:
    menor = numero2
if numero3<numero1 and numero3<numero2:
    menor = numero3

# verificando maior
maior = numero1
if numero2>numero1 and numero2>numero3:
    maior = numero2
if numero3>numero1 and numero3>numero2:
    maior = numero3

print(f'O numero menor é {menor} e o maior é {maior}')