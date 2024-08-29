#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
#no final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.


valores = list()
for cont in range (0,5):
    valores.append(int(input(f'Digite aqui na posição {cont}: '))) # .append para inserir uma variavel na lista
    if cont == 0:  # Se contador for igual a zero 
        max = min = valores[cont] # maior e o menor será igual a contador
    else: # se não  
        if valores[cont] > max: # se contador for maior que o maior valor 
            max = valores[cont] # valor passa a ser ele 
        if valores[cont] < min: # se contador for menor que o menor valor
            min = valores[cont] # valor passa a ser ele
print('=-'*30)
print(f'Você Digitou os numeros {valores}')
print('=-'*30)            
print(f'O maior numero é {max} nas posições ', end='')        
for i, v in enumerate(valores): # i = indice , v = valor # enumarate para pegar a posição da lista
    if v == max: 
        print(f'{i}...', end='') 
print()
print(f'O menor numero é {min} nas posições ', end='')
for i, v in enumerate(valores):
    if v == min:
        print(f'{i}...', end='')
