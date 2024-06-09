

# DESAFIO DE PROJETO
# Criando um Sistema Bancário com Python - parte 3
# Módulo: Dominando Python e suas Estruturas de Dados
# Bootcamp: Python AI Backend Developer Bootcamp
# Conclusão: em desenvolvimento

def titulo(t):
    traco = '-'
    print(f"{traco * 30}")
    print(f'{t.center(30, " ")}')
    print(f"{traco * 30}")


class Cliente(ABC):
    def __init__(self):
        pass
        # self._conta = Conta()
        # self._transacao = Transacao()

    def cadastrar_cliente(self):
        titulo('Cadastro de Clientes')

    def listar_clientes(self):
        titulo('Lista de Clientes')

    def realizar_transacao(self):
        pass

    def adicionar_conta(self):
        pass


class PessoaFisica(Cliente):



class MenuPrincipal:
    def __init__(self, cliente):
        self._cliente = cliente

    def menu(self):
        while True:
            titulo('Menu')
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
                        exit()
            except ValueError as exc:
                print(f'Opção inválida. Erro: {exc}')


cliente = Cliente()
iniciar = MenuPrincipal(cliente)
iniciar.menu()
