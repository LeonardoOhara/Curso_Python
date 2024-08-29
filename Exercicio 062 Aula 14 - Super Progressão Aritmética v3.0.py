#xercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

print('=' * 36)
print('10 TERMOS DA PROGRESSÃO ARITIMETICA')
print('=' * 36)
primeiro = int(input(f'Primeiro Termo '))
razao = int(input(f'Razão '))
termo = primeiro
cont = 1
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} - ', end='')
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais ?'))
print(f'Progressão finalizada com {total} termos mostrados')
