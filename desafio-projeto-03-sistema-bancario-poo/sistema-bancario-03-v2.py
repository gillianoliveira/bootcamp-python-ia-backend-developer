

# Formata o título das seções
def titulo(t):
    traco = '-'
    print(f"{traco * 30}")
    print(f'{t.center(30, " ")}')
    print(f"{traco * 30}")


class MenuPrincipal:
    def __init__(self):
        pass

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
                        pass
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
menu = MenuPrincipal()
menu.menu()
