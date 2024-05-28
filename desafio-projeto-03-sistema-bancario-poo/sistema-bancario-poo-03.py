'''
DESAFIO DE PROJETO 03
Modelando um Sistema Bancário em POO com Python
Módulo: Orientação a Objetos e Boas Práticas em Python	
Bootcamp: Python AI Backend Developer
Conclusão do Desafio: Em andamento
Objetivo no README
'''

class Conta:
    def __init__(self, numero_conta, correntista):
        self.agencia = '001'
        self.saldo = 0.0
        self.numero_conta = numero_conta
        self.correntista = correntista
        self.historico = Historico()
        
    def abertura_conta():
        pass
    
    def sacar():
        pass
    
    def depositar():
        pass
    
    def saldo():
        pass
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class Historico:
    pass


class cliente:
    pass
