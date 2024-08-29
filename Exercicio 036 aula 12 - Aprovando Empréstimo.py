#Exercício Python 36:

#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

# qual o valor da casa? coloco o valor da casa
# qual o salario do comprador ?
# quantos anos ele vai pagar ?

casa = float(input('Digite o Valor da Casa R$ :'))
salario = float(input('Digite o seu Salário R$ :'))
ano = int(input('Quantos anos você deseja pagar:'))
prestação = casa/ (ano*12)
porcentagem = salario * 30/100
if prestação <= porcentagem:
    print('Seu emprestimo foi Aprovado pois ficou abaixo dos 30%')
else:
    print('Seu emprestimo foi Negado! pois ficou acima dos 30%')

print(f'O valor da casa foi de R$ {casa:.2f} o seu Salario é de {salario:.2f} você parcelou em {ano} vezes')
print(f'A prestação mensal ficou de R$ {prestação:.2f}')
print(f'30% do salario equivale a R$ {porcentagem:.2f} reais')

