#xercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
lista = list()
pares = list()
impares = list()
while True:
    lista.append(int(input('Digite aqui um valor: ')))
    resp = str(input('Deseja continuar ? [S/N]'))
    if resp in 'Nn':
        break
print(f'Numeros digitados foram: {lista}')
for indice , valor in enumerate(lista): # i = indice , v = valor
    if valor % 2 == 0:
        pares.append(valor)
    elif valor % 2 == 1:
        impares.append(valor)
print(f'A lista de pares são {pares}')
print(f'A lista de impares são {impares}')