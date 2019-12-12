import json
import pickle
import session
from controllers import filme_controller, cliente_controller
from models.Cliente import Cliente
from models.Administrador import Administrador
from models.Loja import Loja
from helpers import user_helper
import sys
from termcolor import colored

sys.path.insert(1, '/path/to/application/app/folder')

# Loga usuário como cliente ou administrador
def login():
    user_input = input("Digite um nome de usuario para entrar: ")

    user = user_helper.get_user(user_input)

    # New user
    if(user == None):
        create_user = input(colored("Nenhum usuário %s encontrado, gostaria de criar? (y/n) " % user_input, "white"))
        
        if(create_user == 'y'):
            user_role = input(colored("Escolha um tipo de usuário (admin/cliente) ", "white"))

            print(colored('Criando usuário %s do tipo %s...' % (user_input, user_role), "yellow"))

            if(user_role == "admin"):
                store_name = input(colored("Digite um nome para sua nova loja: ", "white"))
                store_location = input(colored("Digite o local da sua nova loja: ", "white"))
                new_store = Loja(store_name, store_location)
                new_user = Administrador(user_input, new_store)

            elif(user_role == "cliente"):
                new_user = Cliente(user_input)

            else:
                login()
            
            user_helper.save(new_user)
            session.client = new_user

        else:
            login()

    # # Existing user
    else:
        session.client = user

def init():
    login()
    print(colored('Bem-vindo à locadora, %s!' % session.client.nome, "yellow"))
    session.client.helper()
    session.client.read_command()

init()