#Faça um programa que leia uma frase pelo teclado e mostre quantas
#vezes aparece a letra “A”, em que posição ela aparece a primeira
#vez e em que posição ela aparece a última vez.

nome = str(input("Digite seu nome ")).strip()
nome= str(nome.upper())
res = str(nome.count('A'))
print(f'A frase contem {res} letras A.')
print(f'A letra A começa em {nome.find("A")+1}')
print(f'A letra A termina em {nome.rfind("A")+1}')

# outro exemplo

frase = str(input('Digite uma frase')).upper().strip()
print (f'A frase contem {frase.count("A")}')
print (f'A letra A aparece primeiro em {frase.find("A")+1}')
print (f'A letra A aparece por ultimo em {frase.rfind("A")+1}')





