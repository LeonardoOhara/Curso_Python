#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite aqui seu salário: '))
aumento = salario + (salario*10/100)
aumento2 = salario + (salario*15/100)
if salario > 1250:
    print(f'Seu salário de R$ {salario:.2f} reais teve um aumento de 10% com o total de R$ {aumento:.2f}')
if salario <= 1250:
    print(f'Seu salário de R$ {salario:.2f} reais teve um aumento de 15% com o total de R$ {aumento2:.2f}')

# outra forma mais simples

salario = float(input('Digite seu Salário aqui R$'))
if salario <= 1250:
    novo = salario + (salario * 15/100)
else:
    novo = salario + (salario * 10/100)

print(f'quem ganhava R$ {salario} reais agora ganha R$ {novo} reais')


