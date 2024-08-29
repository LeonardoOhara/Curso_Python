# Faça um programa que leia o número inteiro e mostre na tela
# o seu sucessor e seu antecessor.

print('='*50)
print('Verifique qual o Numero Sucessor e Antecessor aqui!')
print('='*50)
numero = int(input('Digite um numero aleatório: '))
sucessor = numero + 1
antecessor = numero - 1
print(f'O numero que você digitou foi {numero}\nseu sucessor é {sucessor}\ne seu antecessor é {antecessor}')
print('Fim da Aplicação')

# outro modo com 2 linhas

numero = int(input('Digite um numero'))
print(f'O numero que você digitou foi {numero} e seu sucessor é {(numero+1)} e seu antecessor é {(numero-1)}')
