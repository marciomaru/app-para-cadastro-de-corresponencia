from bd import Bd
from busca import Buscar
from item import Item
from tkinter import messagebox
from tkinter import *
from tkinter import scrolledtext
from tkinter.ttk import Combobox
from tela_de_alteracao_de_dados import Tela_de_alteracao_dados
from preenche_combobox import preenche_cbox


class Tela_de_busca_de_itens:

    def __init__(self, root):
        self.jan = Toplevel()
        self.__root = root
        self.__itens_cbox = preenche_cbox()

        self.l_nome = Label(self.jan, text='Nome ')
        self.l_nome.grid(row=0, column=0)

        self.campo = Entry(self.jan, width=75)
        self.campo.grid(row=0, column=1)
        self.campo.focus()

        self.l_cj = Label(self.jan, text='Cj ')
        self.l_cj.grid(row=0, column=2)

        self.cbox = Combobox(self.jan, width=4)
        self.cbox['values'] = self.__itens_cbox
        self.cbox.current(0)
        self.cbox.grid(row=0, column=3)

        self.botao = Button(self.jan, text='Buscar', command=self.__buscar_itens)
        self.botao.grid(row=0, column=4)

        self.texto = scrolledtext.ScrolledText(self.jan, width=60, height=10)
        self.texto.insert(INSERT, 'COD --> NOME --> CJ --> DESCRIÇÃO\n')
        self.texto['state'] = 'disabled'
        self.texto.grid(row=1, column=0, columnspan=3, rowspan=2)

        self.l_explicativo = Label(self.jan,
                                   text='Digite o código do item para '
                                                  'Excluir ou Alterar',
                                   )
        self.l_explicativo.grid(row=4, column=0, columnspan=3, sticky=W)

        self.l_cod = Label(self.jan, text='Cód. ')
        self.l_cod.grid(row=5, column=0, sticky=E)

        self.campo_cod = Entry(self.jan, width=5)
        self.campo_cod.grid(row=5, column=1, sticky=W)

        self.botao_alterar = Button(self.jan, text='Alterar', command=self.__alterar_dados_dos_itens)
        self.botao_alterar.grid(row=6, column=0, padx=5, pady=10)

        self.botao_excluir = Button(self.jan, text='Excluir')
        self.botao_excluir.grid(row=6, column=1, padx=5, pady=10, sticky=W)

        self.jan.geometry('%dx%d+%d+%d' % (800, 300, 300, 200))
        self.jan.transient(root)
        self.jan.focus_force()
        self.jan.grab_set()

    def __buscar_itens(self):
        self.__limpar_resultado_da_busca()
        argumentos = (self.campo.get(), self.__converte_resultado_do_cbox())
        buscar = Buscar(argumentos, Bd())
        resultado = buscar.buscar()
        self.__mostra_resultado(resultado)

    def __alterar_dados_dos_itens(self):
        tela_de_alteracao = Tela_de_alteracao_dados(self.__root, self.campo_cod.get())

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
