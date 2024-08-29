#Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

# função Area ----------------------------------------------------------------
from re import L


def area (l,c):
    r = l*c
    print('-'*47)
    print(f'A area de um terreno {l} x {c} é de {r}m².')
    print('-'*47)
# programa principal ----------------------------------------------------------------
print ('CONTROLE DE TERRENO')
print ('-'*20)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))    
area(l,c)
