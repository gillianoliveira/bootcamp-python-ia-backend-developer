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
    print(f"{traco * 30}")
    print(f'{t.center(30, " ")}')
    print(f"{traco * 30}")

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

def conta_existe(numero_conta):
    global conta_encontrada
    for conta in contas:
        if conta['numero_conta'] == numero_conta:
            return True        
    return False
        
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
                #soma_depositos.append(valor)
                extrato.append({'data':data, 'valor':valor, 'operacao':'Depósito'})
                print(f'Deósito no valor de R$ {valor:.2f} na conta {numero_conta} realizado com sucesso.')
                menu()
                break
            elif valor <= 0:
                print(f'O valor do depósito precisa ser maior que R$ 0.00.')
                menu()
                break
    if not conta_encontrada:
        print(f'A conta número {numero_conta} não foi encontrada. Transação cancelada.')
  
def sacar(*,quantidade_saques,numero_conta, valor):
    global LIMITE_SAQUES
    global saldo
    global extrato
    
    titulo('Saque')
    conta_saque = len(extrato)
    numero_conta = int(input('Informe o número da conta: '))
    
    conta_existe(numero_conta)
    
    if conta_existe:
        valor = float(input('Digite o valor do saque: R$ '))
        
        if conta_saque > quantidade_saques:
            print(f'Você excedeu o limite diário de {quantidade_saques} saques. Operação não realizada.')
        elif valor > LIMITE_SAQUES:
            print(f'O valor solicitado está acima do limite de R$ {LIMITE_SAQUES:.2f}. Operação não realizada.')
        elif valor > saldo:
            print(f'Você não tem saldo suficiente. Operação não realizada.')
        else:
            saldo -= valor
            data = dt.datetime.now().strftime("%Y-%m-%d %I:%M:%S")
            extrato.append({'numero_conta': numero_conta, 'data': data, 'valor': valor, 'operacao':'Saque'})
            print(f'Saque de R$ {valor:.2f} efetuado com sucesso.')
            menu()
    else:
        print(f'A conta {numero_conta} não foi localizada. Informe um número de conta válido.')        

def visualizar_extrato(numero_conta):
    titulo('Extrato')
    global saldo
    total_depositos = 0.0
    total_saques = 0.0
    
    numero_conta = int(input('Informe o número da conta: '))
    
    conta_existe(numero_conta)
    
    if conta_existe:
        for operacao in extrato:
            print(f"{operacao['data']} - {operacao['operacao']}: R$ {operacao['valor']:.2f}")
            
            if operacao['operacao'] == 'Depósito':
                total_depositos += operacao['valor']
            elif operacao['operacao'] == 'Saque':
                total_saques += operacao['valor']
        saldo = total_depositos - total_saques
        
        print('-' * 30)
        print(f'Total de depósitos: R$ {total_depositos:.2f}')
        print(f'Total de saques: R$ {total_saques:.2f}')    
        print(f'Saldo: R$ {saldo:.2f}')
        menu()    
       
def cadastrar_cliente(clientes):
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
        
def abrir_conta(cpf):
    global numero_conta
    titulo('Abertura de Conta')    
    while True:
        cpf = int(input('Informe o CPF do titular da conta: '))
        validacao_cpf(cpf)
        if cpf_cadastrado == False:
            print('Você precisa cadastrar o titular antes de abrir a conta.')
            menu()
            break
        numero_conta += 1
        conta = {'cpf':cpf, 'agencia': AGENCIA, 'numero_conta':numero_conta}
        contas.append(conta)
        print(f'Conta aberta com sucesso. \nNúmero da conta:{numero_conta}' )
        menu()
        break

def listar_clientes(clientes):
    for cliente in clientes:
        print(cliente)

def listar_contas(contas):
    for conta in contas:
        print(conta) 

def menu():
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
            depositar(contas, valor)
        case 2:
            sacar(
                quantidade_saques = quantidade_saques,
                numero_conta = numero_conta,
                valor = valor            
            )
        case 3:
            visualizar_extrato(numero_conta)
        case 4:
            cadastrar_cliente(clientes)
        case 5:
            abrir_conta(cpf)
        case 6:
            listar_clientes(clientes)
        case 7:
            listar_contas(contas)
        case 8:
            titulo('Sair')
            print('Programa encerrado.')
            exit()
        case _:
            print('Opção inválida.')
            exit()
            

# Variáveis Globais
LIMITE_SAQUES = 500.00
AGENCIA = '0001'
contas = []
clientes = []
extrato = []
soma_depositos = []
saldo = 0.0
valor = 0.0
numero_conta = 0
quantidade_saques = 3
cpf = 0
cpf_cadastrado = False

# Chamando a função principal
menu()