
from ex109 import moeda


p = int(input('Digite um preço R$: '))
print(f'A metade de R$ {moeda.moeda(p)} é {moeda.metade(p,True)}')
print(f'O dobro de R$ {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando 10%, Temos {moeda.aumentar(p, 10, True)}')
print(f'Reduzindo 13%, Temos{moeda.diminuir(p, 13, True)}')

