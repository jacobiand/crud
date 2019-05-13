from tkinter import *
from usuarios import Usuarios
from empregos import Empregos


class Application:
    def __init__(self, master=None):
        self.bigContainer1 = Frame(master)
        self.bigContainer1.pack(side=LEFT)
        self.bigContainer2 = Frame(master)
        self.bigContainer2.pack(side=RIGHT)

        self.fonte = ("Verdana", "10")

        #cadastro de usuario
        self.inicializaBigContainer1()

        #cadastro de empregos
        self.inicializaBigContainer2()



    #verificar senha
    def verificaSenha(self):
        self.lblmsg["text"] = ""
        user = Usuarios()

        user.usuario = self.txtusuario.get()
        user.senha = self.txtsenha.get()

        mensage = user.autenticaUser()
        if (mensage == "Autentica sucesso"):
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
        elif (mensage == "Autentica falha - usuario não encontrado"):
            self.lblmsg["text"] = "Usuário não está cadastrado"
        else:
            self.lblmsg["text"] = "Falha na autenticação"



    #cadastra um novo usuario
    def inserirUsuario(self):
        self.lblmsg["text"] = ""
        user = Usuarios()

        user.email = self.txtemail.get()
        user.telefone = self.txttelefone.get()
        user.nome = self.txtnome.get()
        user.usuario = self.txtusuario.get()
        user.senha = self.txtsenha.get()

        mensage = user.insertUser()
        if mensage == "Insert sucesso":
            self.lblmsg["text"] = "Usuário cadastrado com sucesso"
        elif mensage == "Insert falha - usuario ja existe":
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
        self.container5_2["pady"] = 15
        self.container5_2.pack()


        self.titulo2 = Label(self.container1_2, text="Informe os dados:")
        self.titulo2["font"] = ("Calibri", "9", "bold")
        self.titulo2.pack()

        self.lblemprego = Label(self.container2_2, text="Emprego", font=self.fonte, width=10)
        self.lblemprego.pack(side=LEFT)

        self.txtemprego = Entry(self.container2_2)
        self.txtemprego["width"] = 25
        self.txtemprego["font"] = self.fonte
        self.txtemprego.pack(side=LEFT)

        self.lblempresa = Label(self.container3_2, text="Empresa", font=self.fonte, width=10)
        self.lblempresa.pack(side=LEFT)

        self.txtempresa = Entry(self.container3_2)
        self.txtempresa["width"] = 25
        self.txtempresa["font"] = self.fonte
        self.txtempresa.pack(side=LEFT)

        self.btnbuscar = Button(self.container4_2, text="Buscar", font=self.fonte, width=12)
        self.btnbuscar["command"] = self.buscarEmprego
        self.btnbuscar.pack(side=LEFT)

        self.btncadastraremprego = Button(self.container4_2, text="Cadastrar", font=self.fonte, width=12)
        self.btncadastraremprego["command"] = self.cadastrarEmprego
        self.btncadastraremprego.pack(side=LEFT)

        self.btndeletaremprego = Button(self.container4_2, text="Deletar", font=self.fonte, width=12)
        self.btndeletaremprego["command"] = self.deletarEmprego
        self.btndeletaremprego.pack(side=LEFT)

        self.lblmsg2 = Label(self.container5_2, text="")
        self.lblmsg2["font"] = ("Verdana", "9", "italic")
        self.lblmsg2.pack()


    def buscarEmprego(self):
        emprego = Empregos()

        emprego.emprego = self.txtemprego.get()
        emprego.empresa = self.txtempresa.get()

        self.lblmsg2["text"] = emprego.selectEmpregos()


    def cadastrarEmprego(self):
        emprego = Empregos()

        emprego.emprego = self.txtemprego.get()
        emprego.empresa = self.txtempresa.get()

        self.lblmsg2["text"] = emprego.insertEmpregos()

    def deletarEmprego(self):
        emprego = Empregos()

        emprego.emprego = self.txtemprego.get()
        emprego.empresa = self.txtempresa.get()

        self.lblmsg2["text"] = emprego.deleteEmpregos()

        self.txtemprego.delete(0, END)
        self.txtempresa.delete(0, END)




root = Tk()
root.title("Sistema de cadastro")
Application(root)
root.mainloop()