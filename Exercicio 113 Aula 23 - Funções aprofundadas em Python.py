#Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31m Erro! Digite um numero inteiro válido.\033[m')
        except (KeyboardInterrupt):
            print('\033[0;31mUsuário preferiu não digitar esse valor.\033[m')
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31m Erro! Digite um numero inteiro válido.\033[m')
        except (KeyboardInterrupt):
            print('\033[0;31mUsuário preferiu não digitar esse valor.\033[m')
            return 0
        else:
            return n
        
n1 = leiaint('Digite um Inteiro: ')
n2 = leiafloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {n1} e o valor real {n2}')

