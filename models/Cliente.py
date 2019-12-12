from helpers import movie_helper, user_helper
from termcolor import colored
from controllers import filme_controller
from models.Filme import Filme

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        # self.role = role
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
        for a in self.alugueis:
            print("\n%s\nR$%d" % (a.filme.nome, a.valor))

            if(a.status == 'ativo'):
                print("A ser devolvido em %d dias\n" % a.dias)
            else:
                print("Devolvido em %s\n" % a.devolvido_em)
    
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