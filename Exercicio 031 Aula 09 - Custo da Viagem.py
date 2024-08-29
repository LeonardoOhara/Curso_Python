# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

viagem = float(input('Digite quantos kilometros você pretende percorrer : '))
valor1 = 0.50
valor2 = 0.45
resultado = viagem*0.50
resultado2 = viagem*0.45
print (f'você percorreu {viagem:.0f}KM.')
if viagem<=200:
    print(f'Sua viagem custou R${resultado:.2f} reais.')
if viagem>200:
    print(f'Sua viagem custou R${resultado2:.2f} reais.')

print('Obrigado por viajar conosco! ')

# outra maneira

viagem = float(input('Digite a distancia percorrida:'))
if viagem <= 200:
    preco = viagem*0.50
else:
    preco = viagem*0.45

print(f'Você fez uma Viagem de {viagem:.2f} KM e Custou R${preco:.2f} reais')

# ou desde modo simplificado

viagem = int(input('Digite quantos kilometros você deseja percorrer:'))
preco = viagem*0.50 if viagem <= 200 else viagem * 0.45
print (f'Você percorreu {viagem:.2f}KM e custou {preco:.2f} reais.')