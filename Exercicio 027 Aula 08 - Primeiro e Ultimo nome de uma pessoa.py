#Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.

print('Seja bem vindo')
n = str(input('Escreve seu nome completo :')).strip()
nome = n.split()
print(f'Seu primeiro nome é {(nome[0])}')
print(f'Seu ultimo nome é {(nome[len(nome)-1])}')


