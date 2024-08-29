#Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

resp = 'S'
soma=numero=quant=menor=maior= 0
while resp in 'Ss':
    numero = int(input('Digite seu numero aqui'))
    soma += numero 
    quant += 1
    if quant == 1: 
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero 
    resp = ' '        
    resp = str(input('Quer continuar?')).upper().strip()[0]    
media = soma / quant    
print(f'O maior numero é {maior} e o menor é {menor}')
print(f'O média foi {media:.2f}')
print(f'Foram digitados {numero} numeros')



