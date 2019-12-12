import session
from termcolor import colored

def listar_alugueis(user):
    print(colored("Alugueis do usuario %s" % user.nome, "yellow"))

    lista = user.alugueis

    for a in lista:
        print(a.filme.nome)