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

            self.__b_buscar = Button(janela, text='Procurar itens', command=self.__abrir_tela_busca_de_itens)
            self.__b_buscar['width'] = 20
            self.__b_buscar['height'] = 10
            self.__b_buscar.grid(row=0, column=1)

        def __abrir_tela_cadastro_de_itens(self):
            tela_de_cadastro = Tela_de_cadastro_de_itens(root, self.__preenche_cbox())

        def __abrir_tela_busca_de_itens(self):
            tela_de_busca = Tela_de_busca_de_itens(root, self.__preenche_cbox())

        def fecha_jan(self):
            self.jan.destroy()

        def __preenche_cbox(self):
            numero_do_cj = 10
            lista_de_cjs = ['']
            while numero_do_cj <= 88:
                for contagem in range(8):
                    numero_do_cj += 1
                    lista_de_cjs.append(numero_do_cj)
                numero_do_cj += 2
            return lista_de_cjs[:]


tela(root)

root.geometry('300x165')
root.title('Controle')

root.mainloop()