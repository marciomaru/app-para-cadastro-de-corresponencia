class Cadastrar_item:

    def __init__(self, item, bd=None):
        self.__item = item
        self.__conexao = bd.conexao()
        self.__cursor = self.__conexao.cursor()

    def cadastrar_item_no_bd(self):
        self.__cursor.execute(f'insert into item values (?, ?, ?, ?)',(
            self.__item.id,
            self.__item.nome,
            self.__item.cj,
            self.__item.descricao
        ))
        self.__conexao.commit()
        self.__conexao.close()
