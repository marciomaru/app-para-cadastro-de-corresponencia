from tkinter import messagebox


class Excluir_item:
    def __init__(self, args, bd):
        self.__args = args
        self.__conexao = bd.conexao()
        self.__cursor = self.__conexao.cursor()

    def excluir(self):
        self.__cursor.execute(f'delete from item where id={self.__args}')
        self.__conexao.commit()
        messagebox.showinfo(
            'AVISO DE EXCLUSÃO',
        'O item foi excluido com sucesso!')
        self.__conexao.close()