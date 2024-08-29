#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média

pessoas = dict()
galera = list()
soma = media = 0
while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome: '))
    while True:
        pessoas['sexo'] = str(input('Sexo: [M/F]')).strip().upper()[0]
        if pessoas['sexo'] in 'MF':
            break
        print('Erro! Por favor digite apenas M ou F')
    pessoas['idade'] = int(input('Idade:'))
    soma += pessoas['idade']
    galera.append(pessoas.copy())
    while True:
        resp = str(input('Quer continuar [S/N]')).strip().upper()[0]
        if resp in 'SN':
            break
        print('Erro! Por favor digite apenas S ou N')
    if resp == 'N':
        break   
print('=-'*30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas')
media = soma / len(galera)
print(f'A media de idade é de {media:.2f} anos')
print(f'As mulheres cadastradas foram', end=' ')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f' {p["nome"]}', end=' ')
print()
print('Lista das pessoas que estão acima da média:')
for p in galera:
    if p['idade'] >= media:
        print ('      ')
        for k, v in p.items():
            print(f'{k} = {v}', end=' ')
        print()
print('<< Encerrado >>>')        