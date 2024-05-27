'''
Desafio 02: Criando uma lista de equipamentos
Curso: Dominando os Fundamentos Básicos do Python
Módulo: Dominando Python e suas Estruturas de Dados
Bootcamp: Python AI Backend Developer
Plataforma: Dio.me
Empresa: Vivo
Concluído em: 26/05/2024 
'''

# Desafio
# Você foi designado para desenvolver um programa para gerenciar os equipamentos de uma empresa. 
# O objetivo é criar um solução que permita aos usuários inserir informações sobre os equipamentos 
# que serão cadastrados na rede, em seguida, exibir essa lista de equipamentos. Crie uma Lista para 
# armazenar esses equipamentos e depois um loop para solicitar ao usuário inserir até três equipamentos.
# 
# Entrada
# O programa solicitará ao usuário que insira uma lista com três equipamentos para adicionar a rede.
#
#Saída
# Após a entrada dos itens, o programa exibirá a lista de equipamentos inseridos pelo usuário. 
# Cada equipamento será listado com um prefixo ( - ) de marcação para melhor organização.
#
#Exemplos
#A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. 
# Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

# TODO: Crie uma Lista 'itens' para armazenar os equipamentos:
# TODO: Crie um loop para solicita os itens ao usuário:
# TODO: Solicite o item e armazena na variável "item":
# TODO: Adicione o item à lista "itens":


itens = []
for item in range(3):
    item = input()
    itens.append(item)

print("Lista de Equipamentos:")  
for item in itens:   
    print(f"- {item}")
