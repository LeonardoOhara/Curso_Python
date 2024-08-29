
from ctypes import alignment
import flet as ft
from numpy import save

def main (pagina: ft.Page):
    pagina.title = 'Meu aplicativo'
    pass
    
    # funçoes 
    def login(e):
        if not entrada_nome.value:
            entrada_nome.error_text = 'Por favor preencha seu nome.'
            pagina.update()
        if not entrada_senha.value:
            entrada_senha.error_text = 'Senha obrigatoria'
            pagina.update()
        else:
            nome = entrada_nome.value
            senha = entrada_senha.value
            print(f'Nome: {nome}\n Senha: {senha}')
            pagina.clean() # funcão para limpar a pagina
            pagina.add(ft.Text(f'Olá ,{nome}\nSeja bem vindo a nossa aplicaçao'))
        pass
    # criar os itens que queremos na pagina
    ola = ft.Text(value='Olá mundo', size=30,)
    pagina.controls.append(ola),
    pagina.update()
    
    # adicionar os itens na pagina
    entrada_nome = ft.TextField(label='Digite seu nome')
    entrada_senha = ft.TextField(label='Digite sua Senha')
    pagina.add(
        entrada_nome,
        entrada_senha,
        ft.ElevatedButton('Clique Aqui', on_click=login)
    )
    pass
ft.app(target=main)