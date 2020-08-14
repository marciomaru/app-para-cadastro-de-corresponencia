class Bd:

    def __init__(self):
        self.__lista = [('nadia', 20), ('nadia', 21), ('morango', 22)]

    @property
    def lista(self):
        return self.__lista


