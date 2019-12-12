from helpers import movie_helper, user_helper
from models.Filme import Filme
from models.Aluguel import Aluguel
import pickle
import session
from termcolor import colored

def exibir_filmes():
    data = movie_helper.read()
    
    print(colored("Filmes em vermelho estão indisponíveis para aluguel", "yellow"))
    for filme in data:
        filme.exibir_info()

def exibir_filmes_disponiveis():
    data = movie_helper.read()

    for filme in data:
        if(filme.alugado is False):
            filme.exibir_info()
