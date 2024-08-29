# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.        

def mensagem(msg):
    tam = len(msg) + 4 # tam é igual a tamanho da mensagem + 4 caracteres para printar o '-' 
    print('-' * tam)
    print(f'  {msg}')
    print('-' * tam)


mensagem('Olá mundo')
mensagem('Curso em Video')
mensagem('Léo')

# exemplo com input

nome = str(input('Digite o nome'))
mensagem(nome)

