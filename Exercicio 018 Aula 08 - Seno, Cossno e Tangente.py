# Faça um programa que leia um ângulo qualquer e mostre na
# tela o valor do seno, cosseno e tangente desse ângulo.

import math
angulo = float(input('digite o angulo'))
seno = math.sin(math.radians(angulo))
print (f'O angulo de {angulo} tem o seno {seno:.2f}')
cos = math.cos(math.radians(angulo))
print (f'O angulo de {angulo} tem o cosceno {cos:.2f}')
tg = math.tan(math.radians(angulo))
print (f'O angulo de {angulo} tem a tangente {tg:.2f}')

# outro exemplo

from math import radians, sin, cos, tan
angulo = float(input('digite o angulo'))
seno = sin(radians(angulo))
print (f'O angulo de {angulo} tem o seno {seno:.2f}')
cos = cos(radians(angulo))
print (f'O angulo de {angulo} tem o cosceno {cos:.2f}')
tg = tan(radians(angulo))
print (f'O angulo de {angulo} tem a tangente {tg:.2f}')