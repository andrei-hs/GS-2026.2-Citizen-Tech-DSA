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

    def consultar_registro(self, id_servico=None):
        no_atual = self.head

        if id_servico is None:
            # Mostrar todos os registros
            while no_atual is not None:
                print(no_atual.servico.__dict__)
                no_atual = no_atual.proximo

            return

        # Procurar o registro pelo ID
        while no_atual is not None:
            if no_atual.servico.id_servico == id_servico:
                print(no_atual.servico.__dict__)
                return no_atual

            no_atual = no_atual.proximo

        print(f"Serviço com o ID {id_servico} não encontrado!")
        return None

    def atualizar_registro(self, id_servico, titulo=None, categoria=None, descricao=None, canal=None):
        no = self.consultar_registro(id_servico)

        if no is None:
            return False

        if titulo is not None:
            no.servico.titulo = titulo

        if categoria is not None:
            no.servico.categoria = categoria

        if descricao is not None:
            no.servico.descricao = descricao

        if canal is not None:
            no.servico.canal = canal

        return True

    def excluir_registro(self, id_servico):
        no_atual = self.head
        no_anterior = None

        while no_atual is not None:

            if no_atual.servico.id_servico == id_servico:

                # Caso 1: o registro está no início da lista
                if no_anterior is None:
                    self.head = no_atual.proximo

                # Caso 2: o registro está no meio ou no final
                else:
                    no_anterior.proximo = no_atual.proximo

                self.size -= 1
                return True

            # Avança os ponteiros
            no_anterior = no_atual
            no_atual = no_atual.proximo

        print(f"Serviço com o ID {id_servico} não encontrado!")
        return False

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