'''
DESAFIO DE PROJETO
Criando um Sistema Bancário com Python
Módulo: Dominando Python e suas Estruturas de Dados	
Bootcamp: Python AI Backend Developer Bootcamp
Conclusão do Desafio: ?
Proposta no README
'''
# Função consmética para gerar o título de cada seção
def titulo(t):
    traco = '-'
    print(traco * 30)
    print(f"{t.center(30, ' ')}")
    print(traco * 30)

def depositar():
    pass

def sacar():
    pass

def visualizar_extrato():
    pass

def cadastrar_cliente():
    global clientes
    while True:
        # Solicitar o cpf
        cpf = int(input("CPF: "))
        
        # Verificar a quantidade de dígitos do cpf
        if len(str(cpf)) != 11:
            print('O CPF deve ter 11 dígitos. Digite novamente. ')
            continue
        
        # Verificar se o cpf já está cadastrado
        for cliente in clientes:
            if cliente["cpf"] == cpf:
                print('Cliente já cadastrado.')
                menu()
                return
            else:
                nome = input('Nome completo: ')
                data_nascimento = input('Data de nascimento: ')
                logradouro = input('Digite o logradouro: ')
                numero = input('Digite o número: ')
                bairro = input('Bairro: ')
                cidade = input('Cidade: ')
                estado = input('Sigla do estado: ')
        
        # Armazenar os dados do cliente
        clientes.append({"cpf": cpf, "nome": nome, "data_nascimento": data_nascimento, "logradouro": logradouro, "numero":numero, "bairro": bairro, "cidade":cidade, "estado":estado})
        
def criar_conta():
    pass

# Função principal que chama todas as outras
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
            depositar()
        case 2:
            sacar()
        case 3:
            visualizar_extrato()
        case 4:
            cadastrar_cliente()
        case 5:
            criar_conta()
        case 6:
            print("Sair")
        case _:
            print('Opção inválida')

# Variáveis Globais
clientes = []

# Entrada do Programa
titulo('Menu')
menu()

