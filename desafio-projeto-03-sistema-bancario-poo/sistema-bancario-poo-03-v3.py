# DESAFIO DE PROJETO
# Criando um Sistema Bancário com Python - parte 3
# Módulo: Dominando Python e suas Estruturas de Dados
# Bootcamp: Python AI Backend Developer Bootcamp
# Conclusão: em desenvolvimento

import re
#from abc import ABC, abstractmethod


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
                if cliente['cpf'] == cpf:
                    raise ValueError("O CPF já está cadastrado.")
        else:
            return False


class Cliente():
    __clientes = []

    def __init__(self, endereco=None, telefone=None):
        self.endereco = endereco
        self.telefone = telefone
        # self._conta = Conta()
        # self._transacao = Transacao()

    def cadastrar_cliente(self):
        Estilo.titulo('Cadastro de Clientes')
        cliente = PessoaFisica.cadastro_pessoa_fisica()
        Cliente.__clientes.append(cliente)
        print('Cadastro realizado com sucesso.')

    def listar_clientes(self):
        for cliente in Cliente.__clientes:
            print(cliente)

    def realizar_transacao(self):
        pass

    def adicionar_conta(self):
        pass


class PessoaFisica(Cliente):

    def __init__(self, cpf=None, nome=None, data_nascimento=None,
                 endereco=None, telefone=None):
        super().__init__(endereco, telefone)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

    @staticmethod
    def cadastro_pessoa_fisica():
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


class MenuPrincipal:
    def __init__(self, cliente):
        self._cliente = cliente

    def menu(self):
        while True:
            Estilo.titulo('Menu')
            opcao = int(input('''
        [1] Cadastrar Cliente
        [2] Listar Clientes
        [8] Sair
        Opção escolhida: '''))
            try:
                match opcao:
                    case 1:
                        cliente.cadastrar_cliente()
                    case 2:
                        cliente.listar_clientes()
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
iniciar = MenuPrincipal(cliente)
iniciar.menu()
