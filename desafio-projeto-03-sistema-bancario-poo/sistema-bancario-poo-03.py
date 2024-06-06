'''DESAFIO DE PROJETO 03
Modelando um Sistema Bancário em POO com Python
Módulo: Orientação a Objetos e Boas Práticas em Python
Bootcamp: Python AI Backend Developer
Conclusão do Desafio: Em andamento
Objetivo no README
'''

import re
from datetime import datetime as dt


# Formata o título das seções
def titulo(t):
    traco = '-'
    print(f"{traco * 30}")
    print(f'{t.center(30, " ")}')
    print(f"{traco * 30}")


class Validacao:

    @staticmethod
    def validar_cpf(cpf, clientes):
        if len(cpf) != 11 or not cpf.isdigit():
            raise ValueError("CPF inválido. O CPF deve ter 11 dígitos.")

        for cliente in clientes:
            if cliente["cpf"] == cpf:
                raise ValueError("CPF já cadastrado.")
        return True

    @staticmethod
    def validar_estado(estado):
        if not re.match(r'^[A-Z]{2}$', estado):
            raise ValueError("Estado inválido. Digite a sigla do estado.")

    @staticmethod
    def verificar_se_conta_existe(numero_conta, contas):
        for conta in contas:
            if conta._numero_conta == numero_conta:
                return True

        return False


class Cliente:
    def __init__(self, tipo_cliente=None, endereco=None, email=None,
                 telefone=None):
        self._tipo_cliente = tipo_cliente
        self._endereco = endereco
        self._email = email
        self._telefone = telefone
        self._clientes = []

    def cadastrar_cliente(self):
        while True:
            opcao_tipo_cliente = int(input('''
            Tipo de Cliente:
            [1] Pessoa Física,
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
    def __init__(self, nome_completo=None, cpf=None, endereco=None,
                 email=None, telefone=None):
        super().__init__(endereco=endereco, email=email,
                         telefone=telefone, tipo_cliente='Pessoa Física')
        self._nome_completo = nome_completo if nome_completo is not None else ''
        self._cpf = cpf if cpf is not None else ''

    def cadastrar_pessoa_fisica(self):
        self._nome_completo = input("Nome completo: ")
        self._cpf = input("CPF: ")
        Validacao.validar_cpf(self._cpf, self._clientes)
        _logradouro = input("Logradouro: ")
        _numero = input("Número: ")
        _bairro = input("Bairro: ")
        _cidade = input("Cidade: ")
        _estado = input("Estado: ").upper()
        Validacao.validar_estado(_estado)
        self._endereco = f'{
                        _logradouro}, {_numero}-{_bairro}-{
                            _cidade}/{_estado}'
        self._email = input("E-mail: ")
        self._telefone = input("Telefone: ")

        cliente = {
            'tipo_cliente': self._tipo_cliente,
            'nome_completo': self._nome_completo,
            'cpf': self._cpf,
            'endereco': self._endereco,
            'email': self._email,
            'telefone': self._telefone
            }

        self._clientes.append(cliente)

        return cliente


class PessoaJuridica(Cliente):
    def __init__(self, *, cnpj=None, razao_social=None, tipo_cliente=None,
                 endereco=None, email=None, telefone=None):
        super().__init__(tipo_cliente=tipo_cliente, endereco=endereco,
                         email=email, telefone=telefone)
        self._cnpj = cnpj
        self._razao_social = razao_social

    def cadastrar_pessoa_juridica(self):
        self._razao_social = input("Razão Social: ")
        self._cnpj = input("CNPJ: ")
        _logradouro = input("Logradouro (comercial): ")
        _numero = input("Número: ")
        _bairro = input("Bairro: ")
        _cidade = input("Cidade: ")
        _estado = input("Estado: ").upper()
        Validacao.validar_estado(_estado)
        self._endereco = f'{
                        _logradouro}, {_numero}-{_bairro}-{
                            _cidade}/{_estado}'
        self._email = input("E-mail: ")
        self._telefone = input("Telefone: ")

        cliente = {
            'cnpj': self._cnpj,
            'razao_social': self._razao_social,
            'endereco': self._endereco,
            'email': self._email,
            'telefone': self._telefone,
            'tipo_cliente': self._tipo_cliente
            }

        self.clientes.append(cliente)

        return cliente


class Mei(Cliente):
    def __init__(self, *, cnpj=None, cpf=None, nome_completo=None,
                 tipo_cliente=None, endereco=None, email=None, telefone=None):
        super().__init__(tipo_cliente=tipo_cliente, endereco=endereco,
                         email=email, telefone=telefone)
        self._cnpj = cnpj
        self.cpf = cpf
        self.nome_completo = nome_completo

    def cadastrar_mei(self):
        self._cnpj = input("CNPJ: ")
        self._cpf = input("CPF: ")
        self._nome_completo = input("Nome completo: ")
        _logradouro = input("Logradouro (comercial): ")
        _numero = input("Número: ")
        _bairro = input("Bairro: ")
        _cidade = input("Cidade: ")
        _estado = input("Estado: ").upper()
        self._endereco = f'{
                        _logradouro}, {_numero}-{_bairro}-{
                            _cidade}/{_estado}'
        self._email = input("E-mail: ")
        self._telefone = input("Telefone: ")

        cliente = {
            'cnpj': self._cnpj,
            'nome_completo': self._nome_completo,
            'cpf': self._cpf,
            'endereco': self._endereco,
            'email': self._email,
            'telefone': self._telefone
        }

        self.clientes.append(cliente)

        return cliente


class Extrato:

    def adicionar_deposito_ao_extrato():
        pass


class Conta:
    def __init__(self, numero_conta=None, agencia=1, saldo_inicial=0.0):
        self._agencia = agencia
        self._saldo = saldo_inicial
        self._numero_conta = numero_conta
        self._operacoes = []
        self._contas = []

    def abrir_conta(self):
        titulo('Abertura de Conta')
        while True:
            try:
                cpf = int(input("Informe o CPF do titular da conta: "))
                Validacao.validar_cpf(cpf, Cliente.clientes)
                self._numero_conta += 1
                conta = {'cpf': cpf,
                         'agencia': self._agencia,
                         'numero_conta': self._numero_conta}
                self._contas.append(conta)
                print('Conta {self._numero_conta} aberta com sucesso para o cliente cpf {cpf}')
            except ValueError as exc:
                print(f'Erro: {exc}')

    def depositar(self):
        titulo('Depósito')
        numero_conta = int(input("Informe o número da conta: "))
        if Validacao.verificar_se_conta_existe(numero_conta, contas):
            valor = float(input('Valor do depósito: R$ '))
            if valor > 0:
                self._saldo += valor
                self._data = dt.datetime.now().strftime("%Y-%m-%d %I:%M:%S")
                operacao = {'operacao': 'Depósito',
                            'data': self._data,
                            'valor': valor}
                self._operacoes.append(operacao)
                print(f'Depósito de R$ {valor:.2f} realizado com sucesso na conta {numero_conta}.')
            else:
                print('O valor do depósito deve ser positivo.')
        else:
            print('Conta não localizada. Verifique o número e tente novamente.')


class Menu_Principal:

    def __init__(self):
        self.clientes = Cliente()
        self.contas = Conta()
        self.menu()

    def menu(self):
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
        while True:
            try:
                match opcao:
                    case 1:
                        self.contas.depositar()
                        self.menu(self)
                    case 2:
                        pass
                        # sacar()
                    case 3:
                        pass
                        # visualizar_extrato()
                    case 4:
                        Cliente.cadastrar_cliente(self)
                        print('Cliente cadastrado com sucesso.')
                        self.menu()
                    case 5:
                        Conta.abrir_conta(self)
                    case 6:
                        pass
                        # listar_clientes()
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
menu = Menu_Principal()
