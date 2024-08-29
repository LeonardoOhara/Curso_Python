#Faça um programa que leia a largura e a altura de uma parede
#em metros, calcule a sua área e a quantidade de tinta necessária
#para pinta-la, sabendo que cada litro de tinta, pinta uma
#área de 2m².

a = float(input('qual o valor da altura da parede?'))
l = (float(input('qual o valor da largura da parede?')))

# aqui eu multipliquei 'a' e 'l' e o resultado dividi por 2 que seria o valor dos 2m²de tinta.

r = a*l
r2 = r/2

print(f'sua parede tem uma dimenção de {a} metros de altura e {l} metros de largura')
print (f'a area da parede é {r:.2f}m² e foi usada {r2:.2f} litros de tinta')
