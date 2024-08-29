# Desenvolva um programa que leia as notas de um aluno,calcule e mostre a sua média.

print('Alunos Hoje será o dia da Media das Notas de vocês !')
print('Por favor Professor insira a nota dos seus alunos')
n1 = int(input('Matemática'))
n2 = int(input('Português'))
n3 = int(input('Fisica'))
n4 = int(input('Geografia'))
n5 = int(input('Historia'))
n6 = int(input('Ciências'))
n7 = int(input('Educação Fisica'))
media = (n1+n2+n3+n4+n5+n6+n7)/7
print(f'Matemática {n1}\nPortuguês {n2}\nFisica {n3}\nGeografia {n4}\nHistória {n5}\nCiências {n6}\nEducação Fisica {n7}')
print(f'A média do aluno foi {media:.2f}')
