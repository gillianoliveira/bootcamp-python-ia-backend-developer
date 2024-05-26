'''
DESAFIO DE PROJETO
Criando um Sistema Bancário com Python
Módulo: Dominando Python e suas Estruturas de Dados	
Bootcamp: Python AI Backend Developer Bootcamp
Conclusão do Desafio: ?
Proposta no README
'''

import datetime

# Função consmética para gerar o título de cada seção
def titulo(t):
    traco = '-'
    print(traco * 30)
    print(f"{t.center(30, ' ')}")
    print(traco * 30)

def depositar():
    titulo('Depósito')

def sacar():
    titulo('Saque')

def visualizar_extrato():
    titulo('Extrato')

def cadastrar_cliente():
    titulo('Cadastro de Clientes')
    global clientes
    while True:
        # Solicitar o cpf
        cpf = int(input("CPF: "))
        
        # Verificar a quantidade de dígitos do cpf
        if len(str(cpf)) != 11:
            print('O CPF deve ter 11 dígitos. ')
            menu()
            return
        
        # Verificar se o cpf já está cadastrado
        for cliente in clientes:
            if cliente["cpf"] == cpf:
                print('Cliente já cadastrado.')
                menu()
                return
        
        nome = input('Nome completo: ')
        data_nascimento = input('Data de nascimento(dd/mm/yyyy): ')
        logradouro = input('Logradouro: ')
        numero = input('Número: ')
        bairro = input('Bairro: ')
        cidade = input('Cidade: ')
        estado = input('Sigla do estado: ').capitalize()   
        # Armazenar os dados do cliente
        clientes.append({"cpf": cpf, "nome": nome, "data_nascimento": data_nascimento, "logradouro": logradouro, "numero":numero, "bairro": bairro, "cidade":cidade, "estado":estado})
        print('Cliente cadastrado com sucesso.')
        menu()
        return
    
def criar_conta():
    titulo('Nova Conta')
    global clientes
    global contas   
    global numero_conta
    AGENCIA = '0001'
    
    cpf_titular = int(input('CPF do Titular: '))  # Informe o cpf do titular 
    
    titular_cadastrado = False
    for cliente in clientes:
        if cliente['cpf'] == cpf_titular:
            titular_cadastrado = True
            numero_conta += 1
            conta = {'cpf_titular':cpf_titular,'agencia':AGENCIA,'numero_conta':numero_conta}
            contas.append(conta)
            print('Conta cadastrada com sucesso!')
            menu()
            break
    if not titular_cadastrado:
        print('Você deve fazer o cadastro do titular antes de abrir a conta.')
        menu()
        return
   
def listar_contas():
    titulo('Listar Contas')
    for conta in contas:
        print(conta)

def listar_clientes():
    titulo('Listar Clientes')

def sair():
    print('Programa encerrado.')
    exit()

def menu():
    titulo('Menu')
    opcao_menu = int(input('''
    [1] Depositar
    [2] Sacar
    [3] Visualizar Extrato
    [4] Administrativo
    [5] Sair
    Opção escolhida: '''))
    
    match opcao_menu:
        case 1:
            depositar()
        case 2:
            sacar()
        case 3:
            visualizar_extrato()
        case 4:
            menu_admin()
        case 5:
            print("Sair")
        case _:
            print('Opção inválida')

def menu_admin():
    titulo('Administrativo')
    opcao_menu = int(input('''
    [1] Cadastrar Cliente
    [2] Listar Clientes
    [3] Criar Conta
    [4] Listar Contas
    [5] Menu anterior
    [6] Sair    
    Opção escolhida: '''))
    
    match opcao_menu:
        case 1:
            cadastrar_cliente()
        case 2:
            listar_clientes()
        case 3:
            criar_conta()
        case 4:
            listar_contas()
        case 5:
            menu()
        case 6:
            sair()
        case _:
            print('Opção inválida.')
            sair()   



# Variáveis Globais
NUM_SAQUES = 3
LIMITE_SAQUES = 500.00


clientes = []
numero_conta = 0
contas = []
numero_conta = 0
lista_depositos = []
saldo = 0.0
extrato = []  # depositar()

# Entrada do Programa
# Chamando a função principal menu que chama as demais
menu()

