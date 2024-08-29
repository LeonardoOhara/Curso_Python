
# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.


while True:
    n = int(input('Qual a tabuada que eu faço?'))
    if n <= 0:
        break
    for t in range (1 ,11):
        print(f'{n} x {t} = {t*n}')
print('Programa de Tabuada Encerrado')
