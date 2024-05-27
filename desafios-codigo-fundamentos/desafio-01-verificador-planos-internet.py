'''
Desafio 01: Verificador de Planos de Internet
Curso: Dominando os Fundamentos Básicos do Python
Módulo: Dominando Python e suas Estruturas de Dados
Bootcamp: Python AI Backend Developer
Plataforma: Dio.me
Empresa: Vivo
Concluído em: 26/05/2024 
'''

# Uma empresa de telecomunicações deseja criar uma solução algorítmica que ajude aos seus clientes a escolherem 
# o plano de internet ideal com base em seu consumo mensal de dados. Para a resolução, você pode solicitar ao 
# usuário que insira o seu consumo, sendo este um valor 'float'. Crie uma função chamada recomendar_plano para 
# receber o consumo médio mensal de dados informado pelo cliente, além de utilizar estruturas condicionais para 
# fazer a verificação e retornar o plano adequado.
# 
# Planos Oferecidos:
# - Plano Essencial Fibra - 50Mbps: Recomendado para um consumo médio de até 10 GB.
# - Plano Prata Fibra - 100Mbps: Recomendado para um consumo médio acima de 10 GB até 20 GB.
# - Plano Premium Fibra - 300Mbps: Recomendado para um consumo médio acima de 20 GB.
# Entrada:
# Como entrada solicite o consumo médio mensal de dados em GB (float).
# Saída:
# Retorne o plano ideal para o cliente de acordo com o consumo informado na entrada.

# TODO: Crie uma função recomendar_plano() para receber o consumo médio mensal
# TODO: Crie uma estrutura condicional para verificar o consumo médio mensal
# TODO: Retorne o plano de Internet adequado.

# Solicita ao usuário que insira o consumo médio mensal de dados:
consumo = float(input())

def recomendar_plano(consumo):
    if consumo > 20:
        return 'Plano Premium Fibra - 300Mbps'
    elif consumo > 10:
        return 'Plano Prata Fibra - 100Mbps'
    elif consumo <= 10:
        return 'Plano Essencial Fibra - 50Mbps'
# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
print(recomendar_plano(consumo))