from ex115.lib.interface.__init_ import *


def arquivoExiste(nome):
    try:
        a = open(nome , 'rt')
        a.close()
    except:
        return False
    else:
        return True
def criarArquivo (nome):
    try:
        a = open(nome , 'wt+')
        a.close()
    except:
        print('Não foi possivel abrir o arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

def lerArquivo (nome):
    try:
        a = open(nome , 'rt')
    except:
        print('Não foi possivel abrir o arquivo')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
        print(a.read())
    finally:
        a.close()
   
def cadastrar (arq , nome = 'Desconhecido', idade = 0):
    try:
        a = open(arq , 'at')
    except:
        print('Não foi possivel abrir o arquivo')
    else:
        try:
            a.write(f'{nome}; {idade}\n')
        except:
            print('Não foi possivel escrever no arquivo')
        else:
            print (f'Novo registro de {nome} adicionado')
            a.close()
        

