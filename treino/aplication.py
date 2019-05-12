from tkinter import *
from usuarios import Usuarios


class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceirContainer = Frame(master)
        self.terceirContainer["padx"] = 20
        self.terceirContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.quintoContainer = Frame(master)
        self.quintoContainer["pady"] = 20
        self.quintoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Dados de usuário")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.nomeLabel = Label(self.segundoContainer, text="Nome", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)

        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)

        self.senhaLabel = Label(self.terceirContainer, text="Senha", font=self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)

        self.senha = Entry(self.terceirContainer)
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = "*"
        self.senha.pack(side=LEFT)

        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Autenticar"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.verificaSenha
        self.autenticar.pack(side=LEFT)

        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Cadastrar"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.cadastraUsuario
        self.autenticar.pack(side=LEFT)

        self.mensagem = Label(self.quintoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack(side=TOP)

    #verificar senha
    def verificaSenha(self):
        usuario = self.nome.get()
        senha = self.senha.get()

        dadosusuario = Usuarios(usuario, "1", "2", "3", "4", senha)
        mensage = dadosusuario.autenticaUser()
        if (mensage == "sucesso"):
            self.mensagem["text"] = "Autenticado"
        elif (mensage == "falha"):
            self.mensagem["text"] = "Erro na autenticação"


    def cadastraUsuario(self):
        usuario = self.nome.get()
        senha = self.senha.get()

        dadosusuario = Usuarios(usuario, "1", "2", "3", "4", senha)
        mensage = dadosusuario.insertUser()
        if mensage == "Usuário cadastrado com sucesso!":
            self.mensagem["text"] = "Sucesso no cadastro"
        elif mensage == "Ocorreu um erro na inserção do usuário":
            self.mensagem["text"] = "Falha no cadastro"






root = Tk()
Application(root)
root.mainloop()