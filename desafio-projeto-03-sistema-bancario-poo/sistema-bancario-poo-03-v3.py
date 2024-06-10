# DESAFIO DE PROJETO
# Criando um Sistema Bancário com Python - parte 3
# Módulo: Dominando Python e suas Estruturas de Dados
# Bootcamp: Python AI Backend Developer Bootcamp
# Conclusão: em desenvolvimento

import datetime as dt
import re
# from abc import ABC, abstractmethod


class Estilo:

    @staticmethod
    def titulo(t):
        """
        Estiliza o título da seção.

        Args:
        t (str): Título que vai ser estilizado.
        """
        traco = '-' * 30
        print(f"{traco}")
        print(f'{t.center(30, " ")}')
        print(f"{traco}")


class Validacao:

    def validar_cpf_cadastro(cpf, clientes):
        padrao = r'^(?:\d{3}\.\d{3}\.\d{3}-\d{2}|\d{11})$'
        if re.match(padrao, cpf):
            for cliente in clientes:
                if cliente.cpf == cpf:
                    print("O CPF já está cadastrado.")
                    return False
            return True
        else:
            print("CPF inválido. O CPF deve conter 11 dígitos numéricos.")
            return False


class Historico:
    pass


class Cliente():
    __clientes = []

    def __init__(self, endereco=None, telefone=None):
        self.__endereco = endereco
        self.__telefone = telefone
        # self._conta = Conta()
        # self._transacao = Transacao()

    @classmethod
    def listar_clientes(cls):
        for cliente in cls.__clientes:
            print(f'{cliente}\n')

    @classmethod
    def get_clientes(cls):
        return cls.__clientes

    @property
    def realizar_transacao(self):
        pass

    @property
    def adicionar_conta(self):
        pass

    def cadastrar_cliente(self):
        Estilo.titulo('Cadastro de Clientes')

   

class PessoaFisica(Cliente):

    def __init__(self, cpf=None, nome=None, data_nascimento=None,
                 endereco=None, telefone=None):
        super().__init__(endereco, telefone)
        self.__cpf = cpf
        self.__nome = nome
        self.__data_nascimento = data_nascimento

    def cadastrar_cliente(self):
        while True:
            try:
                cpf = input("CPF: ")
                nome = input("Nome completo: ")
                data_nascimento = input("Data de Nascimento (dd/mm/aaaa): ")
                endereco = input("Endereço (logradouro, nro - bairro - cidade/sigla estado): ")
                telefone = input("Telefone: ")
                cliente = PessoaFisica(cpf=cpf, nome=nome, data_nascimento=data_nascimento, endereco=endereco, telefone=telefone)
                return cliente
            except ValueError as ve:
                print(f'Opção inválida. Erro: {ve}')

    def __str__(self):
        return (f"CPF: {self.cpf}\n"
                f"Nome: {self.nome}\n"
                f"Data de Nascimento: {self.data_nascimento}\n"
                f"Endereço: {self.endereco}\n"
                f"Telefone: {self.telefone}")


class Conta:

    def __init__(self):
        self._saldo = 0.0
        self._cliente = Cliente
        self._historico = Historico
        self._numero = None
        self._agencia = "001"

    @classmethod
    def gerador_numero_conta(cls):
        numero = cls._numero
        cls._numero += 1
        return numero

    def abertura_conta(self):
        Estilo.titulo('Abertura de Conta')
        ContaCorrente.criacao_conta_corrente(self)
        print('Conta criada com sucesso.')

    @classmethod
    def visualizar_contas(cls):
        pass

    @staticmethod
    def data_da_operacao():
        data = dt.datetime.now().strftime("%Y-%m-%d %I:%M:%S")
        return data


class ContaCorrente(Conta):

    def __init__(self, numero: int, agencia: str):
        super().__init__(numero, agencia)
        self._limite = 500.00
        self._limite_saques = 3

    def criacao_conta_corrente(self):
        while True:
            try:
                cpf = input("CPF do Titular ou Responsável: ")
                clientes = Cliente.get_clientes()
                Validacao.validar_cpf_cadastro(cpf, clientes)
                break
            except ValueError as ve:
                print(f'Erro: {ve}')


class MenuPrincipal:
    def __init__(self, cliente, conta):
        self._cliente = cliente
        self._conta = conta

    def menu(self):
        while True:
            Estilo.titulo('Menu')
            opcao = int(input('''
        [1] Abertura de Conta
        [2] Cadastrar Cliente
        [3] Listar Clientes
        [4] Listar Contas
        [8] Sair
        Opção escolhida: '''))
            try:
                match opcao:
                    case 1:
                        conta.abertura_conta()
                    case 2:
                        cliente.cadastrar_cliente()
                    case 3:
                        cliente.listar_clientes()
                    case 4:
                        pass
                    case 8:
                        Estilo.titulo('Sair')
                        print('Programa encerrado.')
                        exit()
                    case _:
                        print('Opção inválida. Programa encerrado.')
                        exit()
            except ValueError as ve:
                print(f'Opção inválida. Erro: {ve}')


cliente = Cliente()
conta = Conta()
iniciar = MenuPrincipal(cliente, conta)
iniciar.menu()
