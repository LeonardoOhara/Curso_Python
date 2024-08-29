from random import randint
from time import time

print('Adivinhe o numero que vou pensar de 0 a 10')
n = int(input('Digite aqui'))
r = randint (0,10)
if n==r:
    print('Acertou ! Você é bom nisso.')
else:
    print('tente de novo =/ ')

print(f'O numero sorteado foi {r} e o numero você digitou foi {n}')

# outro exemplo

import random
from tqdm import tqdm
import time
print('Qual filme vamos Assistir ?')
for i in tqdm(range(10)):
    time.sleep(0.5)
lista = ['Ação', 'Aventura', 'Comédia', 'Besteirol', 'Suspense', 'Drama', 'Terror']
resultado = random.choice(lista)
print(f'Filme escolhido {resultado}')
