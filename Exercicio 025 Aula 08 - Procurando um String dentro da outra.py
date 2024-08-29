# Crie um programa que leia
# o nome de uma pessoa e diga se ela tem “SILVA”

nome = str(input('Digite seu nome :')).strip()
nome = str(nome.upper())
nome = str(nome.lower())
result = ('silva' in nome)
print (f'Seu nome contém Silva? {result}')

# outro exemplo

nome = str(input('Digite seu nome completo')).strip()
print('Seu nome completo tem Silva? {}.'.format('silva' in nome.lower()))

