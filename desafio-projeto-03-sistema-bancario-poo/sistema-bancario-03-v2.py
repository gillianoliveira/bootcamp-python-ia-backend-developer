
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

    def __init__(self, tipo_cliente=None, endereco=None, telefone=None):
        self._tipo_cliente = tipo_cliente
        self._endereco = endereco
        self._telefone = telefone

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
            opcao_tipo_cliente = int(input('''
            Tipo de Cliente:
            [1] Pessoa Física
            [2] Pessoa Jurídica
            [3] Microempreendedor
            Opção escolhida: '''))
            if opcao_tipo_cliente == 1:
                cliente = PessoaFisica(self._clientes).cadastrar_pessoa_fisica()
            elif opcao_tipo_cliente == 2:
                cliente = PessoaJuridica().cadastrar_pessoa_juridica()
            elif opcao_tipo_cliente == 3:
                cliente = Mei().cadastrar_mei()
            else:
                print('Opção inválida.')
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
                Validacao.validar_uf(estado)
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


class PessoaJuridica:
    pass


class Mei:
    pass


class MenuPrincipal:
    def __init__(self, cliente):
        self._cliente = cliente

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
                        pass
                    case 6:
                        self._cliente.visualizar_clientes()
                    case 7:
                        pass
                        # listar_contas()
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
menu = MenuPrincipal(cliente)
menu.menu()
