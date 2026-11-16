class ListaEncadeada:
    def __init__(self):
        self.head = None
        self.size = 0

    def adicionar_servico(self, servico):
        novo_no = No(servico)

        if self.head is None:
            self.head = novo_no 

        else:
            atual = self.head

            while atual.proximo is not None:
                atual = atual.proximo

            atual.proximo = novo_no

        self.size += 1

    def consultar_registro(self, id_servico):
        no_atual = self.head

        while no_atual.servico.id_servico is not id_servico:
            no_atual = no_atual.proximo

        if no_atual == None:
            print(f"Serviço com o id {id_servico} não encontrado!")

        else:
            # Placeholder para mostrar o registro
            print(no_atual.servico.__dict__)

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