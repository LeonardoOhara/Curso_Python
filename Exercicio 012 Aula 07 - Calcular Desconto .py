#Faça um algoritmo que leia o preco de um produto e mostre seu
#novo preço, com 5% de desconto.

produto = float(input('digite o valor do produto R$'))
# aqui foi dividido 5 por 100 e multiplicado por produto e subtrai o preço antigo com o desconto
desconto = produto - (produto*5/100)
print(f'Você comprou no valor de R$ {produto:.2f} e ganhou um desconto de 5% custando apenas {desconto:.2f} reais')
