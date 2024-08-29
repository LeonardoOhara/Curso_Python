#Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

print('==' * 35)
print('Bem Vindo! digite qualquer numero, se quiser cancelar digite 999')
print('Ele irá somar todos os numeros que você digitar')
print('==' * 35)
numero = int(input('Digite um numero'))
soma = 0
contador = 0
while numero != 999:                        # Verifica se dois valores são diferentes
    if numero != 999:
        contador += 1                           # += Adiciona o valor à variável e atribui o resultado.
        soma += numero                             # += atribui e soma usei para somar os numeros digitaos
        numero = int(input('Digite um numero'))
    elif numero == 999:
        print('FIM')
print(f'Foram digitados {contador} numeros e a soma deles foram {soma}')

# outro modo
numero = contador = soma = 0
numero = int(input('Digite um numero:'))
while numero != 999:
    soma += numero
    contador += 1
    numero = int(input('Digite um numero: '))
print(f'Foram Digitados {contador} numeros e a soma deles foi {soma}')
