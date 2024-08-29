#Crie um algoritmo que leia um número e mostre o seu dobro,
#triplo e raiz quadrada.

numero = int(input('Digite seu numero'))
print(f'O numero digitado foi {numero}\nO dobro é {(numero*2)}\nO Triplo é {(numero*3)}\nE a raiz quadrada é {(numero**(1/2)):.2f}')
# Raiz Quadrada se calcula com Potencia divido por meio **(1/2)


#or with pow
umero = int(input('Digite seu numero'))
print(f'O numero digitado foi {numero}\nO dobro é {(numero*2)}\nO Triplo é {(numero*3)}\nE a raiz quadrada é {pow (numero,(1/2)):.2f}')
