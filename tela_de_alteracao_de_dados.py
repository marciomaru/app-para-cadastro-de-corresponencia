from bd import Bd
from item import Item
from cadastrar_item import Cadastrar_item
from tkinter import messagebox
from tkinter import *
from tkinter.ttk import Combobox
from preenche_combobox import preenche_cbox
from tratamento_de_dados import verificar_campos_preenchidos
from alterar_item import Alterar_item


class Tela_de_alteracao_dados:

    def __init__(self, root, item):

        self.__jan = Toplevel()
        self.__root = root
        self.__conexao = Bd().conexao()
        self.__cursor = self.__conexao.cursor()
        self.__itens_cbox = preenche_cbox()
        self.__item = item
        self.teste = '1'

        self.__l_nome = Label(self.__jan, text='Nome ')
        self.__l_nome.grid(row=0, column=0)

        self.__campo = Entry(self.__jan, width=75)
        self.__campo.insert(INSERT, self.__item.nome)
        self.__campo.grid(row=0, column=1)

        self.__l_cj = Label(self.__jan, text='Cj ')
        self.__l_cj.grid(row=0, column=2)

        self.__cbox = Combobox(self.__jan)
        self.__cbox['values'] = self.__itens_cbox
        self.__cbox.insert(INSERT, self.__item.cj)
        self.__cbox.grid(row=0, column=3)

        self.__l_desc = Label(self.__jan, text='Descrição ')
        self.__l_desc.grid(row=1, column=0)

        self.__campo_desc = Entry(self.__jan, width=75)
        self.__campo_desc.insert(INSERT, self.__item.descricao)
        self.__campo_desc.grid(row=1, column=1)

        self.__botao_cadastrar = Button(self.__jan, text='Alterar', command=self.__alterar_dados)
        self.__botao_cadastrar.grid(row=2, column=0, columnspan=3, pady=10)

        self.__botao_limpar = Button(self.__jan, text='Fechar', command=self.__cancelar_alteracao)
        self.__botao_limpar.grid(row=2, column=1, columnspan=3, pady=10)

        self.__jan.geometry('%dx%d+%d+%d' % (750, 200, 300, 200))
        self.__jan.transient(self.__root)
        self.__jan.focus_force()
        self.__jan.grab_set()







    def __alterar_dados(self):
        if verificar_campos_preenchidos(
                self.__campo.get(),
                self.__campo_desc.get(),
                self.__cbox.get(),
                self.__itens_cbox
        ):
            dados_para_alteracao = (
                self.__campo.get(),
                self.__cbox.get(),
                self.__campo_desc.get(),
                self.__item.id
            )
            obj_para_alterar_item = Alterar_item(dados_para_alteracao, Bd())
            obj_para_alterar_item.alterar_item()
            self.__jan.destroy()


    def __cancelar_alteracao(self):
        self.__jan.destroy()
