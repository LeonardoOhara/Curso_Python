#Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.


r = 1
while r == 1:
    sexo = str(input('Digite seu sexo [M/F]')).strip().upper()[0]
    if sexo != 'F' and sexo != 'M':
        print('Sexo incorreto por favor digite novamente!')
    else:
        r = 0
print('Cadastrado realizado com Sucesso')

# outro modo

sexo = str(input('Digite seu sexo: [M/F]')).strip().upper()[0]
while sexo not in 'M,F':
    sexo = str(input('Dados invalidos por favor informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com Sucesso')

