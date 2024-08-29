#Exercício Python 39:
# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar
# ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

import datetime
ano = int(input('Digite a Data de Nascimento: '))
ano_atual = datetime.datetime.now().year
idade = ano_atual - ano
print(f'Quem nasceu em {ano} tem {idade} anos agora em {ano_atual}')
if idade > 18 :
    print(f'Você tem {idade} anos e deveria se Alistar em {ano+18} \nVocê deveria ter se alistado há {idade-18} anos atrás!')
elif idade < 18 :
    print(f'Você tem {idade} anos e falta  {(ano+18)-ano_atual} anos para você poder se alistar\nSeu alistamento será em {((ano+18)-ano_atual)+ano_atual}')
elif idade == 18:
    print(f'Você deve se apresentar ao quartel mais proximo de você ! ')

# outro modo

from datetime import date
atual = date.today().year


nasc = int(input('DIGITE O ANO DE NASCIMENTO:'))
idade = atual - nasc

print('quem nasceu em {} tem {} anos em {}'.format(nasc,idade,atual))
if idade == 18:
    print('Você deve se apresentar as Forças Armadas! ')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu Alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print ('Você ja deveria ter se alistado há {} anos '.format(saldo))

