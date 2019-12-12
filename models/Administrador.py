from controllers import filme_controller 
from models.Filme import Filme
from helpers import movie_helper, user_helper
from termcolor import colored
import session

class Administrador:
    def __init__(self, nome, loja, role):
        self.nome = nome
        self.loja = loja
        self.role = role

    def exibir_loja(self):
        print("Filmes da loja %s (%s)" % (self.loja.nome, self.loja.local))

        for e in self.loja.filmes:
            e.exibir_info()

    def adicionar_filme(self):
        # user_list = user_helper.read()

        # for u in user_list:
        #     if(u.nome == self.nome):
        #         user_list.remove(u)

        # movie_list = movie_helper.read()
        nome = input("Digite o nome do filme: ")
        ano = input("Digite o ano do filme: ")
        genero = input("Digite o gênero do filme: ")

        novo_filme = Filme(nome, ano, genero, self.loja)
        self.loja.filmes.append(novo_filme)

        movie_helper.save(novo_filme)
        user_helper.update(self)

        # movie_list.append(novo_filme)
        # movie_helper.write(movie_list)

        # user_list.append(self)
        # user_helper.write(user_list)

    # def editar_filme(self, nome_filme):
    #     user_list = user_helper.read()

    #     for u in user_list:
    #         if(u.nome == self.nome):
    #             user_list.remove(u)

    #     movie_list = movie_helper.read()
    #     filme = None

    #     for e in movie_list:
    #         if(e.nome == nome_filme and e.loja.nome == self.loja.nome):
    #             filme = e

    #     if(filme is None):
    #         print(colored("Filme %s não encontrado na sua loja" % nome_filme, "red"))
    #         return

    #     nome_novo = input("Nome: (%s) " % filme.nome)
    #     ano_novo = input("Ano: (%s) " % filme.ano)
    #     genero_novo = input("Genero: (%s) " % filme.genero)

    #     if(nome_novo == ""):
    #         nome_novo = filme.nome

    #     if(ano_novo == ""):
    #         ano_novo = filme.ano

    #     if(genero_novo == ""):
    #         genero_novo = filme.genero

    #     filme_edit = Filme(nome_novo, ano_novo, genero_novo, self.loja)

    #     for i in range(len(self.loja.filmes)):
    #         if(self.loja.filmes[i].nome == nome_filme):
    #             self.loja.filmes[i] = filme_edit
            
    #     movie_list.remove(filme)
    #     movie_list.append(filme_edit)
    #     movie_helper.write(movie_list)

    #     user_list.append(self)
    #     user_helper.write(user_list)
    
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
        # # user_list = user_helper.read()

        # # for u in user_list:
        # #     if(u.nome == self.nome):
        # #         user_list.remove(u)
                
        # # movie_list = movie_helper.read()
        # # filme = None

        # for e in movie_list:
        #     if(e.nome == nome_filme and e.loja.nome == self.loja.nome):
        #         filme = e

        # if(filme is None):
        #     print(colored("Filme %s não encontrado na sua loja" % nome_filme, "red"))
        #     return

        # movie_list.remove(filme)

        # for e in self.loja.filmes:
        #     if(e.nome == nome_filme):
        #         self.loja.filmes.remove(e)

        # user_list.append(self)
        # user_helper.write(user_list)
        # movie_helper.write(movie_list)

    def helper(self):
        print("Comandos disponíveis para administradores:")
        print("    loja - exibe os filmes da sua loja")
        print("    add - adiciona um novo filme")
        print("    edit <nome_filme> - editar filme")
        print("    rm <nome_filme> - remover filme")
        print("    h - exibir ajuda")
        print("    q - sair")

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