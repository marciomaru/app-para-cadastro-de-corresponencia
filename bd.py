import sqlite3
'''
Classe estática, faz conexão com o banco de dados,
cria a tabela "item" e retorna a conexão para
a manipulação dos dados.
'''

class Bd:

    @staticmethod
    def conexao():
        __conn = sqlite3.connect('dados.bd')
        cursor = __conn.cursor()
        cursor.execute('create table if not exists item (nome, cj)')
        return __conn
