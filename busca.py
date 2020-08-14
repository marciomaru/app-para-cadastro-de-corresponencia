class Buscar:

    def buscar(self, nome, bd):
        contador = 0
        for item in bd.lista:
            if nome in item[0]:
                contador += 1
        if contador == 0:
            print('Nada encontrado')
        else:
            print(f'Encontrado {contador} ')