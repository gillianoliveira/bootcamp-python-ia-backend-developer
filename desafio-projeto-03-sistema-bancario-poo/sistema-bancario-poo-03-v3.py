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


class Validacao:

    @staticmethod
    def verifica_cpf_cadastro(cpf, clientes):
        if len(cpf) != 11 or not cpf.isdigit():
            raise ValueError("CPF inválido. O CPF deve ter 11 dígitos.")
        # TODO: TypeError: 'NoneType' object is not iterable -
        # erro de validação com a lista vazia
        # for cliente in clientes:
        #     if cliente['cpf'] == cpf:
        #         raise ValueError("CPF já cadastrado.")
        return True


class Cliente:

    __clientes = []

    def __init__(self, endereco=None, telefone=None):
        self.__endereco = endereco
        self.__telefone = telefone

    @property
    def endereco(self):
        return self.__endereco

    @property
    def telefone(self):
        return self.__telefone

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    @classmethod
    def obter_clientes(cls):
        return cls.__clientes

    @classmethod
    def adicionar_clientes_lista(cls, cliente):
        cls.__clientes.append(cliente)

    @classmethod
    def exibir_lista_clientes(cls):
        clientes = Cliente.obter_clientes()
        for pessoa_fisica in clientes:
            print(f"""
        Nome Completo:{pessoa_fisica.nome}
        CPF: {pessoa_fisica.cpf}
        Data de Nascimento: {pessoa_fisica.data_de_nascimento}
        Telefone: {pessoa_fisica.telefone}
        Endereço: {pessoa_fisica.endereco}""")

    @classmethod
    def cadastrar_cliente(cls):
        try:
            cliente = PessoaFisica()
            cliente.cadastrar_cliente()
            cls.adicionar_clientes_lista(cliente)
        except ValueError as ve:
            return f'Erro: {ve}'

    def __str__(self):
        return f"""
        Dados do Cliente:
        Nome Completo:{pessoa_fisica.nome}
        CPF: {pessoa_fisica.cpf}
        Data de Nascimento: {pessoa_fisica.data_de_nascimento}
        Telefone: {pessoa_fisica.telefone}
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

    @property
    def cpf(self):
        return self.__cpf

    @property
    def data_de_nascimento(self):
        return self.__data_de_nascimento

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @cpf.setter
    def cpf(self, cpf):
        clientes = Cliente.exibir_lista_clientes()
        Validacao.verifica_cpf_cadastro(cpf, clientes)
        self.__cpf = cpf

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
                        cliente.exibir_lista_clientes()
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
