from item import Item
from busca import Buscar
from adiciona import Adicionar
from bd import Bd


bd = Bd()

env = Item('marta', 20)

buscar = Buscar()
buscar.buscar('nadia', bd)

adicionar = Adicionar()
adicionar.adicionar(env.nome, env.cj, bd)
