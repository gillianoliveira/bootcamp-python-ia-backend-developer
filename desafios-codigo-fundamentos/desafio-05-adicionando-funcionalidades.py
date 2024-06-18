# Desafio 05: Adicionando funcionalidades ao plano
# Módulo: Dominando Python e suas Estruturas de Dados
# Bootcamp: Python AI Backend Developer
# Plataforma: Dio.me
# Empresa: Vivo
# Concluído em:


# Desafio
# Agora, vamos Adicionar uma funcionalidade à classe UsuarioTelefone para que
# possa ser verificado o saldo disponível em seu plano. Para essa solução,
# você pode criar uma classe PlanoTelefone, o seu método de inicialização
# e encapsular os atributos, 'nome' e 'saldo' dentro da classe.
# Adicione também um método 'verificar_saldo' para verificar o saldo do plano e
# uma  'mensagem_personalizada' para gerar uma mensagem personalizada.

# Condições da verificação do saldo:
# - Caso o saldo seja menor do que 10, retorne: "Seu saldo está baixo. Recarregue e use os serviços do seu plano."
# - Caso o saldo seja maior ou igual a 50, retorne: "Parabéns! Continue aproveitando seu plano sem preocupações."
# - Caso contrário, retorne: "Seu saldo está razoável. Aproveite o uso moderado do seu plano."

# Entrada
# Como entrada, será solicitado o nome, plano (Essencial, Prata, Premium) e saldo atual do cliente.

# Saída
# Mensagem personalizada de acordo o saldo do cliente.

# Exemplos
# A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas.
# Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

# TODO: Crie a classe PlanoTelefone, seu método de inicialização e encapsule os atributos, 'nome' e 'saldo':
class PlanoTelefone:
    def __init__(self, nome_plano, saldo_inicial):
        self._nome_plano = nome_plano
        self._saldo_inicial = saldo_inicial

    @property
    def nome_plano(self):
        return self._nome_plano

    @property
    def saldo_inicial(self):
        return self._saldo_inicial

    @nome_plano.setter
    def nome_plano(self, nome_plano):
        self._nome_plano = nome_plano

    @saldo_inicial.setter
    def saldo_inicial(self, saldo_inicial):
        self._saldo_inicial = saldo_inicial

# TODO: Crie um método 'verificar_saldo' para verificar o saldo do plano sem acessar diretamente o atributo:
    def verificar_saldo(self):
        return self.saldo_inicial

# TODO: Crie um método 'mensagem_personalizada' para gerar uma mensagem personalizada com base no saldo:
    def mensagem_personalizada(self):
        saldo_usuario = self.verificar_saldo()
        if saldo_usuario >= 50:
            return "Parabéns! Continue aproveitando seu plano sem preocupações."
        elif saldo_usuario > 10:
            return "Seu saldo está razoável. Aproveite o uso moderado do seu plano."
        else:
            return "Seu saldo está baixo. Recarregue e use os serviços do seu plano."


# Classe UsuarioTelefone:
class UsuarioTelefone:
    def __init__(self, nome_usuario, plano_usuario):
        self.nome_usuario = nome_usuario
        self.plano_usuario = plano_usuario

# TODO: Crie um método para verificar o saldo do usuário e gerar uma mensagem personalizada:
    def saldo_mensagem(self):
        saldo_usuario = self.plano_usuario.verificar_saldo()
        mensagem_usuario = self.plano_usuario.mensagem_personalizada()
        return saldo_usuario, mensagem_usuario


# Recebendo as entradas do usuário (nome, plano, saldo):
nome_usuario = input()
nome_plano = input()
saldo_inicial = float(input())

# Criação de objetos do plano de telefone e usuário de telefone com dados fornecidos:
plano_usuario = PlanoTelefone(nome_plano, saldo_inicial)
usuario = UsuarioTelefone(nome_usuario, plano_usuario)

# Chamada do método para verificar_saldo sem acessar diretamente os atributos do plano:
saldo_usuario, mensagem_usuario = usuario.saldo_mensagem()
print(mensagem_usuario)