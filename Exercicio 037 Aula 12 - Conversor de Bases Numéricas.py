# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal.


num = int(input('Digite um numero'))
print('[1] Para converter em Binario')
print('[2] Para Converter em Octal')
print('[3] Para converter em Hexadecimal')
opcao = int(input('Digite qual opção deseja'))
b = bin(num)[2:]
o = oct(num)[2:]
h = hex(num)[2:]
if  opcao ==1 :
    print(f'O numero Binario é {b}')
elif opcao ==2 :
    print(f'O numero Octal é :{o}')
elif opcao ==3 :
    print(f'O numero Hexadecimal é : {h}')
else:
    print(f'Opção Invalida!')





