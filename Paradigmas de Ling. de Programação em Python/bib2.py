import tkinter


def funcClicar():
    print("Botão pressionado")


janelaPrincipal = tkinter.Tk()
botao = tkinter.Button(master=janelaPrincipal,
                       text='Clique', command=funcClicar)
botao.pack()
texto = tkinter.Label(master=janelaPrincipal, text="Minha janela exibida")
texto.place(x=50, y=50)

janelaPrincipal.mainloop()
