#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria,
# de acordo com a idade:

#– Até 9 anos: MIRIM
#– Até 14 anos: INFANTIL
#– Até 19 anos: JÚNIOR
#– Até 25 anos: SÊNIOR
#– Acima de 25 anos: MASTER

from datetime import date
print('Bem vindo A Confederação Nascional de Natação.')
print(''' CATEGORIAS:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER
''')
nasc = int(input(' Por favor , digite sua data de nascimento: '))
data = date.today().year
res =  data - nasc
if res <= 9:
    print(f'Esse atleta tem {res} anos e deve competir no MIRIM.')
elif res <= 14:
    print(f'Esse atleta tem {res} anos e deve competir no INFANTIL. ')
elif res <=19:
    print(f'Esse atleta tem {res} anos e deve competir no JÚNIOR.')
elif res <=25:
    print(f'Esse atleta tem {res} anos e deve competir no SÊNIOR')
elif res > 25:
    print(f'Esse atleta tem {res} anos e deve competir no MASTER')

