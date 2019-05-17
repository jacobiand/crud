from banco import Banco


class Carrinho():


    def __init__(self,idinsercao=0, idusuario=0, idproduto=0):
        self.idinsercao = idinsercao
        self.idproduto = idproduto
        self.idusuario = idusuario


    def insertCarrinho(self, idusuario, idproduto):
        banco = Banco()


        self.idusuario = idusuario
        self.idproduto = idproduto
        print(self.idusuario, self.idproduto)

        try:
            bd = banco.conexao.cursor()
            aux = self.selectCarrinhoProduto(self.idusuario, self.idproduto)
            if aux == "select carrinhoProduto sucesso - produto ou carrinho não encontrado":
                bd.execute("insert into carrinhos (idusuario, idproduto) values ('" + self.idusuario + "', '" + self.idproduto + "')")
                #bd.execute('insert into carrinhos (idusuario, idproduto) values (?, ?)', (self.idusuario, self.idproduto))
                banco.conexao.commit()
                bd.close()
                return "select carrinhoProduto sucesso - produto cadastrado"
            elif aux == "select carrinhoProduto sucesso - forneça o id do carrinho ou do usuario":
                bd.close()
                return "falta informações"

            bd.close()
            return aux

        except:
            return "insert carrinho falha"


    def selectCarrinho(self, idusuario):
        banco = Banco()

        #self.idusuario = idusuario

        try:

            bd = banco.conexao.cursor()

            if (self.idusuario != 0):
                bd.execute("select * from carrinhos where idusuario = '" + idusuario + "'")
                for linha in bd:
                    self.idinsercao = linha[0]
                    self.idusuario = linha[1]
                    self.idproduto = linha[2]

                bd.close()
                if self.idusuario == 0:
                    return "select carrinho sucesso - carrinho não cadastrado"
                return "select carrinho sucesso"
            else:
                bd.close()
                return "select carrinho sucesso - forneça o id do carrinho ou do usuario"
        except:
            return "select carrinho falha"


    def selectCarrinhoProduto(self, idusuario, idproduto):
        banco = Banco()
        self.idusuario = idusuario
        self.idproduto = idproduto

        try:

            bd = banco.conexao.cursor()

            if (self.idusuario != 0):
                bd.execute("select * from carrinhos where idusuario = '" + self.idusuario + "' and idproduto = '" + self.idproduto + "'")
                for linha in bd:
                    self.idinsercao = linha[0]
                    self.idusuario = linha[1]
                    self.idproduto = linha[2]

                bd.close()
                if self.idinsercao == 0:
                    return "select carrinhoProduto sucesso - produto ou carrinho não encontrado"
                return "select carrinhoProduto sucesso - produto encontrado"
            else:
                bd.close()
                return "select carrinhoProduto sucesso - forneça o id do carrinho ou do usuario"
        except:
            return "select carrinhoProduto falha"


    def deleteCarrinho(self, idusuario):
        banco = Banco()

        self.idusuario = idusuario

        try:

            bd = banco.conexao.cursor()

            if (self.idusuario != 0):
                bd.execute("delete from carrinhos where idusuario = '" + self.idusuario + "'")
                banco.conexao.commit()
                bd.close()
                return "delete carrinho sucesso"
            else:
                bd.close()
                return "delete carrinho sucesso - forneça o id ou nome do produto"
        except:
            return "delete carrinho falha - error"


    def deleteCarrinhoProduto(self, idusuario, idproduto):
        banco = Banco()

        self.idusuario = idusuario
        self.idproduto = idproduto

        try:

            bd = banco.conexao.cursor()

            if (self.idusuario != 0):
                bd.execute("delete from carrinhos where idusuario = '" + self.idusuario + "' and '" + self.idproduto + "'")
                banco.conexao.commit()
                bd.close()
                return "delete carrinhoProduto sucesso"
            else:
                bd.close()
                return "delete carrinhoProduto sucesso - forneça o id ou nome do produto"
        except:
            return "delete carrinhoProduto falha - error"


