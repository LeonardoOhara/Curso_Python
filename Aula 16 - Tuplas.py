
#tuplas sao imutaveis 


lanche = 'pizza','sorvete','bauru','pastel'
print(lanche)

for comida in lanche:
    print(f'{comida}')
    print('='*20)

for cont in range (0 , len(lanche)):
    print(f'{lanche[cont]}')

for pos, comida in enumerate(lanche):
    print(f'{comida} e {pos}')
    