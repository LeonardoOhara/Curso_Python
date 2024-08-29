from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep


arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu (['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteudo de um arquivo!
        cabeçalho ('Opção 1')
        lerArquivo(arq)

    elif resposta == 2:
        # Opção de cadastrar pessoa
        cabeçalho ('Novo Cadastro')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq,nome,idade)

    elif resposta == 3:
        cabeçalho ('Saindo do Sistema')
        break
    else:
        print ('\033[31m Opção Inválida \033[m')
        sleep(1)