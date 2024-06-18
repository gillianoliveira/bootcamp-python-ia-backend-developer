# Desafio 04: Criando uma Classe de Usuário
# Módulo: Dominando Python e suas Estruturas de Dados
# Bootcamp: Python AI Backend Developer
# Plataforma: Dio.me
# Empresa: Vivo
# Concluído em: 17/06/2024


# Desafio
# Vamos criar uma classe chamada UsuarioTelefone para representar um usuário de telefone.
# Você pode definir um método especial e depois aplicar conceitos de encapsulamento nos atributos dentro da classe.
# Lembre-se que, cada usuário terá um nome, um número de telefone e um plano associado,
# neste desafio, simulamos três planos, sendo: Plano Essencial Fibra, Plano Prata Fibra e Plano Premium Fibra.

# Entrada
# Nome do usuário, número de telefone e plano.

# Saída
# Mensagem indicando que o usuário foi criado com sucesso.

# Exemplos
# A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas.
# Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.


# TODO: Aplique o conceito de encapsulamento, onde os atributos serão encapsulados dentro da classe.
class UsuarioTelefone:

    def __init__(self, nome, numero, plano) -> None:
        self._nome = nome
        self._numero = numero
        self._plano = plano

    @property
    def nome(self):
        return self._nome

    @property
    def numero(self):
        return self._numero

    @property
    def plano(self):
        return self._plano

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @numero.setter
    def numero(self, numero):
        self._numero = numero

    @plano.setter
    def plano(self, plano):
        self._plano = plano

    # A classe `UsuarioTelefone` define um método especial `__str__`, que retorna uma representação em string do objeto.
    def __str__(self):
        return f"Usuário {self.nome} criado com sucesso."


# Entrada:
nome = input()
numero = input()
plano = input()
# TODO: Crie um novo objeto `UsuarioTelefone` com os dados fornecidos:

usuario = UsuarioTelefone(nome, numero, plano)
print(usuario)
