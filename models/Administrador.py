from controllers import filme_controller 
from models.Filme import Filme
from helpers import movie_helper, user_helper
from termcolor import colored
import session

class Administrador:
    def __init__(self, nome, loja):
        self.nome = nome
        self.loja = loja
        # self.role = role

    def helper(self):
        print("Comandos disponíveis para administradores:")
        print("    loja - exibe os filmes da sua loja")
        print("    add - adiciona um novo filme")
        print("    edit <nome_filme> - editar filme")
        print("    rm <nome_filme> - remover filme")
        print("    h - exibir ajuda")
        print("    q - sair")

    def exibir_loja(self):
        print("Filmes da loja %s (%s)" % (self.loja.nome, self.loja.local))

        for e in self.loja.filmes:
            e.exibir_info()

    def adicionar_filme(self):
        nome = input("Digite o nome do filme: ")
        ano = input("Digite o ano do filme: ")
        genero = input("Digite o gênero do filme: ")

        novo_filme = Filme(nome, ano, genero, self.loja)
        self.loja.filmes.append(novo_filme)

        movie_helper.save(novo_filme)
        user_helper.update(self)
    
    def remover_filme(self, nome_filme):
        filme = movie_helper.get_movie(nome_filme)

        if(filme is None):
            print(colored("Filme %s não encontrado" % nome_filme, "red"))

        elif(filme.loja.nome != self.loja.nome):
            print(colored("O filme %s não pertence a sua loja" % nome_filme, "red"))

        elif(filme.alugado is True):
            print(colored("O filme %s não pode ser removido pois está sendo alugado" % nome_filme, "red"))

        else:
            option = input(colored("Tem certeza que deseja remover o filme %s? (y/n)" % nome_filme, "white"))

            if(option == 'y'):
                movie_helper.remove(filme.nome)

                for i, m in enumerate(self.loja.filmes):
                    if(m.nome == filme.nome):
                        del self.loja.filmes[i]

                user_helper.update(self)

    def read_command(self):
        user_input = input("Digite um comando: ")
        args = user_input.split()

        if(args[0] == "q" or args[0] == "Q"):
            return

        elif(args[0] == "loja"):
            self.exibir_loja()

        elif(args[0] == "h"):
            self.helper()

        elif(args[0] == "add"):
            self.adicionar_filme()

        elif(args[0] == "rm"):
            self.remover_filme(user_input[3:])

        elif(args[0] == "edit"):
            filme = movie_helper.get_movie(user_input[5:])

            if(filme is None):
                print(colored("Filme %s não encontrado" % user_input[5:], "red"))

            else:
                filme.editar()
            # self.editar_filme(user_input[5:])

        self.read_command()