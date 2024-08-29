#Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
#Exemplos de palíndromos:
#APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

minha_string = str(input('Digite Algo')).strip().upper()
string_invertida = ''
for c in minha_string:
    string_invertida = c + string_invertida.strip()
if minha_string == string_invertida:
    print('Essa frase é um palindromo')
else:
    print('não é um palindromo')
print(f'{minha_string} ao contrário é : {string_invertida }', end= '' )

# outro modo

frase = str(input('\n Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range (len(junto) -1 , -1 , -1):
    inverso += junto[letra]
if inverso == junto:
    print('Essa Frase é um Palindromo')
else:
    print('Essa frase não é um Palindromo')
print( junto , inverso)

# outro modo sem for

frase = str(input('\n Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto [::-1]
if inverso == junto:
    print('Essa Frase é um Palindromo')
else:
    print('Essa frase não é um Palindromo')
print( junto , inverso)
