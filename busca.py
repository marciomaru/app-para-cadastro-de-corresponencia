class Buscar:

    def __init__(self, args=None, bd=None):
        self.__args = args
        self.__conexao = bd.conexao()
        self.__cursor = self.__conexao.cursor()
        self.__resultado_da_busca = []

    def buscar(self):
        return self.__buscar_nome_e_conjunto()

    def __buscar_nome_e_conjunto(self):
        # buscar um nome em um conjunto.
        if (isinstance(self.__args[0], str) and self.__args[0] != '') and isinstance(self.__args[1], int):
            dados = {'nome': self.__args[0], 'cj': self.__args[1]}
            for row in self.__cursor.execute('select * from item where cj=:cj ', dados):
                local_da_busca = row[1]
                if dados['nome'] in local_da_busca:
                    self.__resultado_da_busca.append(f'{row[0]} --> {row[1]} --> {row[2]} --> {row[3]}')
            self.__conexao.close()
            return self.__resultado_da_busca
        else:
            return self.__buscar_por_nome()

    def __buscar_por_nome(self):
        # vai buscar por nome em todos os conjuntos.
        if (self.__args[0] != '') and self.__args[1] == '':
            nome = self.__args[0]
            for row in self.__cursor.execute('select * from item'):
                local_da_busca = row[1]
                if nome in local_da_busca:
                    self.__resultado_da_busca.append(f'{row[0]} --> {row[1]} --> {row[2]} --> {row[3]}')
            self.__conexao.close()
            return self.__resultado_da_busca
        else:
            return self.__buscar_por_conjunto()

    def __buscar_por_conjunto(self):
        # buscar todos os nomes em um conjunto.
        if self.__args[1] != '':
            for row in self.__cursor.execute('select * from item where cj=:cj', {'cj': self.__args[1]}):
                self.__resultado_da_busca.append(f'{row[0]} --> {row[1]} --> {row[2]} --> {row[3]}')
            self.__conexao.close()
            return self.__resultado_da_busca
        else:
            return self.__buscar_tudo()

    def __buscar_tudo(self):
        # vai buscar tudo, qualquer nome em qualquer conjunto.
        for row in self.__cursor.execute('select * from item'):
            self.__resultado_da_busca.append(f'{row[0]} --> {row[1]} --> {row[2]} --> {row[3]}')
        return self.__resultado_da_busca


if __name__ == '__main__':
    b = Buscar(('joão'))
    b.buscar()
