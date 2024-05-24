'''
DESAFIO DE PROJETO
Criando um Sistema Bancário com Python
Módulo: Dominando Python e suas Estruturas de Dados	
Bootcamp: Python AI Backend Developer Bootcamp
Conclusão do Desafio: ?
Proposta no README
'''

def titulo(t):
    traco = '-'
    print(traco * 30)
    print(f"{t.center(30, ' ')}")
    print(traco * 30)


def menu():
    opcao_menu = int(input('''
    [1] Depositar
    [2] Sacar
    [3] Visualizar Extrato
    [4] Cadastrar Usuário
    [5] Criar nova conta
    [6] Sair
    Opção escolhida: '''))
    
    match opcao_menu:
        case 1:
            print("Depositar")
        case 2:
            print("Sacar")
        case 3:
            print("Visualisar extrato")
        case 4:
            print("Cadastrar Usuário")
        case 5:
            print("Cadastrar Nova Conta")
        case 6:
            print("Sair")
        case _:
            print('Opção inválida')
    
    



# Entrada do Programa
titulo('Menu')
menu()
