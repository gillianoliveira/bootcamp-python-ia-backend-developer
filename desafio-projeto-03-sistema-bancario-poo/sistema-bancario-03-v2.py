

# Formata o título das seções
def titulo(t):
    traco = '-'
    print(f"{traco * 30}")
    print(f'{t.center(30, " ")}')
    print(f"{traco * 30}")


class Validacao:

    @staticmethod
    def validar_cpf(cpf, clientes):
        if len(str(cpf)) != 11:
            raise ValueError("CPF inválido. O CPF deve ter 11 dígitos.")

        for cliente in clientes:
            if int(cliente['cpf']) == cpf:
                raise ValueError("CPF já cadastrado.")

        return True


class Cliente:
    def __init__(self, tipo_cliente=None, endereco=None, telefone=None):
        self._tipo_cliente = tipo_cliente
        self._endereco = endereco
        self._telefone = telefone
        self._clientes = []

    def adicionar_cliente(self, cliente):
        self._clientes.append(cliente)

    def visualizar_clientes(self):
        for cliente in self._clientes:
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
                cliente = PessoaFisica().cadastrar_pessoa_fisica()
            elif opcao_tipo_cliente == 2:
                cliente = PessoaJuridica().cadastrar_pessoa_juridica()
            elif opcao_tipo_cliente == 3:
                cliente = Mei().cadastrar_mei()
            else:
                print('Opção inválida.')
                continue
            return cliente


class PessoaFisica(Cliente):
    def __init__(self, tipo_cliente=None, endereco=None, telefone=None,
                 nome=None, cpf=None, data_nascimento=None, email=None):
        super().__init__(tipo_cliente, endereco, telefone)
        self._tipo_cliente = tipo_cliente
        self._endereco = endereco
        self._telefone = telefone
        self._nome = nome
        self._cpf = cpf
        self._data_nascimento = data_nascimento
        self._email = email

    def cadastrar_pessoa_fisica(self):
        while True:
            cpf = input("CPF: ")
            Validacao.validar_cpf(cpf, cliente._clientes)
            nome = input("Nome: ")
            logradouro = input("Logradouro: ")
            numero = input("Número ")




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
                        pass
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
