#xercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.


resultado = 0
cont = 0
for _ in range(1, 7):  # Usei "_" como variável de iteração, pois não a utilizamos diretamente.
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:  # Verifica se o número é par
        cont += 1 # conta quantos numeros pares tem
        resultado += numero  # Acumula a soma apenas se for par

print(f'você informou {cont} numeros pares e soma dos números é: {resultado}')
