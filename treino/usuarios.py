from banco import Banco


class Usuarios(object):

    def __init__(self, idusuario="", nome="", telefone="", email="", usuario="", senha=""):
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

            c.execute("insert into usuarios (idusuario, nome, telefone, email, usuario, senha) values ('" + self.idusuario + "', '" + self.nome + "', '" + self.telefone + "', '" + self.email + "', '" + self.usuario + "', '" + self.senha + "' )")

            banco.conexao.commit()
            c.close()

            return "Usuário cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na inserção do usuário"

    def updateUser(self):

        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("update usuarios set nome = '" + self.nome + "', telefone = '" + self.telefone + "', email = '" + self.email + "', usuario = '" + self.usuario + "', senha = '" + self.senha + "' where idusuario = '" + self.idusuario + "'")

            banco.conexao.commit()
            c.close()

            return "Usuário atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração do usuário"

    def deleteUser(self):

        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("delete from usuarios where idusuario = '" + self.idusuario + "'")

            banco.conexao.commit()
            c.close()

            return "Usuário excluído com sucesso!"
        except:
            return "Ocorreu um erro na exclusão do usuário"

    def selectUser(self, idusuario):
        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("select * from usuarios where idusuario = '" + idusuario + "'")

            for linha in c:
                self.idusuario = linha[0]
                self.nome = linha[1]
                self.telefone = linha[2]
                self.email = linha[3]
                self.usuario = linha[4]
                self.senha = linha[5]

            c.close()

            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca do usuário"


    def autenticaUser(self):
        banco = Banco()
        try:

            c = banco.conexao.cursor()
            print("1")
            c.execute("select * from usuarios where idusuario = '" + self.idusuario + "' and senha = '" + self.senha + "'")
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
                    return "sucesso"

            c.close()
            return "falha"

        except:
            return "falha"