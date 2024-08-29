#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time do Vasco.


times = ('Palmeiras','Gremio','Atlético-MG','Flamengo','Botafogo','Bragantino',
         'Fluminense','AtleticoPR','Internacional','Fortaleza',
'São Paulo','Cuiaba','Corinthians','Cruzeiro','Vasco','Bahia','Santos',
'Goias','Coritiba','America-MG')

print('='*100)
print(sorted(times))
print('='*100)
print(f'Esses são os 5 primeiros colocados: {times[:5]}')
print('='*100)
print(f'Esses são os 4 ultimos colocados: {times[-4:]}')
print('='*100)
print(f'O Vasco está na {times.index("Vasco")}º posição')
print('='*100)
