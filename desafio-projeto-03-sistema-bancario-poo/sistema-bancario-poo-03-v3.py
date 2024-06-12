# DESAFIO DE PROJETO
# Criando um Sistema Bancário com Python - parte 3
# Módulo: Dominando Python e suas Estruturas de Dados
# Bootcamp: Python AI Backend Developer Bootcamp
# Conclusão: em desenvolvimento


class Estilo:

    @staticmethod
    def titulo(t):
        print("-" * 30)
        print(f'{t.center(30, " ")}')
        print("-" * 30)

class MenuPrincipal:
    def __init__(self):
        self._cliente = cliente
        # self._conta = conta

    def menu(self):
        while True:
            Estilo.titulo("Menu")
            opcao = int(
                input(
                    """
        [1] Abertura de Conta
        [2] Cadastrar Cliente
        [3] Listar Clientes
        [4] Listar Contas
        [8] Sair
        Opção escolhida: """
                )
            )
            try:
                match opcao:
                    case 1:
                        pass
                    case 2:
                        pass
                    case 3:
                        pass
                    case 4:
                        pass
                    case 8:
                        pass
                        print("Programa encerrado.")
                        exit()
                    case _:
                        print("Opção inválida. Programa encerrado.")
                        exit()
            except ValueError as ve:
                print(f"Opção inválida. Erro: {ve}")


# cliente = Cliente()
# conta = Conta()
iniciar = MenuPrincipal()
iniciar.menu()
