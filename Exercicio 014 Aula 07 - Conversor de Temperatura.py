# converter Celsius para Fahrenheit
F = float(input('Digite o valor da temperatura em Cº'))
resultado = (F*1.8)+32
print(f'A temperatura em Fahrenheit é {resultado:.2f} Fº')

# Converter Fahrenheit para Celsius
C = float(input('Digite o valor da temperatura em Fº'))
resultado = (C-32)*5/9
print(f'A temperatura em Celsius é {resultado:.2f} Fº')

# outra forma de calculo para Celsius

F = float(input('digite o valor da temperatura em Cº'))
r = 9*F/5 + 32
print(f'o valor em F° é {r:.2f}')

C = float(input('Digito o valor da Temperatura em Fº'))
r = (C-32)*5/9
print(f'O valor em Cº é {r:.2f} ')
