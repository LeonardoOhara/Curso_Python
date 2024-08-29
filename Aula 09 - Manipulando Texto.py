# Aula 09 : Manipulando Texto

# isnumeric = se ele é numérico
# isalpha = se ele é letra
# isalnum = se ele é letra + numérico
# isupper = Se ele é letra maiúscula
# islower = Se ele está minúscula
# isspace = Se ele está com espaço
# sprinter = Se ele é impresso


#exibir a frase com a string frase
frase = 'curso em video python'
print(frase)

#exibir agora com fatiamento

frase = 'curso em video python'
print(frase[0:5])
print(len(frase))
print(frase.count('o'))
print(frase.upper())
print(frase.capitalize())
print('curso'in frase)
print(frase.find('video'))
print(frase.split())
dividido = (frase.split())
print (dividido[2][2])
print(""" Em Python, list é uma estrutura de dados utilizada para armazenar elementos de
 forma sequencial e ordenada. As listas são acessadas por meio de um índice que inicia com 
 o valor 0 para o primeiro elemento e é incrementada com 1 a cada novo item. Além disso, 
 o último item da lista é representado pelo índice “–1”.""")

