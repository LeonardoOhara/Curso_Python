#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

bloco = dict()
bloco['nome'] = str(input('Nome: '))
bloco['media']  = float(input(f'Média de {bloco["nome"]}: '))
if bloco['media'] >= 7:
    bloco['situação'] = 'Aprovado'
elif 5 <= bloco['media'] < 7:
    bloco['situação'] = 'Recuperação'
else:
    bloco['situação'] = 'Reprovado'
print('=-'*20)
for k , v in bloco.items(): # print com for 
    print(f'O {k} é igual a {v}')
print('--------------------------------')
print(f'O nome é igual a {bloco["nome"]}')
print(f'A media é igual a {bloco["media"]}')
print(f'A situação é igual a {bloco["situação"]}')
print('=-'*20)