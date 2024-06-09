'''DESAFIO DE PROJETO 03
Modelando um Sistema Bancário em POO com Python
Módulo: Orientação a Objetos e Boas Práticas em Python
Bootcamp: Python AI Backend Developer
Conclusão do Desafio: Em andamento
Objetivo no README
'''


class Estilo:

    @staticmethod
    def titulo(t: str):
        """Imprime um título formatado.

        Args:
            t (str): O título a ser exibido.
        """
        print('-' * 30)
        print(f'{t.center(30, " ")}')
        print('-' * 30)


class Cliente:
    pass


class MenuPrincipal:

    def __init__(self) -> None:
        pass

    def menu(self):
        while True:
            try:
                Estilo.titulo('Menu')
                opcao = int(input('''
        [1] Abertura de Conta
        [2] Cadastrar Cliente
        [3] Sair
        Opção escolhida: '''))
                match opcao:
                    case 1:
                        pass
                    case 2:
                        pass
                    case 3:
                        Estilo.titulo('Sair')
                        print("Programa encerrado.")
                        exit()
            except ValueError as ve:
                raise ValueError(f'"Erro": {ve}')


cliente = Cliente()
menu = MenuPrincipal()
menu.menu()
