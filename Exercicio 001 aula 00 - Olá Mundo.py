# digite a palavra olá mundo e mostre na tela#


from tkinter import * # o "*" pega todos os codigos do pacote

def hello_world():
    
    texto_helloworld['text'] =('olá mundo ,eu vou conseguir aprender python!')

janela = Tk()
janela.title('HEllo World!') 

texto_orientação = Label(janela, text="Hello World ! ")
texto_orientação.grid(column=6, row=0, padx=10 , pady=10)

botao = Button(janela, text='clique aqui', command=hello_world)
botao.grid(column=6, row=1)

botao = Button(janela, text='clique aqui', command=hello_world)
botao.grid(column=6, row=1)

texto_helloworld = Label(janela, text="")
texto_helloworld.grid(column=6, row=4)

texto_helloworld = Label(janela, text="")
texto_helloworld.grid(column=6, row=4)

janela.mainloop() 