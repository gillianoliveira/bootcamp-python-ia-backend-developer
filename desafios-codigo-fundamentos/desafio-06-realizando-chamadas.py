# Desafio 05: Adicionando funcionalidades ao plano
# Módulo: Dominando Python e suas Estruturas de Dados
# Bootcamp: Python AI Backend Developer
# Plataforma: Dio.me
# Empresa: Vivo
# Concluído em: 18/06/2024

# Desafio
# Vamos agora, adicionar uma funcionalidade à classe UsuarioTelefone,
# que realizar chamadas para outros usuários. Cada chamada terá uma
# duração em minutos e o custo será deduzido do saldo do usuário,
# suponha o custo de $0.10 por minuto. Você pode criar um método
# fazer_chamada que vai permitir que o usuário faça a chamada, ele
# vai receber o destinatario e duracao como parâmetros. Calcule o
# custo da chamada usando o método 'custo_chamada' do objeto 'plano',
# além de adicionar o método deduzir_saldo para deduzir o valor do saldo
# do plano e depois retorne uma mensagem adequada como mostra no exemplo
# a baixo.

# Entrada
# Número do usuário, número do telefone, saldo inicial, número do
# destinatário e a duração da chamada em minutos.

# Saída
# Mensagem indicando o sucesso da chamada ou saldo insuficiente
# para fazer a chamada.

# Exemplos
# A tabela abaixo apresenta exemplos com alguns dados de entrada
# e suas respectivas saídas esperadas. Certifique-se de testar seu
# programa com esses exemplos e com outros casos possíveis.

# Classe UsuarioTelefone e o encapsulamento dos atributos nome, numero e plano:
class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
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

# TODO: Crie um método fazer_chamada para permitir que um usuário faça uma chamada telefônica:
    def fazer_chamada(self, destinatario, duracao):
        custo = self.plano.custo_chamada(duracao) # TODO: Calcule o custo da chamada usando o método 'custo_chamada' do objeto 'plano':
        if self.plano.verificar_saldo() >= custo: # TODO: Verifique se o saldo do plano é suficiente para a chamada.
            self.plano.deduzir_saldo(custo) # TODO: Se o saldo for suficiente, deduz o custo da chamada do saldo do plano.
            return f"Chamada para {destinatario} realizada com sucesso. Saldo: ${self.plano.verificar_saldo():.2f}"# TODO: E retorne uma mensagem de sucesso com o destinatário e o saldo restante após a chamada:
        else:
            return "Saldo insuficiente para fazer a chamada."


# Classe Pano, ela representa o plano de um usuário de telefone:
class Plano:
    def __init__(self, saldo_inicial):
        self._saldo = saldo_inicial

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo

# TODO: Crie um método para verificar_saldo e retorne o saldo atual:
    def verificar_saldo(self):
        return self.saldo

# TODO: Crie um método custo_chamada para calcular o custo de uma chamada supondo o custo de $0.10 por minuto:
    def custo_chamada(self, duracao):
        tarifa_minuto = 0.10
        custo = duracao * tarifa_minuto
        return custo

# TODO: Crie um método deduzir_saldo para deduzir o valor do saldo do plano:
    def deduzir_saldo(self, valor):
        self.saldo -= valor


# Classe UsuarioPrePago, aqui vemos a herança onde UsuarioPrePago herda os atributos e métodos da classe UsuarioTelefone:
class UsuarioPrePago(UsuarioTelefone):
    def __init__(self, nome, numero, saldo_inicial):
        super().__init__(nome, numero, Plano(saldo_inicial))


# Recebendo as informações do usuário:
nome = input()
numero = input()
saldo_inicial = float(input())

# Objeto de UsuarioPrePago com os dados fornecidos:
usuario_pre_pago = UsuarioPrePago(nome, numero, saldo_inicial)
destinatario = input()
duracao = int(input())

# Chama o método fazer_chamada do objeto usuario_pre_pago e imprime o resultado:
print(usuario_pre_pago.fazer_chamada(destinatario, duracao))