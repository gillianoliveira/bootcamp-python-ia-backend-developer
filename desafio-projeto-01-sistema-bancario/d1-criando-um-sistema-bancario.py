'''
DESAFIO DE PROJETO
Criando um Sistema Bancário com Python
Módulo: Dominando Python e suas Estruturas de Dados	
Bootcamp: Python AI Backend Developer Bootcamp
Conclusão do Desafio: 23-05-2024
Proposta no README
'''

print('-----------------------------------------------------')
print('                         MENU                        ')
print('-----------------------------------------------------')

opcao = int(input('''
[1] Depositar
[2] Sacar
[3] Exibir Extrato
[4] Sair
Opção escolhida: ''')) 

while True:
    if opcao == 1:
        print("Depositar")
    elif opcao == 2:
        print("Sacar")
    elif opcao == 3:
        print("Exibir Extrato")        
    elif opcao == 4:
        print("Progama encerrado.")        
    else:
        print("Opção inválida. Programa encerrado")