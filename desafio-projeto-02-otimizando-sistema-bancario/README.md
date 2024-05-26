<h1>Otimizando o Sistema Bancário com Funções em Python</h1>

```
Bootcamp: Python AI Backend Developer Bootcamp
Plataforma: dio.me
Inscrição: 13-05-2024
Término: em andamento
Carga horária: 67h
Promovido por: Vivo
Veja no Collab: Ainda não criado
```

SUMÁRIO:
- [Objetivo Geral do Desafio 2](#objetivo-geral-do-desafio-2)
- [Requisitos](#requisitos)
- [Regras de Negócios](#regras-de-negócios)
- [Algoritmos](#algoritmos)
  - [Cadastro de clientes](#cadastro-de-clientes)
  - [Criação de nova conta](#criação-de-nova-conta)
  - [Depósito](#depósito)
  - [Saque](#saque)
- [Principais tópicos abordades até o momento em Python](#principais-tópicos-abordades-até-o-momento-em-python)


# Objetivo Geral do Desafio 2
Recriar o código do projeto 'Criando um Sistema Bancário em Python', desafio 1, utilizando funções para executar as features saque, depósito e visualizar extrato, além de criar duas novas funções sendo uma para cadastro de clientes e outra para cadatro de conta bancária. <br />

# Requisitos
[✓] Recriar as features: saque, depósito e visualizar extrado utilizando funções. <br />
[✓] Criar uma funcionalidade para cadastrar novos usuários. <br />
[✓] Criar uma funcionalidade criar conta-corrente. <br />
[✓] Um usuário é composto por: nome, data de nascimento, cpf e endereço. <br />
[✓] Uma conta é composta por: agência, número da conta e usuário. <br />
[✓] O programa deve armazenar contas em uma lista. <br />
[✓] O número da conta é sequencial, iniciando em 1. <br />
[✓] O número da agência é fixo: "0001". <br />
[✓] Endereço é uma string com formato: logradouro, número - bairro - cidade/ sigla do estado. <br />
[✓] O CPF deve ser armazenado apenas com números. <br />
[✓] A função saque deve receber argumentos apenas pelo nome (keyword only). Sugestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_sques. Sugestão de retorno: saldo e extrato <br />
[✓] A função depósito deve receber os argumentos apenas por posição (positional only). Sugestão de argumentos:  saldo, valor, extrato. Sugestão de retorno: saldo e extrato. <br />


# Regras de Negócios
[✓] Não deve ser possível cadastrar dois usuários com o mesmo CPF.<br />
[✓] Um usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.<br />

*Você pode adicionar novas funções como, por exemplo, listar contas.

# Algoritmos

Em andamento...

## Cadastro de clientes
1. Solicitar o CPF.
2. Verificar a quantidade de dígitos do cpf.
3. Verificar se o CPF já está cadastrado.
4. Se o CPF estiver cadastrado, exibir mensagem informado que o cadastro já existe.
5. Se o CPF não estiver cadastrado, solicitar dados para o cadastro
6. Armazenar os dados fornecidos pelo cliente

## Criação de nova conta
1. Solicita o CPF do titular da conta.
2. Verifica se o CPF já está cadastrado.
3. Se o CPF não estiver cadastrado, informa e volta para o menu principal.
4. Se o CPF estiver cadastrado, abre uma nova conta.

## Depósito
1. Solicita o número da conta onde o depósito vai ser efetuado. <br>
2. Se a conta existe:<br>
    2.1 Solicita o valor do depósito.<br>
    2.2 Se o valor for maior que 0:<br>
        2.2.1 Adiciona o valor ao saldo.<br>
        2.2.2 Registra data e hora do depósito.<br>
        2.2.3 Adiciona o depósito ao extrato.<br>
        2.2.4 Imprime uma mensagem dizendo que o depósito foi efetuado com sucesso informando a conta e o valor da transação.<br>
    2.3 Se o valor for menor ou igual a zero:<br>
        2.3.1 Imprime uma mensagem informando que o depósito precisa ser superior a 0 reais.<br>2.3.2 Envia o usuário para o menu principal caso ele queira tentar fazer o depósito novamente ou encerrar o programa.<br>
3. Se a conta não existe:<br>
   3.1 Imprime uma mensagem dizendo que a conta não foi encontrada e que a operação foi cancelada.<br>
   3.2 Programa encerrado.<br>

## Saque
1.

# Principais tópicos abordades até o momento em Python

[✓] Listas <br />
[✓] Tuplas <br />
[✓] Conjuntos <br />
[✓] Dicionários <br />
[✓] Funções  <br />


