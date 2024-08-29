# faça um programa que leia um numero de 0 a 9999 e mostre
# na tela cada um dos digitos separados

numero = int(input("digite a senha do seu cartão "))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print(f'analisando........')
print(f'A senha digitada foi {numero}')
print(f'Unidade : {u}')
print(f'Dezena : {d}')
print(f'Centena : {c}')
print(f'Milhar : {m}')


# modo que não da certo :

numeros = int(input("digite a senha do seu cartão "))
r = str(numeros)
print(f'a unidade é : {r [3]}')
print(f'a dezena é : {r [2]}')
print(f'a centena é : {r [1]}')
print(f'a milhar é : {r [0]}')