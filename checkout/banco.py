import sqlite3


class Banco:

    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.createTableCliente()
        self.createTableProduto()
        self.createTableCarrinho()


    def createTableCliente(self):
        c = self.conexao.cursor()

        c.execute("""create table if not exists usuarios (
                     idusuario integer primary key autoincrement,
                     nome text,
                     telefone text,
                     email text,
                     usuario text,
                     senha text)""")
        self.conexao.commit()
        c.close()


    def createTableProduto(self):
        c = self.conexao.cursor()

        c.execute("""create table if not exists produtos (
                        idproduto integer primary key autoincrement,
                        nome text,
                        preco float,
                        descricao text)""")
        self.conexao.commit()
        c.close()

    def createTableCarrinho(self):
        c = self.conexao.cursor()

        c.execute("""create table if not exists carrinhos (
                        idinsercao integer primary key autoincrement,
                        idusuario integer,
                        idproduto integer)""")
        self.conexao.commit()
        c.close()
