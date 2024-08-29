#Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# Quantidade de notas 
# A maior nota
# A menor nota
# A média da turma
# a situação (opcional)

def notas (*n, sit=False):
    """
    -> Função notas()
    -> Recebe várias notas de alunos e vai retornar um dicionário com as seguintes informações:
    -> Quantidade de notas
    -> A maior nota"""
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r

# Main program

resp = notas(5.5, 2.5, 9 , 8.5, sit = True)
print(resp)
help(notas)