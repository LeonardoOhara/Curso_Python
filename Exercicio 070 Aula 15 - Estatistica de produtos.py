#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. 
#No final, mostre:

#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.

totp=totpr=menor=cont=0
produto2 = ''
while True:
    produto = (str(input('Digite o produto: ')))
    preco = (float(input('Digite o valor: R$'))) 
    totp += preco
    if preco > 1000:
        totpr +=1
    cont +=1
    if cont == 1 or preco < menor:
        menor = preco
        produto2 = produto
    resp = ' '    
    while resp not in 'SN':
        resp = str(input('Deseja continar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total do preço: {totp}')     
print(f'{totpr} custa mais de $1000')
print(f'O produto {produto2} custa : {menor}')