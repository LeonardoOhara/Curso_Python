# Aula 08 Utilizando Modulos:

# Comandos :

# 'import'  --> para importar uma biblioteca generalizada. ex: import math
# 'from' -->  cria uma importação única. ex: from math import srqt

# Biblioteca math:

# 'ceil' = arredondamento pra cima
# 'floor' = arredondamento pra baixo
# 'trunc' = trunca numero , elimina virgula pra frente
# 'pow' = power de potencia que funciona semelhante aos **
# 'sqrt' = raiz quadrada
# 'factorial' = calculo de fatorial de numero


#exemplo de usar o math
import math
num = int(input('digite um numero'))
raiz = math.sqrt(num)
print(f'a raiz de {num} é {math.floor(raiz)}')

# Outro Exemplo
import math
num = int(input('digite um numero'))
raiz = math.sqrt(num)
print(f'a raiz de {num} é {raiz:.2f}')

# Esse outro exemplo com biblioteca especifica sqrt
from math import sqrt
num = int(input('digite um numero'))
raiz = sqrt(num)
print(f'a raiz de {num} é {raiz:.2f}')

# Esse exemplo é de numeros aleatorio
import random
num = random.random()
print(num)

# esse de baixo é um random com numeros inteiro de 1 a 10 #
import random
num = random.randint(1, 10)
print(num)

import emoji
print(emoji.emojize('salve salve :face_with_spiral_eyes:'))




