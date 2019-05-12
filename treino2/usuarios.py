from banco import Banco


class Usuarios(object):

    def __init__(self, idusuario=0, nome="", telefone="", email="", usuario="", senha=""):
        self.info = {}
        self.idusuario = idusuario
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.usuario = usuario
        self.senha = senha

    def insertUser(self):

        banco = Banco()
        try:

            c = banco.conexao.cursor()


            aux = self.selectUser(self.usuario)
            if aux == "Select sucesso - usuario nao existe":
                c.execute("insert into usuarios (nome, telefone, email, usuario, senha) values ('" + self.nome + "', '" + self.telefone + "', '" + self.email + "', '" + self.usuario + "', '" + self.senha + "' )")

            banco.conexao.commit()
            c.close()
            if aux == "Select sucesso - usuario nao existe":
                return "Insert sucesso"
            else:
                return "Insert falha - usuario ja existe"
        except:
            return "Inser falha - error"

    def updateUser(self):

        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("update usuarios set nome = '" + self.nome + "', telefone = '" + self.telefone + "', email = '" + self.email + "', usuario = '" + self.usuario + "', senha = '" + self.senha + "' where idusuario = '" + self.idusuario + "'")

            banco.conexao.commit()
            c.close()

            return "Update sucesso"
        except:
            return "Update falha - error"

    def deleteUser(self):

        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("delete from usuarios where usuario = '" + self.usuario + "'")

            banco.conexao.commit()
            c.close()

            return "Delete sucesso"
        except:
            return "Delete falha - error"

    def selectUser(self, usuario):
        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("select * from usuarios where usuario = '" + usuario + "'")
            for linha in c:
                self.idusuario = linha[0]
                self.nome = linha[1]
                self.telefone = linha[2]
                self.email = linha[3]
                self.usuario = linha[4]
                self.senha = linha[5]

            c.close()
            print(self.idusuario)
            if self.idusuario == 0:
                return "Select sucesso - usuario nao existe"
            else:
                return "Select sucesso - usuario ja existe"
        except:
            return "Select falha - error"


    def autenticaUser(self):
        banco = Banco()
        try:

            c = banco.conexao.cursor()
            print("1")
            c.execute("select * from usuarios where usuario = '" + self.usuario + "' and senha = '" + self.senha + "'")
            print("2")
            for linha in c:
                aux0 = linha[0]
                aux1 = linha[1]
                aux2 = linha[2]
                aux3 = linha[3]
                aux4 = linha[4]
                aux5 = linha[5]
                if ((self.idusuario == aux0) and (self.senha == aux5)):
                    c.close()
                    return "Autentica sucesso"

            c.close()
            return "Autentica falha - usuario não encontrado"

        except:
            return "Autentica falha - error"