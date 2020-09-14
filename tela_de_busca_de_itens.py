from bd import Bd
from busca import Buscar
from item import Item
from tkinter import messagebox
from tkinter import *
from tkinter import scrolledtext
from tkinter.ttk import Combobox


class Tela_de_busca_de_itens:

    def __init__(self, root, itens_cbox):
        self.jan = Toplevel()
        self.__root = root
        self.__itens_cbox = itens_cbox

        self.l_nome = Label(self.jan, text='Nome ')
        self.l_nome.grid(row=0, column=0)

        self.campo = Entry(self.jan, width=75)
        self.campo.grid(row=0, column=1)
        self.campo.focus()

        self.l_cj = Label(self.jan, text='Cj ')
        self.l_cj.grid(row=0, column=2)

        self.cbox = Combobox(self.jan)
        self.cbox['values'] = self.__itens_cbox
        self.cbox.current(0)
        self.cbox.grid(row=0, column=3)

        self.botao = Button(self.jan, text='Buscar', command=self.__buscar_itens)
        self.botao.grid(row=0, column=4)

        self.texto = scrolledtext.ScrolledText(self.jan, width=60, height=10)
        self.texto.insert(INSERT, 'COD --> NOME --> CJ --> DESCRIÇÃO\n')
        self.texto['state'] = 'disabled'
        self.texto.grid(row=1, column=0, columnspan=3)

        self.jan.geometry('%dx%d+%d+%d' % (800, 200, 300, 200))
        self.jan.transient(root)
        self.jan.focus_force()
        self.jan.grab_set()

    def __buscar_itens(self):
        self.__limpar_resultado_da_busca()
        argumentos = (self.campo.get(), self.__converte_resultado_do_cbox())
        buscar = Buscar(argumentos, Bd())
        resultado = buscar.buscar()
        self.__mostra_resultado(resultado)

    def __converte_resultado_do_cbox(self):
        resultado_cbox = self.cbox.get()
        try:
            resultado_convertido = int(resultado_cbox)
            return resultado_convertido
        except:
            return resultado_cbox

    def __mostra_resultado(self, resultado):
        if not resultado:
            messagebox.showinfo(
                'RESULTADO DA BUSCA', 'Não foi encontrado '
                                      'nenhum item'
            )
        else:
            for item in resultado:
                self.texto['state'] = 'normal'
                self.texto.insert(INSERT, f'{item}\n')
                self.texto['state'] = 'disabled'

    def __limpar_resultado_da_busca(self):
        self.texto['state'] = 'normal'
        self.texto.delete(1.0, END)
        self.texto.insert(INSERT, 'COD --> NOME --> CJ --> DESCRIÇÃO\n')
        self.texto['state'] = 'disabled'
        self.campo.focus()
