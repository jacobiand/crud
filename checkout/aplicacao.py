from tkinter import *
from carrinho import Carrinho
from produto import Produto
from cliente import Usuarios


class Application:
    def __init__(self, master=None):
        #self.user = Usuarios()
        #self.produto = Produto()
        #self.carrinho = Carrinho()
        self.bigContainer1 = Frame(master)
        self.bigContainer1.pack(side=LEFT)
        self.bigContainer2 = Frame(master)
        self.bigContainer2.pack(side=RIGHT)
        self.bigContainer3 = Frame(master)
        self.bigContainer3.pack(side=LEFT)

        self.fonte = ("Verdana", "10")

        #cadastro de usuario
        self.inicializaBigContainer1()

        #cadastro de produtos
        self.inicializaBigContainer2()

        #inserção de produtos no carrinho
        self.inicializaBigContainer3()



    #verificar senha
    def verificaSenha(self):
        self.lblmsg["text"] = ""
        user = Usuarios()


        #self.user.usuario = self.txtusuario.get()
        user.usuario = self.txtusuario.get()
        #self.user.senha = self.txtsenha.get()
        user.senha = self.txtsenha.get()

        mensage = user.autenticaUser(user.usuario, user.senha)
        if (mensage == "Autentica usuario sucesso"):
            self.lblmsg["text"] = "Usuário autenticado com sucesso"

            self.lblnome.pack(side=LEFT)

            self.txtnome.pack(side=LEFT)

            self.lbltelefone.pack(side=LEFT)

            self.txttelefone.pack(side=LEFT)

            self.lblemail.pack(side=LEFT)

            self.txtemail.pack(side=LEFT)

            self.btnAlterar.pack(side=LEFT)

            self.btnDeletar.pack(side=LEFT)

            self.btnInsert.pack_forget()

            self.buscarUsuario()
        elif (mensage == "Autentica usuario falha - usuario não encontrado"):
            self.lblmsg["text"] = "Usuário não está cadastrado"
        else:
            self.lblmsg["text"] = "Falha na autenticação"



    #cadastra um novo usuario
    def inserirUsuario(self):
        self.lblmsg["text"] = ""
        user = Usuarios()

        #self.user.email = self.txtemail.get()
        #self.user.telefone = self.txttelefone.get()
        #self.user.nome = self.txtnome.get()
        #self.user.usuario = self.txtusuario.get()
        #self.user.senha = self.txtsenha.get()
        user.email = self.txtemail.get()
        user.telefone = self.txttelefone.get()
        user.nome = self.txtnome.get()
        user.usuario = self.txtusuario.get()
        user.senha = self.txtsenha.get()

        #mensage = self.user.insertUser()
        mensage = user.insertUser()
        if mensage == "Insert usuario sucesso":
            self.lblmsg["text"] = "Usuário cadastrado com sucesso"
        elif mensage == "Insert usuario falha - usuario ja existe":
            self.lblmsg["text"] = "Usuário já esta cadastrado"
        else:
            self.lblmsg["text"] = "Falha ao tentar cadastrar"

        self.hideCadastrar()
        self.txtnome.delete(0, END)
        self.txttelefone.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtusuario.delete(0, END)
        self.txtsenha.delete(0, END)


    #busca um usuario
    def buscarUsuario(self):
        self.lblmsg["text"] = ""
        user = Usuarios()
        usuario = self.txtusuario.get()

        self.lblmsg["text"] = user.selectUser(usuario)

        #self.txtidusuario.delete(0, END)
        #self.txtidusuario.insert(INSERT, user.idusuario)

        self.txtnome.delete(0, END)
        self.txtnome.insert(INSERT, user.nome)

        self.txttelefone.delete(0, END)
        self.txttelefone.insert(INSERT, user.telefone)

        self.txtemail.delete(0, END)
        self.txtemail.insert(INSERT, user.email)

        self.txtusuario.delete(0, END)
        self.txtusuario.insert(INSERT, user.usuario)

        self.txtsenha.delete(0,END)
        self.txtsenha.insert(INSERT, user.senha)


    def alterarUsuario(self):
        self.lblmsg["text"] = ""
        user = Usuarios()

        user.email = self.txtemail.get()
        user.telefone = self.txttelefone.get()
        user.nome = self.txtnome.get()
        user.usuario = self.txtusuario.get()
        user.senha = self.txtsenha.get()

        self.lblmsg["text"] = user.updateUser()

        if self.lblmsg["text"] == "Update sucesso":
            self.txtnome.delete(0, END)
            self.txttelefone.delete(0, END)
            self.txtemail.delete(0, END)


    def deletarUsuario(self):
        self.lblmsg["text"] = ""
        user = Usuarios()

        user.usuario = self.txtusuario.get()

        self.lblmsg["text"] = user.deleteUser()

        self.txtnome.delete(0, END)
        self.txttelefone.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtusuario.delete(0, END)
        self.txtsenha.delete(0, END)


    def showCadastrar(self):
        self.lblmsg["text"] = ""

        self.txtnome.delete(0, END)
        self.txttelefone.delete(0, END)
        self.txtemail.delete(0, END)

        self.lblnome.pack(side=LEFT)

        self.txtnome.pack(side=LEFT)

        self.lbltelefone.pack(side=LEFT)

        self.txttelefone.pack(side=LEFT)

        self.lblemail.pack(side=LEFT)

        self.txtemail.pack(side=LEFT)

        self.btnInsert.pack(side=LEFT)

        self.btnAlterar.pack_forget()

        self.btnDeletar.pack_forget()





    def hideCadastrar(self):

        self.txtnome.delete(0, END)
        self.txttelefone.delete(0, END)
        self.txtemail.delete(0, END)

        self.lblnome.pack_forget()

        self.txtnome.pack_forget()

        self.lbltelefone.pack_forget()

        self.txttelefone.pack_forget()

        self.lblemail.pack_forget()

        self.txtemail.pack_forget()

        self.btnInsert.pack_forget()

        self.btnAlterar.pack_forget()

        self.btnDeletar.pack_forget()


    def inicializaBigContainer1(self):

        self.container1 = Frame(self.bigContainer1)
        self.container1["pady"] = 10
        self.container1.pack()

        self.container2 = Frame(self.bigContainer1)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()

        self.container3 = Frame(self.bigContainer1)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()

        self.container4 = Frame(self.bigContainer1)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()

        self.container5 = Frame(self.bigContainer1)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()

        self.container6 = Frame(self.bigContainer1)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()

        self.container7 = Frame(self.bigContainer1)
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()

        self.container8 = Frame(self.bigContainer1)
        self.container8["padx"] = 20
        self.container8["pady"] = 5
        self.container8.pack()

        self.container9 = Frame(self.bigContainer1)
        self.container9["pady"] = 15
        self.container9.pack()

        self.titulo = Label(self.container1, text="Informe os dados:")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack()

        self.lblusuario = Label(self.container2, text="Usuário", font=self.fonte, width=10)
        self.lblusuario.pack(side=LEFT)

        self.txtusuario = Entry(self.container2)
        self.txtusuario["width"] = 25
        self.txtusuario["font"] = self.fonte
        self.txtusuario.pack(side=LEFT)

        self.lblsenha = Label(self.container3, text="Senha", font=self.fonte, width=10)
        self.lblsenha.pack(side=LEFT)

        self.txtsenha = Entry(self.container3)
        self.txtsenha["width"] = 25
        self.txtsenha["show"] = "*"
        self.txtsenha["font"] = self.fonte
        self.txtsenha.pack(side=LEFT)

        self.btnAutenticar = Button(self.container4, text="Autenticar", font=self.fonte, width=10)
        self.btnAutenticar["command"] = self.verificaSenha
        self.btnAutenticar.pack(side=LEFT)

        self.btnCadastrar = Button(self.container4, text="Cadastrar", font=self.fonte, width=10)
        self.btnCadastrar["command"] = self.showCadastrar
        self.btnCadastrar.pack(side=LEFT)

        self.lblnome = Label(self.container5, text="Nome", font=self.fonte, width=10)

        self.txtnome = Entry(self.container5)
        self.txtnome["width"] = 25
        self.txtnome["font"] = self.fonte

        self.lbltelefone = Label(self.container6, text="Telefone", font=self.fonte, width=10)

        self.txttelefone = Entry(self.container6)
        self.txttelefone["width"] = 25
        self.txttelefone["font"] = self.fonte

        self.lblemail = Label(self.container7, text="E-mail", font=self.fonte, width=10)

        self.txtemail = Entry(self.container7)
        self.txtemail["width"] = 25
        self.txtemail["font"] = self.fonte

        self.btnInsert = Button(self.container8, text="Inserir", font=self.fonte, width=12)
        self.btnInsert["command"] = self.inserirUsuario

        self.btnAlterar = Button(self.container8, text="Alterar", font=self.fonte, width=12)
        self.btnAlterar["command"] = self.alterarUsuario

        self.btnDeletar = Button(self.container8, text="Deletar", font=self.fonte, width=12)
        self.btnDeletar["command"] = self.deletarUsuario

        self.lblmsg = Label(self.container9, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()


    def inicializaBigContainer2(self):
        self.container1_2 = Frame(self.bigContainer2)
        self.container1_2["pady"] = 10
        self.container1_2.pack()

        self.container2_2 = Frame(self.bigContainer2)
        self.container2_2["padx"] = 20
        self.container2_2["pady"] = 5
        self.container2_2.pack()

        self.container3_2 = Frame(self.bigContainer2)
        self.container3_2["padx"] = 20
        self.container3_2["pady"] = 5
        self.container3_2.pack()

        self.container4_2 = Frame(self.bigContainer2)
        self.container4_2["padx"] = 20
        self.container4_2["pady"] = 5
        self.container4_2.pack()

        self.container5_2 = Frame(self.bigContainer2)
        self.container5_2["padx"] = 20
        self.container5_2["pady"] = 5
        self.container5_2.pack()

        self.container6_2 = Frame(self.bigContainer2)
        self.container6_2["pady"] = 15
        self.container6_2.pack()


        self.titulo2 = Label(self.container1_2, text="Informe os dados do produto:")
        self.titulo2["font"] = ("Calibri", "9", "bold")
        self.titulo2.pack()

        self.lblproduto = Label(self.container2_2, text="Nome", font=self.fonte, width=10)
        self.lblproduto.pack(side=LEFT)

        self.txtproduto = Entry(self.container2_2)
        self.txtproduto["width"] = 25
        self.txtproduto["font"] = self.fonte
        self.txtproduto.pack(side=LEFT)

        self.lblpreco = Label(self.container3_2, text="preço", font=self.fonte, width=10)
        self.lblpreco.pack(side=LEFT)

        self.txtpreco = Entry(self.container3_2)
        self.txtpreco["width"] = 25
        self.txtpreco["font"] = self.fonte
        self.txtpreco.pack(side=LEFT)

        self.lbldescricao = Label(self.container4_2, text="descrição", font=self.fonte, width=10)
        self.lbldescricao.pack(side=LEFT)

        self.txtdescricao = Entry(self.container4_2)
        self.txtdescricao["width"] = 25
        self.txtdescricao["font"] = self.fonte
        self.txtdescricao.pack(side=LEFT)

        self.btnbuscar = Button(self.container5_2, text="Buscar", font=self.fonte, width=12)
        self.btnbuscar["command"] = self.buscarProduto
        self.btnbuscar.pack(side=LEFT)

        self.btncadastraremprego = Button(self.container5_2, text="Cadastrar", font=self.fonte, width=12)
        self.btncadastraremprego["command"] = self.cadastrarProduto
        self.btncadastraremprego.pack(side=LEFT)

        self.btndeletaremprego = Button(self.container5_2, text="Deletar", font=self.fonte, width=12)
        self.btndeletaremprego["command"] = self.deletarProduto
        self.btndeletaremprego.pack(side=LEFT)

        self.lblmsg2 = Label(self.container6_2, text="")
        self.lblmsg2["font"] = ("Verdana", "9", "italic")
        self.lblmsg2.pack()


    def buscarProduto(self):

        produto = Produto()
        produto.nome = self.txtproduto.get()
        produto.preco = self.txtpreco.get()
        produto.descricao = self.txtdescricao.get()

        self.lblmsg2["text"] = produto.selectProduto(0, produto.nome)

        self.txtproduto.delete(0, END)
        self.txtproduto.insert(INSERT, produto.nome)

        self.txtpreco.delete(0, END)
        self.txtpreco.insert(INSERT, produto.preco)

        self.txtdescricao.delete(0, END)
        self.txtdescricao.insert(INSERT, produto.descricao)


    def cadastrarProduto(self):
        produto = Produto()
        produto.nome = self.txtproduto.get()
        produto.preco = self.txtpreco.get()
        produto.descricao = self.txtdescricao.get()

        self.lblmsg2["text"] = produto.insertProduto(0, produto.nome, produto.preco, produto.descricao)

    def deletarProduto(self):
        produto = Produto()
        produto.nome = self.txtproduto.get()
        produto.preco = self.txtpreco.get()
        produto.descricao = self.txtdescricao.get()

        self.lblmsg2["text"] = produto.deleteProduto(0, produto.nome)

        if self.lblmsg2["text"] == "delete produto sucesso":
            self.txtproduto.delete(0, END)
            self.txtpreco.delete(0, END)
            self.txtdescricao.delete(0, END)


    def inicializaBigContainer3(self):
        self.container1_3 = Frame(self.bigContainer3)
        self.container1_3["pady"] = 10
        self.container1_3.pack()

        self.container2_3 = Frame(self.bigContainer3)
        self.container2_3["padx"] = 20
        self.container2_3["pady"] = 5
        self.container2_3.pack()

        self.container3_3 = Frame(self.bigContainer3)
        self.container3_3["padx"] = 20
        self.container3_3["pady"] = 5
        self.container3_3.pack()

        self.container4_3 = Frame(self.bigContainer3)
        self.container4_3["padx"] = 20
        self.container4_3["pady"] = 5
        self.container4_3.pack()

        self.container5_3 = Frame(self.bigContainer3)
        self.container5_3["padx"] = 20
        self.container5_3["pady"] = 5
        self.container5_3.pack()

        self.container6_3 = Frame(self.bigContainer3)
        self.container6_3["pady"] = 15
        self.container6_3.pack()


        self.titulo3 = Label(self.container1_3, text="Insira o produto no carrinho:")
        self.titulo3["font"] = ("Calibri", "9", "bold")
        self.titulo3.pack()

        #self.lblprodutocarrinho = Label(self.container2_3, text="Produto", font=self.fonte, width=10)
        #self.lblprodutocarrinho.pack(side=LEFT)

        #self.txtprodutocarrinho = Entry(self.container2_3)
        #self.txtprodutocarrinho["width"] = 25
        #self.txtprodutocarrinho["font"] = self.fonte
        #self.txtprodutocarrinho.pack(side=LEFT)


        self.btnbuscarprodutocarrinho = Button(self.container5_3, text="Buscar", font=self.fonte, width=12)
        #self.btnbuscarprodutocarrinho["command"] = self.buscarProdutoCarrinho
        self.btnbuscarprodutocarrinho.pack(side=LEFT)

        self.btncadastrarprodutocarrinho = Button(self.container5_3, text="Cadastrar", font=self.fonte, width=12)
        self.btncadastrarprodutocarrinho["command"] = self.cadastrarProdutoCarrinho
        self.btncadastrarprodutocarrinho.pack(side=LEFT)

        self.btndeletarprodutocarrinho = Button(self.container5_3, text="Deletar", font=self.fonte, width=12)
        #self.btndeletarprodutocarrinho["command"] = self.deletarProdutoCarrinho
        self.btndeletarprodutocarrinho.pack(side=LEFT)

        self.lblmsg3 = Label(self.container6_3, text="")
        self.lblmsg3["font"] = ("Verdana", "9", "italic")
        self.lblmsg3.pack()


    def buscarProdutoCarrinho(self):
        carrinho = Carrinho()
        user = Usuarios()
        produto = Produto()
        carrinho.idusuario = self.user.log
        carrinho.idproduto = self.produto.idproduto

        if carrinho.idusuario > 0 and carrinho.idproduto > 0:
            if carrinho.selectCarrinho(carrinho.idusuario) == "select carrinho sucesso":
                self.lblmsg3["text"] = carrinho.selectCarrinhoProduto(carrinho.idusuario, carrinho.idproduto)
            else:
                self.lblmsg3["text"] = "produto não encontrado"
        else:
            self.lblmsg3["text"] = "dados não informados corretamente"



    def cadastrarProdutoCarrinho(self):
        carrinho = Carrinho()
        user = Usuarios()
        produto = Produto()

        user.autenticaUser(self.txtusuario.get(), self.txtsenha.get())
        produto.selectProduto(0, self.txtproduto.get())

        carrinho.idusuario = user.idusuario
        carrinho.idproduto = produto.idproduto

        print(carrinho.idusuario, carrinho.idproduto)

        if carrinho.idusuario > 0 and carrinho.idproduto > 0:
            self.lblmsg3["text"] = carrinho.insertCarrinho(carrinho.idusuario, carrinho.idproduto)
        else:
            self.lblmsg3["text"] = "produto não inserido no carrinho, autentique o usuario e selecione o produto"

    def deletarProdutoCarrinho(self):
        carrinho = Carrinho()
        user = Usuarios()
        produto = Produto()
        carrinho.idusuario = self.user.log
        carrinho.idproduto = self.produto.idproduto

        self.lblmsg3["text"] = self.carrinho.deleteCarrinhoProduto(self.carrinho.idusuario, self.carrinho.idproduto)

        if self.lblmsg3["text"] == "delete carrinhoProduto sucesso":
            self.txtprodutocarrinho.delete(0, END)





root = Tk()
root.title("Sistema de cadastro")
Application(root)
root.mainloop()