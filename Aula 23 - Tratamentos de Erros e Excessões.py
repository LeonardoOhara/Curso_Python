try:
    a = int(input('numerador: '))
    b = int(input('Denominador: '))
    r = a/b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou')
except ZeroDivisionError:
    print('Não é possível dividir por 0')
except KeyboardInterrupt:
    print('Usuário interrompido pelo programa')
except Exception as erro:
    print(f'O problema q deu foi {erro.__cause__}')
else:
    print(f'O resultado é {r:.2f}')
finally:
    print('FIM')