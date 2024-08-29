# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

numero = int(input('Digite um numero '))
if numero % 2 ==0:
    print ('O numero é par')
else:
    print('O numero é impar')


# outro modo de fazer

numero = int(input('Digite um numero'))
resultado = numero % 2
if resultado == 0:
    print('O numero é Par')
else:
    print('O Numero é Impar')