from classes import ListaEncadeada, Servico

def executar_menu(lista):

    while True:

        print("\n========== CITIZEN ASSIST AI ==========")
        print("1 - Cadastrar serviço")
        print("2 - Consultar todos os serviços")
        print("3 - Consultar serviço por ID")
        print("4 - Pesquisar por título ou categoria")
        print("5 - Atualizar serviço")
        print("6 - Excluir serviço")
        print("7 - Ordenar serviços")
        print("0 - Sair")
        print("=======================================")

        opcao = input("Escolha uma opção: ").strip()

        # Cadastrar serviço
        if opcao == "1":

            id_servico = input("ID: ").strip()
            titulo = input("Título: ").strip()
            categoria = input("Categoria: ").strip()
            descricao = input("Descrição: ").strip()
            canal = input("Canal/local: ").strip()

            # Validação dos campos obrigatórios
            if not id_servico or not titulo or not categoria or not descricao or not canal:
                print("Erro: todos os campos são obrigatórios!")
                continue

            servico = Servico(
                id_servico,
                titulo,
                categoria,
                descricao,
                canal
            )

            lista.adicionar_servico(servico)

        # Consultar todos os serviços
        elif opcao == "2":

            if lista.head is None:
                print("Não existem serviços cadastrados.")
            else:
                lista.consultar_registro()

        # Consultar por ID
        elif opcao == "3":

            id_servico = input("Informe o ID do serviço: ").strip()

            if not id_servico:
                print("Erro: o ID não pode estar vazio!")
                continue

            lista.consultar_registro(id_servico=id_servico)

        # Pesquisar por título ou categoria
        elif opcao == "4":

            print("\nPesquisar por:")
            print("1 - Título")
            print("2 - Categoria")

            criterio = input("Escolha o critério: ").strip()

            if criterio == "1":
                atributo = "titulo"
            elif criterio == "2":
                atributo = "categoria"
            else:
                print("Opção de pesquisa inválida!")
                continue

            termo = input("Digite o termo de pesquisa: ").strip()

            if not termo:
                print("Erro: o termo de pesquisa não pode estar vazio!")
                continue

            lista.consultar_registro(
                atributo=atributo,
                termo=termo
            )

        # Atualizar serviço
        elif opcao == "5":

            id_servico = input("Informe o ID do serviço: ").strip()

            if not id_servico:
                print("Erro: o ID não pode estar vazio!")
                continue

            # Verifica se o serviço existe
            no = lista.consultar_registro(id_servico=id_servico)

            if no is None:
                continue

            print("\nDeixe o campo vazio para manter o valor atual.")

            titulo = input("Novo título: ").strip()
            categoria = input("Nova categoria: ").strip()
            descricao = input("Nova descrição: ").strip()
            canal = input("Novo canal/local: ").strip()

            # Impede que campos informados sejam apenas espaços
            resultado = lista.atualizar_registro(
                id_servico,
                titulo=titulo if titulo else None,
                categoria=categoria if categoria else None,
                descricao=descricao if descricao else None,
                canal=canal if canal else None
            )

            if resultado:
                print("Serviço atualizado com sucesso!")

        # Excluir serviço
        elif opcao == "6":

            id_servico = input("Informe o ID do serviço: ").strip()

            if not id_servico:
                print("Erro: o ID não pode estar vazio!")
                continue

            lista.excluir_registro(id_servico)

        # Ordenar serviços
        elif opcao == "7":

            print("\nOrdenar por:")
            print("1 - Título")
            print("2 - Identificador")

            criterio = input("Escolha o critério: ").strip()

            if criterio == "1":
                criterio = "titulo"
            elif criterio == "2":
                criterio = "id_servico"
            else:
                print("Opção de ordenação inválida!")
                continue

            if lista.ordenar_registros(criterio):
                print("Serviços ordenados com sucesso!")
                lista.consultar_registro()

        # Encerrar programa
        elif opcao == "0":

            print("Encerrando o Citizen Assist AI. Até mais!")
            break

        else:
            print("Opção inválida! Digite uma opção disponível no menu.")

if __name__ == "__main__":
    lista = ListaEncadeada()

    executar_menu(lista)