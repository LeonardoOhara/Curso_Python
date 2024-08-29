# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
# mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

carro = int(input('Digite sua velocidade'))
print (f'A velocidade do carro é de {carro} Km/h')
#condição carro
if carro>80:
    print('Você está acima da velocidade permitida que é de 80km/h! ')
else :
    print('Você está na velocidade da via')

#condição multa
multa = (carro-80)*7
if carro>80:
    print(f'Você passou a {carro} km/h e foi multado no valor de R$ {multa} reais')
else:
    print('Siga viagem! ')
