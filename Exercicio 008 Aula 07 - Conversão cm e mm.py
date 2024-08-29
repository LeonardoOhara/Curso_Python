#Escreve um programa que leia um valor em metros e o exiba
#convertido em centimetros e milimetros.

print('conversor de metros para centrimetro e milimetros')
medida = int(input("digite o valor de metro desejado"))
de = medida/10 #Converter para Decâmeto dividir medida por 10
he = medida/100 #Converter para Hectometro dividir medida por 100
km = medida/1000 #Converter para Kilometros dividir medida por 1000
dc = medida*10 #Converter para Decimetro multiplicar medida por 10
cm = medida*100 # Converter para centimetros multiplicar por 100
mm = medida*1000 # Converter para milimetros multiplicar por 1000
print('o valor de {} convertido dá \n {} decâmeto \n {} hectometro \n {} kilometro'.format(medida, de, he, km))
print('{} decímetro \n {} centimetro \n {} milimetro'.format(dc, cm, mm))
