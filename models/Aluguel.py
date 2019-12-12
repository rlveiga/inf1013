class Aluguel:
    def __init__(self, filme, usuario, valor, dias):
        self.filme = filme
        self.usuario = usuario
        self.status = 'ativo'
        self.valor = valor
        self.dias = dias
        self.devolvido_em = None

