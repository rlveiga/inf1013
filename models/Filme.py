from termcolor import colored
from helpers import movie_helper, user_helper
from models.Aluguel import Aluguel
import session
from datetime import datetime

class Filme:
    def __init__(self, nome, ano, genero, loja):
        self.nome = nome
        self.ano = ano
        self.genero = genero
        self.alugado = False
        self.alugado_por = None
        self.loja = loja

    def exibir_info(self):
        color = None

        if self.alugado:
            color = "red"
    
        print(colored("\n%s\n%s\n%s\n" % (self.nome, self.ano, self.genero), color))

    def editar(self):
        previous_name = self.nome
        
        nome_novo = input("Nome: (%s) " % self.nome)
        ano_novo = input("Ano: (%s) " % self.ano)
        genero_novo = input("Genero: (%s) " % self.genero)

        if(nome_novo == ""):
            nome_novo = self.nome

        if(ano_novo == ""):
            ano_novo = self.ano

        if(genero_novo == ""):
            genero_novo = self.genero

        self.nome = nome_novo
        self.ano = ano_novo
        self.genero = genero_novo

        movie_helper.update(previous_name, self)

        for i, m in enumerate(session.client.loja.filmes):
            if(m.nome == previous_name):
                session.client.loja.filmes[i] = self

        user_helper.update(session.client)
        
    def alugar(self):
        if(self.alugado is True):
            print(colored("Este filme não está disponível para aluguel", "red"))

        else:
            option = input(colored("Tem certeza que deseja alugar o filme %s? (y/n)" % self.nome, "white"))

            if(option == 'y'):
                self.alugado = True
                self.alugado_por = session.client.nome

                novo_aluguel = Aluguel(self, session.client.nome, 10, 7)

                session.client.alugueis.append(novo_aluguel)

                movie_helper.update(self.nome, self)
                user_helper.update(session.client)

    def devolver(self):
        if(self.alugado is False):
            print(colored("Este filme não está disponível para devolução", "red"))

        elif(self.alugado_por != session.client.nome):
            print(colored("Você não alugou este filme para devolvê-lo", "red"))

        else:
            self.alugado = False
            self.alugado_por = None

            for i, a in enumerate(session.client.alugueis):
                if(a.filme.nome == self.nome and a.status == 'ativo'):
                    session.client.alugueis[i].status = 'devolvido'
                    session.client.alugueis[i].devolvido_em = datetime.now()
                    break

            movie_helper.update(self.nome, self)
            user_helper.update(session.client)
