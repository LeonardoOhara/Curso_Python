#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

#– EQUILÁTERO: todos os lados iguais
#– ISÓSCELES: dois lados iguais, um diferente
#– ESCALENO: todos os lados diferentes

t1 = float(input('Digite a primeira medida do triangulo:'))
t2 = float(input('Digite a segunda medida do triangulo:'))
t3 = float(input('Digite a terceira medida do triangulo'))

if t1 < t2 + t3 and t2 < t1 +t3 and t3 < t2 + t1:
    print('Sua medida pode formar um triangulo')
    if t1 == t2 == t3:
        print('é um Equilatéro')
    elif  t1 == t3 != t2 or t2 == t1 != t3 or t2 == t3 != t1:
        print('é um Isosceles')
    elif t1!= t2 != t3:
        print('é um Escaleno')
else:
    print('sua medida não pode formar um triangulo')

#============================================================#
#outro modo

t1 = float(input('Digite a primeira medida do triangulo:'))
t2 = float(input('Digite a segunda medida do triangulo:'))
t3 = float(input('Digite a terceira medida do triangulo'))

if t1 < t2 + t3 and t2 < t1 +t3 and t3 < t2 + t1:
    print('Sua medida pode formar um triangulo')
    if t1 == t2 == t3:
        print('é um equilatéro')
    elif t1 != t2 != t3:
        print('é um escaleno')
    else:
        print('é um escaleno')
else: print ('Sua medida não pdoe formar um truangulo')


