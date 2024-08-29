#Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

for c in range (1 , 51):                    # aqui a cpu faz 3 movimentos pq nao tem o outro numero de pular (1 , 51 ,'2').
    print('.', end = ' ')
    if c % 2 == 0:
        print(c , end =' ')
print('Aqui estão todos numeros pares')

# outro exemplo exigindo menos da memoria

for c in range (2 , 52 , 2):
    print('.', end = '')
    print(c, end = ' ')
print('FIM')

