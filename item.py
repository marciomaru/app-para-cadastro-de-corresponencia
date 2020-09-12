class Item:

    def __init__(self, id, nome, cj, descricao):
        self.__id = id
        self.__nome = nome
        self.__cj = cj
        self.__descricao = descricao

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def cj(self):
        return self.__cj

    @cj.setter
    def cj(self, cj):
        self.__cj = cj

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao