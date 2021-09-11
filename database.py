import sqlite3
from typing import ContextManager
import sqlite3
from sqlite3.dbapi2 import SQLITE_CREATE_TABLE


class Note:
    def __init__(self, id=None, title=None, content=''):
        self.id = id
        self.title = title
        self.content = content

class Database():
    def __init__(self, banco):
        self.banco = banco
        self.conn = sqlite3.connect(self.banco+".db")
        cur = self.conn.cursor()
        sql = "CREATE TABLE IF NOT EXISTS note(id INTEGER PRIMARY KEY, title STRING, content STRING NOT NULL)"
        cur.execute(sql)

    def add(self, note):
        self.note = note
        tasks = ((note.id), (note.title), (note.content))
        sql = "INSERT INTO note (id, title, content) VALUES (?,?,?)"
        cur = self.conn.cursor()
        cur.execute(sql, tasks)
        self.conn.commit()

# Ele não recebe nenhum argumento e devolve uma lista de Note, com os valores obtidos do banco de dados.
    def get_all(self):
        sql = "SELECT id, title, content FROM note"
        cursor = self.conn.execute(sql)
        # conn.commit()

        lista = []
        for linha in cursor:
            id = linha[0]
            title = linha[1]
            content = linha[2]
            lista.append(Note(id=id, title = title, content=content))

        return lista

# Implemente o método update(self, entry), que recebe um valor do tipo Note (com todos os atributos, inclusive o id, preenchidos) e atualiza essa entrada no banco de dados.
# Novamente você terá que usar o método execute. Não se esqueça de chamar o método commit, assim como na inserção de dados.
# O teste test_update_row verifica se a sua implementação está correta.

# UPDATE NOME_DA_TABELA SET NOME_DA_COLUNA = NOVO_VALOR_DA_COLUNA WHERE CONDICAO
# UPDATE dados_pessoais SET cpf = '555.555.555-55' WHERE identificador = 2

    def update(self,entry):
        self.entry = entry
        sql = (f"UPDATE note SET title='{entry.title}', content='{entry.content}' WHERE id={entry.id}")

        self.conn.execute(sql)

        self.conn.commit()

# DELETE FROM NOME_DA_TABELA WHERE CONDICAO;
# DELETE FROM dados_pessoais WHERE identificador = 5

    def delete(self, note_id):
        sql = (f"DELETE FROM note WHERE id={note_id}")
        self.conn.execute(sql)
        self.conn.commit()
