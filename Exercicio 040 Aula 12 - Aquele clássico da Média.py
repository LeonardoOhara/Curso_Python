#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#– Média abaixo de 5.0: REPROVADO
#– Média entre 5.0 e 6.9: RECUPERAÇÃO
#– Média 7.0 ou superior: APROVADO

m1 = float(input('Digite a primeira nota'))
m2 = float(input('Digite a segunda nota'))
md = (m1+m2)/2
print(f'Sua primeira nota foi {m1} e a segunda nota foi {m2} e sua média é {md:.1f}')
if md < 5:
    print('Você foi Reprovado')
elif 6.9 > md >= 5:
    print('Você está de Recuperação')
elif md >= 7:
    print(f'Você foi aprovado parabéns ! ')

