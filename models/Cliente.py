from helpers import movie_helper, user_helper
from termcolor import colored
from controllers import filme_controller
from models.Filme import Filme

class Cliente:
    def __init__(self, nome, role):
        self.nome = nome
        self.role = role
        self.alugueis = []

    def helper(self):
        print("Comandos disponíveis para clientes:")
        print("    u - listar todos os seus filmes alugados")
        print("    la - listar todos os filmes")
        print("    ld - listar todos os filmes disponíveis")
        print("    alugar <nome_filme> - alugar filme")
        print("    devolver <nome_filme> - devolver filme")
        print("    h - exibir ajuda")
        print("    q - sair")

    def listar_alugueis(self):
        print(colored("Alugueis do usuario %s" % self.nome, "yellow"))
        for e in self.alugueis:
            print(e.nome)
    
    def alugar_filme(self, nome_filme):
        movie_list = movie_helper.read()
        user_list = user_helper.read()
        
        filme = None
        admin = None

        for e in movie_list:
            if(e.nome == nome_filme):
                filme = e

        if(filme is None):
            print(colored("Filme não encontrado", "red"))

            return
        
        if(filme.alugado is True):
            print(colored("Filme não disponível para aluguel", "red"))

            return

        for u in user_list:
            if(u.role == 'admin' and u.loja.nome == filme.loja.nome):
                admin = u
                user_list.remove(u)
                
            else:
                if(u.nome == self.nome):
                    user_list.remove(u)

        movie_list.remove(filme)

        filme.alugado = True
        filme.alugado_por = self.nome

        for i in range(len(admin.loja.filmes)):
            if(admin.loja.filmes[i].nome == nome_filme):
                admin.loja.filmes[i] = filme

        self.alugueis.append(filme)

        movie_list.append(filme)
        user_list.append(self)
        user_list.append(admin)

        movie_helper.write(movie_list)
        user_helper.write(user_list)

    def devolver_filme(self, nome_filme):
        movie_list = movie_helper.read()
        user_list = user_helper.read()
        
        filme = None
        user = None
        admin = None

        for e in movie_list:
            if(e.nome == nome_filme):
                filme = e

        if(filme is None):
            print(colored("Filme não encontrado", "red"))

            return
        
        if(filme.alugado is False or filme.alugado_por != self.nome):
            print(colored("Filme não disponível para devolução", "red"))

            return

        for i, u in enumerate(user_list):
            print(u.nome)
            if(u.role == 'admin' and u.loja.nome == filme.loja.nome):
                print('achou admin')
                admin = u
                
            else:
                if(u.nome == self.nome):
                    print('achou cliente')
                    user = u

        movie_list.remove(filme)
        user_list.remove(admin)
        user_list.remove(user)

        filme.alugado = False
        filme.alugado_por = None

        for i, e in enumerate(self.alugueis):
            if e.nome == nome_filme:
                del self.alugueis[i]
                break

        for i in range(len(admin.loja.filmes)):
            if(admin.loja.filmes[i].nome == nome_filme):
                admin.loja.filmes[i] = filme
                break

        movie_list.append(filme)
        user_list.append(self)
        user_list.append(admin)

        movie_helper.write(movie_list)
        user_helper.write(user_list)

    def read_command(self):
        user_input = input("Digite um comando: ")
        args = user_input.split()

        if(args[0] == "q" or args[0] == "Q"):
            return

        elif(args[0] == "h"):
            self.helper()

        elif(args[0] == "la"):
            filme_controller.exibir_filmes()

        elif(args[0] == "ld"):
            filme_controller.exibir_filmes_disponiveis()

        elif(args[0] == "alugar"):
            filme = movie_helper.get_movie(user_input[7:])

            if(filme is None):
                print(colored("Filme %s não encontrado" % user_input[7:], "red"))

            else:
                filme.alugar()

        elif(args[0] == "devolver"):
            filme = movie_helper.get_movie(user_input[9:])

            if(filme is None):
                print(colored("Filme %s não encontrado" % user_input[9:], "red"))
            
            else:
                filme.devolver()

        elif(args[0] == "u"):
            self.listar_alugueis()

        self.read_command()