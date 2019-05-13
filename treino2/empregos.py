from banco import Banco


class Empregos(object):

    def __init__(self, idemprego=0,  emprego="", empresa=""):
        self.idemprego = idemprego
        self.emprego = emprego
        self.empresa = empresa


    def insertEmpregos(self):
        banco = Banco()

        try:
            if self.verificaEmpregos() == "Verifica sucesso - emprego não cadastrado":
                c = banco.conexao.cursor()

                c.execute("insert into empregos (emprego, empresa) values ('" + self.emprego + "', '" + self.empresa + "')")

                banco.conexao.commit()
                c.close()

                return "Insert sucesso"

            #banco.conexao.commit()
            #c.close()
            return "Insert sucesso - emprego nesta empresa ja cadastrado"
        except:
            return "Insert falha"


    def deleteEmpregos(self):
        banco = Banco()

        try:

            c = banco.conexao.cursor()

            c.execute("delete from empregos where emprego = '" + self.emprego + "' and empresa = '" + self.empresa + "'")

            banco.conexao.commit()
            c.close()

            return "Delete sucesso"
        except:
            return "Delete falha"


    def updateEmpregos(self):
        banco = Banco()

        try:

            c = banco.conexao.cursor()

            c.execute("update empregos set emprego = '" + self.emprego + "', empresa = '" + self.empresa + "' where emprego = '" + self.emprego + "', '" + self.empresa + "'")

            banco.conexao.commit()
            c.close()

            return "Update sucesso"
        except:
            return "Update falha"


    def selectEmpregos(self):
        banco = Banco()

        try:

            c = banco.conexao.cursor()

            c.execute("select * from empregos where emprego = '" + self.emprego + "'")
            for linha in c:
                self.idemprego = linha[0]
                self.emprego = linha[1]
                self.empresa = linha[2]

            c.close()
            if self.idemprego == 0:
                return "Select sucesso - emprego não cadastrado"
            return "Select sucesso"
        except:
            return "Select falha"


    def verificaEmpregos(self):
        banco = Banco()

        try:

            c = banco.conexao.cursor()

            c.execute("select * from empregos where emprego = '" + self.emprego + "' and empresa = '" + self.empresa + "'")
            for linha in c:
                self.idemprego = linha[0]
                self.emprego = linha[1]
                self.empresa = linha[2]

            c.close()
            if self.idemprego == 0:
                return "Verifica sucesso - emprego não cadastrado"
            return "Verifica sucesso"
        except:
            return "Verifica falha"

