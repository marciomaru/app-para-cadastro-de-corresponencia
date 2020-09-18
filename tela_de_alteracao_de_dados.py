from bd import Bd
from item import Item
from cadastrar_item import Cadastrar_item
from tkinter import messagebox
from tkinter import *
from tkinter.ttk import Combobox
from preenche_combobox import preenche_cbox


class Tela_de_alteracao_dados:

    def __init__(self, root, codigo):

        self.__jan = Toplevel()
        self.__root = root
        self.__codigo = codigo
        self.__conexao = Bd().conexao()
        self.__cursor = self.__conexao.cursor()
        self.__itens_cbox = preenche_cbox()
        self.__buscar_item_para_alteracao()

        self.__l_nome = Label(self.__jan, text='Nome ')
        self.__l_nome.grid(row=0, column=0)

        self.__campo = Entry(self.__jan, width=75)
        self.__campo.grid(row=0, column=1)

        self.__l_cj = Label(self.__jan, text='Cj ')
        self.__l_cj.grid(row=0, column=2)

        self.__cbox = Combobox(self.__jan)
        self.__cbox['values'] = self.__itens_cbox
        self.__cbox.current(0)
        self.__cbox.grid(row=0, column=3)

        self.__l_desc = Label(self.__jan, text='Descrição ')
        self.__l_desc.grid(row=1, column=0)

        self.__campo_desc = Entry(self.__jan, width=75)
        self.__campo_desc.grid(row=1, column=1)
        self.__campo.focus()

        self.__botao_cadastrar = Button(self.__jan, text='Alterar', command=self.__alterar_dados)
        self.__botao_cadastrar.grid(row=2, column=0, columnspan=3, pady=10)

        self.__botao_limpar = Button(self.__jan, text='Cancelar', command=self.__cancelar_alteracao)
        self.__botao_limpar.grid(row=2, column=1, columnspan=3, pady=10)

        self.__jan.geometry('%dx%d+%d+%d' % (750, 200, 300, 200))
        self.__jan.transient(self.__root)
        self.__jan.focus_force()
        self.__jan.grab_set()

    def __verificar_campos_preenchidos(self):
        if self.__campo.get() != '' and (self.__campo_desc.get() != ''):
            return self.__verificar_valor_no_cbox()
        else:
            messagebox.showinfo(
                'ERRO AO CADASTRAR ITEM',
                'Preencha os campos "Nome" e "Descrição"'
            )

    def __verificar_valor_no_cbox(self):
        try:
            valor_cbox = int(self.__cbox.get())
            if valor_cbox in self.__itens_cbox:
                return True
            else:
                messagebox.showinfo(
                    'ERRO AO CADASTRAR ITEM',
                    'Valor no campo "cj" está incorreto'
                )
                return False
        except:
            messagebox.showinfo(
                'ERRO AO CADASTRAR ITEM',
                'Valor no campo "cj" está incorreto'
            )
            return False

    def __buscar_item_para_alteracao(self):
        dados_do_item = self.__cursor.execute('select * from item where id=:cod', {'cod': self.__codigo})

    def __alterar_dados(self):
        if self.__verificar_campos_preenchidos():
            item = Item(None, self.__campo.get(), self.__cbox.get(), self.__campo_desc.get())
            obj_para_cadastar_item = Cadastrar_item(item, Bd())
            obj_para_cadastar_item.cadastrar_item_no_bd()
            self.__limpar_campos()

    def __cancelar_alteracao(self):
        self.__jan.destroy()