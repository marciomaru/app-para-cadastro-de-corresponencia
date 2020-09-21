from tkinter import messagebox, END, INSERT

def converte_resultado_do_cbox(cbox):
    resultado_cbox = cbox
    try:
        resultado_convertido = int(resultado_cbox)
        return resultado_convertido
    except:
        return resultado_cbox

def verificar_campos_preenchidos(campo, campo_desc, cbox, itens_cbox):
    print(f'valor no cbox: {type(cbox)}, {cbox}')
    if campo != '' and (campo_desc != ''):
        return __verificar_valor_no_cbox(cbox, itens_cbox)
    else:
        messagebox.showinfo(
            'ERRO AO CADASTRAR ITEM',
            'Preencha os campos "Nome" e "Descrição"'
        )

def __verificar_valor_no_cbox(cbox, itens_cbox):
    try:
        valor_cbox = int(cbox)
        print(f'valor do valor_box: {valor_cbox}, {type(valor_cbox)}')
        if valor_cbox in itens_cbox:
            return True
        else:
            print('aqui')
            messagebox.showinfo(
                'ERRO AO CADASTRAR ITEM',
                'Valor no campo "cj" está incorreto'
            )
            return False
    except:
        print('ou aqui')
        messagebox.showinfo(
            'ERRO AO CADASTRAR ITEM',
            'Valor no campo "cj" está incorreto'
        )
        return False

def limpar_resultado_da_busca(texto, campo):
    texto['state'] = 'normal'
    texto.delete(1.0, END)
    texto.insert(INSERT, 'COD --> NOME --> CJ --> DESCRIÇÃO\n')
    texto['state'] = 'disabled'
    campo.focus()