<h1>Otimizando o Sistema Bancário com Funções em Python</h1>

```
Bootcamp: Python AI Backend Developer
Plataforma: dio.me
Inscrição: 13-05-2024
Término: 26/05/2024
Carga horária: 67h
Promovido por: Vivo
Veja no Collab: [https://colab.research.google.com/drive/1vfuB7IXVY7Z_iZtYooiRb8wdWUP3-r0G?usp=sharing](https://colab.research.google.com/drive/1vfuB7IXVY7Z_iZtYooiRb8wdWUP3-r0G?usp=sharing)
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
  - [Extrato](#extrato)
- [Pontos a melhorar para a próxima versão](#pontos-a-melhorar-para-a-próxima-versão)
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
1. Solicitar número da conta onde o saque vai ser realizado.
2. Verificar se a conta existe.
3. Se a conta existir:<br>
    3.1 Solicitar o valor do saque.<br>
    3.2 Verificar se o número de saques diários foi excedido.<br>
    3.3 Verificar se o valor do saque está dentro do limite permitido.<br>
    3.4 Verificar se o cliente tem saldo suficiente para fazer o saque.<br>
    3.5 Se o cliente passar nas verificações 3.2 a 3.4:<br>
        3.5.1 Efetuar saque<br>
        3.5.2 Registrar data e hora<br>
        3.5.3 Adicinar saque ao extrato<br>
        3.5.4 Imprimir mensagem de sucesso.<br>
4. Se a conta não existir imprimir mensagem informando que a conta não foi localizada.

## Extrato
1. Solicitar o número da conta onde vai ser feito o saque.
2. Verificar se a conta existe.
3. Se a conta existe:
    3.1 Listar as operações registradas no extrato
    3.2 Se a operação for depósito, somar ao saldo
    3.3 Se a operação for saque, debitar do saldo.
    3.4 Diminuir o total de saques do total de depósitos
    3.5 Imprimir o total de depósitos
    3.6 Imprimir o total de saques
    3.7 Imprimir o saldo atualizado.
4. Se a conta não existe: exibir mensagem informando.

# Pontos a melhorar para a próxima versão

1. Tratar erros por valores usando vírgula ao invés de pontos como separador decimal.
2. Erros gerados por CPFs começados com zero.
3. Conversão de string para data.
4. Limitar o número de caracteres nos campos número e Sigla do Estado.
5. Melhorar a exibição das listas de usuários e contas.

# Principais tópicos abordades até o momento em Python

[✓] Listas <br />
[✓] Tuplas <br />
[✓] Conjuntos <br />
[✓] Dicionários <br />
[✓] Funções  <br />


