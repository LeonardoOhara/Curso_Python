#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep
numero = int(input('Digite um Numero'))
numero2 = int(input('Digite outro Numero'))
opcoes = 0
print('=' * 35)
print('''[ 1 ] Soma
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos numeros 
[ 5 ] Sair do Programa''')
print('=' * 35)
while not opcoes == 5:
    opcoes = int(input('escolha a opção'))
    if opcoes > 5:
        print('error')
    if opcoes == 1:
        resultado = numero + numero2
        print(f'A soma de {numero} + {numero2} é: {resultado}')
    if opcoes == 2:
        resultado2 = numero * numero2
        print(f'A multiplicação de {numero} x {numero2} é: {resultado2}')
    if opcoes == 3:
        if numero > numero2:
            print(f'O maior numero é o {numero}')
        elif numero < numero2:
            print(f'O maior numero é o {numero2}')
        else:
            print(f'Os 2 numeros são iguais')
    if opcoes == 4:
        numero = int(input('Digite um Numero'))
        numero2 = int(input('Digite outro Numero'))
    if opcoes == 5:
        print('')
print('Saindo......')
sleep(2)
print('Fim do Programa')

# Outra forma de fazer

num1 = int(input('Digite um numero:'))
num2 = int(input('Digite outro numero'))
opcoes = 0
print('Bem Vindo ao Software multi função')
print('==' * 20)
print('''[ 1 ] Soma
[ 2 ] Multiplicação
[ 3 ] Maior 
[ 4 ] Digite outros valores
[ 5 ] Sair do Programa''')
print('==' * 20)
while opcoes != 5:
    opcoes = int(input('Selecione sua opção:'))
    if opcoes == 1:
        soma = num1 + num2
        print(f'A soma de {num1} e {num2} é : {soma}')
    elif opcoes == 2:
        mult = num1 * num2
        print(f'A multiplicação de {num1} e {num2} é : {mult}')
    elif opcoes == 3:
        if num1 > num2:
            print(f'O numero maior é {num1}')
        else:
            print(f'O numero maior é {num2}')
    elif opcoes == 4:
        print('Digite novamente')
        num1 = int(input('Digite um numero'))
        num2 = int(input('Digite outro numero'))
    elif opcoes == 5:
        print('Finalizando Aplicação')
    else:
        print('Error , Digite novamente')
print('Fim do Programa')
