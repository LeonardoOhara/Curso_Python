def soma (a, b):
    print(f'A = {a} + {b}')
    s = a + b
    print(f'A soma A + B = {s}')

# programa principal

soma (b=4,a=5)
soma(7,2)

# ----------------------------------------------------------------
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [7,2,5,0,4]
dobra(valores)
print(valores)

# ----------------------------------------------------------------
def soma1 (*valores): #desempacotamento
    s = 0
    for num in valores:
        s += num
    print(f'A soma dos {valores} é {s}')


soma1 (5,2)
soma1 (3,4,5,6)
