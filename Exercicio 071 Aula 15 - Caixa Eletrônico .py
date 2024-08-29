#Crie um programa que simule o funcionamento de um caixa eletrônico. No início, 
#pergunte ao usuário qual será o valor a ser sacado (número inteiro) 
#e o programa vai informar quantas cédulas de cada valor serão entregues. 
#OBS:
#considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

cont=div=total=0

while True:
    saque = int(input('Digite o valor do Saque: R$'))
    nota50 = saque//50
    resto50 = saque%50
    nota20 = resto50//20
    resto20 = resto50%20
    nota10 = resto20//10
    resto10 = resto20%10
    nota1 = resto10//1
    print(f'Seu saque foi de {saque:.0f} reais')
    if nota50 !=0:
        print(f'{nota50:.0f} de notas de 50 reais')
    if nota20 !=0:
        print(f'{nota20:.0f} de notas de 20 reais')
    if nota10 !=0:
        print(f'{nota10:.0f} de nota de 10 reais')    
    if nota1 !=0:
        print(f'{nota1:.0f} de notas de 1 real')
        break
print('Dinheiro Sacado! ')

