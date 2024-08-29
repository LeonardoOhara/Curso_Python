# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

carro = float(input('Quantos KM você percorreu com o veiculo?'))
dias = float(input('Quantos dias você alugou o carro?'))
aluguel = dias*60 + carro*0.15
media = (dias*60 + carro*0.15)/dias
media2 = (dias*60 + carro*0.15)/carro
print(f'O veiculo percorreu {carro:.2f} km, custou um total de: R$ {aluguel:.2f}')
print(f'A média de gastos por dia é {media}')
print(f'A média de gastos por km rodado é {media2}')


