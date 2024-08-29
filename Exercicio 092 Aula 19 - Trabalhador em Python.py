#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

import datetime

from numpy import datetime_data
agora = datetime.datetime.now()
ano_atual = agora.year
Cadastro = dict()

Cadastro['Nome'] = str(input('Nome: '))
Cadastro['Nascimento'] = int(input(f'Ano de Nascimento: '))
Cadastro['CTPS'] = int(input(f'Carteira de Trabalho (0 não tem):'))
Nova_idade = ano_atual - Cadastro['Nascimento']
if Cadastro['CTPS']!= 0:
    Cadastro['Contratacao'] = int(input(f'Ano de contratação:'))
    CPTS = (Cadastro['Contratacao'] + 35) - Cadastro['Nascimento']
    Cadastro['Salario'] = int(input(f'Salario: R$'))
    Cadastro['Aposentadoria'] = CPTS 
print('=-'*20)
print(f'O nome é :{Cadastro["Nome"]}')
print(f'Tem {Nova_idade} anos de idade')
if Cadastro['CTPS'] != 0:
    print(f'Seu cadastro no CPTS é {Cadastro["CTPS"]}')
    print(f'Salario é de {Cadastro["Salario"]} reais')
    print(f'Você irá se aposentar  com {CPTS} anos de idade')
    print('=-'*20)

for i, k in enumerate(Cadastro):
    print(f' {k} é igual a {Cadastro[k]}')

# modo Guanabara 

from datetime import date, datetime
dados = dict()
dados['nome'] = str(input('nome: '))
nasc = int(input('ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem):'))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação'))
    dados['salarios'] = float(input('Salario: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('=-' * 30)
for i , k in enumerate(dados):
    print(f' {k} é igual a {dados[k]}')