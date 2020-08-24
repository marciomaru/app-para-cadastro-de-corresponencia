from bd import Bd


class Buscar:

    def __init__(self, args=None, bd=None):
        self.__args = args
        self.__conexao = bd.conexao()
        self.__cursor = self.__conexao.cursor()

    def buscar(self):
        if self.__args is None:
            self.buscar_tudo()
        elif isinstance(self.__args[0], str) and isinstance(self.__args[1], int):
            self.buscar_nome_e_conjunto()
        else:
            self.buscar_por_nome()

    def buscar_por_nome(self):
        # vai buscar por nome em todos os conjuntos.
        try:
            nome = self.__args[0]
            for row in self.__cursor.execute('select * from item'):
                local_da_busca = row[0]
                if nome in local_da_busca:
                    print(row)
            self.__conexao.close()
        except:
            self.buscar_por_conjunto()

    def buscar_por_conjunto(self):
        # buscar todos os nomes em um conjunto.
        for row in self.__cursor.execute('select * from item where cj=:cj', {'cj': self.__args[1]}):
            print(row)

    def buscar_nome_e_conjunto(self):
        # buscar um nome em um conjunto.
        dados = {'nome': self.__args[0], 'cj': self.__args[1]}
        for row in self.__cursor.execute('select * from item where cj=:cj ', dados):
            local_da_busca = row[0]
            if dados['nome'] in local_da_busca:
                print(row)

    def buscar_tudo(self):
        # vai buscar tudo, qualquer nome em qualquer conjunto.
        for row in self.__cursor.execute('select * from item'):
            print(row)


if __name__ == '__main__':
    b = Buscar(('a', 72))
    b.buscar()
