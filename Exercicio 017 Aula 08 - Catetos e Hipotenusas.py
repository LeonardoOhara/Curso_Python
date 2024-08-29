# faça um programa que leia o comprimento do cateto oposto e do cateto
# adjacente de um tricangulo retangulo, calcule e mostre o comprimento
# da hipotenusa.

import emoji
from math import sqrt, pow
co = float(input('digite o valor do cateto oposto'))
ca = float(input('digite o valor do cateto adjacente'))
r = sqrt(pow(co,2) + pow(ca,2))
print (emoji.emojize(f'o comprimento da hipotenusa é {r:.2f} :smiling_face_with_sunglasses:'))

# outra maneira de fazer o codigo

co = float(input('digite o valor do cateto oposto'))
ca = float(input('digite o valor do cateto adjacente'))
r = (co ** 2 + ca ** 2 ) ** (1/2)
print (f'a hipotenusa é {r:.2f}')

# outro modelo bem mais simples

import math
co = float(input('digite o valor do cateto oposto'))
ca = float(input('digite o valor do cateto adjacente'))
r = math.hypot(ca, co)
print(f'a hipotenusa é {r:.2f}')

# ou

from math import hypot
co = float(input('digite o valor do cateto oposto'))
ca = float(input('digite o valor do cateto adjacente'))
r = hypot(ca, co)
print(f'a hipotenusa é {r:.2f}')
