#Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#– O primeiro valor é maior
#– O segundo valor é maior
#– Não existe valor maior, os dois são iguais

n1 = int(input('digite um numero:'))
n2 = int(input('digite outro numero:'))

if n1>n2:
    print('O primeiro numero é maior ')
elif n2>n1:
    print('O Segundo numero é maior')
elif n1==n2:
    print('Não existe valor maior, os dois são iguais')

