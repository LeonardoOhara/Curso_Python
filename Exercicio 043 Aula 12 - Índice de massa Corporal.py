# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e
# mostre seu status, de acordo com a tabela abaixo:

#– IMC abaixo de 18,5: Abaixo do Peso
#– Entre 18,5 e 25: Peso Ideal
#– 25 até 30: Sobrepeso
#– 30 até 40: Obesidade
#– Acima de 40: Obesidade Mórbida

print('Calculadora de indice de massa corporal (IMC)')
peso = float(input('Digite seu peso (KG) :'))
altura = float(input('Digite sua altura'))
imc = peso/(altura ** 2)
print(f'seu IMC é de {imc:.1f}')
if imc < 18.5:
    print('Você está Abaixo do peso ')
elif 18.5 <= imc < 25 :
    print('você está no peso Ideal')
elif 25 <= imc < 30:
    print('você está com sobrepeso')
elif 30 <= imc < 40:
    print('Voce está com obesidade')
else :
    print('Você está com obsidade mórbida')
