'''DESAFIO DE PROJETO 03
Modelando um Sistema Bancário em POO com Python
Módulo: Orientação a Objetos e Boas Práticas em Python
Bootcamp: Python AI Backend Developer
Conclusão do Desafio: Em andamento
Objetivo no README
'''


# Formata o título das seções
def titulo(t):
    traco = '-'
    print(f"{traco * 30}")
    print(f'{t.center(30, " ")}')
    print(f"{traco * 30}")


class Cliente:
    def __init__(self, endereco, telefone, email, tipo_cliente):
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self.tipo_cliente = tipo_cliente
        self.contas = []

    def cadastrar_cliente(self):
        while True:
            tipo_cliente = int(input('''
            Tipo de Cliente:
            [1] Pessoa Física,
            [2] Pessoa Jurídica
            [3] Microempreendedor
            Opção escolhida: '''))
            if tipo_cliente == 1:
                self.cpf = int(input('CPF: '))
                self.nome_completo = input("Nome Completo: ")
                self.data_nascimento = input("Data de Nascimento: ")
                self.telefone = input('Telefone: ')
                self.email = input("E-mail: ")
                self.logradouro = input("Logradouro: ")
                self.numero = input("Número: ")
                self.bairro = input("Bairro: ")
                self.cidade = input("Cidade: ")
                self.estado = input("Estado: ").upper()
                endereco = f'{self.logradouro}, {self.numero}-{self.bairro}-{self.cidade}/{self.estado}'
                cliente = {
                    'cpf': self.cpf,
                    'nome_completo': self.nome_completo,
                    'data_nascimento': self.data_nascimento,
                    'endereco': self.endereco,
                    'telefone': self.telefone,
                    'email': self.email
                }
                cliente.append(cliente)
                break
            elif tipo_cliente == 2:
                self.cnpj = int(input("CNPJ: "))
                self.nome_fantasia = input("Nome Fantasia: ")
                self.razao_social = input("Razão Social: ")
                self.representante_legal = input("Representante Legal: ")
                self.cpf_representante_legal = int(input("CPF do Representante Legal: "))
                self.data_abertura = input("Representante Legal: ")
                self.telefone = int(input("Telefone comercial: "))
                self.email = input("E-mail corporativo: ")
                self.logradouro = input("Logradouro: ")
                self.numero = input("Número: ")
                self.bairro = input("Bairro: ")
                self.cidade = input("Cidade: ")
                self.estado = input("Estado: ").upper()
                endereco = f'{self.logradouro}, {self.numero}-{self.bairro}-{self.cidade}/{self.estado}'
                cliente = {
                    'cnpj': self.cnpj,
                    'nome_fantasia': self.nome_fantasia,
                    'razao_social': self.razao_social,
                    'representante_legal': self.representante_legal,
                    'cpf_representante_legal': self.cpf_representante_legal,
                    'data_abertura': self.data_abertura,
                    'telefone': self.telefone,
                    'email': self.email,
                    'endereco': endereco}
            elif tipo_cliente == 3:
                self.cnpj = int(input("CNPJ: "))
                self.cpf = int(input('CPF: '))
                self.nome_completo = input("Nome Completo do Cliente: ")
                self.data_nascimento = input("Data de Nascimento: ")
                self.telefone = int(input("Telefone: "))
                self.email = input("E-mail: ")
                self.razao_social = input("Razão Social: ")
                self.logradouro = input("Logradouro (comercial): ")
                self.numero = input("Número: ")
                self.bairro = input("Bairro: ")
                self.cidade = input("Cidade: ")
                self.estado = input("Estado: ").upper()
                endereco = f'{self.logradouro}, {self.numero}-{self.bairro}-{self.cidade}/{self.estado}'
                cliente = {
                    'cnpj': self.cnpj,
                    'cpf': self.cpf,
                    'nome_completo': self.nome_completo,
                    'data_nascimento': self.data_nascimento,
                    'razao_social': self.razao_social,
                    'endereco': self.endereco,
                    'telefone': self.telefone,
                    'email': self.email
                }
            else:
                print("Opção inválida. Programa encerrado.")
                break

    def exibir_cadastro_cliente(self):
        pass


class PessoaFisica(Cliente):
    def __init__(self, *, endereco, telefone, email, tipo_cliente, cpf,
                 nome_completo, data_nascimento):
        super().__init__(endereco=endereco, telefone=telefone,
                         email=email, tipo_cliente=tipo_cliente)
        self.cpf = cpf
        self.nome_completo = nome_completo
        self.data_nascimento = data_nascimento

    def cadastrar_cliente(self):
        pass


class Conta:
    pass


class Menu_Principal:

    def __init__(self):
        self.cliente = Cliente()
        self.conta = Conta()
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
                pass
                # cadastrar_cliente()
            case 5:
                pass
                # abrir_conta()
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


# Início do programa
menu = Menu_Principal()


