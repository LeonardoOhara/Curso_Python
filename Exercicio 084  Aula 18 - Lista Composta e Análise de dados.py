# Python 084: Faça um programa que leia nome e peso de várias pessoas,guardando tudo em uma lista. No final, mostre:                                                                                                    
#A) Quantas pessoas foram cadastradas.                                                                                                                
#B) Uma listagem com as pessoas mais pesadas.                                                                                                    
#C) Uma listagem com as pessoas mais leves.

from emoji import analyze

print('=-'*25)
print('Lista composta e Analise de dados:')
print('=-'*25)
temp = list()
princ = list()
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    princ.append(temp[:])
    temp.clear()
    resp = ' '
    resp = str(input('Quer continuar?'))
    if resp in 'Nn':
        break
print('=-' * 30)
print(f'Você cadastrou {len(princ)} pessoas') 
print(f'O Maior peso foi de {max(princ)[1]}KG. Os participantes com maiores pesos foram : ', end= '')    
for p in princ:
    if p[1] == max(princ)[1]:   
        print(f'{p[0]}, ' , end = '') 
print()
print(f'O Menor peso foi de {min(princ)[1]}KG. Os participantes com menores pesos foram :', end= '')
for p in princ:
    if p[1] == min(princ)[1]:
        print(f'{p[0]}, ', end = '')     
print()
