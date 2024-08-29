#Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha (jog='<desconhecido>', gol = 0): 
    print (f'O jogador {jog} fez {gol} gol(s) no campeonato')

# Main program
    
n = str(input('Nome do Jogador:'))
g = str(input('Numeros de Gols:'))
if g.isnumeric(): # se g é numero então g é igual a inteiro 
    g = int(g)
else: # se g não é numero então g é igual a zero 
    g = 0
if n.strip() == '': # se n estiver vazio só a quantidade de gols
    ficha(gol = g)
else: # se não passa o n e o g 
    ficha(n, g)
