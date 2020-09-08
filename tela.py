#-*- coding:UTF-8 -*-
from bd import Bd
from busca import Buscar
from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter.ttk import Combobox

root=Tk()

class tela:

        def __init__(self, janela):
            self.teste()
            self.caixa=Frame(janela)
            self.caixa.grid()
            self.b=Button(janela, text='Abrir', command=self.new_jan)
            self.b.grid()
            self.l1=Label(janela, text='raiz!')
            self.l1.grid()

        def new_jan(self):
            self.jan = Toplevel()

            self.campo = Entry(self.jan, width=75)
            self.campo.grid(row=0, column=0)

            self.cbox = Combobox(self.jan)
            self.cbox['values'] = ('', 72, 73, 74)
            self.cbox.current(0)
            self.cbox.grid(row=0, column=1)

            self.botao = Button(self.jan, text='Buscar', command=self.efetuar_busca)
            self.botao.grid(row=0, column=2)

            self.texto = scrolledtext.ScrolledText(self.jan, width=60, height=10)
            self.texto.grid(row=1, column=0, columnspan=3)

            self.jan.geometry('800x200')
            self.jan.transient(root)
            self.jan.focus_force()
            self.jan.grab_set()

        def fecha_jan(self):
            self.jan.destroy()

        def efetuar_busca(self):
            argumentos = (self.campo.get(), 74)
            buscar = Buscar(argumentos, Bd())
            resultado = buscar.buscar()
            self.mostra_resultado(resultado)

        def mostra_resultado(self, resultado):
            if not resultado:
                messagebox.showinfo(
                    'RESULTADO DA BUSCA', 'Não foi encontrado '
                                          'nenhum item'
                    )
            else:
                for item in resultado:
                    self.texto.insert(INSERT, f'{item}\n')

        def teste(self):
            con = Bd.conexao()
            cursor = con.cursor()
            aria = 'aria'
            joao = 'joao'
            n1 = 72
            n2 = 73
            cursor.execute("insert into item values(?, ?)", (aria, n1))
            cursor.execute("insert into item values(?, ?)", (aria, n1))
            cursor.execute("insert into item values(?, ?)", (joao, n2))
            con.commit()
            con.close()


tela(root)

root.geometry('300x200')

root.mainloop()