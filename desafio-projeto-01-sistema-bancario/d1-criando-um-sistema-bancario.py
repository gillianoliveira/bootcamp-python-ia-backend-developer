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
        print("Sacar")
    elif opcao == 3:
        print("Extrato")
        
        for operacao in extrato:
            print(f"{operacao['data']} - {operacao['operacao']}: R$ {operacao['valor']:.2f}")
                
    elif opcao == 4:
        print("Progama encerrado.")        
    else:
        print("Opção inválida. Programa encerrado")