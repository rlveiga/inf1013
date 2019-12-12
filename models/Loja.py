class Loja:
    def __init__(self, nome, local):
        self.nome = nome
        self.local = local
        self.filmes = []

    def listar_filmes(self):
        print(self.filmes)