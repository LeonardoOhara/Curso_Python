#Faça um programa que leia algo pelo teclado e mostre na
#tela o seu tipo primitivo e todas as informações possiveis
#sobre ela.

a = (input('Digite algo: '))
print(f'''
    É Alpha númerico? {a.isalnum()}, 
    É alpha? {a.isalpha()},
    É Minuscula? {a.islower()},
    É maiuscula? {a.isupper()},
    Está capitalizada? {a.istitle()},
    É Decimal? {a.isdecimal()},
    É numérica? {a.isnumeric()},
    É espaço? {a.isspace()}
      ''')

# outro exemplo

# Verifica se a string é alfanumérica (contém apenas letras e números)
print(f"É Alfanumérico? {a.isalnum()}")  # Retorna True
# Verifica se a string contém apenas letras
print(f"É Alfabético? {a.isalpha()}")  # Retorna False, pois há números
# Verifica se todas as letras da string são minúsculas
print(f"É Minúscula? {a.islower()}")  # Retorna False, pois há letras maiúsculas
# Verifica se todas as letras da string são maiúsculas
print(f"É Maiúscula? {a.isupper()}")  # Retorna False, pois há letras minúsculas
# Verifica se a string está capitalizada (a primeira letra é maiúscula e o restante é minúsculo)
print(f"Está Capitalizada? {a.istitle()}")  # Retorna True, pois segue o padrão de título
# Verifica se a string contém apenas dígitos decimais
print(f"É Decimal? {a.isdecimal()}")  # Retorna False, pois há letras
# Verifica se a string contém apenas caracteres numéricos
print(f"É Numérico? {a.isnumeric()}")  # Retorna False, pois há letras e não apenas números
# Verifica se a string contém apenas espaços em branco
print(f"É Espaço? {a.isspace()}")  # Retorna False, pois não contém apenas espaços
