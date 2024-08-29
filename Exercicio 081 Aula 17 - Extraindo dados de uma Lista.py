#Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.                  
#Depois disso, mostre:                                                                                                                                                
#A) Quantos números foram digitados.                                                                                                                    
#B) A lista de valores, ordenada de forma decrescente.                                                                                          
#C) Se o valor 5 foi digitado e está ou não na lista.

from ast import While


n = []
cont = 0
while True: 
    n.append(int(input('Digite aqui o numero: ')))
    cont+=1
    resp = str(input('Deseja continuar ? [S/N]: ')).strip().upper()[0]
    print('=-'*30)
    if resp in 'Nn':
        break
if 5 in n:
    print('tem numero 5')
else:
    print('Não tem 5')    
print(f'Você digitou {cont} Elementos')
n.sort(reverse=True)
print(f'Essa é a lista em forma decrescente : {n}')

# modo guanabara 

valores = []
while True:
    valores.append(int(input('Digite aqui :')))
    resp = str(input('Deseja continuar? [S/N]:'))
    if resp in 'Nn':
        break
print('-='*30)
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('Tem 5 na lista')
else:
    print('Nao tem 5 na lista')
    