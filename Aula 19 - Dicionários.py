
locadora = []
filme = { 'titulo' : 'star war','ano' : '1997', 'diretor' : 'George',}
locadora.append(filme)
print (f'O filme {filme["titulo"]} do ano de {filme["ano"]} foi dirigido por {filme["diretor"]}')
print( filme.keys())
print(filme.values())
print(filme.items())
del filme['ano']
filme ['critica'] = '10'
filme ['diretor'] = 'Romero'
print (filme)
print (locadora)
print (locadora[0]['titulo'])
for k, v in filme.items():
    print(f'o {k} é {v}')
print('FIM')


estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')    

