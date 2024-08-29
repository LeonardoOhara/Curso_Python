#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
#Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
valores = list()
while True:
    valores.append(int(input('Digite Aqui: ')))
    continuar = str(input('Deseja Continuar? [S/N]:')).strip().upper()[0]
    for elemento in valores:
        while valores.count(elemento)>1:
            if valores.count(elemento)>1:
                print('Valor Duplicado não irei adicionar !')
            valores.remove(elemento)
    if continuar == 'N':
        break
print(f'Você digitou na ordem: {valores}')    
print(f'O programa ordenou em forma crescente: {sorted(valores)}')

# modo do guanabara

numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso')
    else:
        print('Valor Duplicado , não adicionado')
    r = str(input('quer continuar?:'))
    if r in 'Nn':
        break
print(f'Você digitou {sorted(numeros)}')