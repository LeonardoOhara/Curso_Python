# Crie um programa que leia o nome completo de uma pessoa e mostre:
# o nome com todas as letras maiusculas
# o nome com todas minusculas
# quantas letras ao todo ( sem considerar esçaços)
# quantas letras tem o primeiro nome

nome = str(input('escreva seu nome completo: '))
nome.strip()
print(f'seu nome completo maisuculo é :{nome.upper()}')
print(f'seu nome completo minusculo é: {nome.lower()}')
q = len(nome.replace(' ',''))
print(f'Seu nome completo contem {q} caracteres')
separa = nome.split()
print(f'O seu primeiro nome é {separa [0]} e a quantidade de letras é {len(separa [0])}')

# outro exemplo

nome = str(input('digite seu nome completo')).strip()
print ('analizando .......')
print (f'seu nome maiusculo é {nome.upper()}')
print (f'seu nome minusculo é {nome.lower()}')
print('seu nome completo é {}'.format(len(nome) - nome.count(' ')))
print(f'seu primeiro nome tem {nome.find(" ")} letras')
