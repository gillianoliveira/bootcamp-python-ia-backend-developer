import datetime as dt


# Formata o título das seções
def titulo(t):
    traco = '-'
    print(f"{traco * 30}")
    print(f'{t.center(30, " ")}')
    print(f"{traco * 30}")


class Validacao:

    @staticmethod
    def validar_cpf_cadastro(cpf, clientes):
        if len(cpf) != 11 or not cpf.isdigit():
            raise ValueError("CPF inválido. O CPF deve ter 11 dígitos.")

        for cliente in clientes:
            if cliente['cpf'] == cpf:
                raise ValueError("CPF já cadastrado.")

        return True

    @staticmethod
    def validar_cpf_existente(cpf, clientes):
        if len(cpf) != 11 or not cpf.isdigit():
            raise ValueError("CPF inválido. O CPD deve ter 11 dígitos.")

        for cliente in clientes:
            if cliente['cpf'] == cpf:
                return True

        raise ValueError("CPF não encontrado. Por favor, cadastre o cliente antes.")


class Cliente:
    # Lista de clientes
    _clientes = []

    def __init__(self, endereco=None, telefone=None, conta=None):
        self._endereco = endereco
        self._telefone = telefone
        self._conta = conta

    @classmethod
    def adicionar_cliente(cls, cliente):
        """Adiciona o dicionário cliente a lista de clientes"""
        cls._clientes.append(cliente)
        print("Cliente cadastrado com sucesso.")

    @classmethod
    def visualizar_clientes(cls):
        """Exibe a lista de clientes. Se vazia exibe mensagem informando."""
        if not cls._clientes:
            print("Nenhum cliente cadastrado.")
        for cliente in cls._clientes:
            print(cliente)

    @classmethod
    def obter_clientes(cls):
        return cls._clientes

    def cadastrar_cliente(self):
        """Chama o método que cadastra os dados informados pelo cliente."""
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
        self._endereco = None
        self._telefone = None
        self._nome = None
        self._cpf = None
        self._data_nascimento = None
        self._email = None

    def cadastrar_pessoa_fisica(self):
        """
        Cria um dicionário com os dados informados pelo cliente e chama o
        método que o adiciona a lista de clientes.
        """
        while True:
            try:
                cpf = input("CPF: ")
                Validacao.validar_cpf_cadastro(cpf, Cliente.obter_clientes())
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
                    'nome': self._nome,
                    'data_nascimento': self._data_nascimento,
                    'cpf': cpf,
                    'endereco': self._endereco,
                    'email': self._email,
                    'telefone': self._telefone
                }
                Cliente.adicionar_cliente(cliente)
                break
            except ValueError as exc:
                print(f'Erro ao cadastrar cliente: {exc}')
                print('Por favor, tente novamente.')
                continue


class Extrato:
    pass


class Conta:
    _contas = []
    numero_conta = 1

    def __init__(self, clientes):
        self._saldo = 0.0
        self._agencia = "0001"
        self._numero_conta = None
        self._titulares = []
        self._clientes = clientes

    def adicionar_titular(self, titular):
        self._titulares.append(titular)

    @classmethod
    def gerador_numero_conta(cls):
        numero = cls.numero_conta
        cls.numero_conta += 1
        return numero

    @staticmethod
    def data_da_operacao():
        data = dt.datetime.now().strftime("%Y-%m-%d %I:%M:%S")
        return data

    @staticmethod
    def tipo_conta(tipo):
        tipos_conta = {
            1: 'Conta-corrente pessoa física',
            2: 'Conta-corrente corporativa',
            3: 'Conta-corrente conjunta',
            4: 'Conta-poupança pessoa física'
        }
        return tipos_conta.get(tipo, 'Tipo de conta inválido.')

    # @staticmethod
    # def tipo_conta(tipo_conta):
    #     if tipo_conta == 1:
    #         return 'Conta-corrente pessoa física'
    #     elif tipo_conta == 2:
    #         return 'Conta-corrente corporativa'
    #     elif tipo_conta == 3:
    #         return 'Conta-corrente conjunta'
    #     elif tipo_conta == 4:
    #         return 'Conta-poupança pessoa física'

    def abertura_conta(self):
        titulo('Abertura de Conta')
        while True:
            try:
                cpf = input("CPF do Titular ou Responsável: ")
                Validacao.validar_cpf_existente(cpf, self._clientes)
                self._titulares = cpf
                tipo_conta_input = int(input('''
                Tipo de conta:
                [1] Conta-corrente pessoa física
                [2] Conta-corrente corporativa
                [3] Conta-corrente conjunta
                [4] Conta-poupança pessoa física
                Opção escolhida: '''))
                if tipo_conta_input not in [1, 2, 3, 4]:
                    print('Opção inválida.')
                    continue
                if tipo_conta_input == 1:
                    self._numero_conta = Conta.gerador_numero_conta()
                    data = Conta.data_da_operacao()
                    #tipo_conta = Conta.tipo_conta(tipo_conta_input)
                    conta = {
                        'tipo_conta': self._tipo_conta,
                        'data': data,
                        'agencia': self._agencia,
                        'numero_conta': self._numero_conta,
                        'cpf_titular':  self._titulares
                    }
                    if 'contas' not in self._clientes[cpf]:
                        self._clientes[cpf]['contas'] = []
                    self._clientes[cpf]['contas'].appeend(conta)

                    self._contas.append(conta)
                    print(f'Conta {self._numero_conta} aberta com sucesso.')
                    return conta
                # elif tipo_conta == 2:
                #     print("Em constr")
                # elif tipo_conta == 2:
                #     print("Conta-corrente conjunta")
                # elif tipo_conta == 3:
                #     print("Conta-poupança pessoa física")
                break
            except ValueError as exc:
                print(f'Erro ao abrir conta: {exc}')
                print("Por favor, tente novamente.")
                continue


class MenuPrincipal:
    def __init__(self, cliente, conta):
        self._cliente = cliente
        self._conta = conta

    def menu(self):
        """Método principal que chama os demais."""
        while True:
            titulo('Menu')
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
conta = Conta(Cliente.obter_clientes())
menu = MenuPrincipal(cliente, conta)
menu.menu()
