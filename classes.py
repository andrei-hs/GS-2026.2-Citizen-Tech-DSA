class ListaEncadeada:
    def __init__(self):
        self.head = None
        self.size = 0

class Servico:
    def __init__(self, id_servico, titulo, categoria, descricao, canal):
        self.id_servico = id_servico
        self.titulo = titulo
        self.categoria = categoria
        self.descricao = descricao
        self.canal = canal

class No:
    def __init__(self, servico):
        self.servico = servico
        self.proximo = None