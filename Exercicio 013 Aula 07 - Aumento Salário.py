#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
nome = str(input('Digite seu nome:'))
print(f'Seja bem vindo {nome}')
numero = float(input('Digite o salario do Funcionario R$'))
salario = numero + (numero*15/100)
print(f'O reajuste do seu salario foi de 15%.\nSalário atual R${numero:.2f}\nSalário reajustado R${salario:.2f}')
print(f'Você recebeu {(numero*15/100):.2f} reais a mais')
