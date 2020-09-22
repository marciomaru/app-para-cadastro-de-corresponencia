#-*- coding:UTF-8 -*-
from bd import Bd
from tkinter import *
from tela_de_cadastro_de_itens import Tela_de_cadastro_de_itens
from tela_de_busca_de_itens import Tela_de_busca_de_itens

root = Tk()

class tela:

        def __init__(self, janela):
            # self.teste() # insere valores para teste no bd
            self.__caixa = Frame(janela)
            self.__caixa.grid()

            self.__b_cadastro = Button(janela, text='Cadastrar itens',
                                     command=self.__abrir_tela_cadastro_de_itens)
            self.__b_cadastro['width'] = 20
            self.__b_cadastro['height'] = 10
            self.__b_cadastro.grid(row=0, column=0)

            self.__b_buscar = Button(janela,
                                     text='Procurar,\n'
                                          ' Alterar e\n'
                                          'Excluir itens',
                                     command=self.__abrir_tela_busca_de_itens)
            self.__b_buscar['width'] = 20
            self.__b_buscar['height'] = 10
            self.__b_buscar.grid(row=0, column=1)

        def __abrir_tela_cadastro_de_itens(self):
            tela_de_cadastro = Tela_de_cadastro_de_itens(root)

        def __abrir_tela_busca_de_itens(self):
            tela_de_busca = Tela_de_busca_de_itens(root)




tela(root)

root.geometry('%dx%d+%d+%d' % (300, 165, 300, 200))
root.title('Controle')

root.mainloop()