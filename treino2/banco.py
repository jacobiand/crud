import sqlite3


class Banco:

    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.createTableUsuarios()
        self.createTableEmpregos()
        self.createTableEmpregados()

    def createTableUsuarios(self):
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


    def createTableEmpregos(self):
        c = self.conexao.cursor()

        c.execute("""create table if not exists empregos (
                        idemprego integer primary key autoincrement,
                        emprego text,
                        empresa text)""")

    def createTableEmpregados(self):
        c = self.conexao.cursor()

        c.execute("""create table if not exists empregados (
                        idrelacao integer primary key autoincrement,
                        idempregado text,
                        idemprego text)""")