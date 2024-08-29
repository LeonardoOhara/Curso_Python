#Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa,
# mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

soma_idade = 0
idade_homem_velho = 0
nome_homem_velho = ''
mulher_menor_20 = 0

for c in range (4):
    print(f'---- {c + 1} Pessoa ----')
    nome = str(input('Digite seu nome'))
    idade = int(input('Digite sua idade'))
    sexo = str(input('Digite seu Sexo [M/F]'))

    # Atualizar a soma das idades
    soma_idade += idade

    # Verificar se a pessoa é o homem mais velho
    if sexo.upper() == 'M' and idade > idade_homem_velho:
        idade_homem_velho = idade
        nome_homem_velho = nome

    # Verificar se a pessoa é uma mulher com menos de 20 anos
    if sexo.upper() == 'F' and idade < 20:
        mulher_menor_20 += 1

#calcular a média da idade
media_idade = soma_idade/4

#exibir resultados
print(f'A média de idade do grupo é : {media_idade}')
if nome_homem_velho:
    print(f'O homem mais velho é {nome_homem_velho} com {idade_homem_velho}')
else:
    print(f'não há homens no grupo')
print(f'Exite {mulher_menor_20} mulheres com menos de 20 anos no grupo')

