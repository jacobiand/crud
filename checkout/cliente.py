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
        self.log = 0

    def insertUser(self):

        banco = Banco()
        try:

            c = banco.conexao.cursor()


            aux = self.selectUser(self.usuario)
            if aux == "Select usuario sucesso - usuario nao existe":
                c.execute("insert into usuarios (nome, telefone, email, usuario, senha) values ('" + self.nome + "', '" + self.telefone + "', '" + self.email + "', '" + self.usuario + "', '" + self.senha + "' )")

            banco.conexao.commit()
            c.close()
            if aux == "Select usuario sucesso - usuario nao existe":
                return "Insert usuario sucesso"
            else:
                return "Insert usuario falha - usuario ja existe"
        except:
            return "Inser usuario falha - error"

    def updateUser(self):

        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("update usuarios set nome = '" + self.nome + "', telefone = '" + self.telefone + "', email = '" + self.email + "', usuario = '" + self.usuario + "', senha = '" + self.senha + "' where usuario = '" + self.usuario + "'")

            banco.conexao.commit()
            c.close()
            return "Update usuario sucesso"
        except:
            return "Update usuario falha - error"

    def deleteUser(self):

        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("delete from usuarios where usuario = '" + self.usuario + "'")

            banco.conexao.commit()
            c.close()

            return "Delete usuario sucesso"
        except:
            return "Delete usuario falha - error"


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

            if self.idusuario == 0:
                return "Select usuario sucesso - usuario nao existe"
            else:
                return "Select usuario sucesso - usuario ja existe"
        except:
            return "Select usuario falha - error"


    def autenticaUser(self, usuario, senha):
        banco = Banco()

        self.usuario = usuario
        self.senha = senha
        try:

            c = banco.conexao.cursor()

            c.execute("select * from usuarios where usuario = '" + self.usuario + "' and senha = '" + self.senha + "'")

            for linha in c:
                self.idusuario = linha[0]
                self.nome = linha[1]
                self.telefone = linha[2]
                self.email = linha[3]
                self.usuario = linha[4]
                self.senha = linha[5]

            c.close()
            if self.idusuario > 0:
                self.log = self.idusuario
                return "Autentica usuario sucesso"

            return "Autentica usuario falha - usuario não encontrado"

        except:
            return "Autentica usuario falha - error"