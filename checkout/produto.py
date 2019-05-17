from banco import Banco


class Produto():


    def __init__(self,idproduto=0, nome="", descricao="", preco=0):
        self.idproduto = idproduto
        self.nome = nome
        self.descricao = descricao
        self.preco = preco


    def insertProduto(self, idproduto, nome, preco, descricao):
        banco = Banco()

        self.idproduto = idproduto
        self.nome = nome
        self.descricao = descricao
        self.preco = preco

        try:
            bd = banco.conexao.cursor()

            if self.selectProduto(self.idproduto, self.nome) == "select produto sucesso - produto não cadastrado":
                bd.execute("insert into produtos (nome, preco, descricao) values ('" + self.nome + "', '" + self.preco + "', '" + self.descricao + "')")
                banco.conexao.commit()
                bd.close()
                return "insert produto sucesso"
            banco.conexao.commit()
            bd.close()
            return "insert produto sucesso - produto ja cadastrado"
        except:
            return "insert produto falha"


    def selectProduto(self, idproduto, nome):
        banco = Banco()

        self.idproduto = idproduto
        self.nome = nome

        try:

            bd = banco.conexao.cursor()

            if(self.idproduto != 0):
                bd.execute("select * from produtos where idproduto = '" + self.idproduto + "'")
                for linha in bd:
                    self.idproduto = linha[0]
                    self.nome = linha[1]
                    self.preco = linha[2]
                    self.descricao = linha[3]

                bd.close()
                if self.idproduto == 0:
                    return "select produto sucesso - produto não cadastrado"
                return "select produto sucesso"
            elif (self.nome != ""):
                bd.execute("select * from produtos where nome = '" + self.nome + "'")
                for linha in bd:
                    self.idproduto = linha[0]
                    self.nome = linha[1]
                    self.preco = linha[2]
                    self.descricao = linha[3]

                bd.close()
                if self.idproduto == 0:
                    return "select produto sucesso - produto não cadastrado"
                return "select produto sucesso"
            else:
                bd.close()
                return "select produto sucesso - forneça o id ou nome do produto"
        except:
            return "select produto falha"


    def deleteProduto(self, idproduto, nome):
        banco = Banco()

        self.idproduto = idproduto
        self.nome = nome

        try:

            bd = banco.conexao.cursor()
            if (self.idproduto != 0):
                bd.execute("delete from produtos where idproduto = '" + self.idproduto + "'")
                banco.conexao.commit()
                bd.close()
                return "delete produto sucesso"
            elif (self.nome != ""):
                bd.execute("delete from produtos where nome = '" + self.nome + "'")
                banco.conexao.commit()
                bd.close()
                return "delete produto sucesso"
            else:
                bd.close()
                return "delete produto sucesso - forneça o id ou nome do produto"

        except:
            return "delete produto falha - error"
