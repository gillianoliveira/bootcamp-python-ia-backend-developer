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
