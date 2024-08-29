# primeiro exemplo da aula
c = 1
while c < 10:
    print(c)
    c += 1
print('fim')

# Segundo exemplo

n = 1
while n != 0:
    n = int(input('Digite um valor'))
print('fim')

# outro exemplo

r = 'S'
while r == 'S':
    n = int(input('Digite um valor'))
    r = str(input('Deseja continuar ? [S/N]')).upper()
print('fim')

# outro exemplo

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor'))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Voce Digitou {impar} numeros impas e {par} numeros par')
