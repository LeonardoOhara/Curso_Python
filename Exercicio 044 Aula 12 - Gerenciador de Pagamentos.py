#Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal
#– 3x ou mais no cartão: 20% de juros


print ('Portal do Aprendizado')
preco = float(input('Digite o preço do produto R$ '))
print('''[1]A Vista 
[2]A Vista do Cartão 
[3]2x cartão 
[4]3x cartão''')
opcao = int(input('Selecione a opção:'))
if opcao == 1:
    total = preco - (preco * 10/100)
    preco2 = preco*10/100
    print(f'Sua compra de R${preco:.2f} teve 10% de desconto {preco2:.2f} reais e agora custa: {total:.2f}')
elif opcao == 2:
    total = preco - (preco * 5/100)
    preco2 = preco*5/100
    print(f'Sua compra de R${preco:.2f} teve 5% de desconto {preco2:.2f} reais e agora custa: {total:.2f}')
elif opcao == 3:
    total = preco
    parcela = total/2
    print(f'Sua compra será parcelada em 2x de R$ {parcela:.2f}')
elif opcao == 4:
    total = preco + (preco*20/100)
    totparc = int(input('Digite o numero de parcelas:'))
    parcela = total / totparc
    print(f'Sua compra será parcelada em {totparc:.0f} vezes de R$ {parcela:.2f} com juros!')
else:
    total = 0
    print('opção invalida de pagamento !!!')
print(f'Sua compra de R$ {preco:.2f} vai custar {total:.2f} no final')

