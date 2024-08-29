# Aula 12 Condições em Python

# 'if' --> Se. Ex: Se o carro for pra frente.
#                  'If' carro...
# 'elif' --> senão se. Ex: se não se o carro for pra frente
#                          "elif" o carro....
# 'else' --> senão. Ex: se não ele só segue pra direita.
#                       'else' ele só segue....

#=================================================================================#

# Se você digitar "erika" e "tyson", o código vai executar as condições em ordem e imprimir a primeira condição que seja verdadeira.
# No seu código, a ordem das condições é importante, e a primeira condição que for verdadeira será executada. Portanto:
# Se você digitar "erika", a primeira condição verdadeira será elif nome == 'Erika' or nome == 'Tyson', e o programa imprimirá "Nome ainda mais bonito".
# Se você digitar "tyson", a mesma condição será verdadeira, e o programa imprimirá "Nome ainda mais bonito".
# Portanto, a saída será determinada pela ordem das condições e pela primeira que for verdadeira.
# Se você deseja que ambas as expressões sejam impressas se ambas as condições forem verdadeiras,
# você pode ajustar o código para fazer isso, por exemplo:

nome = input('Digite um nome: ').strip().capitalize()
if nome == 'Leonardo':
    print('Nome Bonito')
elif nome == 'Erika' or nome == 'Tyson':
    print('Nome ainda mais bonito')
    if nome in ['Tyson', 'Erika']:
        print('Amo Você')
else:
    print('Esse nome é comum')

print(f'Seja bem-vindo, {nome}')




