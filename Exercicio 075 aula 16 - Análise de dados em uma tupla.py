#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.

numero = (int(input('Digite um numero: ')),
            int(input('Digite outro numero:')),
            int(input('Outro:')) ,
            int(input('E outro:')))
print(f'Os numeros digitados foram: {numero}')
print(f'O numero 9 apareceu {numero.count(9)} vezes')
if 3 in numero:
    print(f'O numero 3 está na posição {numero.index(3)+1}')
else:
    print('Não há numero 3 ')
print('Os valores pares digitados foram', end='')
for n in numero:
    if n % 2 == 0:
        print(n, end='')

