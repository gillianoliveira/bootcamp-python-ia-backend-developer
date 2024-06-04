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
                cpf = int(input('CPF: '))
                nome_completo = input("Nome Completo: ")
                data_nascimento = input("Data de Nascimento: ")
                telefone = input('Telefone: ')
                email = input("E-mail: ")
                logradouro = input("Logradouro: ")
                numero = input("Número: ")
                bairro = input("Bairro: ")
                cidade = input("Cidade: ")
                estado = input("Estado: ").upper()
                endereco = f'{logradouro}, {numero}-{bairro}-{cidade}/{estado}'
                cliente = {
                    'cpf': cpf,
                    'nome_completo': nome_completo,
                    'data_nascimento': data_nascimento,
                    'endereco': endereco,
                    'telefone': telefone,
                    'email': email
                }
                cliente.append(cliente)
                break
            elif tipo_cliente == 2:
                cnpj = int(input("CNPJ: "))
                nome_fantasia = input("Nome Fantasia: ")
                razao_social = input("Razão Social: ")
                representante_legal = input("Representante Legal: ")
                cpf_representante_legal = int(input("CPF do Representante Legal: "))
                data_abertura = input("Representante Legal: ")
                telefone = int(input("Telefone comercial: "))
                email = input("E-mail corporativo: ")
                logradouro = input("Logradouro: ")
                numero = input("Número: ")
                bairro = input("Bairro: ")
                cidade = input("Cidade: ")
                estado = input("Estado: ").upper()
                endereco = f'{logradouro}, {numero}-{bairro}-{cidade}/{estado}'
                cliente = {
                    'cnpj': cnpj,
                    'nome_fantasia': nome_fantasia,
                    'razao_social': razao_social,
                    'representante_legal': representante_legal,
                    'cpf_representante_legal': cpf_representante_legal,
                    'data_abertura': data_abertura,
                    'telefone': telefone,
                    'email': email,
                    'endereco': endereco}
            elif tipo_cliente == 3:
                cnpj = int(input("CNPJ: "))
                cpf = int(input('CPF: '))
                nome_completo = input("Nome Completo do Cliente: ")
                data_nascimento = input("Data de Nascimento: ")
                telefone = int(input("Telefone: "))
                email = input("E-mail: ")
                razao_social = input("Razão Social: ")
                logradouro = input("Logradouro (comercial): ")
                numero = input("Número: ")
                bairro = input("Bairro: ")
                cidade = input("Cidade: ")
                estado = input("Estado: ").upper()
                endereco = f'{logradouro}, {numero}-{bairro}-{cidade}/{estado}'
                cliente = {
                    'cnpj': cnpj,
                    'cpf': cpf,
                    'nome_completo': nome_completo,
                    'data_nascimento': data_nascimento,
                    'razao_social': razao_social,
                    'endereco': endereco,
                    'telefone': telefone,
                    'email': email
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


