<h1>Criando um Sistema Bancário em Python</h1>

```
Bootcamp: Python AI Backend Developer Bootcamp
Plataforma: dio.me
Inscrição: 13-05-2024
Término: em andamento
Carga horária: 67h
Promovido por: Vivo
Veja no Collab: [https://colab.research.google.com/drive/1GbHW4FnGeP50taYokh9kX9vJmryiBmtw?usp=sharing](https://colab.research.google.com/drive/1GbHW4FnGeP50taYokh9kX9vJmryiBmtw?usp=sharing)
```

SUMÁRIO:

- [Objetivo Geral do Desafio 1:](#objetivo-geral-do-desafio-1)
- [Requisitos](#requisitos)
    - [Operação de Depósito](#operação-de-depósito)
    - [Operação de Saque](#operação-de-saque)
    - [Operação Extrato](#operação-extrato)
- [Algoritmos criados por operação](#algoritmos-criados-por-operação)
  - [Algoritmo de depósito](#algoritmo-de-depósito)
  - [Algoritmo de saque](#algoritmo-de-saque)
- [Repositório oficial](#repositório-oficial)
- [Mensagem](#mensagem)
- [Principais tópicos abordados até o momento](#principais-tópicos-abordados-até-o-momento)
  - [Tipos de Operadores](#tipos-de-operadores)
  - [Estruturas Condicionais e de Repetição](#estruturas-condicionais-e-de-repetição)
  - [Manipulação de Strings](#manipulação-de-strings)



# Objetivo Geral do Desafio 1:

Criar um sistema bancário com as operações a seguir:
* sacar 
* depositar
* visualizar extrado

# Requisitos

### Operação de Depósito

[✓] A versão 1 do projeto trabalha com 1 único usuário, dessa forma não é necessário o número da agência e conta bancária. <br /><br />
[✓] Não podem haver depósitos negativos.

### Operação de Saque

[✓] O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque.<br />
[✓] Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informado que não será possível sacar o dinheiro por falta de saldo.<br />
[✓] Todos os saques devem ser armazenados em uma variável e exibidos na operação extrato.<br />

### Operação Extrato
[✓] Deve listar todos os depósitos e saques realizados na conta. <br />
[✓] No fim da listagem deve ser exibido o saldo atual da conta. <br />
[✓] Se o extrato estiver em branco, exibir a mensagem: Não foram realizadas movimentações.<br />
[✓] Os valores devem ser exibidos no formato R$ xxx.xx. Ex: R$ 1500.45<br />

OBS: A primeira solução ficou parecida com a do repositório oficial do curso e para não parecer uma cópia modificada, adicionei tópicos de etapas posteriores do curso.


# Algoritmos criados por operação

## Algoritmo de depósito
1 Pedir que o cliente informe o valor a ser depositado. <br />
2 Verificar se o valor do depósito é um número positivo. <br />
3 Realizar a operação de crédito adicionando o valor ao saldo. <br />
4 Gravar a operação no extrato. <br />
5 Oferecer novas opções. <br />

## Algoritmo de saque
1 Verificar se a opção selecionada foi 1 no menu principal <br />
2 Pedir que o cliente informe o valor que deseja sacar. <br />
3 Verificar se o cliente já excedeu o limite de 3 saques diários <br />
4 Verificar se o valor solicitado está dentro do limite de R$500,00 <br />
5 Verificar se o cliente tem saldo suficiente para efetuar o saque.<br />
6 Realizar a operação de saque <br />
7 Gravar a operação no extrato <br />
8 Oferecer novas opções <br />

# Repositório oficial
O repositório oficial com a solução proposta pelo instrutor Guilherme Arthur de Carvalho (@decarvalhogui) pode ser acessado através do endereço a seguir: [https://github.com/digitalinnovationone/trilha-python-dio/blob/main/00%20-%20Fundamentos/desafio.py](https://github.com/digitalinnovationone/trilha-python-dio/blob/main/00%20-%20Fundamentos/desafio.py)


# Mensagem

Explore todos os conceitos explorados até aqui e replique (ou melhore, porque não?) este projeto prático.

# Principais tópicos abordados até o momento

[✓] Ambiente de Desenvolvimento <br />
[✓] Versionamento de Código com Git e Github <br />
[✓] Tipos de Operadores com Python <br />
[✓] Estruturas Condicionais e de Repetição em Python <br />
[✓] Manipulando Strings com Python <br />


## Tipos de Operadores

[✓] Operadores Aritméticos <br />
[✓] Operadores de Comparação <br />
[✓] Operadores de Atribuição <br />
[✓] Operadores Lógicos <br />
[✓] Operadores de Identidade <br />
[✓] Operadores de Associação <br />


## Estruturas Condicionais e de Repetição
[✓] Indentação e blocos <br />
[✓] if / if-else / elif <br />
[✓] if ternário <br />
[✓] if aninhado <br />
[✓] for <br />
[✓] for + range() <br />
[✓] while <br />
[✓] for-else <br />
[✓] while-else <br />

## Manipulação de Strings

[✓] .upper() <br />
[✓] .lower() <br />
[✓] .title() <br />
[✓] .strip() <br />
[✓] .lstrip() <br />
[✓] .rstrip() <br />
[✓] .center(num, "#") <br />
[✓] .join(var) <br />
[✓] interpolação de variáveis (3 formas diferentes) <br />
[✓] Fatiamento de strings <br />
[✓] Strings em múltiplas linhas <br />



