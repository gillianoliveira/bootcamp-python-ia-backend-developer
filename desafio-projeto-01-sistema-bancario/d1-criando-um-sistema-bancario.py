'''
DESAFIO DE PROJETO
Criando um Sistema Bancário com Python
Módulo: Dominando Python e suas Estruturas de Dados	
Bootcamp: Python AI Backend Developer Bootcamp
Conclusão do Desafio: 23-05-2024
Proposta no README
'''
import datetime as dt

print('----------------------------------------')
print('                 MENU                   ')
print('----------------------------------------')

# Variáveis Globais
saldo = 0.0
valor = 0.0
extrato = []
depositos = []
NUM_SAQUES = 3
LIMITE_SAQUES = 500.00

while True:
    opcao = int(input('''
[1] Depositar
[2] Sacar
[3] Exibir Extrato
[4] Sair
Opção escolhida: ''')) 
    
    if opcao == 1:
        valor = float(input('Informe o valor do depósito: R$ '))
        if valor > 0:
            saldo += valor
            data = dt.datetime.now().strftime("%Y-%m-%d %I:%M:%S")
            extrato.append({'data': data, 'valor': valor, 'operacao': 'Depósito'})
        else:
            print('Valor inválido. Depósito não realizado.')        
    elif opcao == 2:
        conta_saques = len(extrato)
        valor = float(input('Informe o valor do saque: R$ '))
        
        if conta_saques > NUM_SAQUES:
            print(f'Você excedeu o limite de {NUM_SAQUES} saques diários. Operação não realizada.')
        elif valor > LIMITE_SAQUES:
            print(f'Esse valor excede o limite de R$ {LIMITE_SAQUES} por saque. Operação não realizada.')
        elif valor > saldo:
            print(f'Você não tem saldo suficiente para efetuar esta operação. Operação não realizada.')
        else:
            saldo -= valor
            data = dt.datetime.now().strftime("%Y-%m-%d %I:%M:%S")
            extrato.append({'data': data, 'valor': valor, 'operacao': 'Saque'})            
    elif opcao == 3:
        total_depositos = 0.0
        total_saques = 0.0
        print("Extrato") 
        total_transacoes = len(extrato)
        
        if total_transacoes > 1:
            for operacao in extrato:
                print(f"{operacao['data']} => R$ {operacao['valor']:.2f} - {operacao['operacao']}")
                
                if operacao['operacao'] == 'Depósito':
                    total_depositos += operacao['valor']
                elif operacao['operacao'] == 'Saque':
                    total_saques += operacao['valor']        
        
            print('-' * 30)
            print(f'Total de depósitos: R$ {total_depositos:.2f}')
            print(f'Total de saques: R$ {total_saques:.2f}')
            print(f'Saldo: R$ {saldo:.2f}')
        else:
            print('Não foram realizadas movimentações.')   
            
    elif opcao == 4:
        print("Progama encerrado.")
        exit()
                
    else:
        print("Opção inválida. Programa encerrado")
        exit()