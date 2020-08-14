class Item:

    def __init__(self, nome, cj):
        self.__nome = nome
        self.__cj = cj

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