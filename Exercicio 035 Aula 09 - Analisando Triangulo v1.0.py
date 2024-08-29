# Desenvolva um programa que leia o comprimento de três retas e
# diga ao usuário se elas podem ou não formar um triângulo.

t1 = float(input('Digite a primeira medida do triangulo:'))
t2 = float(input('Digite a segunda medida do triangulo:'))
t3 = float(input('Digite a terceira medida do triangulo'))

if t1 < t2 + t3 and t2 < t1 +t3 and t3 < t2 + t1:
    print('Sua medida pode formar um triangulo')
else:
    print('sua medida não pode formar um triangulo')

