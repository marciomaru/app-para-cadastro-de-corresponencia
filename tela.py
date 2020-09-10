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

            self.b_cadastro = Button(janela, text='Cadastrar itens')
            self.b_cadastro['width'] = 20
            self.b_cadastro['height'] = 10
            self.b_cadastro.grid(row=0, column=0)

            self.b_buscar = Button(janela, text='Procurar itens', command=self.__tela_de_busca)
            self.b_buscar['width'] = 20
            self.b_buscar['height'] = 10
            self.b_buscar.grid(row=0, column=1)


        def __tela_de_busca(self):
            self.jan = Toplevel()

            self.l_nome = Label(self.jan, text='Nome ')
            self.l_nome.grid(row=0, column=0)

            self.campo = Entry(self.jan, width=75)
            self.campo.grid(row=0, column=1)

            self.l_cj = Label(self.jan, text='Cj ')
            self.l_cj.grid(row=0, column=2)

            self.cbox = Combobox(self.jan)
            self.cbox['values'] = self.__preenche_cbox()
            self.cbox.current(0)
            self.cbox.grid(row=0, column=3)

            self.botao = Button(self.jan, text='Buscar', command=self.__efetuar_busca)
            self.botao.grid(row=0, column=4)

            self.texto = scrolledtext.ScrolledText(self.jan, width=60, height=10)
            self.texto['state'] = 'disabled'
            self.texto.grid(row=1, column=0, columnspan=3)

            self.jan.geometry('800x200')
            self.jan.transient(root)
            self.jan.focus_force()
            self.jan.grab_set()

        def fecha_jan(self):
            self.jan.destroy()

        def __efetuar_busca(self):
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

        def __preenche_cbox(self):
            numero_do_cj = 10
            lista_de_cjs = ['']
            while numero_do_cj <= 88:
                for contagem in range(8):
                    numero_do_cj += 1
                    lista_de_cjs.append(numero_do_cj)
                numero_do_cj += 2
            return lista_de_cjs[:]

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

root.geometry('300x165')

root.mainloop()