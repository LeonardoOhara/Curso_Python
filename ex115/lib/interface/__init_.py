def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print()
        except (KeyboardInterrupt):
            print('\033[0;31mUsuário preferiu não digitar esse valor.\033[m')
            return 0
        else:
            return n

def linha(tam=42):
    return '-' * tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu (lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m {item}\033[m')
        c += 1
    print(linha())
    opc = leiaint('\033[32m Sua opção: \033[m')
    return opc