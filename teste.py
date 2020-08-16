from item import Item
from busca import Buscar
from adiciona import Adicionar
from bd import Bd


# bd = Bd()
#
# env = Item('marta', 20)
#
# buscar = Buscar()
# buscar.buscar('nadia', bd)
#
# adicionar = Adicionar()
# adicionar.adicionar(env.nome, env.cj, bd)

from bd import Bd

con = Bd.conexao()
cursor = con.cursor()
aria = 'aria'
joao = 'joão'
n1 = 72
n2 = 73
cursor.execute("insert into item values(?, ?)", (aria, n1))
cursor.execute("insert into item values(?, ?)", (aria, n1))
cursor.execute("insert into item values(?, ?)", (joao, n2))
parte = 'where cj=:cj'
di = {'cj': 72}
for row in cursor.execute(f'select * from item {parte}', di):
    local_da_busca = row[0]
    # if 'a' in local_da_busca:
    print(row)
cursor.close()