from ex108 import moeda


p = float(input('Digite um preço R$: '))
print(f'A metade de R$ {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}') # type: ignore
print(f'O dobro de R$ {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}') # type: ignore
print(f'Aumentando 10%, Temos {moeda.moeda(moeda.aumentar(p , 10))}') # type: ignore


