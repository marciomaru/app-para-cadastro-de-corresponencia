from bd import Bd
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox


class Tela_de_cadastro_de_itens:

    def __init__(self, root, itens_cbox):

        self.jan = Toplevel()
        self.__root = root
        self.__itens_cbox = itens_cbox

        self.l_nome = Label(self.jan, text='Nome ')
        self.l_nome.grid(row=0, column=0)

        self.campo = Entry(self.jan, width=75)
        self.campo.grid(row=0, column=1)

        self.l_cj = Label(self.jan, text='Cj ')
        self.l_cj.grid(row=0, column=2)

        self.cbox = Combobox(self.jan)
        self.cbox['values'] = self.__itens_cbox
        self.cbox.current(0)
        self.cbox.grid(row=0, column=3)

        self.l_desc = Label(self.jan, text='Descrição ')
        self.l_desc.grid(row=1, column=0)

        self.campo_desc = Entry(self.jan, width=75)
        self.campo_desc.grid(row=1, column=1)

        self.botao_cadastrar = Button(self.jan, text='Cadastrar')
        self.botao_cadastrar.grid(row=2, column=1)

        self.jan.geometry('750x200')
        self.jan.transient(self.__root)
        self.jan.focus_force()
        self.jan.grab_set()


if __name__ == '__main__':
    tela = Tela_de_cadastro_de_itens()