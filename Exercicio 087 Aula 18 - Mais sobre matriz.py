#Aprimore o desafio anterior, mostrando no final:                                                    
#A) A soma de todos os valores pares digitados.                                                                                                  
#B) A soma dos valores da terceira coluna.                                                                                                                
#C) O maior valor da segunda linha.

print('=-'*15)
print('Matriz Melhorada')
print('=-'*15)
matriz = [[0,0,0], [0,0,0], [0,0,0]] # [ [lista0], [lista1], [lista2]]
resultado = resultado2 = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))
        if matriz[l][c] % 2 == 0:
            resultado += matriz[l][c]     
        resultado2 = matriz[0][2] + matriz[1][2] + matriz[2][2]
print ('-='*25)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('=-'*25)    
print(f'A soma dos pares são: {resultado}')          
print(f'A soma dos valores da terceira coluna é : {resultado2}')
print(f'O maior valor da segunda linha é : {max(matriz[1])}')
print('=-'*25)