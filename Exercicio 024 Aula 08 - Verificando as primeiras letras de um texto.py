# Crie um programa que leia o nome de uma cidade diga
# se ela começa ou não com o nome “SANTO”.

cidade = str(input('digite sua cidade'))
cidade = str(cidade.upper())
cidade = str(cidade.lower())
print('santo'in cidade[:5])

# outr exemplo

cidade = str(input('digite a cidade')).strip()
print(cidade[:5].upper() == 'SANTO')

