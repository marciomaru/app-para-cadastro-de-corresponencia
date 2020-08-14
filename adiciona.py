class Adicionar:

    def adicionar(self, nome, num, bd):
        item = (nome, num)
        bd.lista.append(item)
        print(bd.lista)
