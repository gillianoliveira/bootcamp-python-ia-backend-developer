'''
DESAFIO DE PROJETO
Criando um Sistema Bancário com Python
Módulo: Dominando Python e suas Estruturas de Dados	
Bootcamp: Python AI Backend Developer Bootcamp
Conclusão do Desafio: ?
Proposta no README
'''

import datetime as dt

# Funções complementares
def titulo(t):
    traco = '-'
    print(traco * 30)
    print(f"{t.center(30, ' ')}")
    print(traco * 30)

def validacao_cpf(cpf):
    global cpf_cadastrado    
    if len(str(cpf)) != 11:
        print('O cpf deve ter 11 dígitos.')
        menu()
        return
    else:
        for cliente in clientes:
            if cliente["cpf"] == cpf:
                cpf_cadastrado = True
                return cpf

def listar_clientes(clientes):
    for cliente in clientes:
        print(cliente)

def listar_contas(contas):
    for conta in contas:
        print(conta) 

# Funções Principais 
def depositar(contas, valor):
    global saldo
    global soma_depositos    
    titulo('Depósito')
    
    numero_conta = int(input('Informe o número da conta: '))
    
    conta_encontrada = False

    for conta in contas:
        if conta['numero_conta'] == numero_conta:
            conta_encontrada = True
            valor = float(input('Valor do depósito: R$ '))
            if valor > 0:
                saldo += valor
                data = dt.datetime.now().strftime("%Y-%m-%d %I:%M:%S") 
                soma_depositos.append(valor)
                extrato.append({'data':data, 'valor':valor, 'operacao':'Depósito'})
                print(f'Deósito no valor de R$ {valor:.2f} na conta {numero_conta} realizado com sucesso.')
            elif valor == 0:
                print(f'O valor do depósito precisa ser maior que R$ 0.00.')
                menu()
                break
    if not conta_encontrada:
        print(f'A conta número {numero_conta} não foi encontrada. Depósito não realizado.')

def sacar():
    titulo('Saque')

def visualizar_extrato():
    titulo('Extrato')

def cadastrar_cliente():
    titulo('Cadastrar Cliente')
    
    while True:
        cpf = int(input("CPF: "))
        validacao_cpf(cpf)
        nome = input('Nome Completo: ')
        data_nascimento = input('Data de nascimento (dd/mm/aaaa): ')
        logradouro = input('Logradouro: ')
        numero = input('Número: ')
        bairro = input('Bairro: ')
        cidade = input('Cidade: ')
        estado = input('Sigla do estado: ').upper()
        endereco = f'{logradouro}, {numero}-{bairro}-{cidade}/{estado}'
        cliente = {
            'cpf': cpf, 
            'nome': nome,
            'data_nascimento': data_nascimento,
            'endereco': endereco
            }
        clientes.append(cliente)        
        menu()
        break
    
def abrir_conta():
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
   


    titulo('Listar Clientes')

def sair():
    print('Programa encerrado.')
    exit()

def menu():
    titulo('Menu')
    opcao = int(input('''
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Cadastrar Cliente
    [5] Abertura de Conta
    [6] Sair
    Opção escolhida: '''))
    
    match opcao:
        case 1:
            depositar(contas, valor)
        case 2:
            sacar()
        case 3:
            visualizar_extrato()
        case 4:
            cadastrar_cliente(clientes)
        case 5:
            abrir_conta(AGENCIA)
        case 6:
            titulo('Sair')
            print('Programa encerrado.')
            exit()
        case _:
            print('Opção inválida.')
            exit()



# Variáveis Globais
NUM_SAQUES = 3
LIMITE_SAQUES = 500.00
AGENCIA = '0001'
contas = []
clientes = []
extrato = []
soma_depositos = []
saldo = 0.0
valor = 0.0
numero_conta = 0
cpf_cadastrado = False
conta_cadastrada = False

# Entrada do Programa
# Chamando a função principal menu que chama as demais
menu()

