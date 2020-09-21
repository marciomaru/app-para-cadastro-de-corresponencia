from tkinter import messagebox


class Alterar_item:
    def __init__(self, args, bd):
        self.__args = args
        self.__conexao = bd.conexao()
        self.__cursor = self.__conexao.cursor()

    def alterar_item(self):
        self.__cursor.execute(
            f'update item set '
            f'nome="{self.__args[0]}", '
            f'cj="{self.__args[1]}", '
            f'descricao="{self.__args[2]}" '
            f'where id="{self.__args[3]}"'
            )
        self.__conexao.commit()
        self.__conexao.close()
        messagebox.showinfo('AVISO DE ALTERAÇÃO DE DADOS',
                            'Alteração realizada com sucesso!')
