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
    def __init__(self, *, tipo_cliente=None, endereco=None, email=None,
                 telefone=None):
        self._tipo_cliente = tipo_cliente if tipo_cliente is not None else ''
        self._endereco = endereco if endereco is not None else ''
        self._email = email if email is not None else ''
        self._telefone = telefone if telefone is not None else ''
        self.clientes = []

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

            self.clientes.append(cliente)
            break


class PessoaFisica(Cliente):
    def __init__(self, nome=None, cpf=None, endereco=None,
                 email=None, telefone=None):
        super().__init__(endereco=endereco, email=email,
                         telefone=telefone, tipo_cliente='Pessoa Física')
        self._nome = nome if nome is not None else ''
        self._cpf = cpf if cpf is not None else ''

    def cadastrar_pessoa_fisica(self):
        self._nome = input("Nome: ")
        self._cpf = input("CPF: ")
        _logradouro = input("Logradouro: ")
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
            'tipo_cliente': self._tipo_cliente,
            'nome': self._nome,
            'cpf': self._cpf,
            'endereco': self._endereco,
            'email': self._email,
            'telefone': self._telefone
            }

        self.clientes.append(cliente)

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
    pass



class Menu_Principal:

    def __init__(self):
        self.cliente = Cliente()
        # self.conta = Conta()
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
                self.cliente.cadastrar_cliente()
                print('Cliente cadastrado.')
                self.menu()
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
