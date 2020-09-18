def preenche_cbox():
    numero_do_cj = 10
    lista_de_cjs = ['']
    while numero_do_cj <= 88:
        for contagem in range(8):
            numero_do_cj += 1
            lista_de_cjs.append(numero_do_cj)
        numero_do_cj += 2
    return lista_de_cjs[:]