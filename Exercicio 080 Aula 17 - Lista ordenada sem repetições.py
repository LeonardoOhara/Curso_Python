#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista = []
for c in range (0,5):
    n = (int(input('Digite um valor: ')))
    if c == 0 or n > lista[-1]: #Se ele for o primeiro ou  se o numero foi maior q o ultimo elemento
        lista.append(n)
        print('adicionado ao fim da lista...')     
    else:
        pos = 0
        while pos < len(lista): #enquanto a posição for menor que lista
            if n <= lista[pos]: 
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos +=1
print(f'Os valores Digitados em ordem foram {lista}')
