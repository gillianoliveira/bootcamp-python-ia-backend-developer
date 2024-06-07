
# Formata o título das seções
def titulo(t):
    traco = '-'
    print(f"{traco * 30}")
    print(f'{t.center(30, " ")}')
    print(f"{traco * 30}")


class Validacao:

    @staticmethod
    def validar_cpf(cpf, clientes):
        if len(cpf) != 11:
            raise ValueError("CPF inválido. O CPF deve ter 11 dígitos.")

        for cliente in clientes:
            if cliente['cpf'] == cpf:
                raise ValueError("CPF já cadastrado.")

        return True


class Cliente:
    # Lista de clientes
    _clientes = []

    def __init__(self, tipo_cliente=None, endereco=None, telefone=None, conta=None):
        self._tipo_cliente = tipo_cliente
        self._endereco = endereco
        self._telefone = telefone
        self._conta = conta

    @classmethod
    def adicionar_cliente(cls, cliente):
        cls._clientes.append(cliente)
        print("Cliente cadastrado com sucesso.")

    @classmethod
    def visualizar_clientes(cls):
        if not cls._clientes:
            print("Nenhum cliente cadastrado.")
        for cliente in cls._clientes:
            print(cliente)

    def cadastrar_cliente(self):
        titulo('Cadastrar Cliente')
        while True:
            try:
                PessoaFisica(self._clientes).cadastrar_pessoa_fisica()
            except ValueError as exc:
                print(f'Opção inválida. Erro: {exc}')
                continue
            return cliente


class PessoaFisica(Cliente):
    def __init__(self, clientes):
        super().__init__(self)
        self._tipo_cliente = "Pessoa Física"
        self._endereco = None
        self._telefone = None
        self._nome = None
        self._cpf = None
        self._data_nascimento = None
        self._email = None

    def cadastrar_pessoa_fisica(self):
        while True:
            try:
                cpf = input("CPF: ")
                Validacao.validar_cpf(cpf, self._clientes)
                self._nome = input("Nome completo: ").capitalize()
                self._data_nascimento = input("Data de Nascimento: ")
                _logradouro = input("Logradouro: ")
                _numero = input("Número ")
                _bairro = input("Bairro: ")
                _cidade = input("Cidade: ")
                estado = input("Estado: ").upper()
                self._endereco = f'{
                            _logradouro}, {_numero}-{_bairro}-{
                                _cidade}/{estado}'
                self._email = input("E-mail: ")
                self._telefone = input("Telefone: ")

                cliente = {
                    'tipo_cliente': self._tipo_cliente,
                    'nome': self._nome,
                    'data_nascimento': self._data_nascimento,
                    'cpf': cpf,
                    'endereco': self._endereco,
                    'email': self._email,
                    'telefone': self._telefone
                }
                self.adicionar_cliente(cliente)
                break
            except ValueError as exc:
                print(f'Erro ao cadastrar cliente: {exc}')
                print('Por favor, tente novamente.')
                continue


class Extrato:
    pass


class Conta:
    _contas = []

    def __init__(self):
        self._saldo = 0.0
        self._agencia = "0001"
        self._numero_conta = None
        self._extrato = Extrato()

    def abertura_conta(self):
        titulo('Abertura de Conta')
        while True:
            cpf = input("CPF do Titular ou Responsável: ")
            Validacao.validar_cpf(cpf, )


class MenuPrincipal:
    def __init__(self, cliente, conta):
        self._cliente = cliente
        self._conta = conta

    def menu(self):
        titulo('Menu')
        while True:
            opcao = int(input('''
            [1] Depositar
            [2] Sacar
            [3] Extrato
            [4] Cadastrar Cliente
            [5] Abertura de Conta
            [6] Listar Clientes
            [7] Listar Contas
            [8] Sair
            Opção escolhida: '''))
            try:
                match opcao:
                    case 1:
                        pass
                        # depositar()
                    case 2:
                        pass
                        # sacar()
                    case 3:
                        pass
                        # visualizar_extrato()
                    case 4:
                        self._cliente.cadastrar_cliente()
                    case 5:
                        self._conta.abertura_conta()
                    case 6:
                        self._cliente.visualizar_clientes()
                    case 7:
                        pass
                    case 8:
                        titulo('Sair')
                        print('Programa encerrado.')
                        exit()
                    case _:
                        print('Opção inválida.')
                        exit()
            except ValueError as e:
                print(f'Erro de validação: {e}')
                continue


# Início do programa
cliente = Cliente()
conta = Conta()
menu = MenuPrincipal(cliente, conta)
menu.menu()
