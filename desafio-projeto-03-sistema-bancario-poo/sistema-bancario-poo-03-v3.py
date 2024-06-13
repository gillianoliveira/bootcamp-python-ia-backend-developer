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


class Cliente:

    def __init__(self, endereco=None, telefone=None):
        self.__endereco = endereco
        self.__telefone = telefone

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    def cadastrar_cliente(self):
        try:
            cliente = pessoa_fisica.cadastrar_cliente()
            print(cliente)
        except ValueError as ve:
            return f'Erro: {ve}'

    def __str__(self):
        return f"""\nDados do Cliente:\n
                     Nome Completo:{pessoa_fisica.nome}\n
                     CPF: {pessoa_fisica.cpf}\n
                     Data de Nascimento: {pessoa_fisica.data_de_nascimento}\n
                     Telefone: {pessoa_fisica.telefone}\n
                     Endereço: {pessoa_fisica.endereco}"""


class PessoaFisica(Cliente):

    def __init__(self, nome=None, cpf=None, data_de_nascimento=None,
                 endereco=None, telefone=None):
        super().__init__(endereco, telefone)
        self.__nome = nome
        self.__cpf = cpf
        self.__data_de_nascimento = data_de_nascimento

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def data_de_nascimento(self):
        return self.__data_de_nascimento

    @data_de_nascimento.setter
    def data_de_nascimento(self, data_de_nascimento):
        self.__data_de_nascimento = data_de_nascimento

    def cadastrar_cliente(self):
        self.cpf = input("CPF: ")
        self.nome = input("Nome Completo: ")
        self.data_de_nascimento = input("Data de Nascimento: ")
        self.telefone = input("Telefone: ")
        self.endereco = input("Endereço: ")
        return self


class MenuPrincipal:
    def __init__(self, cliente):
        self._cliente = cliente
        # self._pessoa_fisica = pessoa_fisica
        # self._conta = conta

    def menu(self):
        while True:
            Estilo.titulo("Menu")
            try:
                opcao = int(input("""
        [1] Abertura de Conta
        [2] Cadastrar Cliente
        [3] Listar Clientes
        [4] Listar Contas
        [8] Sair
        Opção escolhida: """))
                match opcao:
                    case 1:
                        pass
                    case 2:
                        self._cliente.cadastrar_cliente()
                    case 3:
                        pass
                    case 4:
                        pass
                    case 8:
                        Estilo.titulo("Sair")
                        print("Programa encerrado.")
                        exit()
                    case _:
                        print("Opção inválida. Programa encerrado.")
                        exit()
            except ValueError as ve:
                print(f"Opção inválida. Erro: {ve}")


cliente = Cliente()
pessoa_fisica = PessoaFisica()
# conta = Conta()
iniciar = MenuPrincipal(cliente)
iniciar.menu()
