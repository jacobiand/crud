from banco import Banco


class Empregados(object):

    def __init__(self, idemprego=0,  emprego="", empresa=""):
        self.idemprego = idemprego
        self.emprego = emprego
        self.empresa = empresa


    def insertEmpregos(self):
        banco = Banco()

        try:

            c = banco.conexao.cursor()

            c.execute("insert into empregos (emprego, empresa) values ('" + self.emprego + "', '" + self.empresa + "')")

            banco.conexao.commit()
            c.close()

            return "Insert sucesso"
        except:
            return "Insert falha"


    def deleteEmpregos(self):
        banco = Banco()

        try:

            c = banco.conexao.cursor()

            c.execute("delete from empregos where idemprego = '" + self.idemprego + "'")

            banco.conexao.commit()
            c.close()

            return "Delete sucesso"
        except:
            return "Delete falha"


    def updateEmpregos(self):
        banco = Banco()

        try:

            c = banco.conexao.cursor()

            c.execute("update empregos set emprego = '" + self.emprego + "', empresa = '" + self.empresa + "' where idemprego = '" + self.idemprego + "'")

            banco.conexao.commit()
            c.close()

            return "Update sucesso"
        except:
            return "Update falha"


    def selectEmpregos(self):
        banco = Banco()

        try:

            c = banco.conexao.cursor()

            c.execute("select * from empregos where '" + self.idemprego + "'")
            for linha on c:
                self.idemprego = linha[0]
                self.emprego = linha[1]
                self.empresa = linha[2]

            c.close()

            return "Select sucesso"
        except:
            return "Select falha"

