# DESAFIO DE PROJETO
# Criando um Sistema Bancário com Python - parte 3
# Módulo: Dominando Python e suas Estruturas de Dados
# Bootcamp: Python AI Backend Developer Bootcamp
# Conclusão: em desenvolvimento
from abc import ABC, abstractmethod
from datetime import datetime


class Estilo:

    @staticmethod
    def titulo(t):
        print("-" * 30)
        print(f'{t.center(30, " ")}')
        print("-" * 30)


class Validacao:

    @staticmethod
    def verifica_cpf_cadastro(cpf):
        if len(cpf) != 11 or not cpf.isdigit():
            raise ValueError("CPF inválido. O CPF deve ter 11 dígitos.")
        lista_clientes = Cliente.obter_clientes()
        for cliente in lista_clientes:
            if cliente.cpf == cpf:
                raise ValueError("CPF já cadastrado.")
        return True

    @staticmethod
    def verifica_cpf_abertura_conta(cpf):
        if len(cpf) != 11 or not cpf.isdigit():
            raise ValueError("CPF inválido. O CPF deve ter 11 dígitos.")
        lista_clientes = Cliente.obter_clientes()
        for cliente in lista_clientes:
            if cliente.cpf == cpf:
                return True
        print('CPF não cadastrado.')
        return False

    @staticmethod
    def verifica_se_conta_existe(conta):
        contas = Conta.listar_contas()
        if contas is None:
            print("Nenhuma conta cadastrada.")
            return False
        for conta in contas:
            if conta.numero == conta:
                return True
            return False


class Cliente:

    __clientes = []

    def __init__(self, endereco=None, telefone=None):
        self.__endereco = endereco
        self.__telefone = telefone
        self.__contas = []

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
    def obter_cliente_por_cpf(cls, cpf):
        lista_clientes = cls.obter_clientes()
        for cliente in lista_clientes:
            if cliente.cpf == cpf:
                return cliente
        return None

    @classmethod
    def adicionar_clientes_lista(cls, cliente):
        cls.__clientes.append(cliente)

    @classmethod
    def exibir_lista_clientes(cls):
        clientes = Cliente.obter_clientes()
        for pessoa_fisica in clientes:
            print(f"""
        Nome completo:{pessoa_fisica.nome}
        CPF: {pessoa_fisica.cpf}
        Data de nascimento: {pessoa_fisica.data_de_nascimento}
        Telefone: {pessoa_fisica.telefone}
        Endereço: {pessoa_fisica.endereco}""")

    @classmethod
    def cadastrar_cliente(cls):
        try:
            cliente = PessoaFisica()
            cliente.cadastrar_cliente()
            cls.adicionar_clientes_lista(cliente)
        except ValueError as ve:
            print(f'Erro: {ve}')

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.__contas.append(conta)

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
        Validacao.verifica_cpf_cadastro(cpf)
        self.__cpf = cpf

    @data_de_nascimento.setter
    def data_de_nascimento(self, data_de_nascimento):
        # TODO: Formatar a data para dd/mm/aaaa. Atual: 2000-09-28 00:00:00
        dt_data_de_nascimento = datetime.strptime(data_de_nascimento, "%d/%m/%Y")
        self.__data_de_nascimento = dt_data_de_nascimento

    def cadastrar_cliente(self):
        self.cpf = input("CPF: ")
        self.nome = input("Nome Completo: ")
        self.data_de_nascimento = input("Data de Nascimento: ")
        self.telefone = input("Telefone: ")
        self.endereco = input("Endereço: ")
        return self


class Conta:

    contador = 0
    __contas = []

    def __init__(self, numero=None, agencia="001", saldo=0) -> None:
        self.__agencia = agencia
        self.__numero = Conta.contador
        self.__saldo = saldo
        self.__cliente = None
        self.__historico = Historico()
        Conta.contador += 1

    @property
    def numero(self):
        return self.__numero

    @property
    def agencia(self):
        return self.__agencia

    @property
    def saldo(self):
        return self.__saldo

    @property
    def cliente(self):
        return self.__cliente

    @property
    def historico(self):
        return self.__historico

    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    @classmethod
    def nova_conta(cls):
        conta_corrente = ContaCorrente()
        return conta_corrente.nova_conta()

    @classmethod
    def adicionar_conta(cls, conta):
        cls.__contas.append(conta)

    @classmethod
    def obter_contas(cls):
        return cls.__contas

    @classmethod
    def listar_contas(cls):
        contas = cls.obter_contas()
        if not contas:
            return "Nenuma conta cadastada."
        for conta in contas:
            print(conta)
        return False
    # @classmethod
    # def listar_contas(cls):
    #     for conta in cls.__contas:
    #         return cls.__contas

    def sacar(self, valor: float):
        saque = Saque(valor, self, self.cliente)
        return saque.regras_saque(valor)

    def depositar(self) -> bool:
        deposito = Deposito(self, self.cliente)
        return deposito.regras_deposito()

    def __str__(self) -> str:
        cliente_cpf = self.cliente.cpf if self.cliente else 'Nenhum cliente associado'
        return f"""
    Dados da Conta:
    agência: {self.agencia}
    conta: {self.numero}
    saldo: {self.saldo}
    cliente: {cliente_cpf}
    """


class ContaCorrente(Conta):

    def __init__(self, numero=None, agencia="001", saldo=0,
                 limite=500, limite_saques=3) -> None:
        super().__init__(numero, agencia, saldo)
        self.__limite = limite
        self.__limite_saques = limite_saques

    def nova_conta(self):
        while True:
            cpf = input('Informe o CPF do titular: ')
            valida_cpf = Validacao.verifica_cpf_abertura_conta(cpf)
            if valida_cpf:
                cliente = Cliente.obter_cliente_por_cpf(cpf)
                if cliente:
                    self.cliente = cliente
                    cliente.adicionar_conta(self)
                    Conta._Conta__contas.append(self)
                    return self
                else:
                    print('Erro ao obter cliete.')
            else:
                break

    def sacar(self, valor):
        pass


class Transacao(ABC):

    @abstractmethod
    def registrar(self, conta):
        pass


class Deposito(Transacao):

    def __init__(self, conta, cliente) -> None:
        super().__init__()
        self.__cliente = cliente
        self.__conta = conta

    def regras_deposito(self) -> bool:
        numero_conta = input("Informe o número da conta: ")
        Validacao.verifica_se_conta_existe(numero_conta)
        conta_valida = conta
        if conta_valida:
            valor = float(input("Informe o valor: R$ "))
            if valor > 0:
                conta_valida.saldo += valor
                print("Depósito efetuado.")
                return True
            else:
                print("Operação não realizada. Valor inválido.")
        else:
            print('Conta não localizada.')
        return False

    def registrar(self):
        if self.regras_deposito() != False:
            



class Saque(Transacao):
    def __init__(self, valor, conta, cliente) -> None:
        super().__init__()
        self.__valor = valor
        self.__conta = conta
        self.__cliente = cliente

    def regras_saque(self, valor: float) -> bool:
        while True:
            numero_conta = input("Informe o número da conta: ")
            Validacao.verifica_se_conta_existe(numero_conta)
            self.__valor = float(input("Informe o valor: R$ "))
            if self.__conta.saldo >= self.__valor:
                return True
            elif conta.__saldo <= 0:
                print('Operação não realizada. Saldo insuficiente.')
            elif valor <= 0:
                print('Operação não realizada. Valor inválido')
            return False

    def registrar(self, conta):
        return super().registrar(conta)


class Historico:

    def __init__(self) -> None:
        self.__transacoes = []


class MenuPrincipal:
    def __init__(self, cliente, conta):
        self._cliente = cliente
        self._conta = conta

    def menu(self):
        """Menu principal da aplição que chama as demais funcionalidades."""
        while True:
            Estilo.titulo("Menu")
            opcao = int(input("""
        [1] Abertura de Conta
        [2] Cadastrar Cliente
        [3] Depositar
        [4] Listar Clientes
        [5] Listar Contas
        [6] Sacar
        [7] Visualizar Extrato
        [8] Visualizar Saldo
        [9] Sair
        Opção escolhida: """))
            match opcao:
                case 1:
                    Estilo.titulo('Abertura de Conta')
                    nova_conta = self._conta.nova_conta()
                    print(nova_conta)
                case 2:
                    Estilo.titulo('Cadastro de Clientes')
                    self._cliente.cadastrar_cliente()
                case 3:
                    Estilo.titulo('Depósito')
                    self._conta.depositar()
                case 4:
                    Estilo.titulo('Lista de Clientes')
                    self._cliente.exibir_lista_clientes()
                case 5:
                    Estilo.titulo('Lista de Contas')
                    self._conta.listar_contas()
                case 6:
                    Estilo.titulo('Sacar')
                    self._conta.saque()
                case 7:
                    Estilo.titulo('Visualizar Extrato')
                case 8:
                    Estilo.titulo('Visualizar Saldo')
                case 9:
                    Estilo.titulo("Sair")
                    print("Programa encerrado.")
                    exit()
                case _:
                    print("Opção inválida. Programa encerrado.")
                    exit()


cliente = Cliente()
pessoa_fisica = PessoaFisica()
conta = Conta()
iniciar = MenuPrincipal(cliente, conta)
iniciar.menu()
