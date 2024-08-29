# interactive help - ajuda interativa
#help()
#print(input.__doc__)
#help(input)

# docstrings - string de documentação

from re import A


def contador (i,f,p):
    ''' -> Faz uma contagem e mostra na tela.
 para i : inicio da contagem
 para f : fim da contagem
 para p: passso da contagem
 return: sem retorno'''
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('FIM')
contador(2, 10, 2)

help(contador)
print('-'*50)
# parametros opcionais 

def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma é {s}')
somar (3,2,5)
somar (8,4)
somar ( )
print ('-'*50)
# escopo de variaveis

def funcao():
   n1 = 4
   print(f'N1 dentro vale {n1}')


n1 = 2 
print(f'N1 fora vale {n1}')
funcao ()
print ('-'*50)

def teste(b):
    
    a = 8
    b +=4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 12
teste(a)
print(f'A fora vale {a}')

# retorno de valores 
# return

def soma(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = soma(3,2,5)
r2 = soma(1,7)
r3 = soma(4)


print(f'Os meus calculos deram {r1}, {r2} e {r3}')

# parte pratica 

def factorial(num =1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

n = int(input('Digite um numero: '))

print(f'O fatorial de {n} é igual a {factorial(n)}')
f1 = factorial(5)
f2 = factorial(4)
f3 = factorial()
print(f'Os resultaos são {f1}, {f2}, {f3}')

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

n = int(input('Digite um numero: '))

if par(n):
    print(f'O numero {n} é par')
else:
    print(f'O numero {n} é impar')